from tkinter import *

BACKGROUND = "#A6CDC6"


window= Tk()
window.title("Project X")
window.config(padx= 20, pady= 20, bg=BACKGROUND)
window.minsize(width=800, height=500)

#===============

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






window.mainloop()