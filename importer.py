import openpyxl
import sys

def main():
    wb = openpyxl.load_workbook(sys.argv[1])
    sheet = wb[sys.argv[2]]

if __name__ == "__main__":
    main()
