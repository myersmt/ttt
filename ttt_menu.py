'''
Matt Myers
09/LW/2021
Tic Tac Toe Options Menu
'''
import PySimpleGUI as sg
from ttt import ttt

#Theme
sg.theme('Dark Teal 2')

# Window
font=('helvetica', 12, 'bold',)
layout = [[sg.Text("\nChoose your Game Mode",font=font)],
          [sg.Button('1 V 1')], 
          [sg.Button('1 V CPU')],
          [sg.Button('Quit')]]

# *Window.Create
window = sg.Window('Tic Tac Toe Menu', layout, size=(300,200), element_justification='c')

# *Window.Display
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break
    if event == '1 V 1':
        pass


# *Window.Close
window.close()