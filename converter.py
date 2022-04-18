import PySimpleGUI as sg

layout = [
    [sg.Text('Text'), sg.Spin(['item 1', 'item 2'])],
    [sg.Button('Button')],
    [sg.Input()],
    [sg.Text('Test'), sg.Button('Test Button')]
]

window = sg.Window('Converter', layout)

while True:
    event, values = window.read()
    
    if event == sg.WIN_CLOSED:
        break
    
window.close()