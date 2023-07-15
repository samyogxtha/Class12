from customtkinter import *
app=CTk()
def segmented_button_callback(value):
    print("segmented button clicked:", value)

segemented_button = CTkSegmentedButton(app, values=["Value 1", "Value 2", "Value 3"],
                                                     command=segmented_button_callback)
segemented_button.pack()
segemented_button.set("Value 1")
app.mainloop()