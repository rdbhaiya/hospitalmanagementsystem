
import subprocess
from pathlib import Path
from tkcalendar import DateEntry
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage,OptionMenu, StringVar,messagebox,ttk
from insertsql import insert_values

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\RUPAM DAS\Desktop\CLLG\build\assets\frame0")
FILE_PATH_GUI4 = r"C:\Users\RUPAM DAS\Desktop\CLLG\build\gui4.py"

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)
def clear_entry_fields():
    entry_1.delete(0, 'end')
    entry_2.delete(0, 'end')
    entry_3.delete(0, 'end')
    entry_4.delete(0, 'end')
    entry_5.delete(0, 'end')
def button_2_clicked():
    patient_id=entry_1.get()
    patient_name=entry_2.get()
    dob=dob_entry.get_date()
    age=entry_3.get()
    gender=selected_gender.get()
    blood_grp=selected_blood.get()
    email=entry_4.get()
    mobile_no=entry_5.get()
    sql = "INSERT INTO PATIENTS (PATIENTS_ID, PATIENTS_NAME,DOB,AGE,GENDER,BLOOD_GRP,EMAIL,MOBILE_NO) VALUES (%s, %s, %s, %s, %s, %s , %s, %s)"
    value=(patient_id,patient_name,dob,age,gender,blood_grp,email,mobile_no)
    insert_values(sql,value)
    messagebox.showinfo("Success", "Patient registered successfully")
    subprocess.Popen(['python', FILE_PATH_GUI4])
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
    height = 602,
    width = 900,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)

selected_gender = StringVar(window)
selected_gender.set('-SELECT-') 
options = ['MALE','FEMALE','OTHERS']
gender_dropdown = OptionMenu(window, selected_gender, *options)
gender_dropdown.place(x=429.31, y=458.54, width=206, height=23.44)
def on_dropdown_select(*args):
    print(selected_gender.get())
selected_gender.trace('w', on_dropdown_select)

selected_blood = StringVar(window)
selected_blood.set('-SELECT-') 
options = ['A+', 'A-', 'B+', 'B-','O+','O-','AB+','AB-']
blood_dropdown = OptionMenu(window, selected_blood, *options)
blood_dropdown.place(x=429.31, y=366.02, width=206, height=23.44)
def on_dropdown_select(*args):
    print(selected_blood.get())
selected_blood.trace('w', on_dropdown_select)

dob_entry = DateEntry(window, date_pattern='yyyy-mm-dd')
dob_entry.place(x=429.31, y=304.34, width=206, height=23.44)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_11111.png"))
image_1 = canvas.create_image(
    450.0,
    301.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_21111.png"))
image_2 = canvas.create_image(
    450.0,
    108.0,
    image=image_image_2
)

canvas.create_rectangle(
    293.0,
    189.0,
    660.0,
    555.3831787109375,
    fill="#D9D9D9",
    outline="")

canvas.create_text(
    321.37310791015625,
    278.0,
    anchor="nw",
    text="Name:",
    fill="#000000",
    font=("Inter", 12 * -1)
)

canvas.create_text(
    321.37310791015625,
    309.0,
    anchor="nw",
    text="D.O.B:",
    fill="#000000",
    font=("Inter", 12 * -1)
)

canvas.create_text(
    321.37310791015625,
    340.0,
    anchor="nw",
    text="AGE:",
    fill="#000000",
    font=("Inter", 12 * -1)
)

canvas.create_text(
    321.37310791015625,
    371.0,
    anchor="nw",
    text="BLOOD GROUP:",
    fill="#000000",
    font=("Inter", 12 * -1)
)

canvas.create_text(
    321.37310791015625,
    402.0,
    anchor="nw",
    text="EMAIL:",
    fill="#000000",
    font=("Inter", 12 * -1)
)

canvas.create_text(
    318.9058837890625,
    433.0,
    anchor="nw",
    text="PHONE NO:",
    fill="#000000",
    font=("Inter", 12 * -1)
)

canvas.create_text(
    318.0,
    464.0,
    anchor="nw",
    text="Gender:",
    fill="#000000",
    font=("Inter", 12 * -1)
)

canvas.create_text(
    321.0,
    247.0,
    anchor="nw",
    text="PATIENT ID:",
    fill="#000000",
    font=("Inter", 12 * -1)
)

canvas.create_text(
    442.0,
    206.0,
    anchor="nw",
    text="Patient Details",
    fill="#000000",
    font=("Inter", 15 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_11111.png"))
entry_bg_1 = canvas.create_image(
    532.3209915161133,
    254.3815155029297,
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
    y=242.6621856689453,
    width=206.01344299316406,
    height=21.43865966796875
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_21111.png"))
entry_bg_2 = canvas.create_image(
    532.3209915161133,
    285.2218322753906,
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
    y=273.50250244140625,
    width=206.01344299316406,
    height=21.43865966796875
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_31111.png"))
entry_bg_3 = canvas.create_image(
    532.3209915161133,
    346.90252685546875,
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
    y=335.1831970214844,
    width=206.01344299316406,
    height=21.43865966796875
)

entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_41111.png"))
entry_bg_4 = canvas.create_image(
    532.3209915161133,
    408.58319091796875,
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
    y=396.8638610839844,
    width=206.01344299316406,
    height=21.43865966796875
)

entry_image_5 = PhotoImage(
    file=relative_to_assets("entry_51111.png"))
entry_bg_5 = canvas.create_image(
    532.3209915161133,
    439.4235534667969,
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
    y=427.7042236328125,
    width=206.01344299316406,
    height=21.43865966796875
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_11111.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=clear_entry_fields,
    relief="flat"
)
button_1.place(
    x=425.61346435546875,
    y=500.4873962402344,
    width=81.41848754882812,
    height=32.073944091796875
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_21111.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=button_2_clicked,
    relief="flat"
)
button_2.place(
    x=553.9092407226562,
    y=501.72100830078125,
    width=81.41848754882812,
    height=32.073944091796875
)
window.resizable(False, False)
window.mainloop()
