

import subprocess
from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import mysql.connector


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\RUPAM DAS\Desktop\CLLG\build\assets\frame0")

FILE_PATH_GUI11 = r"C:\Users\RUPAM DAS\Desktop\CLLG\build\gui11.py"
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def display_prescription():
    patient_id = entry_2.get()

    # Establish database connection
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="rupamdas",
        database="hospitalmanagement"
    )
    cursor = conn.cursor()

    # Fetch prescription details for the given patient ID
    query = "SELECT DOCTOR_ID, DISCRIPTION, DATE_TIME FROM PRESCRIPTION WHERE PATIENTS_ID = %s"
    cursor.execute(query, (patient_id,))
    prescription_result = cursor.fetchall()

    # If prescription details exist, display them in the Text widget
    if prescription_result:
        prescription_text = ""
        for row in prescription_result:
            doctor_id, description, date_time = row
            prescription_text += f"Doctor ID: {doctor_id}\nDescription: {description}\nDate Time: {date_time}\n\n"
        
        entry_1.delete("1.0", "end")  # Clear previous text
        entry_1.insert("end", prescription_text)
    else:
        entry_1.delete("1.0", "end")  # Clear previous text
        entry_1.insert("end", "No prescription found for this patient")

    # Close database connection
    cursor.close()
    conn.close()

def button_2_clicked():
    subprocess.Popen(['python', FILE_PATH_GUI11])
    window.iconify() 
window = Tk()
window.title("Your Window Title")
window_width = 900
window_height = 600

# Get the screen width and height
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# Calculate the position for the window to be centered
x_coordinate = (screen_width / 2) - (window_width / 2)
y_coordinate = (screen_height / 2) - (window_height / 2)

# Set the window size and position
window.geometry(f"{window_width}x{window_height}+{int(x_coordinate)}+{int(y_coordinate)}")
window.configure(bg="#FFFFFF")



canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 600,
    width = 900,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1111111111.png"))
image_1 = canvas.create_image(
    450.0,
    300.0,
    image=image_image_1
)

canvas.create_rectangle(
    95.0,
    162.0,
    792.0,
    561.0,
    fill="#D9D9D9",
    outline="")

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1111111111.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=display_prescription,
    relief="flat"
)
button_1.place(
    x=583.0,
    y=202.0,
    width=154.0,
    height=41.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2111111111.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=button_2_clicked,
    relief="flat"
)
button_2.place(
    x=630.0,
    y=505.0,
    width=107.0,
    height=41.0
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1111111111.png"))
entry_bg_1 = canvas.create_image(
    443.0,
    377.0,
    image=entry_image_1
)
entry_1 = Text(
    bd=0,
    bg="#FFF7F7",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=119.0,
    y=259.0,
    width=648.0,
    height=234.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2111111111.png"))
entry_bg_2 = canvas.create_image(
    331.5,
    222.5,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#FFF7F7",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=220.0,
    y=202.0,
    width=223.0,
    height=39.0
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2111111111.png"))
image_2 = canvas.create_image(
    450.0,
    88.0,
    image=image_image_2
)

canvas.create_text(
    413.0,
    176.0,
    anchor="nw",
    text="Pharmacy",
    fill="#000000",
    font=("Inter", 15 * -1)
)

canvas.create_text(
    134.0,
    213.0,
    anchor="nw",
    text="Patient Id:",
    fill="#000000",
    font=("Inter", 15 * -1)
)
window.resizable(False, False)
window.mainloop()
