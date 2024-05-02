import tkinter as tk
from tkinter import filedialog

import customtkinter

from App.Components import CompBool, CompSet, CompCat
from App.Components import CompIntRange
from App.GlobalMap import GlobalMap

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")


class App(customtkinter.CTk):
    """
    Main application made with tkinter to display the different parameters it's assigned at creation
    """

    def __init__(self, cEntrances: list[tuple[str, str, str, str]]):
        """
        Constructor function
        :param cEntrances: A List of tuples of 4 elements that contain (eTypeId, eValues, eNameId, eDescription)
            eTypeId: Type of variable selection
            eValues: Set of values to select
            eNameId: The name of the attribute to select
            eDescription: A description of the attribute
        """
        super().__init__()

        self.title("Wizard City of Weird Fishes")
        self.geometry(f"{580}x{580}")

        self.gMap = GlobalMap(cEntrances)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.scrollable_frame = customtkinter.CTkScrollableFrame(self)
        self.scrollable_frame.grid(row=0, column=0, columnspan=2, sticky='nsew')

        self.button = customtkinter.CTkButton(self, text="Export", command=self.exportFileEvent,
                                              font=("Helvetica", 16, "bold"))
        self.button.grid(row=1, column=0, columnspan=2, sticky='e', pady=10, padx=10)

        for i in cEntrances:
            if i[0] == "bool":  # Bool Part
                element = CompBool.CompBool(self.scrollable_frame, f"{i[2]}", self.gMap, i[3])
                element.frame.pack(fill='both', expand=True, pady=5)
            elif i[0] == "int-range":  # Range Part
                element = CompIntRange.CompIntRange(self.scrollable_frame, i[1], f"{i[2]}", self.gMap, i[3])
                element.frame.pack(fill='both', expand=True, pady=5)
            elif i[0] == "set":  # Select Part
                element = CompSet.CompSet(self.scrollable_frame, i[1], f"{i[2]}", self.gMap, i[3])
                element.frame.pack(fill='both', expand=True, pady=5)
            elif i[0] == "cat":  # Only Text:
                element = CompCat.CompCat(self.scrollable_frame, i[2], self.gMap)
                element.frame.pack(fill='both', expand=True, pady=5)

    def exportFileEvent(self) -> None:
        root = tk.Tk()
        root.withdraw()

        # Open the save file dialog
        file_path = filedialog.asksaveasfilename(defaultextension=".txt")

        # Check if a file path was selected
        if file_path:
            with open(file_path, 'w') as f:
                for key, value in self.gMap.getDic().items():
                    # Write each key-value pair on its own line
                    f.write(f'{key}:{value}\n')
