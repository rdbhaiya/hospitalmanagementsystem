
import subprocess
from pathlib import Path
import mysql.connector
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\RUPAM DAS\Desktop\CLLG\build\assets\frame0")

db_config = {
    "host": "localhost",
    "user": "root",
    "password": "rupamdas",
    "database": "hospitalmanagement"
}
FILE_PATH_GUI12 = r"C:\Users\RUPAM DAS\Desktop\CLLG\build\gui12.py"
def button_1_clicked():
    subprocess.Popen(['python', FILE_PATH_GUI12])
    window.iconify()
def display_table_content_in_entry(table_name):
    # Connect to the database
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    # Fetch content of the respective table
    query = f'''SELECT DISTINCT *
    FROM EMPLOYEE INNER JOIN {table_name} ON EMPLOYEE.EMPLOYEE_ID = {table_name}.EMPLOYEE_ID'''
    cursor.execute(query)
    result = cursor.fetchall()

    # Display content in entry_1
    entry_1.delete(1.0, "end")  # Clear previous content
    for row in result:
        entry_1.insert("end", f"===================================================\n{row}\n")

    cursor.close()
    conn.close()
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


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
    file=relative_to_assets("image_1admin1.png"))
image_1 = canvas.create_image(
    451.0,
    300.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2admin1.png"))
image_2 = canvas.create_image(
    450.0,
    80.0,
    image=image_image_2
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1admin1.png"))
entry_bg_1 = canvas.create_image(
    451.0,
    303.5,
    image=entry_image_1
)
entry_1 = Text(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=39.0,
    y=134.0,
    width=824.0,
    height=337.0
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1admin1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=button_1_clicked,
    relief="flat"
)
button_1.place(
    x=39.0,
    y=496.0,
    width=158.0,
    height=50.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2admin1.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: display_table_content_in_entry("receptionist"),
    relief="flat"
)
button_2.place(
    x=261.0,
    y=496.0,
    width=158.0,
    height=50.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3admin1.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: display_table_content_in_entry("doctor"),
    relief="flat"
)
button_3.place(
    x=483.0,
    y=496.0,
    width=158.0,
    height=50.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4admin1.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: display_table_content_in_entry("pharmacist"),
    relief="flat"
)
button_4.place(
    x=705.0,
    y=496.0,
    width=158.0,
    height=50.0
)
window.resizable(False, False)
window.mainloop()
