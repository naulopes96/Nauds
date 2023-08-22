import PySimpleGUI as sg
from playsound import playsound 
import numpy as np
import PySimpleGUI as psg


names = [1,2,3,5,6,7,8,9]
lst = psg.Listbox(names, size=(20, 4), font=('Arial Bold', 14), expand_y=True, enable_events=True, key='-LIST-')
lst2 = psg.Listbox(names, size=(20, 4), font=('Arial Bold', 14), expand_y=True, enable_events=True, key='-LIST2-')
sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.

layout = [  
            
            [sg.Text('Endereço do Osciloscópio: ')],
            [psg.Input(size=(20, 1), font=('Arial Bold', 14), expand_x=True, key='-INPUT-'),
                #psg.Button('Add'),
                #psg.Button('Remove'),
                #psg.Button('Exit')],
                [lst]],
            [sg.Text('Endereço do contador de freq')],
            [psg.Input(key='-INPUT2-'),[lst2]],
            [sg.Image('fundo.png')],
            [sg.Button('Ok'), sg.Button('Cancel')] ]



# Create the Window
window = sg.Window('Programa FODA para tirar resultados QUENTES', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    print('You entered {}'.format(values['-LIST-']))
    # i = np.random.randint(2)
    # if i == 0:

    # if i == 1:
    #     playsound('vcs tem q tirar essa porra hj.mp3')
window.close()