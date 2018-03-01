import xml.dom.minidom as md
import sqlite3


from tasks import xml2ram, ram2xml, ram2sqlite, ram
xml = md.parse("tasks.xml")
schema = xml2ram(xml)
resXML = ram2xml(schema)
with open("result.xml", "w") as file:
    file.write(resXML.toprettyxml(encoding="utf-8").decode("utf-8"))
connect = sqlite3.connect(":memory:")  # используем оперативную память
ram2sqlite(schema, connect)
connect.close()
del connect
