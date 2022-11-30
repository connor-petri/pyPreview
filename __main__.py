import PySimpleGUI as sg

import resources.functions as func
from resources.preview import Preview
from resources.csv_functions import import_csv, export_csv
from resources.window import make_import_window
from resources.backup import make_backup


def import_export_window(save_dict: dict):
    try:

        instructions = "Instructions:\n\nImporting:\nClick Browse and select a .csv file, then click Import.csv to import it. MAKE SURE THE ROW WITH COLUMN NAMES IS ROW 3.\n\nExporting:\nClick Save As and choose there you want to save the exported .csv file, then click Export .csv to export it."

        sg.Popup(instructions, title="Instructions", font=("Ariel", 14))

        ################################################################

        window = make_import_window()

        while True:

            event, values = window.read()
            print("\n", event, values)

            if event in (sg.WIN_CLOSED, "Exit"):
                break

            match event:
                    case "-import-":
                        import_csv(window, save_dict, values["-file_path-"])
                        break

                    case "-export-":
                        export_csv(save_dict, values["-save_as-"])
                        break

        window.close()

    except Exception as e:
        print(f"{e.__class__.__name__} raised in __main__.main(): ", e)
        sg.Popup(f"{e.__class__.__name__} raised in __main__.main(): ", e, title="Error", keep_on_top=True) 



def main():
    try:

        # initialization - loads save data and makes window.
        save_dict, window = func.init()

        # Makes backup of save data and deletes old ones
        make_backup(save_dict)


        ####################################################################################

    
        while True:

            event, values = window.read()
            print("\n", event, values) # Used for debugging. Comment out line when ready.


            ################################################################################


            if event in (sg.WIN_CLOSED, "Exit"):
                break


            # Event switch statement. Checks what the event is and responds accordingly
            match event:

                # checks for an event from the listbox and updates the form
                case "-saves-":
                    preview: Preview = save_dict[values["-saves-"][0]]
                    func.update_form(window, preview.unpack())


                # Listbox Functions
                case "-new-":
                    func.add_new_preview(window, save_dict)

                case "-delete-":
                    try:
                        confirmation = sg.popup_yes_no("Are you sure you want to delete " + values["-saves-"][0] + "?", font=("Ariel", 16), keep_on_top=True)

                        if confirmation == "Yes":
                            func.delete_preview(window, save_dict, values["-saves-"][0])

                    except IndexError:
                        print("Expeced IndexError in __main__.main().")

                    except Exception as e:
                        print(e)


                # Save Button
                case "-save-":
                    func.save_preview(window, save_dict, values)

                case "-csv_menu-":
                    import_export_window(save_dict)
                    window["-saves-"].update(save_dict)


    except Exception as e:
        print(f"{e.__class__.__name__} raised in __main__.main(): ", e)
        sg.Popup(f"{e.__class__.__name__} raised in __main__.main(): ", e, title="Error", keep_on_top=True) 


    finally:
        func.dump_save_data(save_dict)
        make_backup(save_dict)
        window.close()


if __name__ == "__main__":
    main()
    exit()


#########################################################################################
#########################################################################################
#########################################################################################
#########################################################################################
#########################################################################################

# Bugs:

# To-Do:
# - figure out packaging
# - test packaging


# Done:
# - GUI
# - Preview object
# - save data functions
# - Update form functionality
# - add preview
# - delete preview
# - save preview
# - delete confirmation popup
# - save preview popup
# - csv import functionality
# - finalize exception handeling
# - csv export functionality
# - import/export instruction popup
# - backup functionality
# - test, bug fix, and make error messages