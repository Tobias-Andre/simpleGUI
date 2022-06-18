import PySimpleGUI as sg

sg.theme('dark')

layout = [
    [
        sg.Input(key = '-INPUT-'),
        sg.Spin(['kg to pounds','pounds to kg', 'km to miles', 'miles to km', 'seconds to minutes', 'seconds to hours', 'seconds to days', 'minutes to seconds', 'minutes to hours', 'minutes to days', 'hours to seconds', 'hours to minutes', 'hours to days', 'days to seconds', 'days to minutes', 'days to hours'], key = '-UNITS-'),
        sg.Button('Convert!', key = '-CONVERT-')
    ],
    [sg.Text('Output', enable_events = True, key = '-OUTPUT-')]
]

window = sg.Window('Converter', layout)

while True:
    event, values = window.read()
    
    if event == sg.WIN_CLOSED:
        break
    
    if event == '-OUTPUT-':
        window['-OUTPUT-'].update('')
    
    if event == '-CONVERT-':
        input_value = values['-INPUT-']
        if input_value.isnumeric():
            match values['-UNITS-']:
                case 'kg to pounds':
                    output = round(float(input_value) * 2.20462,2)
                    output_string = f'{input_value} kg are {output} pounds.'
                case 'pounds to kg':
                    output = round(float(input_value) / 2.20462,2)
                    output_string = f'{input_value} pounds are {output} kg.'
                case 'km to miles':
                    output = round(float(input_value) * 0.6214,2)
                    output_string = f'{input_value} km are {output} miles.'
                case 'miles to km':
                    output = round(float(input_value) / 0.6214,2)
                    output_string = f'{input_value} miles are {output} km.'
                case 'seconds to minutes':
                    output = round(float(input_value) / 60.0,2)
                    output_string = f'{input_value} seconds are {output} minutes.'
                case 'seconds to hours':
                    output = round(float(input_value) / 3600.0,2)
                    output_string = f'{input_value} seconds are {output} hours.'
                case 'seconds to days':
                    output = round(float(input_value) / 86400.0,2)
                    output_string = f'{input_value} seconds are {output} days.'
                case 'minutes to seconds':
                    output = round(float(input_value) * 60.0,2)
                    output_string = f'{input_value} minutes are {output} seconds.'
                case 'minutes to hours':
                    output = round(float(input_value) / 60.0,2)
                    output_string = f'{input_value} minutes are {output} hours.'
                case 'minutes to days':
                    output = round(float(input_value) / 1440.0,2)
                    output_string = f'{input_value} minutes are {output} days.'
                case 'hours to seconds':
                    output = round(float(input_value) * 3600.0,2)
                    output_string = f'{input_value} hours are {output} seconds.'
                case 'hours to minutes':
                    output = round(float(input_value) * 60.0,2)
                    output_string = f'{input_value} hours are {output} minutes.'
                case 'hours to days':
                    output = round(float(input_value) / 24.0,2)
                    output_string = f'{input_value} hours are {output} days.'
                case 'days to seconds':
                    output = round(float(input_value) * 86400.0,2)
                    output_string = f'{input_value} hours are {output} seconds.'
                case 'days to minutes':
                    output = round(float(input_value) * 1440.0,2)
                    output_string = f'{input_value} hours are {output} minutes.'
                case 'days to hours':
                    output = round(float(input_value) * 24.0,2)
                    output_string = f'{input_value} hours are {output} hours.'

            window['-OUTPUT-'].update(output_string)
        else:
            window['-OUTPUT-'].update('Please insert a number!')

    
window.close()