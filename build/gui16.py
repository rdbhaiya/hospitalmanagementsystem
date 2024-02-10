
import subprocess
from pathlib import Path
from tkcalendar import DateEntry
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import mysql.connector
FILE_PATH_GUI12 = r"C:\Users\RUPAM DAS\Desktop\CLLG\build\gui12.py"
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\RUPAM DAS\Desktop\CLLG\build\assets\frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)
def button_1_clicked():
    subprocess.Popen(['python', FILE_PATH_GUI12])
    window.iconify()
def calculate_total_charges():
    # Retrieve the date from the DateEntry widget
    selected_date = dob_entry.get_date()

    # Connect to the database
    db_config = {
        "host": "localhost",
        "user": "root",
        "password": "rupamdas",  # Replace with your actual password
        "database": "hospitalmanagement"   # Replace with your actual database name
    }
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    # Prepare the SQL query to get the sum of total charges for the selected date
    query = f"SELECT SUM(TOTAL_CHARGES) FROM bill WHERE DATE(DATE_TIME) = '{selected_date}'"

    # Execute the query
    cursor.execute(query)

    # Fetch the result
    total_charges = cursor.fetchone()[0]
    if total_charges is None:
        total_charges = 0  # If there are no charges for the date, set total_charges to 0

    # Display the total charges in the Text widget
    entry_1.delete(1.0, "end")
    entry_1.insert("end", f"Total Charges for {selected_date}: {total_charges}")

    # Close the cursor and connection
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

dob_entry = DateEntry(window, date_pattern='yyyy-mm-dd')
dob_entry.place(x=390, y=185, width=253,height=33)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1admin4.png"))
image_1 = canvas.create_image(
    450.0,
    300.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2admin4.png"))
image_2 = canvas.create_image(
    450.0,
    80.0,
    image=image_image_2
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1admin4.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=button_1_clicked,
    relief="flat"
)
button_1.place(
    x=426.0,
    y=411.0,
    width=97.0,
    height=40.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2admin4.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=calculate_total_charges,
    relief="flat"
)
button_2.place(
    x=577.0,
    y=411.0,
    width=97.0,
    height=40.0
)

canvas.create_rectangle(
    230.0,
    136.0,
    674.0,
    380.0,
    fill="#D9D9D9",
    outline="")

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1admin4.png"))
entry_bg_1 = canvas.create_image(
    453.5,
    279.0,
    image=entry_image_1
)
entry_1 = Text(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=264.0,
    y=240.0,
    width=379.0,
    height=76.0
)

canvas.create_text(
    334.0,
    193.0,
    anchor="nw",
    text="Date:",
    fill="#000000",
    font=("Inter SemiBold", 16 * -1)
)

canvas.create_text(
    376.0,
    145.0,
    anchor="nw",
    text="Total Earning",
    fill="#000000",
    font=("Inter SemiBold", 20 * -1)
)
window.resizable(False, False)
window.mainloop()
