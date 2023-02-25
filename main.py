from customtkinter import *

from interface import VERSION, build_application

set_appearance_mode("dark")
set_default_color_theme("dark-blue")

app = CTk()
app.title(f"Community Medals Config Generator (v{VERSION})")
# app.geometry("900x600")
app.geometry("500x340")
app.wm_iconbitmap("icon.ico")

build_application(app)

# noinspection SpellCheckingInspection
if not os.path.exists("CMCG"):
    # noinspection SpellCheckingInspection
    os.makedirs("CMCG")

app.mainloop()
