class GlobalMap:
    """
    A class used as a structure to host all the unique attributes that can be modified, and the current value
    """

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
        """
        Given a idValue set the new value that will be assigned
        :param idValue: The unique str name of the attribute
        :param newValue: The new value that will be assigned
        :return: None
        """
        self.dic[idValue] = str(newValue)

    def getDic(self) -> dict[str, str]:
        """
        Returns the class as a dictionary
        :return: Returns the class as a dictionary
        """
        return self.dic
