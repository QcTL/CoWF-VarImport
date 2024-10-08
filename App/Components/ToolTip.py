import tkinter as tk


class ToolTip(object):
    """
    Class that display the components description on the screen when the text is hovered
    """

    def __init__(self, widget):
        self.text = None
        self.widget = widget
        self.tipWindow = None
        self.id = None
        self.x = self.y = 0

    def showtip(self, text):
        """
        Display the text in tooltip window
        :param text: The text you want to display
        :return: None
        """
        self.text = text
        if self.tipWindow or not self.text:
            return
        x, y, _, _ = self.widget.bbox("insert")
        x = x + self.widget.winfo_rootx() + 25
        y = y + self.widget.winfo_rooty() + 20
        self.tipWindow = tw = tk.Toplevel(self.widget)
        tw.wm_overrideredirect(1)
        tw.wm_geometry(f"+{x}+{y}")
        label = tk.Label(tw, text=self.text, background="white", relief="solid", borderwidth=1)
        label.pack(ipadx=1)

    def hidetip(self):
        """
        Hide the tooltip window
        :return: None
        """
        tw = self.tipWindow
        self.tipWindow = None
        if tw:
            tw.destroy()


def createToolTip(widget, text):
    toolTip = ToolTip(widget)

    def enter(event):
        toolTip.showtip(text)

    def leave(event):
        toolTip.hidetip()

    widget.bind('<Enter>', enter)
    widget.bind('<Leave>', leave)
