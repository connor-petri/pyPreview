import PySimpleGUI as sg
import os

from resources.stylesheet import stylesheet


def make_import_window():

    si, f = stylesheet()

    import_frame = [[
        sg.Input(k="-file_path-", s=si["box1"], font=f["b1"]), 
        sg.FileBrowse("Browse", target="-file_path-", k="-filebrowse-", font=f["b1"]), 
        sg.B("Import .csv", k="-import-", font=f["b1"])
        ]]

    export_frame = [[
        sg.Input(k="-export_path-", s=si["box1"], font=f["b1"]), 
        sg.FileSaveAs("Save as", target="-export_path-", k="-save_as-", font=f["b1"]), 
        sg.B("Export .csv", k="-export-", font=f["b1"])
        ]]

    layout = [
        [sg.Frame("Import .csv", import_frame, font=f["h2"])],
        [sg.Frame("Export to .csv", export_frame, font=f["h2"])],
        [sg.Push(), sg.Exit(font=f["b1"])]
    ]

    return sg.Window("Import/Export .csv", layout, keep_on_top=True, location=(625, 700)) 


def make_window():


    # Style, theme, and fonts:

    si, f = stylesheet()


    ########################################################################

    # Column 1:

    listbox = [
        [sg.Listbox([], k="-saves-", s=si["listbox"], font=f["b1"], enable_events=True)]
    ]

    col1 = [
        [sg.Push(), sg.Image(source=os.getcwd()+"/resources/logo.png"), sg.Push()],
        [sg.Frame("Saved Previews:", listbox, font=f["h2"])],
        [sg.B("New", k="-new-", font=f["b1"]), sg.B("Delete", k="-delete-", font=f["b1"], border_width=si["frame"]), sg.Push(), sg.Exit(font=f["b1"])],
        [sg.B("Import/Export .csv", k="-csv_menu-", font=f["b1"])]
    ]


    ###########################################################################

    # Column 2:
    
    info = [
        [sg.T("Parent's Name:", font=f["h2"]), sg.Push(), sg.Input(k="-parent_name-", s=si["box1"], font=f["b1"])],
        [sg.T("Child's Name:", font=f["h2"]), sg.Push(), sg.Input(k="-child_name-", s=si["box1"], font=f["b1"])],
        [sg.T("Email:", font=f["h2"]), sg.Push(), sg.Input(k="-email-", s=si["box1"], font=f["b1"])],
        [sg.T("Phone:", font=f["h2"]), sg.Push(), sg.Input(k="-phone-", s=si["box1"], font=f["b1"])],
        [sg.T("Preview Class:", font=f["h2"]), sg.Push(), sg.Input(k="-preclass-", s=si["box1"], font=f["b1"])]
    ]


    pre1 = [
        [sg.Input(s=si["box2"], k="-pre1a-", font=f["b1"]), sg.T("Coming/Left Message", font=f["b1"])],
        [sg.Input(s=si["box2"], k="-pre1b-", font=f["b1"]), sg.T("Completed/No-Show", font=f["b1"])]
    ]


    pre2 =[
        [sg.Input(s=si["box2"], k="-pre2a-", font=f["b1"]), sg.T("Coming/Left Message", font=f["b1"])],
        [sg.Input(s=si["box2"], k="-pre2b-", font=f["b1"]), sg.T("Completed/No-Show", font=f["b1"])]
    ]


    pre3 = [
        [sg.Input(s=si["box2"], k="-pre3a-", font=f["b1"]), sg.T("Coming/Left Message", font=f["b1"])],
        [sg.Input(s=si["box2"], k="-pre3b-", font=f["b1"]), sg.T("Completed/No-Show", font=f["b1"])]
    ]


    col2 = [
        [sg.Frame("Info:", layout=info, font=f["h2"], border_width=si["frame"]), sg.Push(),],
        [sg.Push(), sg.Frame("1st Preview:", layout=pre1, font=f["h2"], border_width=si["frame"]), sg.Push()],
        [sg.Push(), sg.Frame("2nd Preview:", layout=pre2, font=f["h2"], border_width=si["frame"]), sg.Push()],
        [sg.Push(), sg.Frame("3rd Preview:", layout=pre3, font=f["h2"], border_width=si["frame"]), sg.Push()],
        [sg.HSep()],
        [sg.Push(), sg.Frame("Preview Notes", layout=[[sg.Multiline(s=si["multiline"], k="-notes-", font=f["b1"])]], font=f["h2"]), sg.Push()],
        [sg.Push(), sg.Frame("Follow-up Call Date & Notes", layout=[[sg.Multiline(s=si["multiline"], k="-followup-", font=f["b1"])]], font=f["h2"]), sg.Push()],
        [sg.Push(), sg.B("Save Preview", k="-save-", font=f["b1"]), sg.Push()]
    ]


    #########################################################################


    layout = [
        [sg.Column(col1), sg.VSep(), sg.Column(col2)],
    ]


    return sg.Window("pyPreview", layout)