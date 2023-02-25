import json
import os.path
from tkinter import messagebox

from customtkinter import *


# noinspection SpellCheckingInspection
def export_json(name_entry: CTkEntry, description_entry: CTkEntry, image_entry: CTkEntry, order_entry: CTkEntry, defaultOrder: list):
    if not name_entry.get():
        messagebox.showwarning("Name Required", "A name is required for your medal.\nIf this is bypassed, it will default to something else.")
        return

    file_path = filedialog.asksaveasfilename(filetypes=[("JSON files", "*.json")], defaultextension=".json", initialdir="./CMCG")
    if not file_path:
        return

    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            existing_config = json.load(file)

        if "_aOrder" not in existing_config:
            messagebox.showwarning("This is not valid", "The file you plan to replace is not a valid medals config file.\nPlease only choose valid files.")
            return

        if order_entry.get() in existing_config["_aMedals"] and existing_config["_aOrder"]:
            confirm = messagebox.askyesno("Duplicate Medal", "A medal with the same order was found, would you like to update it?")
            if not confirm:
                return
        elif order_entry.get() == "":
            if "DEFAULT" in existing_config["_aMedals"] and existing_config["_aOrder"]:
                confirm = messagebox.askyesno("Duplicate Medal", "A medal with the same order was found, would you like to update it?")
                if not confirm:
                    return

            # def return_default():
            #     return "DEFAULT"

            # order_entry.get = return_default

        existing_config["_aMedals"][order_entry.get().upper() or "DEFAULT"] = {
            "hasLevels": True,
            "url": image_entry.get() or "https://images.gamebanana.com/img/ico/games/banana.gif",
            "metaData": {
                "title": name_entry.get() or "This is required to be filled out in CMCG.",
                "description": description_entry.get() or None
            }
        }

        if order_entry.get() and order_entry.get() != "DEFAULT" and order_entry.get() not in existing_config["_aOrder"] and existing_config["_aMedals"]:
            existing_config["_aOrder"].append(order_entry.get().upper())
            for order in defaultOrder:
                existing_config["_aOrder"].remove(order)
                existing_config["_aOrder"].append(order)
        else:
            if "DEFAULT" not in existing_config["_aOrder"] and existing_config["_aMedals"]:
                existing_config["_aOrder"].append("DEFAULT")
                for order in defaultOrder:
                    existing_config["_aOrder"].append(order)

        # for key, var in checkbox_vars.items():
        #     if not var.get():  # only add unchecked checkboxes to the config dictionary
        #         existing_config["_aOrder"].append(key)

        # Write the updated JSON back to the file
        with open(file_path, "w") as file:
            json.dump(existing_config, file, indent=4)
    else:
        config = {
            "_aOrder": [],
            "_aMedals": {
                order_entry.get().upper() or "DEFAULT": {
                    "hasLevels": True,
                    "url": image_entry.get() or "https://images.gamebanana.com/img/ico/games/banana.gif",
                    "metaData": {
                        "title": name_entry.get() or "This is required to be filled out in CMCG.",
                        "description": description_entry.get() or None
                    }
                }
            }
        }

        if order_entry.get() and order_entry.get() != "DEFAULT" and order_entry.get() not in config["_aOrder"] and config["_aMedals"]:
            config["_aOrder"].append(order_entry.get().upper())
            for order in defaultOrder:
                config["_aOrder"].append(order)
        else:
            if "DEFAULT" not in config["_aOrder"] and config["_aMedals"]:
                config["_aOrder"].append("DEFAULT")
                for order in defaultOrder:
                    config["_aOrder"].append(order)

        # for key, var in checkbox_vars.items():
        #     if not var.get():  # only add unchecked checkboxes to the config dictionary
        #         config["_aOrder"].append(key)

        with open(file_path, 'w') as file:
            json.dump(config, file, indent=4)

    messagebox.showinfo("Successful Operation!", f"The \"{name_entry.get()}\" medal has been successfully added/updated in your config!")
    name_entry.delete(0, END)
    description_entry.delete(0, END)
    image_entry.delete(0, END)
    order_entry.delete(0, END)
