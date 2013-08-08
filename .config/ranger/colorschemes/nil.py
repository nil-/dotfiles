#
# Ranger colorscheme
# ~/.config/ranger/colorschemes/nil.py
# Name: nil

# Parameters:
# bg/fg: black, blue, cyan, green, magenta, red, white, yellow, default
# attr: normal, bold, blink, reverse, underline, invisible

from ranger.gui.colorscheme import ColorScheme
from ranger.gui.color import *

class Default(ColorScheme):
    progress_bar_color = blue

    def use(self, context):
        fg, bg, attr = default_colors

        if context.reset:
            return default_colors

        elif context.in_browser:
            if context.selected:
                attr = reverse
            else:
                attr = normal
            if context.empty or context.error:
                bg = red
            if context.border:
                fg = default
            if context.media:
                if context.image:
                    fg = yellow
                if context.audio:
                    fg = cyan
                # Else (e.g. video).
                else:
                    fg = magenta
            if context.container:
                fg = red
            if context.directory:
                #attr |= bold
                fg = blue
                #fg = white
            # These files are finicky, as it also colors things like *.txts and
            #   random rc/config files.
            elif context.executable and not \
                    any((context.media, context.container,
                        context.fifo, context.socket)):
                #attr |= bold
                #fg = green
                fg = default
            if context.socket:
                fg = magenta
                #attr |= bold
            if context.fifo or context.device:
                fg = yellow
                #if context.device:
                    #attr |= bold
            if context.link:
                fg = context.good and cyan or magenta
            if context.tag_marker and not context.selected:
                #attr |= bold
                if fg in (red, magenta):
                    fg = white
                else:
                    fg = red
            if not context.selected and (context.cut or context.copied):
                #fg = black
                attr |= bold
            if context.main_column:
                if context.marked:
                    #attr |= bold
                    fg = yellow
            if context.badinfo:
                if attr & reverse:
                    bg = magenta
                else:
                    fg = magenta

        elif context.in_titlebar:
            if context.hostname:
                #fg = context.bad and red or green
                #fg = context.bad and red or default
                fg = black
                #attr |= bold
            elif context.directory:
                #fg = blue
                fg = red
                #attr |= bold
            elif context.tab:
                if context.good:
                    bg = green
                    #attr |= bold
            elif context.link:
                fg = cyan
                #attr |= bold

        elif context.in_statusbar:
            if context.permissions:
                if context.good:
                    fg = cyan
                elif context.bad:
                    #fg = magenta
                    fg = red
            if context.marked:
                #attr |= bold | reverse
                fg = yellow
            if context.message:
                if context.bad:
                    #attr |= bold
                    fg = red
            if context.loaded:
                bg = self.progress_bar_color

        if context.text:
            if context.highlight:
                attr |= reverse

        if context.in_taskview:
            if context.title:
                fg = blue

            if context.selected:
                attr |= reverse

            if context.loaded:
                if context.selected:
                    fg = self.progress_bar_color
                else:
                    bg = self.progress_bar_color

        return fg, bg, attr

