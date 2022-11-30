import PySimpleGUI as sg

def stylesheet():

    sg.LOOK_AND_FEEL_TABLE['gymboree'] = {
        'BACKGROUND': '#F89619',
        'TEXT': '#FFFFFF',
        'INPUT': '#FFFFFF',
        'TEXT_INPUT': '#000000',
        'SCROLL': '#99CC99',
        'BUTTON': ('#003333', '#FFCC66'),
        'PROGRESS': ('#D1826B', '#CC8019'),
        'BORDER': 1, 'SLIDER_DEPTH': 0, 
        'PROGRESS_DEPTH': 0, }


    sg.theme("gymboree")


    # Sizes (for elements):

    si = {
        "listbox": (25, 35),
        "box1": (25, 1),
        "box2": (15, 1),
        "multiline": (30, 10),
        "frame": 2
    }

    # Fonts
    f = {
        "h1": ("Ariel", 24, "bold"),
        "h2": ("Ariel", 16, "bold"),
        "b1": ("Ariel", 16),
        "b2": ("Ariel", 12)
    }

    return si, f