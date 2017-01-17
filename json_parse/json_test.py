import json

file = open ('board.json')
values = json.load(file)

#print values
file.close()

idlist = 0

for i in values["lists"]:
	if i["name"] == "Todo":
		idlist = i["id"]
print idlist

for i in values["cards"]:
	if i["idList"] == idlist:
		print i["desc"]
		print "----------------"