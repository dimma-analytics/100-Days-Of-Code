from tkinter import *

#Buttons
def action():
    km_value = int(entry.get()) * 1.60934
    kilometer_converter_label.config(text=km_value)
    


window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=500, height=300)
window.config(padx=100, pady=50)

#Entry
entry= Entry(width=10, font=("Arial", 20, "bold"))
#Add some text to begin with
entry.insert(END, string="0")
#Gets text in entry
print(entry.get())
entry.grid(column=1, row=0)


#Mile label
miles_label = Label(text="Miles", font=("Arial", 20, "bold"))
miles_label.grid(column=2, row=0)
miles_label.config(padx=10, pady=10)

#Is equal label
is_equal_label = Label(text="is equal to", font=("Arial", 20, "bold"))
is_equal_label.grid(column=0, row=1)
is_equal_label.config(padx=10,pady=10)

#kilometer converter label
kilometer_converter_label = Label(text="0",font=("Arial", 20, "bold"))
kilometer_converter_label.grid(column=1, row=1)

#kilometer label
kilometer_label = Label(text="Km",font=("Arial", 20, "bold"))
kilometer_label.grid(column=2, row=1)


#calls action() when pressed
button = Button(text="Calculate", command=action, font=("Arial", 20, "bold"))
button.grid(column=1, row=2)







window.mainloop()