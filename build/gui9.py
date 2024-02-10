
import subprocess
from pathlib import Path
from datetime import datetime
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage,messagebox
from insertsql import insert_values
import mysql.connector
current_datetime = datetime.now()

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\RUPAM DAS\Desktop\CLLG\build\assets\frame0")
FILE_PATH_GUI8 = r"C:\Users\RUPAM DAS\Desktop\CLLG\build\gui8.py"

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)
def clear_entry_fields():
    entry_1.delete(0, 'end')
    entry_2.delete(0, 'end')
    entry_3.delete(0, 'end')
def button_2_clicked():
    subprocess.Popen(['python', FILE_PATH_GUI8])
    window.iconify()
def button_3_clicked():
    patient_id = entry_3.get()
    doctor_id = entry_1.get()
    description = entry_2.get()
    date_and_time = current_datetime.strftime("%Y-%m-%d %H:%M:%S")

    # Establish database connection
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="rupamdas",
        database="hospitalmanagement"
    )
    cursor = conn.cursor()

    # Check if the patient ID exists in the 'Patient' table
    query_patient_id = "SELECT COUNT(*) FROM PATIENTS WHERE PATIENTS_ID = %s"
    cursor.execute(query_patient_id, (patient_id,))
    patient_id_result = cursor.fetchone()

    # Check if the doctor ID exists in the 'Doctor' table
    query_doctor_id = "SELECT COUNT(*) FROM DOCTOR WHERE DOCTOR_ID = %s"
    cursor.execute(query_doctor_id, (doctor_id,))
    doctor_id_result = cursor.fetchone()

    # If both patient and doctor IDs exist, proceed with insertion
    if patient_id_result and doctor_id_result and patient_id_result[0] > 0 and doctor_id_result[0] > 0:
        sql = "INSERT INTO PRESCRIPTION (PATIENTS_ID, DOCTOR_ID, DISCRIPTION, DATE_TIME) VALUES (%s, %s, %s, %s)"
        value = (patient_id, doctor_id, description, date_and_time)
        
        # Insert into 'Prescription' table
        insert_values(sql, value)
        messagebox.showinfo("Success", "Prescription added successfully")

    else:
        messagebox.showerror("Error", "Patient ID or Doctor ID does not exist")

    # Close database connection
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
    file=relative_to_assets("image_111111111.png"))
image_1 = canvas.create_image(
    450.0,
    300.0,
    image=image_image_1
)

canvas.create_rectangle(
    35.0,
    158.0,
    877.0,
    568.0,
    fill="#BBA8A8",
    outline="")

canvas.create_text(
    409.0,
    168.0,
    anchor="nw",
    text="Prescription",
    fill="#000000",
    font=("Inter", 15 * -1)
)

canvas.create_text(
    72.0,
    234.0,
    anchor="nw",
    text="Description:",
    fill="#000000",
    font=("Inter", 12 * -1)
)

canvas.create_text(
    72.0,
    193.0,
    anchor="nw",
    text="Patient ID:",
    fill="#000000",
    font=("Inter", 12 * -1)
)

canvas.create_text(
    537.0,
    194.0,
    anchor="nw",
    text="Doctor ID:",
    fill="#000000",
    font=("Inter", 12 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_111111111.png"))
entry_bg_1 = canvas.create_image(
    706.0067138671875,
    201.2104377746582,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=603.0,
    y=188.0,
    width=206.013427734375,
    height=24.420875549316406
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_211111111.png"))
entry_bg_2 = canvas.create_image(
    453.5,
    380.5,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=54.0,
    y=257.0,
    width=799.0,
    height=245.0
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_311111111.png"))
entry_bg_3 = canvas.create_image(
    245.00672149658203,
    201.2104377746582,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_3.place(
    x=142.0,
    y=188.0,
    width=206.01344299316406,
    height=24.420875549316406
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_111111111.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=clear_entry_fields,
    relief="flat"
)
button_1.place(
    x=670.0,
    y=513.0,
    width=81.41848754882812,
    height=36.154876708984375
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_211111111.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=button_2_clicked,
    relief="flat"
)
button_2.place(
    x=568.0,
    y=513.0,
    width=81.41848754882812,
    height=36.154876708984375
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_311111111.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=button_3_clicked,
    relief="flat"
)
button_3.place(
    x=772.0,
    y=513.0,
    width=81.41848754882812,
    height=36.154876708984375
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_211111111.png"))
image_2 = canvas.create_image(
    450.0,
    95.0,
    image=image_image_2
)
window.resizable(False, False)
window.mainloop()
