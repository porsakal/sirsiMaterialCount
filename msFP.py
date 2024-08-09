# Material Stat File Processor
# Processes txt and creates json format
from msLogger import logger
from msConfig import maStConf
from pprint import pp

byLocation = {}
allTypes = {
    "BOOK": ["ARTBOOK", "BOOK", "EASYBOOK", "MANUSCRIPT", "PUBTHESIS", "RES_ARTBO", "RES_BOOK", "RES_REFBK", "WEEKLYBOOK"]
    # Diğer kategoriler burada eklenebilir
}

with open(maStConf.fileToProcess, "r", encoding="utf-8") as file:
    content = file.readlines()

for info in content:
    cleared = info.lstrip().rstrip("|\n").replace(" ", "|")
    information = cleared.split("|")
    count = int(information[0])
    itemType = information[1]
    location = information[2]
    
    # itemType'ın hangi kategoriye ait olduğunu bulma
    found_category = None
    for category, types in allTypes.items():
        if itemType in types:
            found_category = category
            break
    
    if found_category is None:
        # Eğer itemType herhangi bir kategoriye ait değilse, kendisi bir kategori olur
        found_category = itemType
    
    # Sözlük yapısını oluşturma ve toplama
    if location not in byLocation:
        byLocation[location] = {}
    
    if found_category not in byLocation[location]:
        byLocation[location][found_category] = 0
    
    byLocation[location][found_category] += count

pp(byLocation)
