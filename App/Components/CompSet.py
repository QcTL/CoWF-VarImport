import customtkinter

from App.Components.ToolTip import createToolTip
from App.GlobalMap import GlobalMap


class CompSet:
    def __init__(self, master, setValues: list[str], text: str, gMap: GlobalMap, description: str = ""):
        self.frame = customtkinter.CTkFrame(master, fg_color="#3D3D3D")
        self.frame.grid_columnconfigure(0, weight=1)

        self.gMap = gMap
        self.idValue = text

        self.label = customtkinter.CTkLabel(self.frame, text=text, font=("Helvetica", 16, "bold"))
        self.setValue = setValues[0]

        self.setChooseMenu = customtkinter.CTkOptionMenu(self.frame, values=setValues,
                                                         command=self.setCurrentElement)

        self.label.grid(row=0, column=0, padx=10, pady=10, sticky='w')
        self.setChooseMenu.grid(row=0, column=1, padx=10, pady=10, sticky='e')

        createToolTip(self.label, description)

    def setCurrentElement(self, newValue: str) -> None:
        self.setValue = newValue
        self.gMap.setValue(self.idValue, self.setValue)
