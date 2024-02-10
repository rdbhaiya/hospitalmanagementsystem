
from pathlib import Path
import subprocess
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage,StringVar,OptionMenu,messagebox
import mysql.connector
from datetime import datetime
from insertsql import insert_values
current_datetime = datetime.now()

FILE_PATH_GUI10 = r"C:\Users\RUPAM DAS\Desktop\CLLG\build\gui10.py"

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\RUPAM DAS\Desktop\CLLG\build\assets\frame0")



# Your database connection configuration
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "yourpassword",
    "database": "hospitalmanagement"
}

def calculate_total_cost():
    medicine_names = [
        selected_medicine.get(),
        selected_medicine1.get(),
        selected_medicine2.get(),
        selected_medicine3.get(),
        selected_medicine4.get()
    ]

    quantities = [
        int(entry_3.get() or 0),
        int(entry_4.get() or 0),
        int(entry_5.get() or 0),
        int(entry_6.get() or 0),
        int(entry_7.get() or 0)
    ]
    patients_id=entry_1.get()
    date_and_time=current_datetime.strftime("%Y-%m-%d %H:%M:%S")
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    query = "SELECT PATIENTS_ID FROM patients WHERE PATIENTS_ID = %s"
    cursor.execute(query, (patients_id,))
    result = cursor.fetchone()

    if result:
        total_cost = 600

        for i, medicine_name in enumerate(medicine_names):
            if medicine_name != "-SELECT-" and quantities[i] > 0:
                # Fetch medicine price from the database based on the medicine name
                query = "SELECT MEDICINE_PRICE FROM medicine WHERE MEDICINE_NAME = %s"
                cursor.execute(query, (medicine_name,))
                result = cursor.fetchone()

                if result:
                    medicine_price = float(result[0])
                    total_cost += (medicine_price *quantities[i])
        sql = "INSERT INTO BILL ( PATIENTS_ID,TOTAL_CHARGES,DATE_TIME) VALUES (%s, %s,%s)"
        value=(patients_id,total_cost,date_and_time)
        insert_values(sql,value)
         # Display the total cost
        messagebox.showerror("ordered Succesfully!","Ask Receptionist for Bill")
    else:
        messagebox.showerror("Error","Invalid PatitentID")
    cursor.close()
    conn.close()

   

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)
def clear_entry_fields():
    entry_1.delete(0, 'end')
    entry_3.delete(0, 'end')
    entry_4.delete(0, 'end')
    entry_5.delete(0, 'end')
    entry_6.delete(0, 'end')
    entry_7.delete(0, 'end')
def button_2_clicked():
    subprocess.Popen(['python', FILE_PATH_GUI10])
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

selected_medicine = StringVar(window)
selected_medicine.set('-SELECT-') 
options = [
    'Aspirin',
    'Paracetamol (Acetaminophen)',
    'Ibuprofen',
    'Acetaminophen/Codeine',
    'Acetaminophen/Hydrocodone',
    'Acetaminophen/Oxycodone',
    'Naproxen',
    'Prednisone',
    'Cetirizine',
    'Loratadine',
    'Ranitidine',
    'Omeprazole',
    'Pantoprazole',
    'Metformin',
    'Insulin',
    'Atorvastatin',
    'Simvastatin',
    'Lisinopril',
    'Amlodipine',
    'Losartan',
    'Hydrochlorothiazide',
    'Furosemide',
    'Clopidogrel',
    'Warfarin',
    'Enalapril',
    'Levothyroxine',
    'Albuterol',
    'Fluticasone/Salmeterol',
    'Montelukast',
    'Olanzapine',
    'Sertraline',
    'Fluoxetine',
    'Escitalopram',
    'Citalopram',
    'Venlafaxine',
    'Quetiapine',
    'Risperidone',
    'Diazepam',
    'Lorazepam',
    'Amoxicillin',
    'Azithromycin',
    'Ciprofloxacin',
    'Fluconazole',
    'Acyclovir',
    'Oseltamivir',
    'Metronidazole',
    'Clindamycin',
    'Tamsulosin',
    'Finasteride',
    'Sildenafil'
]
medicine_dropdown = OptionMenu(window, selected_medicine, *options)
medicine_dropdown.place(x=396, y=317, width=234, height=23)
def on_dropdown_select(*args):
    print(selected_medicine.get())
selected_medicine.trace('w', on_dropdown_select)

selected_medicine1 = StringVar(window)
selected_medicine1.set('-SELECT-') 
options1 = [
    'Aspirin',
    'Paracetamol (Acetaminophen)',
    'Ibuprofen',
    'Acetaminophen/Codeine',
    'Acetaminophen/Hydrocodone',
    'Acetaminophen/Oxycodone',
    'Naproxen',
    'Prednisone',
    'Cetirizine',
    'Loratadine',
    'Ranitidine',
    'Omeprazole',
    'Pantoprazole',
    'Metformin',
    'Insulin',
    'Atorvastatin',
    'Simvastatin',
    'Lisinopril',
    'Amlodipine',
    'Losartan',
    'Hydrochlorothiazide',
    'Furosemide',
    'Clopidogrel',
    'Warfarin',
    'Enalapril',
    'Levothyroxine',
    'Albuterol',
    'Fluticasone/Salmeterol',
    'Montelukast',
    'Olanzapine',
    'Sertraline',
    'Fluoxetine',
    'Escitalopram',
    'Citalopram',
    'Venlafaxine',
    'Quetiapine',
    'Risperidone',
    'Diazepam',
    'Lorazepam',
    'Amoxicillin',
    'Azithromycin',
    'Ciprofloxacin',
    'Fluconazole',
    'Acyclovir',
    'Oseltamivir',
    'Metronidazole',
    'Clindamycin',
    'Tamsulosin',
    'Finasteride',
    'Sildenafil'
]
medicine_dropdown1 = OptionMenu(window, selected_medicine1, *options1)
medicine_dropdown1.place(x=396, y=347, width=234, height=23)
def on_dropdown_select(*args):
    print(selected_medicine1.get())
selected_medicine1.trace('w', on_dropdown_select)

selected_medicine2 = StringVar(window)
selected_medicine2.set('-SELECT-') 
options2 = [
    'Aspirin',
    'Paracetamol (Acetaminophen)',
    'Ibuprofen',
    'Acetaminophen/Codeine',
    'Acetaminophen/Hydrocodone',
    'Acetaminophen/Oxycodone',
    'Naproxen',
    'Prednisone',
    'Cetirizine',
    'Loratadine',
    'Ranitidine',
    'Omeprazole',
    'Pantoprazole',
    'Metformin',
    'Insulin',
    'Atorvastatin',
    'Simvastatin',
    'Lisinopril',
    'Amlodipine',
    'Losartan',
    'Hydrochlorothiazide',
    'Furosemide',
    'Clopidogrel',
    'Warfarin',
    'Enalapril',
    'Levothyroxine',
    'Albuterol',
    'Fluticasone/Salmeterol',
    'Montelukast',
    'Olanzapine',
    'Sertraline',
    'Fluoxetine',
    'Escitalopram',
    'Citalopram',
    'Venlafaxine',
    'Quetiapine',
    'Risperidone',
    'Diazepam',
    'Lorazepam',
    'Amoxicillin',
    'Azithromycin',
    'Ciprofloxacin',
    'Fluconazole',
    'Acyclovir',
    'Oseltamivir',
    'Metronidazole',
    'Clindamycin',
    'Tamsulosin',
    'Finasteride',
    'Sildenafil'
]
medicine_dropdown2 = OptionMenu(window, selected_medicine2, *options2)
medicine_dropdown2.place(x=396, y=377, width=234, height=23)
def on_dropdown_select(*args):
    print(selected_medicine2.get())
selected_medicine2.trace('w', on_dropdown_select)

selected_medicine3 = StringVar(window)
selected_medicine3.set('-SELECT-') 
options3 = [
    'Aspirin',
    'Paracetamol (Acetaminophen)',
    'Ibuprofen',
    'Acetaminophen/Codeine',
    'Acetaminophen/Hydrocodone',
    'Acetaminophen/Oxycodone',
    'Naproxen',
    'Prednisone',
    'Cetirizine',
    'Loratadine',
    'Ranitidine',
    'Omeprazole',
    'Pantoprazole',
    'Metformin',
    'Insulin',
    'Atorvastatin',
    'Simvastatin',
    'Lisinopril',
    'Amlodipine',
    'Losartan',
    'Hydrochlorothiazide',
    'Furosemide',
    'Clopidogrel',
    'Warfarin',
    'Enalapril',
    'Levothyroxine',
    'Albuterol',
    'Fluticasone/Salmeterol',
    'Montelukast',
    'Olanzapine',
    'Sertraline',
    'Fluoxetine',
    'Escitalopram',
    'Citalopram',
    'Venlafaxine',
    'Quetiapine',
    'Risperidone',
    'Diazepam',
    'Lorazepam',
    'Amoxicillin',
    'Azithromycin',
    'Ciprofloxacin',
    'Fluconazole',
    'Acyclovir',
    'Oseltamivir',
    'Metronidazole',
    'Clindamycin',
    'Tamsulosin',
    'Finasteride',
    'Sildenafil'
]
medicine_dropdown3 = OptionMenu(window, selected_medicine3, *options3)
medicine_dropdown3.place(x=396, y=407, width=234, height=23)
def on_dropdown_select(*args):
    print(selected_medicine3.get())
selected_medicine3.trace('w', on_dropdown_select)

selected_medicine4 = StringVar(window)
selected_medicine4.set('-SELECT-') 
options4 = [
    'Aspirin',
    'Paracetamol (Acetaminophen)',
    'Ibuprofen',
    'Acetaminophen/Codeine',
    'Acetaminophen/Hydrocodone',
    'Acetaminophen/Oxycodone',
    'Naproxen',
    'Prednisone',
    'Cetirizine',
    'Loratadine',
    'Ranitidine',
    'Omeprazole',
    'Pantoprazole',
    'Metformin',
    'Insulin',
    'Atorvastatin',
    'Simvastatin',
    'Lisinopril',
    'Amlodipine',
    'Losartan',
    'Hydrochlorothiazide',
    'Furosemide',
    'Clopidogrel',
    'Warfarin',
    'Enalapril',
    'Levothyroxine',
    'Albuterol',
    'Fluticasone/Salmeterol',
    'Montelukast',
    'Olanzapine',
    'Sertraline',
    'Fluoxetine',
    'Escitalopram',
    'Citalopram',
    'Venlafaxine',
    'Quetiapine',
    'Risperidone',
    'Diazepam',
    'Lorazepam',
    'Amoxicillin',
    'Azithromycin',
    'Ciprofloxacin',
    'Fluconazole',
    'Acyclovir',
    'Oseltamivir',
    'Metronidazole',
    'Clindamycin',
    'Tamsulosin',
    'Finasteride',
    'Sildenafil'
]
medicine_dropdown4 = OptionMenu(window, selected_medicine4, *options4)
medicine_dropdown4.place(x=396, y=437, width=234, height=23)
def on_dropdown_select(*args):
    print(selected_medicine4.get())
selected_medicine4.trace('w', on_dropdown_select)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1pharma.png"))
image_1 = canvas.create_image(
    450.0,
    300.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2pharma.png"))
image_2 = canvas.create_image(
    450.0,
    108.0,
    image=image_image_2
)

canvas.create_rectangle(
    281.0,
    186.0,
    706.0,
    513.0,
    fill="#D9D9D9",
    outline="")

canvas.create_text(
    456.56658935546875,
    205.0,
    anchor="nw",
    text="Medicine",
    fill="#000000",
    font=("Inter", 15 * -1)
)

canvas.create_text(
    305.0,
    321.0,
    anchor="nw",
    text="Medicine 1:",
    fill="#000000",
    font=("Inter", 12 * -1)
)

canvas.create_text(
    305.0,
    351.0,
    anchor="nw",
    text="Medicine 2:",
    fill="#000000",
    font=("Inter", 12 * -1)
)

canvas.create_text(
    305.0,
    381.0,
    anchor="nw",
    text="Medicine 3:",
    fill="#000000",
    font=("Inter", 12 * -1)
)

canvas.create_text(
    305.0,
    411.0,
    anchor="nw",
    text="Medicine 4:",
    fill="#000000",
    font=("Inter", 12 * -1)
)

canvas.create_text(
    305.0,
    441.0,
    anchor="nw",
    text="Medicine 5:",
    fill="#000000",
    font=("Inter", 12 * -1)
)

canvas.create_text(
    633.0,
    296.0,
    anchor="nw",
    text="Quantity",
    fill="#000000",
    font=("Inter", 12 * -1)
)

canvas.create_text(
    305.0,
    238.0,
    anchor="nw",
    text="Patient ID:",
    fill="#000000",
    font=("Inter", 12 * -1)
)


entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1pharma.png"))
entry_bg_1 = canvas.create_image(
    513.0,
    245.5,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=396.0,
    y=234.0,
    width=234.0,
    height=21.0
)



entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3pharma.png"))
entry_bg_3 = canvas.create_image(
    661.4595336914062,
    328.5,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_3.place(
    x=645.0,
    y=317.0,
    width=32.9190673828125,
    height=21.0
)

entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4pharma.png"))
entry_bg_4 = canvas.create_image(
    661.4595336914062,
    358.5,
    image=entry_image_4
)
entry_4 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_4.place(
    x=645.0,
    y=347.0,
    width=32.9190673828125,
    height=21.0
)

entry_image_5 = PhotoImage(
    file=relative_to_assets("entry_5pharma.png"))
entry_bg_5 = canvas.create_image(
    661.4595336914062,
    388.5,
    image=entry_image_5
)
entry_5 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_5.place(
    x=645.0,
    y=377.0,
    width=32.9190673828125,
    height=21.0
)

entry_image_6 = PhotoImage(
    file=relative_to_assets("entry_6pharma.png"))
entry_bg_6 = canvas.create_image(
    661.4595336914062,
    418.5,
    image=entry_image_6
)
entry_6 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_6.place(
    x=645.0,
    y=407.0,
    width=32.9190673828125,
    height=21.0
)

entry_image_7 = PhotoImage(
    file=relative_to_assets("entry_7pharma.png"))
entry_bg_7 = canvas.create_image(
    661.4595336914062,
    448.5,
    image=entry_image_7
)
entry_7 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_7.place(
    x=645.0,
    y=437.0,
    width=32.9190673828125,
    height=21.0
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1pharma.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=clear_entry_fields,
    relief="flat"
)
button_1.place(
    x=452.0,
    y=476.0,
    width=83.75687408447266,
    height=32.073944091796875
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2pharma.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=button_2_clicked,
    relief="flat"
)
button_2.place(
    x=354.0,
    y=476.0,
    width=83.75687408447266,
    height=32.073944091796875
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3pharma.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=calculate_total_cost,
    relief="flat"
)
button_3.place(
    x=549.0,
    y=476.0,
    width=83.75686645507812,
    height=32.073944091796875
)
window.resizable(False, False)
window.mainloop()
