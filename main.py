import json

from App.mWizardWizard import App

with open('file.json', 'r') as f:
    data = json.load(f)

tEntries = []

for element in data:
    eValues = None
    eTypeId, eCrudValues, eNameId, eDescription = element
    if eTypeId == "int-range":
        eValues = [int(eCrudValues.split(':')[0]), int(eCrudValues.split(':')[1])]
    elif eTypeId == "bool":
        eValues = None
    elif eTypeId == "set":
        eValues = eCrudValues

    tEntries.append((eTypeId, eValues, eNameId, eDescription))

print(tEntries)

app = App(tEntries)
app.mainloop()