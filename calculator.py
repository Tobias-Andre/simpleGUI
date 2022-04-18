import PySimpleGUI as sg

def create_window(theme):
    sg.theme(theme)
    sg.set_options(font = 'Franklin 18', button_element_size = (4,2))
    button_size = (4,2)
    layout = [
        [sg.Text(
            'Output', 
            font = 'Franklin 30', 
            justification = 'right', 
            expand_x = True, 
            pad = (10,20),
            right_click_menu = theme_menu)
         ],
        [sg.Button('Clear', expand_x = True), sg.Button('Enter', expand_x = True)],
        [sg.Button(7, size = button_size), sg.Button(8, size = button_size), sg.Button(9, size = button_size), sg.Button('*', size = button_size)],
        [sg.Button(4, size = button_size), sg.Button(5, size = button_size), sg.Button(6, size = button_size), sg.Button('/', size = button_size)],
        [sg.Button(1, size = button_size), sg.Button(2, size = button_size), sg.Button(3, size = button_size), sg.Button('+', size = button_size)],
        [sg.Button(0, expand_x = True), sg.Button('.', size = button_size), sg.Button('-', size = button_size)]
    ]
    
    return sg.Window('Calculator', layout)

theme_menu = ['Menu', ['LightGrey1','dark','DarkGray8','random']]
window = create_window('dark')

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
        
window.close()