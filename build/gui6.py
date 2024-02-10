
import subprocess
from pathlib import Path
from datetime import datetime
import mysql.connector
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage,OptionMenu,StringVar,messagebox
from insertsql import insert_values
current_datetime = datetime.now()

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\RUPAM DAS\Desktop\CLLG\build\assets\frame0")
FILE_PATH_GUI4 = r"C:\Users\RUPAM DAS\Desktop\CLLG\build\gui4.py"

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)
def button_2_clicked():
    patient_id = entry_1.get()
    problem = entry_2.get()
    qualification = selected_specialty.get()
    date_and_time = current_datetime.strftime("%Y-%m-%d %H:%M:%S")

    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="rupamdas",
        database="hospitalmanagement"
    )
    cursor = conn.cursor()

    # Check if the patient ID exists in the PATIENTS table before insertion
    query_patient_id = "SELECT COUNT(*) FROM PATIENTS WHERE PATIENTS_ID = %s"
    cursor.execute(query_patient_id, (patient_id,))
    patient_id_result = cursor.fetchone()

    if patient_id_result and patient_id_result[0] > 0:  # If patient ID exists in PATIENTS table
        sql = "INSERT INTO APPOINTMENTS (PATIENTS_ID, DISEASE, QUALIFICATION, DATE_TIME) VALUES (%s, %s, %s, %s)"
        value = (patient_id, problem, qualification, date_and_time)

        cursor.execute(sql, value)
        conn.commit()

        messagebox.showinfo("Success", "Appointment Saved successfully")
        subprocess.Popen(['python', FILE_PATH_GUI4])
        window.iconify()
        
    else:
        messagebox.showerror("Error", "Patient ID does not exist")

    cursor.close()
    conn.close()
def clear_entry_fields():
    entry_1.delete(0, 'end')
    entry_2.delete(0, 'end') 
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
    file=relative_to_assets("image_111111.png"))

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
specialty_dropdown.place(x=413, y=364, width=197, height=26)

# Function to handle third dropdown selection change
def on_specialty_select(*args):
    print(selected_specialty.get())

# If you want to perform some action when the dropdown value changes
selected_specialty.trace('w', on_specialty_select)

image_1 = canvas.create_image(
    449.0,
    300.0,
    image=image_image_1
)

canvas.create_rectangle(
    266.70367431640625,
    190.0,
    633.2963562011719,
    493.0,
    fill="#FFFFFF",
    outline="")

canvas.create_text(
    397.5582580566406,
    208.0,
    anchor="nw",
    text="Appointments",
    fill="#000000",
    font=("Inter", 15 * -1)
)

canvas.create_text(
    293.6737060546875,
    367.0,
    anchor="nw",
    text="Doctor Qualification:",
    fill="#000000",
    font=("Inter", 12 * -1)
)

canvas.create_text(
    293.6737060546875,
    314.0,
    anchor="nw",
    text="Problem:",
    fill="#000000",
    font=("Inter", 12 * -1)
)

canvas.create_text(
    293.6737060546875,
    265.5101013183594,
    anchor="nw",
    text="Patient ID:",
    fill="#000000",
    font=("Inter", 12 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_111111.png"))
entry_bg_1 = canvas.create_image(
    506.7579345703125,
    273.2104377746582,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=403.86553955078125,
    y=260.0,
    width=205.7847900390625,
    height=24.420875549316406
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_211111.png"))
entry_bg_2 = canvas.create_image(
    506.4440002441406,
    322.2104377746582,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=403.5516052246094,
    y=309.0,
    width=205.7847900390625,
    height=24.420875549316406
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_111111.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=clear_entry_fields,
    relief="flat"
)
button_1.place(
    x=403.5516052246094,
    y=414.0,
    width=81.328125,
    height=36.154876708984375
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_211111.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=button_2_clicked,
    relief="flat"
)
button_2.place(
    x=528.4129028320312,
    y=414.0,
    width=81.328125,
    height=36.154876708984375
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_211111.png"))
image_2 = canvas.create_image(
    449.99888610839844,
    88.0,
    image=image_image_2
)
window.resizable(False, False)
window.mainloop()
