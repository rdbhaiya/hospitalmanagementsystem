
from pathlib import Path
import subprocess
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\RUPAM DAS\Desktop\CLLG\build\assets\frame0")
FILE_PATH_GUI13 = r"C:\Users\RUPAM DAS\Desktop\CLLG\build\gui13.py"
FILE_PATH_GUI14 = r"C:\Users\RUPAM DAS\Desktop\CLLG\build\gui14.py"
FILE_PATH_GUI15 = r"C:\Users\RUPAM DAS\Desktop\CLLG\build\gui15.py"
FILE_PATH_GUI16 = r"C:\Users\RUPAM DAS\Desktop\CLLG\build\gui16.py"
def button_1_clicked():
    subprocess.Popen(['python', FILE_PATH_GUI13])
    window.iconify()
def button_2_clicked():
    subprocess.Popen(['python', FILE_PATH_GUI14])
    window.iconify()
def button_3_clicked():
    subprocess.Popen(['python', FILE_PATH_GUI15])
    window.iconify()
def button_4_clicked():
    subprocess.Popen(['python', FILE_PATH_GUI16])
    window.iconify()
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
    file=relative_to_assets("image_1admin.png"))
image_1 = canvas.create_image(
    450.0,
    300.0,
    image=image_image_1
)

canvas.create_rectangle(
    550.0,
    179.0,
    857.0,
    517.0,
    fill="#D9D9D9",
    outline="")

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1admin.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=button_1_clicked,
    relief="flat"
)
button_1.place(
    x=592.0,
    y=219.0,
    width=223.0,
    height=41.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2admin.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=button_2_clicked,
    relief="flat"
)
button_2.place(
    x=592.0,
    y=295.0,
    width=223.0,
    height=41.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3admin.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=button_3_clicked,
    relief="flat"
)
button_3.place(
    x=592.0,
    y=371.0,
    width=223.0,
    height=41.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4admin.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=button_4_clicked,
    relief="flat"
)
button_4.place(
    x=592.0,
    y=447.0,
    width=223.0,
    height=41.0
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2admin.png"))
image_2 = canvas.create_image(
    450.0,
    88.0,
    image=image_image_2
)
window.resizable(False, False)
window.mainloop()
