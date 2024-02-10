
from pathlib import Path
import mysql.connector
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage,messagebox
import subprocess

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
    entry_2.delete(0, 'end')
    entry_3.delete(0, 'end')
    entry_4.delete(0, 'end')
    entry_5.delete(0, 'end')
    entry_6.delete(0, 'end')

db_config = {
    "host": "localhost",
    "user": "root",
    "password": "rupamdas",
    "database": "hospitalmanagement"
}

# Function to update the employee table based on the provided entries
def update_employee_details():
    # Retrieve the entries
    emp_id = entry_1.get()
    emp_name = entry_2.get()
    age = entry_3.get()
    emp_email = entry_4.get()
    emp_mobile = entry_5.get()
    emp_address = entry_6.get()

    # Connect to the database
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    # Prepare the SQL query to update the employee table
    update_query = '''UPDATE employee 
                    SET EMPLOYEE_NAME = %s, AGE = %s, 
                    EMAIL = %s, MOBILE = %s, ADDRESS = %s 
                    WHERE EMPLOYEE_ID = %s'''

# Execute the update query with parameters
    cursor.execute(update_query, (emp_name, age, emp_email, emp_mobile, emp_address, emp_id))

    # Commit the changes to the database
    conn.commit()
    messagebox.showerror("Sucess!","Updated Sucessfully")
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
    file=relative_to_assets("image_1admin2.png"))
image_1 = canvas.create_image(
    451.0,
    300.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2admin2.png"))
image_2 = canvas.create_image(
    450.0,
    80.0,
    image=image_image_2
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1admin2.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=button_1_clicked,
    relief="flat"
)
button_1.place(
    x=230.0,
    y=501.0,
    width=97.0,
    height=40.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2admin2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=clear_entry_fields,
    relief="flat"
)
button_2.place(
    x=402.0,
    y=501.0,
    width=100.72555541992188,
    height=40.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3admin2.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=update_employee_details,
    relief="flat"
)
button_3.place(
    x=577.0,
    y=502.0,
    width=97.0,
    height=40.0
)

canvas.create_rectangle(
    230.0,
    136.0,
    674.0,
    477.0,
    fill="#D9D9D9",
    outline="")

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1admin2.png"))
entry_bg_1 = canvas.create_image(
    532.0,
    201.5,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=419.0,
    y=185.0,
    width=226.0,
    height=31.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2admin2.png"))
entry_bg_2 = canvas.create_image(
    532.0,
    249.5,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=419.0,
    y=233.0,
    width=226.0,
    height=31.0
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3admin2.png"))
entry_bg_3 = canvas.create_image(
    532.0,
    297.5,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_3.place(
    x=419.0,
    y=281.0,
    width=226.0,
    height=31.0
)

entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4admin2.png"))
entry_bg_4 = canvas.create_image(
    532.0,
    345.5,
    image=entry_image_4
)
entry_4 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_4.place(
    x=419.0,
    y=329.0,
    width=226.0,
    height=31.0
)

entry_image_5 = PhotoImage(
    file=relative_to_assets("entry_5admin2.png"))
entry_bg_5 = canvas.create_image(
    532.0,
    393.5,
    image=entry_image_5
)
entry_5 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_5.place(
    x=419.0,
    y=377.0,
    width=226.0,
    height=31.0
)

entry_image_6 = PhotoImage(
    file=relative_to_assets("entry_6admin2.png"))
entry_bg_6 = canvas.create_image(
    532.0,
    441.5,
    image=entry_image_6
)
entry_6 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_6.place(
    x=419.0,
    y=425.0,
    width=226.0,
    height=31.0
)

canvas.create_text(
    280.0,
    194.0,
    anchor="nw",
    text="Employee ID:",
    fill="#000000",
    font=("Inter SemiBold", 12 * -1)
)

canvas.create_text(
    280.0,
    242.0,
    anchor="nw",
    text="Employee Name:",
    fill="#000000",
    font=("Inter SemiBold", 12 * -1)
)

canvas.create_text(
    280.0,
    290.0,
    anchor="nw",
    text="Employee Age:",
    fill="#000000",
    font=("Inter SemiBold", 12 * -1)
)

canvas.create_text(
    280.0,
    338.0,
    anchor="nw",
    text="Employee Email:",
    fill="#000000",
    font=("Inter SemiBold", 12 * -1)
)

canvas.create_text(
    280.0,
    386.0,
    anchor="nw",
    text="Employee Mobile No:",
    fill="#000000",
    font=("Inter SemiBold", 12 * -1)
)

canvas.create_text(
    280.0,
    434.0,
    anchor="nw",
    text="Employee Address:",
    fill="#000000",
    font=("Inter SemiBold", 12 * -1)
)

canvas.create_text(
    376.0,
    145.0,
    anchor="nw",
    text="Update Details",
    fill="#000000",
    font=("Inter SemiBold", 20 * -1)
)
window.resizable(False, False)
window.mainloop()
