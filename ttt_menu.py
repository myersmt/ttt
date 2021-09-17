'''
Matt Myers
09/LW/2021
Tic Tac Toe Options Menu
'''
import PySimpleGUI as sg
from ttt import main as ttt1v1

#Theme
sg.theme('Dark Teal 2')

# Window
font=('helvetica', 12, 'bold','underline')
layout = [[sg.Text("\nChoose your Game Mode\n\n",font=font)],
          [sg.Button('1 V 1', auto_size_button=False)], 
          [sg.Button('1 V CPU', auto_size_button=False)],
          [sg.Button('Quit', auto_size_button=False)]]

# *Window.Create
window = sg.Window('Tic Tac Toe Menu', layout, size=(300,200), element_justification='c')

# *Window.Display
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break
    if event == '1 V 1':
        window.close()
        ttt1v1()
    if event == '1 V CPU':
        window.close()
        sg.popup('Coming Soon')


# *Window.Close
window.close()