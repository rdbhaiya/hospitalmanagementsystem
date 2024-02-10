
from pathlib import Path
import subprocess
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage,messagebox
import mysql.connector

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\RUPAM DAS\Desktop\CLLG\build\assets\frame0")

FILE_PATH_GUI1 = r"C:\Users\RUPAM DAS\Desktop\CLLG\build\gui.py"
FILE_PATH_GUI4 = r"C:\Users\RUPAM DAS\Desktop\CLLG\build\gui4.py"
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def button_1_clicked():
    subprocess.Popen(['python', FILE_PATH_GUI1])
    window.iconify()
def button_2_clicked():
    recep_id = entry_1.get()
    recep_password = entry_2.get()
    
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="rupamdas",
        database="HospitalManagement"
    )
    cursor = conn.cursor()

    # Fetch EMPLOYEE_ID for the given RECEPTIONIST_ID
    query_employee_id = "SELECT EMPLOYEE_ID FROM RECEPTIONIST WHERE RECEPTIONIST_ID = %s"
    cursor.execute(query_employee_id, (recep_id,))
    employee_id_result = cursor.fetchone()

    if employee_id_result:
        employee_id = employee_id_result[0]

        # Fetch password from the IDS_AND_PASSWORD table for the obtained EMPLOYEE_ID
        query_password = "SELECT PASSWORDS FROM IDS_AND_PASSWORD WHERE EMPLOYEE_ID = %s"
        cursor.execute(query_password, (employee_id,))
        password_result = cursor.fetchone()

        if password_result and password_result[0] == recep_password:
            # Valid credentials - Receptionsit authenticated
            # You can open the next window or perform actions here
            messagebox.showinfo("Login Successful", "Receptionsit Logged in successfully")
            subprocess.Popen(['python', FILE_PATH_GUI4])
            window.iconify()
            # Add your logic here to proceed after successful login
        
        else:
            # Invalid credentials - Show a popup message
            messagebox.showerror("Login Failed", "Invalid credentials")

    else:
        # Receptionsit ID not found - Show a popup message
        messagebox.showerror("Receptionsit ID not found", "Invalid Receptionsit ID")

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
    file=relative_to_assets("image_11.png"))
image_1 = canvas.create_image(
    450.0,
    300.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_21.png"))
image_2 = canvas.create_image(
    450.0,
    101.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_31.png"))
image_3 = canvas.create_image(
    450.0,
    375.0,
    image=image_image_3
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_11.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=button_1_clicked,
    relief="flat"
)
button_1.place(
    x=379.712646484375,
    y=443.04022216796875,
    width=79.87933349609375,
    height=27.925277709960938
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_21.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=button_2_clicked,
    relief="flat"
)
button_2.place(
    x=500.5057373046875,
    y=443.04022216796875,
    width=79.87933349609375,
    height=27.275863647460938
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_11.png"))
entry_bg_1 = canvas.create_image(
    480.7079772949219,
    344.4529571533203,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=380.85400390625,
    y=328.5098876953125,
    width=199.70794677734375,
    height=29.886138916015625
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_21.png"))
entry_bg_2 = canvas.create_image(
    480.7079772949219,
    395.6386260986328,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=380.85400390625,
    y=379.695556640625,
    width=199.70794677734375,
    height=29.886138916015625
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_41.png"))
image_4 = canvas.create_image(
    346.0469970703125,
    394.39605712890625,
    image=image_image_4
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_51.png"))
image_5 = canvas.create_image(
    347.6336669921875,
    342.2796936035156,
    image=image_image_5
)

canvas.create_text(
    313.7252197265625,
    225.29949951171875,
    anchor="nw",
    text="Login Here",
    fill="#3CA7D5",
    font=("Inter", 24 * -1)
)

canvas.create_text(
    317.3677978515625,
    272.24139404296875,
    anchor="nw",
    text="MEMBER’S LOGIN PANEL",
    fill="#3CA7D5",
    font=("Inter", 12 * -1)
)
window.resizable(False, False)
window.mainloop()
