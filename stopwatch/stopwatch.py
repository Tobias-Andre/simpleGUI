import PySimpleGUI as sg
from time import time

def create_window():
    sg.theme('black')
    layout = [
        [sg.Push(), sg.Text('X', font = 'Young 14', text_color = 'red', pad = 0, enable_events = True, key = '-CLOSE-')],
        [sg.VPush()],
        [sg.Text('time', font = 'Young 50', key = '-TIME-')],
        [
            sg.Button('Start', button_color = ('#ffffff', '#ff0000'), border_width = '0', key = '-STARTSTOP-'),
            sg.Button('Lap', button_color = ('#ffffff', '#ff0000'), border_width = '0', key = '-LAP-', visible = False),
        ],
        [sg.Column([[]], key = '-LAPS-')],
        [sg.VPush()]
    ]
    return sg.Window(
        'Stopwatch',
        layout,
        size = (300, 300),
        no_titlebar = True,
        element_justification = 'center')

window = create_window()

start_time = 0
active = False

while True:
    event, values = window.read(timeout = 10)
    if event in (sg.WIN_CLOSED, '-CLOSE-'):
        break
    
    if event == '-STARTSTOP-':
        if active:
            # from active to stop
            active = False
            window['-STARTSTOP-'].update('Reset')
            window['-LAP-'].update(visible = False)

        else:
            # from stop to reset
            if start_time > 0:
                window.close()
                window = create_window()
                start_time = 0
                
            # from start to active
            else:
                start_time = time()
                active = True
                window['-STARTSTOP-'].update('Stop')
                window['-LAP-'].update(visible = True)

        
    if active:
        elapsed_time = round(time() - start_time, 1)
        window['-TIME-']. update(elapsed_time)
        
    if event == '-LAP-':
        window.extend_layout(window['-LAPS-'], [[sg.Text('1'), sg.VSeparator(), sg.Text('time')]])
    
window.close()