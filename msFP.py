# Material Stat File Processor
# Processes txt and creates json format
from msLogger import logger
from msConfig import maStConf
from pprint import pp
byLocation={}
byType={}

with open(maStConf.fileToProcess,"r",encoding="utf-8") as file:
    content=file.readlines()

for info in content:
    cleared=info.lstrip().rstrip("|\n").replace(" ","|")
    information=cleared.split("|")
    location=information[2]
    if location not in byLocation.keys():
        byLocation[location]=int(information[0])
    else:
        byLocation[location]+=int(information[0])

for info in content:
    cleared=info.lstrip().rstrip("|\n").replace(" ","|")
    information=cleared.split("|")
    itemType=information[1]
    if itemType not in byType.keys():
        byType[itemType]=int(information[0])
    else:
        byLocation[location]+=int(information[0])
byLocation["ALLSPECIALCOL"]=byLocation["H-ALIYUCEL"]+byLocation['INALCIK']+byLocation["SPECIALCOL"]

pp(byType)