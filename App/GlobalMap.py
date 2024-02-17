class GlobalMap:

    def __init__(self, eList):
        self.dic = {}

        for i in eList:
            if i[0] == "bool":
                self.dic[i[2]] = "false"
            elif i[0] == "int-range":
                self.dic[i[2]] = str(i[1][0])
            elif i[0] == "set":
                self.dic[i[2]] = str(i[1][0])

    def setValue(self, idValue: str, newValue: str) -> None:
        self.dic[idValue] = str(newValue)

    def getDic(self) -> dict[str, str]:
        return self.dic
