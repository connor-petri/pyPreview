import datetime
import os

import PySimpleGUI as sg

from resources.csv_functions import export_csv


def make_backup(save_dict: dict, max_files: int = 15):
    try:

        dir = os.getcwd() + "/backups"

        try:
            os.mkdir(dir)
        except FileExistsError: pass

        filename = "Backup " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        path = dir + "/" + filename

        export_csv(save_dict, path, False)

        if len(os.listdir(dir)) >= max_files:
            while len(os.listdir(dir)) > max_files:
                os.remove(dir + "/" + os.listdir(dir)[-1])

    except Exception as e:
        print(f"{e.__class__.__name__} raised in resources.functions.init(): ", e)
        sg.Popup(f"{e.__class__.__name__} raised in resouces.functions.init(): ", e, title="Error", keep_on_top=True) 