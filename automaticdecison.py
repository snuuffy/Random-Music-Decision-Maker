import PySimpleGUI as sg
import random

list = ["Blues", "Country", "Dance", "Drum and bass", "Electronica", "Folk", "Funk", "Gospel", "Heavy Metal", "Hip Hop", "Rap", "House", "Jazz", "Muzyka klasyczna", "Pop", "Punk rock", "Rave", "R & B", "Reggae", "Rock", "Rock and roll", "Ska", "Soul", "Techno", "Trance"]
# All the stuff inside your window.
layout = [  [sg.Text('Miejsce na wpisanie'), sg.InputText(key='gatunek')],
            [sg.Button('Ok'), sg.Button('Cancel')] ]

sg.theme('black')
# Create the Window
window = sg.Window('Decision Maker', layout)
# Event Loop to process "events" and get the "values" of the inputs
event, values = window.Read()
if event == 'Ok':
    box = sg.popup(random.choice(list))

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break

window.close()