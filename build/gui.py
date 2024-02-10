import subprocess
from tkinter import Tk, Canvas, Button, PhotoImage
from pathlib import Path

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\RUPAM DAS\Desktop\CLLG\build\assets\frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

doctor_file = r"C:\Users\RUPAM DAS\Desktop\CLLG\build\gui2.py"
FILE_PATH_GUI3 = r"C:\Users\RUPAM DAS\Desktop\CLLG\build\gui3.py"
admin_file= r"C:\Users\RUPAM DAS\Desktop\CLLG\build\gui21.py"
recp_file=r"C:\Users\RUPAM DAS\Desktop\CLLG\build\gui211.py"
phar_file=r"C:\Users\RUPAM DAS\Desktop\CLLG\build\gui2111.py"
def button_1_clicked():
    subprocess.Popen(['python', FILE_PATH_GUI3])
    window.iconify()
def button_2_clicked():
    # Replace 'file_path_for_button_2.py' with the path to the Python file you want to open
    subprocess.Popen(['python', admin_file])
    window.iconify()
def button_3_clicked():
    # Replace 'file_path_for_button_3.py' with the path to the Python file you want to open
    subprocess.Popen(['python', recp_file])
    window.iconify()

def button_4_clicked():
    # Replace 'file_path_for_button_4.py' with the path to the Python file you want to open
    subprocess.Popen(['python', doctor_file])
    window.iconify()
def button_5_clicked():
    # Replace 'file_path_for_button_5.py' with the path to the Python file you want to open
    subprocess.Popen(['python', phar_file])
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
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    450.0,
    300.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    450.0,
    67.0,
    image=image_image_2
)
image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    450.0,
    160.0,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    460.0,
    278.0,
    image=image_image_4
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=button_1_clicked,
    relief="flat"
)
button_1.place(
    x=393.0,
    y=471.0,
    width=114.23077392578125,
    height=42.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=button_2_clicked,
    relief="flat"
)
button_2.place(x=165.0, y=361.0, width=123.9679946899414, height=40.28959655761719)
button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=button_3_clicked,
    relief="flat"
)
button_3.place(x=320.0, y=361.0, width=123.96798706054688, height=40.28959655761719)
button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=button_4_clicked,
    relief="flat"
)
button_4.place(x=476.0, y=361.0, width=123.96798706054688, height=40.28959655761719)
button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=button_5_clicked,
    relief="flat"
)
button_5.place(x=632.0, y=361.0, width=123.968017578125, height=40.28959655761719)
window.resizable(False, False)
window.mainloop()
