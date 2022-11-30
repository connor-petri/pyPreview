import csv
import datetime
import os

import PySimpleGUI as sg

from resources.preview import Preview
from resources.functions import dump_save_data
from resources.stylesheet import stylesheet


def import_csv(window: sg.Window, save_dict: dict, path: str = "./resources/data.csv", name_row_num: int = 3):
    try:

        si, f = stylesheet()
    
        with open(path, "r", encoding="utf8") as file:
            csv_reader = csv.reader(file, delimiter=",")
            line_count = 0

            for row in csv_reader:

                if line_count > (name_row_num - 1):
                    preview_data = {
                        "-parent_name-": row[0],
                        "-child_name-": row[1],
                        "-email-": row[2],
                        "-phone-": row[3],
                        "-preclass-": row[4],
                        "-pre1a-": row[5],
                        "-pre1b-": row[6],
                        "-pre2a-": row[7],
                        "-pre2b-": row[8],
                        "-pre3a-": row[9],
                        "-pre3b-": row[10],
                        "-notes-": row[11],
                        "-followup-": row[12]
                    }

                    preview = Preview(preview_data)
                    save_dict[preview.title] = preview
                    
                line_count += 1

        dump_save_data(save_dict)

    except IndexError:
        sg.Popup("File needs to be .csv", title="Error", keep_on_top=True, font=f["b1"])
    except UnicodeDecodeError:
        sg.Popup("File needs to be .csv", title="Error", keep_on_top=True, font=f["b1"])
    

    except Exception as e:
        print(f"{e.__class__.__name__} raised in resources.csv_functions.import_csv(): ", e)
        sg.Popup(f"{e.__class__.__name__} raised in resouces.csv_functions.import_csv(): \n\nMost likely a file other than a .csv was imported. Make sure file is of type .csv.", e, title="Error", keep_on_top=True, font=f["b1"])


def export_csv(save_dict: dict, path: str, show_message: bool = True):
    try:

        si, f = stylesheet()

        dump_save_data(save_dict)

        with open(path, "w", encoding="utf8") as file:
            writer = csv.writer(file, delimiter=",")

            writer.writerow(["", "", "", "", "CM - Coming", "LM - Left Message", "C - Completed", "NS - No Show", "", "", "", "", ""])
            writer.writerow(["", "", "", "", "", "", "", "", "", "", "", "", ""])
            writer.writerow(["Parent Name", "Child Name", "Email", "Phone", "Preview Class", "1st Preview CM/LM", "1st Preview C/NS", "2nd Preview CM/LM", "2nd Preview C/NS", "3rd Preview CM/LM", "3rd Preview C/NS", "Notes", "Followup Date and Notes"])

            for p in save_dict.values():
                p: Preview = p
                writer.writerow([p.parent_name, p.child_name, p.email, p.phone, p.preclass, p.pre1a, p.pre1b, p.pre2a, p.pre2b, p.pre3a, p.pre3b, p.notes, p.followup])

        if show_message:
            sg.Popup(f"Save data exported to {os.getcwd() + path[1:]}", font=("Ariel", 16), keep_on_top=True)


    except FileNotFoundError:
        sg.Popup("Please use the Save As button to select your file then press Export .csv", title="Error", keep_on_top=True, font=f["b1"])

    except Exception as e:
        print(f"{e.__class__.__name__} raised in resources.csv_functions.export_csv(): ", e)
        sg.Popup(f"{e.__class__.__name__} raised in resouces.csv_functions.export_csv(): ", e, title="Error", keep_on_top=True) 