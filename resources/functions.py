import json
import re
import os
import shutil
import datetime

import PySimpleGUI as sg

from resources.preview import Preview
from resources.window import make_window


#########################################################


def update_form(window: sg.Window, preview_data: dict={}):
    try:
        for key, value in preview_data.items():
            window[key].update(value)

    except Exception as e:
        print(f"{e.__class__.__name__} raised in resources.functions.update_form(): ", e)
        sg.Popup(f"{e.__class__.__name__} raised in resouces.functions.update_form(): ", e, title="Error", keep_on_top=True)


def add_new_preview(window: sg.Window, save_dict: dict):
    try:
        # Default parameters for the new preview object. Needed because I pass a dict to the object.
        default_dict = {
            "-parent_name-": "New Parent",
            "-child_name-": "New Child",
            "-email-": "",
            "-phone-": "",
            "-preclass-": "",
            "-pre1a-": "",
            "-pre1b-": "",
            "-pre2a-": "",
            "-pre2b-": "",
            "-pre3a-": "",
            "-pre3b-": "",
            "-notes-": "",
            "-followup-": ""
        }
        
        new_preview = Preview(default_dict)
        
        # Figures out if there are empty save and how many there are.
        new_num = 0
        for value in save_dict.values():
            match1 = re.match("^New Parent - New Child", value.title)
            match2 = re.match("^New Parent [0-9] - New Child ([0-9])$", value.title)

        if (match1 is not None) and (match2 is None):
            new_num = 1
        elif match2 is not None:
            new_num = int(match2.group(1)) + 1


        if new_num > 0:
            new_preview.parent_name = f"New Parent {new_num}"
            new_preview.child_name = f"New Child {new_num}"
            new_preview.title = f"New Parent {new_num} - New Child {new_num}"

        save_dict[new_preview.title] = new_preview

        window['-saves-'].update(save_dict)

    except Exception as e:
        print(f"{e.__class__.__name__} raised in resources.functions.add_new_preview: ", e)
        sg.Popup(f"{e.__class__.__name__} raised in resouces.functions.add_new_preview: ", e, title="Error", keep_on_top=True)


def delete_preview(window: sg.Window, save_dict: dict, key: str):
    try:
        save_dict.pop(key)
        window['-saves-'].update(save_dict)

    except Exception as e:
        sg.Popup(f"{e.__class__.__name__} raised in resouces.functions.delete_preview(): ", e, title="Error", keep_on_top=True)


def save_preview(window: sg.Window, save_dict: dict, values: dict):
    try:
        preview: Preview = save_dict[values["-saves-"][0]]

        preview.set_values(values["-parent_name-"], values["-child_name-"], values["-email-"], values["-phone-"], values["-preclass-"], values["-pre1a-"], values["-pre1b-"], values["-pre2a-"], values["-pre2b-"], values["-pre3a-"], values["-pre3b-"], values["-notes-"], values["-followup-"])

        save_dict.pop(values["-saves-"][0])
        save_dict[preview.title] = preview

        window["-saves-"].update(save_dict)

        sg.Popup("Save Succesful!", font=("Ariel", 16), auto_close=True, auto_close_duration=5, keep_on_top=True, any_key_closes=True)


    except KeyError as e:
        print("KEYERROR: Possibly expected KeyError in save_preview() in functions.py | KeyError:", e)
    except IndexError as e:
        print("INDEXERROR: Possibly expected IndexError in save_preview() in functions.py | IndexError:", e)

    except Exception as e:
        print(f"{e.__class__.__name__} raised in resources.functions.save_preview(): ", e)
        sg.Popup(f"{e.__class__.__name__} raised in resouces.functions.save_preview(): ", e, title="Error", keep_on_top=True)
    




#########################################################

# Save file functions:

def load_save_data(path: str = "./resources/save_data.json"):
    try:
        with open(path, "r", encoding="utf8") as file:
            return json.load(file)["save data"]

    except Exception as e:
        print(f"{e.__class__.__name__} raised in resources.functions.load_save_data(): ", e)
        sg.Popup(f"{e.__class__.__name__} raised in resouces.functions.load_save_data(): ", e, title="Error", keep_on_top=True)


def dump_save_data(save_dict: dict, path: str = "./resources/save_data.json"):
    try:
        data = {}

        for preview in save_dict.values():
            data[preview.title] = preview.unpack()


        with open(path, "w", encoding="utf8") as file:
            json_obj = json.dumps({"save data": data}, indent=4)
            file.write(json_obj)

    except Exception as e:
        print(f"{e.__class__.__name__} raised in resources.functions.dump_save_data(): ", e)
        sg.Popup(f"{e.__class__.__name__} raised in resouces.functions.dump_save_data(): ", e, title="Error", keep_on_top=True)



#########################################################

# Misc functions:

def preview_generator(data:dict):

    for preview_data in data.values():
        yield Preview(preview_data)


#########################################################


def init():
    try:

        data = load_save_data() # Loads save data
        save_dict = {}
        
        # Generates dict of preview.title: preview object
        for preview in preview_generator(data):
            save_dict[preview.title] = preview


        window = make_window().Finalize() # initializes the window
        window["-saves-"].update(save_dict.keys()) # initializes the listbox with save data


        return save_dict, window

    except Exception as e:
        print(f"{e.__class__.__name__} raised in resources.functions.init(): ", e)
        sg.Popup(f"{e.__class__.__name__} raised in resouces.functions.init(): ", e, title="Error", keep_on_top=True) 