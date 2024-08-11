# Material Stat File Processor
# Processes txt and creates json format
from pprint import pp

fileToProcess="test.txt"

byLocation = {}
allTypes = {
    "BOOK": ["ARTBOOK", "BOOK", "ILL-BOOK", "ILLBOOKINT","EASYBOOK", "MANUSCRIPT", "PUBTHESIS", "RES_ARTBO", "RES_BOOK", "RES_REFBK", "WEEKLYBOOK","REF-BOOK","OFFPRINT","BRAILLE","PRINTMUSIC"],
    "ILL": [  "ILL_IN_ART", "ILL_NA_ART"],
    "MULTIMEDIA": ["AUDIOBOOK","CD","CD-ROM","DISKETTE","DVD","SUPCD","SUPCDROM","SUPDVD","SUPVCD","SUPVIDEO","PHOTO","VCD","VIDEOCASS","SUPCASS","CASSETTE","BLU-RAYDIS","AV-EQUIP","SOUNDTAPE"],
    "JOURNAL": ["BARTJOURNA","BJOURNAL","JOURNAL","JOURNAL1"],
    "ROOM": ["GS-ROOM","MMGS-ROOM","MMVB-ROOM"]
}
allLocations = {
    "ALLSPECIAL": ["INALCIK", "H-ALIYUCEL", "SPECIALCOL"],
    "ROOMS": ["GSROOMS","MMROOMS"],
    "STORAGES": ["B111STORAG","CATSTORAGE","REFSTORAGE","STORAGECOL"]
    
}

with open(fileToProcess, "r", encoding="utf-8") as file:
    content = file.readlines()

for info in content:
    cleared = info.lstrip().rstrip("|\n").replace(" ", "|")
    information = cleared.split("|")
    count = int(information[0])
    itemType = information[1]
    location = information[2]
    
    # Determine the main type category
    typeCategory = None
    for mainType, typeList in allTypes.items():
        if itemType in typeList:
            typeCategory = mainType
            break

    # If not found in allTypes, use the itemType itself as the category
    if typeCategory is None:
        typeCategory = itemType

    # Update byLocation dictionary
    if location not in byLocation:
        byLocation[location] = {}
    if typeCategory not in byLocation[location]:
        byLocation[location][typeCategory] = 0
    byLocation[location][typeCategory] += count

    # Check for combined locations
    for combinedLoc, locList in allLocations.items():
        if location in locList:
            if combinedLoc not in byLocation:
                byLocation[combinedLoc] = {}
            if typeCategory not in byLocation[combinedLoc]:
                byLocation[combinedLoc][typeCategory] = 0
            byLocation[combinedLoc][typeCategory] += count
pp(byLocation)