import openpyxl
import sys

def main():
    wb = openpyxl.load_workbook(sys.argv[1])
    sheet = wb[sys.argv[2]]

    for row in tuple(sheet[2:sheet.max_row + 1]):
        for cell in row:
            print(cell.value)

if __name__ == "__main__":
    main()

# def parseAlbum(title, url):
#     if(title == "NA" or url == "NA"):
#         return
#     else:
        

# def parseSong(title, url, releaseDate, lyrics, pageViews)
# def parsePerson(name)
# def parseJob(title)
# def parseCategory(title)
# def parseTag(name)

# def parseIsCategorizedAs(title, url)
# def parseIsFeaturedIn(title, url)
# def parseIsTaggedAs(title, url)
# def parseWorked(title, url)
