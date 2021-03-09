import PySimpleGUI as sg
class Layout:
    def __init__(self,list):
        sg.change_look_and_feel('Light Blue 3')

    def generate_layout(text, listofstuff):

        if len(listofstuff) <= 19:  # If everything fits in one screen, hide the scroll bars
            scrollable_flag = False
        elif 19 < len(listofstuff) <= 51:   # item_count > 19 and item_count <= 37
            scrollable_flag = True
        else:
            print("This is actually a problem and it will not be displayed correctly. :~/")

            def generate_button(
                    stuffinlist):  # Adds the text to be displayed on the button (Which is also the value of the button), and gives it properties (size, visibility..)
                # #-----DEFAULT SETTINGS--------------------------##
                button_visib: dict = {'size': (19, 1), 'font': ('Franklin Gothic Book', 12),
                                    'button_color': ("black", "#F8F8F8"), 'visible': True}  # Visible button
                button_visib_over: dict = {'size': (19, 2), 'font': ('Franklin Gothic Book', 12),
                                        'button_color': ("black", "#F8F8F8"), 'visible': True}  # Over sized button
                button_invis: dict = {'size': (19, 1), 'font': ('Franklin Gothic Book', 12),
                                    'button_color': ("black", "#F8F8F8"), 'visible': False}  # Invisible button

                if (stuffinlist != ""):  # If not an empty character, we read it.
                    if (len(stuffinlist) > 25):  # If string is too long, we make the box double
                        return sg.Button(stuffinlist, **button_visib_over)
                    else:
                        return sg.Button(stuffinlist, **button_visib)
                else:                                                       # If it is an empty character, we turn the visibility off
                    return sg.Button(stuffinlist, **button_invis)

        col = []
        for i in range(1, len(listofstuff), 2):
            if i+1 <= len(listofstuff)-1:
                col += [[generate_button(listofstuff[i]),
                        generate_button(listofstuff[i+1])]]
            else:
                col += [[generate_button(listofstuff[i]), generate_button("")]]

        top = [[sg.Button("Back", size=(5, 1), font=('Franklin Gothic Book', 12), button_color=("black", "#84848a"), visible=True),
                sg.Text(text, size=(34, 1), justification='right', background_color="#272533",  # Layer 2:  text question (variable) and back button
                        text_color='white', font=('Franklin Gothic Book', 12))]]

        # This is the layout of the GUI
        layout: list = [
            [sg.Text('Program Opener ' + version_code, size=(50, 1), justification='right', background_color="#272533",
                    # Layer 1:  Program opener <version>
                    text_color='white', font=('Franklin Gothic Book', 12, 'bold'))],
            [sg.Column(top, background_color="#272533")],
            [sg.Column(col, size=(390, 400), background_color="#272533",
                    scrollable=scrollable_flag, vertical_scroll_only=scrollable_flag)]

        ]
        return layout

    # Start or refresh the window(Text for the window, list of things)
    def new_window(text, varRead):
        global prevWinLoc
        sizelayout = get_size_layout()
        window: object = sg.Window('Program Opener ' + version_code, margins=(3, 2), layout=generate_layout(text, varRead),
                                background_color="#272533", size=sizelayout, return_keyboard_events=False,
                                location=prevWinLoc, icon=popenericon)

        event, values = window.read()

        if event is None:
            window.close()
            sys.exit()
        else:
            prevWinLoc = window.CurrentLocation()
            print("DEBUG: Window location: " + str(prevWinLoc))
            window.close()
            return (event)
