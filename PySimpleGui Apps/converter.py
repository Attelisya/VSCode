import PySimpleGUI as sg

sg.theme('Dark Blue 4')

units = ['', ['километры в метры', 'килограммы в граммы', 'секунды в минуты']]

layout = [
    [sg.Text('Добро пожаловать в конвертатор, выберите из списка что нужно конвертировать и введите число')],
    [
        sg.Input(key = '-INPUT-', expand_x= 4), 
        sg.Spin(['километры в метры', 'килограммы в граммы', 'секунды в минуты'], key = '-UNITS-', right_click_menu=units), 
        sg.Button('Конвертация', key = '-CONVERT-')
    ],
    [sg.Text('Выходные значения', key = '-OUTPUT-')]
]

window = sg.Window('Конвертация', layout, alpha_channel=0.9)

while True:
    event, values = window.read()
    
    if event == sg.WIN_CLOSED:
        break
    
    if event == '-CONVERT-':
        input_value = values['-INPUT-']
        if input_value.isnumeric():
            match values['-UNITS-']:
                case 'километры в метры':
                    output = round(float(input_value) * 100, 2)
                    output_string = f'в {input_value} км {output} метров.'
                case 'килограммы в граммы':
                    output = round(float(input_value) * 1000, 2)
                    output_string = f'в {input_value} кг {output} грамм.'
                case 'секунды в минуты':
                    output = round(float(input_value) / 60, 2)
                    output_string = f'в {input_value} сек {output} минут.'
 
            window['-OUTPUT-'].update(output_string)
        else:
            window['-OUTPUT-'].update('Введите число!')
    
    match event:
        case 'километры в метры':
            window['-UNITS-'].update('километры в метры')
        case 'килограммы в граммы':
            window['-UNITS-'].update('килограммы в граммы')
        case 'секунды в минуты':
            window['-UNITS-'].update('секунды в минуты')
    
window.close()