from tkinter import *
import math
import cable_catalog

BACKGROUND = "#A6CDC6"

ISOLATION_TYPE= ["CU/PVC/PVC", "AL/PVC/PVC", "CU/PVC/STA/PVC", "AL/PVC/STA/PVC", "CU/PVC/SWA/PVC", "AL/PVC/SWA/PVC",
        "CU/XLPE/PVC", "AL/XLPE/PVC", "CU/XLPE/STA/PVC", "AL/XLPE/STA/PVC", "CU/XLPE/SWA/PVC", "AL/XLPE/SWA/PVC"]
BREAKER_SIZE= [10, 16, 20, 25, 32, 40, 50, 63, 80, 125, 160, 250, 400, 630, 800, 1000, 1250, 1600, 3200]
CABLE_SIZE= [1.5, 2.5, 4, 6, 8, 10, 16, 25, 35, 50, 70, 95, 120, 150, 185, 240, 300]

ENVIRONMENT= ["ground", "duct", "air"]
#=================================================== Screen ===========================================================
window= Tk()
window.title("Project X")
window.config(padx= 20, pady= 20, bg=BACKGROUND)
window.minsize(width=800, height=500)

#================================================ Function ============================================================
def get_power_type():
    power_unit.config(text=("KW" if usage_power.get() == 1 else "KVA"))

def get_result():
    power = float(power_input.get())
    p_f = float(power_factor_input.get())
    voltage = float(voltage_input.get())
    current = 1

    # 3 Phase
    if r_volt.get() == 1:
        voltage = voltage * math.sqrt(3)
    # Single phase
    elif r_volt.get() == 2:
        voltage = voltage

    # Power Kw
    if usage_power.get() == 1:
        current = round( ( power * 1000 / voltage * p_f ) * 1.25, 2)
    # Power KVA
    elif usage_power.get() == 2:
        current = round(  (power * 1000 / voltage ) * 1.25, 2)

    current_value.config(text=f"{current} Amp")
    # Breaker Selection
    for breaker in BREAKER_SIZE:
        if breaker >= current:
            breaker_description.config(text=f"{breaker} Amp")
            break

    # Cable Selection
    isolation = ISOLATION_TYPE[cable_type.get()]
    surround_environment = ENVIRONMENT[envi_type.get()]
    selected_cable = cable_catalog.cable_data[isolation][surround_environment]
    for cable in selected_cable:
        if cable["current"] >= current:
            cable_size = cable["size"]
            cable_description.config(text=f"{isolation}, {cable_size} mm2")


#======================================================= Labels =======================================================

isolation_type = Label(text="Isolation Type :", font=("arial", 11, "bold"), bg=BACKGROUND)
isolation_type.place(x=0, y=0)

environment_text= Label(text="Environment :", font=("arial", 11, "bold"), bg=BACKGROUND)
environment_text.place(x=230, y=0)

number_of_phase_text= Label(text="Number of Phase :",font=("arial", 11, "bold"), bg=BACKGROUND)
number_of_phase_text.place(x=230, y= 150)

power_type= Label(text="Usage Power :",font=("arial", 11, "bold"), bg=BACKGROUND)
power_type.place(x=230, y= 270)

power_text = Label(text="Power : ", font=("arial", 10, "normal"), bg=BACKGROUND)
power_text.place(x=500, y=0)

power_unit= Label(text="-", width=5, font=("arial", 9, "normal"), bg=BACKGROUND)
power_unit.place(x= 620, y= 0)

power_factor_text = Label(text="P.f : ", font=("arial", 10, "normal"), bg=BACKGROUND)
power_factor_text.place(x=521, y=60)

current_value= Label(text="---", font=("arial", 10, "bold"), bg=BACKGROUND)
current_value.place(x=578, y=150)

current_text= Label(text="Current :", font=("arial", 11, "bold"), bg=BACKGROUND)
current_text.place(x=512, y=150)

cable_text= Label(text="Cable Description :", font=("arial", 11, "bold"), bg=BACKGROUND)
cable_text.place(x=440, y=210)

cable_description = Label(text="---", font=("arial", 10, "bold"), bg=BACKGROUND)
cable_description.place(x=578, y=210)

voltage_text = Label(text="Voltage :", font=("arial", 10, "normal"), bg=BACKGROUND)
voltage_text.place(x=493, y=30)

voltage_unit = Label(text="Volt", font=("arial", 9, "normal"), bg=BACKGROUND )
voltage_unit.place(x=628, y=30)

breaker_text = Label(text="C.B Description  :", font=("arial", 11, "bold"), bg=BACKGROUND)
breaker_text.place(x=450, y=180)

breaker_description = Label(text="---", font=("arial", 10, "bold"), bg=BACKGROUND)
breaker_description.place(x=578, y=180)

earth_cable_text = Label(text="Earth Cable :", font=("arial", 11, "bold"), bg=BACKGROUND)
earth_cable_text.place(x=485, y=240)

earth_cable_description = Label(text="---", font=("arial", 10, "bold"), bg=BACKGROUND)
earth_cable_description.place(x=578, y=240)

#=============================================== Selections ===========================================================

# Isolation Type:
cable_type = IntVar()
type1 = Radiobutton(text="CU/PVC/PVC", font=("arial", 10, "bold"), value=0, variable=cable_type, bg=BACKGROUND)
type1.place(x=0, y=30)
type2 = Radiobutton(text="AL/PVC/PVC", font=("arial", 10, "bold"), value=1, variable=cable_type, bg=BACKGROUND)
type2.place(x=0, y=60)
type3 = Radiobutton(text="CU/PVC/STA/PVC", font=("arial", 10, "bold"), value=2, variable=cable_type, bg=BACKGROUND)
type3.place(x=0, y=90)
type4 = Radiobutton(text="AL/PVC/STA/PVC", font=("arial", 10, "bold"), value=3, variable=cable_type, bg=BACKGROUND)
type4.place(x=0, y=120)
type5 = Radiobutton(text="CU/PVC/SWA/PVC", font=("arial", 10, "bold"), value=4, variable=cable_type, bg=BACKGROUND)
type5.place(x=0, y=150)
type6 = Radiobutton(text="AL/PVC/SWA/PVC", font=("arial", 10, "bold"), value=5, variable=cable_type, bg=BACKGROUND)
type6.place(x=0, y=180)
type7 = Radiobutton(text="CU/XLPE/PVC", font=("arial", 10, "bold"), value=6, variable=cable_type, bg=BACKGROUND)
type7.place(x=0, y=210)
type8 = Radiobutton(text="AL/XLPE/PVC", font=("arial", 10, "bold"), value=7, variable=cable_type, bg=BACKGROUND)
type8.place(x=0, y=240)
type9 = Radiobutton(text="CU/XLPE/STA/PVC", font=("arial", 10, "bold"), value=8, variable=cable_type, bg=BACKGROUND)
type9.place(x=0, y=270)
type10 = Radiobutton(text="AL/XLPE/STA/PVC", font=("arial", 10, "bold"), value=9, variable=cable_type, bg=BACKGROUND)
type10.place(x=0, y=300)
type11 = Radiobutton(text="CU/XLPE/SWA/PVC", font=("arial", 10, "bold"), value=10, variable=cable_type, bg=BACKGROUND)
type11.place(x=0, y=330)
type12 = Radiobutton(text="AL/XLPE/SWA/PVC", font=("arial", 10, "bold"), value=11, variable=cable_type, bg=BACKGROUND)
type12.place(x=0, y=360)

# Surrounded Environment:
envi_type = IntVar()
envir1= Radiobutton(text="Ground", font=("arial", 10, "bold"), value=0, variable=envi_type, padx=50, bg=BACKGROUND)
envir1.place(x=185, y=30)
envir2 = Radiobutton(text="Duct", font=("arial", 10, "bold"), value=1, variable=envi_type, padx=50, bg=BACKGROUND)
envir2.place(x=185, y=60)
envir3 = Radiobutton(text="Air", font=("arial", 10, "bold"), value=2, variable=envi_type, padx=100, bg=BACKGROUND)
envir3.place(x=135, y=90)

# Number of Phase:
r_volt = IntVar()
volt1= Radiobutton(text="3 Ø", font=("arial", 10, "bold"), value=1, variable=r_volt, padx=50, bg=BACKGROUND)
volt1.place(x=185, y=180)
volt2 = Radiobutton(text="1 Ø", font=("arial", 10, "bold"), value=2, variable=r_volt, padx=50, bg=BACKGROUND)
volt2.place(x=185, y=210)

# Power Type
usage_power= IntVar()
watt= Radiobutton(text="KW", font=("arial", 10, "bold"), value=1, variable=usage_power, padx=50, bg=BACKGROUND,
                    command= get_power_type)
watt.place(x=185, y=300)
va = Radiobutton(text="KVA", font=("arial", 10, "bold"), value=2, variable=usage_power, padx=50, bg=BACKGROUND,
                    command= get_power_type)
va.place(x=185, y=330)

#================================================== Entry ============================================================

power_input= Entry(width=10)
power_input.place(x=550, y=0,)
#set the courser in power input field
power_input.focus()

power_factor_input= Entry(width=10)
power_factor_input.insert(END, string="1")
power_factor_input.place(x=550, y=60, )

voltage_input = Entry(width=10)
voltage_input.place(x=550, y=30)
#=============================================== Button ==============================================================
get_button = Button(text="Get", width=10, command=get_result)
get_button.place(x=330, y=420)
window.mainloop()

window.mainloop()