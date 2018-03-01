import xml.dom.minidom as md


from tasks import xml2ram, ram2xml
xml = md.parse("tasks.xml")
schema = xml2ram(xml)
resXML = ram2xml(schema)
with open("result.xml", "w") as file:
    file.write(resXML.toprettyxml(encoding="utf-8").decode("utf-8"))