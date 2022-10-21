import os
import sys
import csv
import fitz
import json
from copy import deepcopy
from PyQt6.QtWidgets import QApplication
from .ui.main_window import MainWindow
from .fencer import Fencer
from .grouper import Grouper

group_num = 4
weapons_num = 1
current_filepath = None
groups = []

app = QApplication(sys.argv)
window = MainWindow()
window.show()

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS # type: ignore
    except:
        base_path = os.path.abspath('.')
    return os.path.join(base_path, relative_path)

def startGrouping(new_filepath = None):
    global current_filepath
    global weapons_num
    global group_num
    global groups
    if new_filepath:
        current_filepath = new_filepath
    elif not current_filepath:
        raise Exception('no filepath specified')
    data = parseCSV(current_filepath)
    fencers = extractData(data)
    grouper = Grouper(fencers, group_num)
    groups = grouper.groups
    weapons_num = grouper.weapons_num
    if weapons_num > group_num:
        group_num = weapons_num
        window.updateGroupNumLabel()
    window.visualizeGroups(grouper.groups)

def parseCSV(filepath) -> list[list[str]]:
    data = []
    with open(filepath, encoding='utf-16-le') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        for line in reader:
            if line: data.append(line)
    return data[1:]

def extractData(data) -> list[Fencer]:
    fencers = []
    clubs = []
    path = resource_path('./package/res/clubs.json')
    with open(path, 'r') as f:
        try:
            clubs = json.load(f)
        except:
            pass
    for line in data:
        fencers.append(Fencer(
            lastname = line[1],
            firstname = line[2],
            birthdate = line[3],
            gender = line[4] if line[4] == 'M' else 'W',
            club = clubs[line[7]] if line[7] in clubs else line[7],
            weapon = line[-1][0]))
    return fencers

def buildPDF(place, date) -> fitz.Document:
    global groups
    if not groups: raise Exception('no groups present')
    groups = window.getGroups()
    path = resource_path('./package/res/Beobachtungsbogen.pdf')
    doc = fitz.Document(path)
    page_index = 0
    for group_index, group in enumerate(deepcopy(groups)):
        while group:
            doc.fullcopy_page(0, to=-1)
            page_index += 1
            page = doc[page_index]
            weapon = 'Florett' if group[0].weapon == 'F' else 'Degen'
            page.insert_text(fitz.Point(285, 105), weapon, fontsize = 28) # type: ignore
            page.insert_text(fitz.Point(780, 161), f'({group_index + 1})') # type: ignore
            if place and date:
                page.insert_text(fitz.Point(165, 161), f'{place}, {date}') # type: ignore
            for y in range(9):
                if not group: break
                fencer = group.pop(0)
                y_start = 245
                page.insert_text(fitz.Point(41, y_start + y * 34), fencer.str_PDF()) # type: ignore
    doc.delete_page(0)
    print()
    return doc

def run():
    app.exec()
