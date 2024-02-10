
import subprocess
from pathlib import Path
import mysql.connector
# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage,messagebox


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\RUPAM DAS\Desktop\CLLG\build\assets\frame0")

FILE_PATH_GUI12 = r"C:\Users\RUPAM DAS\Desktop\CLLG\build\gui12.py"
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)
def button_1_clicked():
    subprocess.Popen(['python', FILE_PATH_GUI12])
    window.iconify()
def clear_entry_fields():
    entry_1.delete(0, 'end')
def delete_employee_details():
    # Retrieve the EMPLOYEE_ID
    emp_id = entry_1.get()

    # Connect to the database
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="yourpassword",
        database="hospitalmanagement"
    )
    cursor = conn.cursor()

    # Delete from ids_and_password table first
    delete_ids_query = f"DELETE FROM ids_and_password WHERE EMPLOYEE_ID = '{emp_id}'"
    cursor.execute(delete_ids_query)

    # Then delete from employee table
    delete_query = f"DELETE FROM employee WHERE EMPLOYEE_ID = '{emp_id}'"
    cursor.execute(delete_query)

    # Commit the changes to the database
    conn.commit()
    messagebox.showerror("Sucess!","Deleted Sucessfully")
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
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1admin3.png"))
image_1 = canvas.create_image(
    451.0,
    300.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2admin3.png"))
image_2 = canvas.create_image(
    450.0,
    80.0,
    image=image_image_2
)

canvas.create_rectangle(
    230.0,
    182.0,
    674.0,
    437.0,
    fill="#D9D9D9",
    outline="")

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1admin3.png"))
entry_bg_1 = canvas.create_image(
    520.0,
    336.5,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=407.0,
    y=320.0,
    width=226.0,
    height=31.0
)

canvas.create_text(
    264.0,
    329.0,
    anchor="nw",
    text="Employee ID:",
    fill="#000000",
    font=("Inter SemiBold", 15 * -1)
)

canvas.create_text(
    378.0,
    213.0,
    anchor="nw",
    text="Delete Details",
    fill="#000000",
    font=("Inter SemiBold", 20 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1admin3.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=button_1_clicked,
    relief="flat"
)
button_1.place(
    x=245.0,
    y=458.0,
    width=91.31982421875,
    height=40.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2admin3.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=clear_entry_fields,
    relief="flat"
)
button_2.place(
    x=406.92791748046875,
    y=458.0,
    width=94.82720947265625,
    height=40.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3admin3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=delete_employee_details,
    relief="flat"
)
button_3.place(
    x=571.68017578125,
    y=459.0,
    width=91.31982421875,
    height=40.0
)
window.resizable(False, False)
window.mainloop()
