import json

from customtkinter import *

from manage import export_json

VERSION = "1.0"


def build_application(app):
    # Other Funcs
    # def check_or_uncheck():
    #     all_checked = all(var.get() for var in checkbox_vars.values())
    #
    #     if all_checked:
    #         for var in checkbox_vars.values():
    #             var.set(False)
    #         check_button.configure(hover_color="green", border_color="green")
    #     else:
    #         for var in checkbox_vars.values():
    #             var.set(True)
    #         check_button.configure(hover_color="red", border_color="red")

    # Top Stuff
    # noinspection SpellCheckingInspection
    # title = CTkLabel(master=app, text=f"CMCG v{VERSION}")
    # title.pack()

    headerFrame = CTkFrame(master=app)
    headerFrame.pack(side="top", fill="x")

    manage_medal = CTkLabel(master=headerFrame, text="Append/Create Custom Medal"
                                                     "\nIf the order doesn't exists, it will automatically be created.", font=('Arial', 16))
    manage_medal.grid(row=0, column=1, padx=60, pady=10)

    # auto_create_label = CTkLabel(master=headerFrame, text="If the order doesn't exists,-\nit will automatically be created.", font=('Arial', 16))
    # auto_create_label.grid(row=1, column=2, padx=60, pady=10)

    # manage_order = CTkLabel(master=headerFrame, text="Manage Configuration Order"
    #                                                  "\nCheck to remove. Uncheck to add.", font=('Arial', 16))
    # manage_order.grid(row=0, column=0, padx=20, pady=10)

    # check_button = CTkButton(master=headerFrame, text="Check/Uncheck All", fg_color="transparent", hover_color="green", border_width=2, border_color="green",
    #                          command=check_or_uncheck)
    # check_button.grid(row=1, column=0)

    # Frames

    # checkboxFrame = CTkScrollableFrame(master=app)
    # checkboxFrame.pack(padx=25, pady=15, ipady=100, side="left", fill="both")

    createFrame = CTkFrame(master=app)
    # createFrame.place(x=280, y=99)
    createFrame.pack(pady=15)

    # Really the rest of the application

    # noinspection SpellCheckingInspection
    # mc_label = CTkLabel(master=main, text="Medals Configuration", font=('Arial', 16))
    # mc_label.pack(ipady=50)

    defaultOrder = [
        'PERSONAL', 'MEDALS_CONTRIBUTOR', 'MEDALS_CLUB_MEMBER', 'AGE', 'CLEARANCE', 'GAME_MANAGER', 'TREEHOUSE', 'RIPE', 'COUNTRY', 'GAME', 'PERSONALITY', 'FURSONALITY',
        'ALIGNMENT', 'CLUB_LEADER', 'STUDIO_LEADER', 'POINTS', 'POSTS', 'EF', 'FEATURES', 'SUBSCRIBERS', 'BUDDIES', 'APPS', 'ARTICLES', 'BLOGS', 'BUGS', 'CONCEPTS', 'GAMEFILES',
        'GUIS', 'IDEAS', 'JAMS', 'MAPS', 'MODELS', 'NEWS', 'POLLS', 'PREFABS', 'PROJECTS', 'QUESTIONS', 'REQUESTS', 'REVIEWS', 'SCRIPTS', 'SKINS', 'SOUNDS', 'SPRAYS', 'SPRITES',
        'TEXTURES', 'THREADS', 'TOOLS', 'TUTORIALS', 'WARES', 'WIKIS', 'WIPS'
    ]

    # checkbox_vars = {k: BooleanVar() for k in defaultOrder}
    # checkboxes = []
    # for i, key in enumerate(defaultOrder):
    #     checkbox_var = checkbox_vars[key]
    #     checkbox = CTkCheckBox(checkboxFrame, text=key, variable=checkbox_var, fg_color="black", hover_color="black")
    #     checkbox.grid(row=i, column=0, sticky='w')
    #     checkboxes.append(checkbox)

    name_label = CTkLabel(master=createFrame, text="Medal Name", font=('Arial', 14))
    name_label.grid(row=0, column=0, padx=15, pady=5)
    name_entry = CTkEntry(master=createFrame)
    name_entry.grid(row=0, column=1, padx=15, pady=5)

    description_label = CTkLabel(master=createFrame, text="Medal Description (Default: None)", font=('Arial', 14))
    description_label.grid(row=1, column=0, padx=15, pady=5)
    description_entry = CTkEntry(master=createFrame)
    description_entry.grid(row=1, column=1, padx=15, pady=5, ipadx=25)

    image_label = CTkLabel(master=createFrame, text="Medal Image (Default: GB Icon)", font=('Arial', 14))
    image_label.grid(row=2, column=0, padx=15, pady=5)
    image_entry = CTkEntry(master=createFrame)
    image_entry.grid(row=2, column=1, padx=15, pady=5)

    order_label = CTkLabel(master=createFrame, text="Medal Order (Default: DEFAULT)", font=('Arial', 14))
    order_label.grid(row=3, column=0, padx=15, pady=5)
    order_entry = CTkEntry(master=createFrame)
    order_entry.grid(row=3, column=1, padx=15, pady=5)

    # Other buttons

    buttonFrame = CTkFrame(master=app)
    buttonFrame.pack(pady=15)

    export_config = CTkButton(master=buttonFrame, text="Export Config (.JSON)", fg_color="transparent", hover_color="purple", border_width=2, border_color="purple",
                              command=lambda: export_json(name_entry, description_entry, image_entry, order_entry, defaultOrder))
    # export_config.place(relx=0.2, rely=0.67, x=200)
    export_config.grid(row=0, column=0, padx=20, pady=20)

    # load_config = CTkButton(master=buttonFrame, text="Load Config (.JSON)", fg_color="transparent", hover_color="pink", border_width=2, border_color="pink",
    #                         command=None)
    # # load_config.place(relx=0.2, rely=0.67, x=360)
    # load_config.grid(row=0, column=1, padx=20, pady=20)
