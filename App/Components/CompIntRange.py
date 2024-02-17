import customtkinter

from App.Components.ToolTip import createToolTip


class CompIntRange:
    def __init__(self, master, rangeValue, text, gMap, description = ""):
        self.frame = customtkinter.CTkFrame(master, fg_color="#3D3D3D")
        self.label = customtkinter.CTkLabel(self.frame, text=text)
        self.frame.grid_columnconfigure(0, weight=1)

        self.gMap = gMap
        self.idValue = text

        self.sliderValue = rangeValue[0]
        self.label = customtkinter.CTkLabel(self.frame, text=text,  font=("Helvetica", 16, "bold"))
        self.labelValue = customtkinter.CTkLabel(self.frame, text=self.sliderValue,  font=("Helvetica", 16, "bold"))
        self.slider = customtkinter.CTkSlider(self.frame, from_=rangeValue[0], to=rangeValue[1], command=self.slider_event)
        self.slider.set(rangeValue[0])
        self.label.grid(row=0, column=0, padx=10, sticky='w')
        self.labelValue.grid(row=0, column=1, padx=10)
        self.slider.grid(row=1, column=0, padx=10,  pady=10, sticky="e")

        createToolTip(self.label, description)

    def slider_event(self, value: float) -> None:
        self.sliderValue = int(value)
        self.labelValue.configure(text=self.sliderValue)
        self.gMap.setValue(self.idValue, self.sliderValue)
