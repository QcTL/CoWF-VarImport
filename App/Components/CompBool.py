import customtkinter

from App.Components.ToolTip import createToolTip


class CompBool:
    """
    Class that display the component type "Bool" to the application
    """
    def __init__(self, master, text, gMap, description = ""):
        self.frame = customtkinter.CTkFrame(master, fg_color="#3D3D3D")
        self.frame.grid_columnconfigure(0, weight=1)

        self.gMap = gMap
        self.idValue = text

        self.label = customtkinter.CTkLabel(self.frame, text=text, font=("Helvetica", 16, "bold"))
        self.check_var = customtkinter.StringVar(value="off")
        self.checkbox = customtkinter.CTkCheckBox(self.frame, text="", command=self.checkbox_event,
                                                  variable=self.check_var, onvalue="on", offvalue="off")
        self.label.grid(row=0, column=0, padx=10,  pady=10, sticky='w')
        self.checkbox.grid(row=0, column=1, pady=10, padx=10, sticky="e")

        createToolTip(self.label, description)

    def checkbox_event(self) -> None:
        """
        Event that is called when the checkbox of the element Bool is pressed
        :return:
        """
        self.gMap.setValue(self.idValue, self.check_var.get())
