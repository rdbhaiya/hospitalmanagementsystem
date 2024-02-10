
import subprocess
from pathlib import Path
import random as r
# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage,OptionMenu, StringVar,messagebox
from insertsql import insert_values


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\RUPAM DAS\Desktop\CLLG\build\assets\frame0")
FILE_PATH_GUI1 = r"C:\Users\RUPAM DAS\Desktop\CLLG\build\gui.py"

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def clear_entry_fields():
    entry_1.delete(0, 'end')
    entry_2.delete(0, 'end')
    entry_3.delete(0, 'end')
    entry_4.delete(0, 'end')
    entry_5.delete(0, 'end')
    entry_6.delete(0, 'end')
def insert_values_table():
    emp_pass=entry_1.get()
    emp_id="EMP"+str(r.randint(0,99999))
    emp_name=entry_2.get()
    age=entry_4.get()
    emp_type=selected_type.get()
    gender=selected_gender.get()
    email=entry_5.get()
    mobile=entry_6.get()
    address=entry_3.get()
    sql = "INSERT INTO EMPLOYEE (EMPLOYEE_ID, EMPLOYEE_NAME, AGE,EMP_TYPE, GENDER,EMAIL, MOBILE,ADDRESS) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    val = (emp_id, emp_name, age, emp_type, gender, email, mobile, address)
    insert_values(sql,val)
    sql6 = "INSERT INTO IDS_AND_PASSWORD (EMPLOYEE_ID, PASSWORDS) VALUES (%s, %s)"
    val6= (emp_id,emp_pass)
    insert_values(sql6,val6)
    if(emp_type=="ADMIN"):
        admin_id="ADMIN"+str(r.randint(0,99999))
        sql2 = "INSERT INTO ADMIN (ADMIN_ID, EMPLOYEE_ID) VALUES (%s, %s)"
        val2=(admin_id,emp_id)
        message="YOUR ID: "+admin_id
        insert_values(sql2,val2)
    elif(emp_type=="DOCTOR"):
        doctor_id="DOCTOR"+str(r.randint(0,99999))
        quali=selected_specialty.get()
        sql3 = "INSERT INTO DOCTOR (DOCTOR_ID, EMPLOYEE_ID, QUALIFICATION) VALUES (%s, %s, %s)"
        val3 =(doctor_id,emp_id,quali)
        message="YOUR ID: "+doctor_id
        insert_values(sql3,val3)
    elif(emp_type=="RECEPTIONIST"):
        recp_id="RECP"+str(r.randint(0,99999))
        sql4 = "INSERT INTO RECEPTIONIST (RECEPTIONIST_ID, EMPLOYEE_ID) VALUES (%s, %s)"
        val4=(recp_id,emp_id)
        message="YOUR ID: "+recp_id
        insert_values(sql4,val4)
    elif(emp_type=="PHARMACIST"):
        phar_id="PHARM"+str(r.randint(0,99999))
        sql5 = "INSERT INTO PHARMACIST (PHARMACIST_ID, EMPLOYEE_ID) VALUES (%s, %s)"
        val5=(phar_id,emp_id)
        message="YOUR ID: "+phar_id
        insert_values(sql5,val5)
    messagebox.showinfo("Success", message)
    subprocess.Popen(['python', FILE_PATH_GUI1])
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
selected_type = StringVar(window)
selected_type.set('-SELECT-')  # Setting the default value as 'ADMIN'

# Dropdown menu options
options = ['ADMIN', 'DOCTOR', 'RECEPTIONIST', 'PHARMACIST']

# Creating the dropdown menu
type_dropdown = OptionMenu(window, selected_type, *options)
type_dropdown.place(x=429.31, y=247, width=206, height=26.42)

# Access the selected value using selected_type.get()
# For example, to print the selected value:
def on_dropdown_select(*args):
    print(selected_type.get())

selected_type.trace('w', on_dropdown_select)

# Create a StringVar to hold the selected value from the second dropdown
selected_gender = StringVar(window)
selected_gender.set('-SELECT-')  # Set the default value as 'MALE'

# Dropdown menu options for the second dropdown
gender_options = ['MALE', 'FEMALE', 'OTHERS']

# Create the second dropdown menu
gender_dropdown = OptionMenu(window, selected_gender, *gender_options)
gender_dropdown.place(x=429.31, y=492, width=206, height=26.42)

# Function to handle second dropdown selection change
def on_gender_select(*args):
    print(selected_gender.get())

# If you want to perform some action when the dropdown value changes
selected_gender.trace('w', on_gender_select)

selected_specialty = StringVar(window)
selected_specialty.set('-SELECT-')  # Set the default value

# Dropdown menu options for the third dropdown
specialty_options = [
    'General Practitioners (GPs)',
    'Cardiologists',
    'Dermatologists',
    'Gastroenterologists',
    'Neurologists',
    'Orthopedic Surgeons',
    'Pediatricians',
    'Psychiatrists',
    'Gynecologists ',
    'Ophthalmologists',
    '(ENT) Specialists',
    'Others'
]

# Create the third dropdown menu
specialty_dropdown = OptionMenu(window, selected_specialty, *specialty_options)
specialty_dropdown.place(x=429.31, y=387, width=206, height=26.42)

# Function to handle third dropdown selection change
def on_specialty_select(*args):
    print(selected_specialty.get())

# If you want to perform some action when the dropdown value changes
selected_specialty.trace('w', on_specialty_select)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_111.png"))
image_1 = canvas.create_image(
    450.0,
    301.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_211.png"))
image_2 = canvas.create_image(
    450.0,
    95.0,
    image=image_image_2
)

canvas.create_rectangle(
    293.0,
    169.0,
    660.0,
    582.0,
    fill="#D9D9D9",
    outline="")

canvas.create_text(
    442.0,
    188.16299438476562,
    anchor="nw",
    text="Member Details",
    fill="#000000",
    font=("Inter", 15 * -1)
)

canvas.create_text(
    321.0,
    283.0,
    anchor="nw",
    text="Name:",
    fill="#000000",
    font=("Inter", 12 * -1)
)

canvas.create_text(
    321.0,
    322.0,
    anchor="nw",
    text="Address:",
    fill="#000000",
    font=("Inter", 12 * -1)
)

canvas.create_text(
    319.0,
    353.0,
    anchor="nw",
    text="AGE:",
    fill="#000000",
    font=("Inter", 12 * -1)
)

canvas.create_text(
    319.0,
    388.0,
    anchor="nw",
    text="Qualification:",
    fill="#000000",
    font=("Inter", 12 * -1)
)

canvas.create_text(
    321.0,
    419.0,
    anchor="nw",
    text="EMAIL:",
    fill="#000000",
    font=("Inter", 12 * -1)
)

canvas.create_text(
    321.0,
    462.0,
    anchor="nw",
    text="PHONE NO:",
    fill="#000000",
    font=("Inter", 12 * -1)
)

canvas.create_text(
    319.0,
    497.0,
    anchor="nw",
    text="Gender:",
    fill="#000000",
    font=("Inter", 12 * -1)
)

canvas.create_text(
    319.0,
    248.0,
    anchor="nw",
    text="Type:",
    fill="#000000",
    font=("Inter", 12 * -1)
)

canvas.create_text(
    319.0,
    217.0,
    anchor="nw",
    text="Member OTP:",
    fill="#000000",
    font=("Inter", 12 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_111.png"))
entry_bg_1 = canvas.create_image(
    532.3209915161133,
    224.70033645629883,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=429.31427001953125,
    y=211.48989868164062,
    width=206.01344299316406,
    height=24.420875549316406
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_211.png"))
entry_bg_2 = canvas.create_image(
    532.3209915161133,
    295.2104377746582,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=429.31427001953125,
    y=282.0,
    width=206.01344299316406,
    height=24.420875549316406
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_311.png"))
entry_bg_3 = canvas.create_image(
    532.3209915161133,
    330.2104377746582,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_3.place(
    x=429.31427001953125,
    y=317.0,
    width=206.01344299316406,
    height=24.420875549316406
)

entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_411.png"))
entry_bg_4 = canvas.create_image(
    532.3209915161133,
    365.2104377746582,
    image=entry_image_4
)
entry_4 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_4.place(
    x=429.31427001953125,
    y=352.0,
    width=206.01344299316406,
    height=24.420875549316406
)

entry_image_5 = PhotoImage(
    file=relative_to_assets("entry_511.png"))
entry_bg_5 = canvas.create_image(
    532.3209915161133,
    435.21043395996094,
    image=entry_image_5
)
entry_5 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_5.place(
    x=429.31427001953125,
    y=422.0,
    width=206.01344299316406,
    height=24.420867919921875
)

entry_image_6 = PhotoImage(
    file=relative_to_assets("entry_611.png"))
entry_bg_6 = canvas.create_image(
    532.3209915161133,
    470.21043395996094,
    image=entry_image_6
)
entry_6 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_6.place(
    x=429.31427001953125,
    y=457.0,
    width=206.01344299316406,
    height=24.420867919921875
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_111.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=clear_entry_fields,
    relief="flat"
)
button_1.place(
    x=425.61346435546875,
    y=526.1195068359375,
    width=81.41848754882812,
    height=36.154876708984375
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_211.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=insert_values_table,
    relief="flat"
)
button_2.place(
    x=553.9092407226562,
    y=526.5101318359375,
    width=81.41848754882812,
    height=36.154876708984375
)
window.resizable(False, False)
window.mainloop()
