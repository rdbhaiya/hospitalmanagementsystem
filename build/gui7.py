
import subprocess
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import mysql.connector

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\RUPAM DAS\Desktop\CLLG\build\assets\frame0")

FILE_PATH_GUI4 = r"C:\Users\RUPAM DAS\Desktop\CLLG\build\gui4.py"
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "rupamdas",
    "database": "hospitalmanagement"
}

def clear_entry_fields():
    subprocess.Popen(['python', FILE_PATH_GUI4])
    window.iconify()
def display_total_charge():
    # Get the entered Patient ID
    patient_id = entry_1.get()

    # Connect to the database
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    query = "SELECT TOTAL_CHARGES FROM BILL WHERE PATIENTS_ID = %s"
    cursor.execute(query, (patient_id,))
    result = cursor.fetchone()

    if result:
        total_charges = result[0]
        entry_3.delete(1.0, "end")  # Clear the existing text in entry_3
        entry_3.insert("end", 'Rs '+ str(total_charges))  # Display total charges in entry_3
    else:
        entry_3.delete(1.0, "end")  # Clear the existing text in entry_3
        entry_3.insert("end", "No data Found")

    cursor.close()
    conn.close()

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
    file=relative_to_assets("image_1problem.png"))
image_1 = canvas.create_image(
    450.0,
    300.0,
    image=image_image_1
)

canvas.create_rectangle(
    265.0,
    215.0,
    632.0,
    495.0,
    fill="#BBA8A8",
    outline="")

canvas.create_text(
    438.0,
    236.0,
    anchor="nw",
    text="Bill",
    fill="#000000",
    font=("Inter", 15 * -1)
)

canvas.create_text(
    292.0,
    376.0,
    anchor="nw",
    text="Total Charges:",
    fill="#000000",
    font=("Inter", 12 * -1)
)


canvas.create_text(
    292.0,
    289.0,
    anchor="nw",
    text="Patient ID:",
    fill="#000000",
    font=("Inter", 12 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1problem.png"))
entry_bg_1 = canvas.create_image(
    505.00672149658203,
    297.2104377746582,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=402.0,
    y=284.0,
    width=206.01344299316406,
    height=24.420875549316406
)


entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3problem.png"))
entry_bg_3 = canvas.create_image(
    505.00672149658203,
    383.2104377746582,
    image=entry_image_3
)
entry_3 = Text(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_3.place(
    x=402.0,
    y=370.0,
    width=206.01344299316406,
    height=24.420875549316406
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1problem.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=clear_entry_fields,
    relief="flat"
)
button_1.place(
    x=402.0,
    y=416.0,
    width=81.41848754882812,
    height=36.154876708984375
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2problem.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=display_total_charge,
    relief="flat"
)
button_2.place(
    x=527.0,
    y=416.0,
    width=81.41848754882812,
    height=36.154876708984375
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2problem.png"))
image_2 = canvas.create_image(
    450.0,
    95.0,
    image=image_image_2
)
window.resizable(False, False)
window.mainloop()
