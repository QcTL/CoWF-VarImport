import customtkinter

from App.Components.ToolTip import createToolTip
from App.GlobalMap import GlobalMap


class CompCat:
    def __init__(self, master, text: str, gMap: GlobalMap):
        self.frame = customtkinter.CTkFrame(master, fg_color="#2B2B2B")
        self.frame.grid_columnconfigure(0, weight=1)

        self.label = customtkinter.CTkLabel(self.frame, text=text, font=("Helvetica", 21, "bold"))

        self.label.grid(row=0, column=0, padx=10, pady=10, sticky='w')