
import subprocess

from pathlib import Path
from datetime import datetime, timedelta
import mysql.connector
# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
FILE_PATH_GUI9 = r"C:\Users\RUPAM DAS\Desktop\CLLG\build\gui9.py"

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\RUPAM DAS\Desktop\CLLG\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)
def button_1_clicked():
    subprocess.Popen(['python', FILE_PATH_GUI9])
    window.iconify()
def fetch_appointments():
    # Connect to the database
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="rupamdas",
        database="hospitalmanagement"
    )
    cursor = conn.cursor()

    # Get today's date and format it
    today_date = datetime.now().strftime("%Y-%m-%d")

    # Fetch appointments with today's date from the APPOINTMENTS table
    query = "SELECT * FROM APPOINTMENTS WHERE DATE_FORMAT(DATE_TIME, '%Y-%m-%d') = %s"
    cursor.execute(query, (today_date,))
    appointments = cursor.fetchall()

    # Close database connection
    cursor.close()
    conn.close()

    # Display fetched appointments in the entry_1 Text widget
    if appointments:
        entry_1.delete(1.0, "end")  # Clear previous content
        for appointment in appointments:
            # Append appointment details to the entry_1 Text widget
            appointment_str = f"Patient ID: {appointment[0]}\nDisease: {appointment[1]}\n" \
                              f"Qualification: {appointment[2]}\nDate and Time: {appointment[3]}\n\n"
            entry_1.insert("end", appointment_str)
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
    file=relative_to_assets("image_11111111.png"))
image_1 = canvas.create_image(
    450.0,
    300.0,
    image=image_image_1
)

canvas.create_rectangle(
    17.0,
    146.0,
    878.0,
    491.0,
    fill="#D9D9D9",
    outline="")

button_image_1 = PhotoImage(
    file=relative_to_assets("button_11111111.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=button_1_clicked,
    relief="flat"
)
button_1.place(
    x=634.0,
    y=510.0,
    width=223.0,
    height=41.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_21111111.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=fetch_appointments,
    relief="flat"
)
button_2.place(
    x=37.0,
    y=510.0,
    width=223.0,
    height=41.0
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_21111111.png"))
image_2 = canvas.create_image(
    450.0,
    88.0,
    image=image_image_2
)

canvas.create_text(
    376.0,
    153.0,
    anchor="nw",
    text="Today’s Patients List",
    fill="#000000",
    font=("Inter", 15 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_11111111.png"))
entry_bg_1 = canvas.create_image(
    447.5,
    323.0,
    image=entry_image_1
)
entry_1 = Text(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=38.0,
    y=178.0,
    width=819.0,
    height=288.0
)
window.resizable(False, False)
window.mainloop()
