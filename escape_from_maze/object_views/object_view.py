import curses


class ObjectView:
    def __init__(self, view, color):
        self.view = view
        self.color = color
        self.ord = curses.color_pair(self.color) + ord(self.view)
