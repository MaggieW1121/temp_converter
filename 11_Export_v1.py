from tkinter import *
from functools import partial # To prevent unwanted windows
from tkmacosx import Button 

import random

class Convertor:
    def __init__(self):
        
        # Formatting variables...
        background_color = "light blue"

        # Convertor Main Screen GUI...
        self.convertor_frame = Frame(width=300, height= 300, bg=background_color,
                                     pady=10) # apply padding to the convertor frame
        self.convertor_frame.grid()

        # Temperature Convertor Heading (row 0)
        self.temp_convertor_label = Label(self.convertor_frame, text="Temperature Converter",
                                          font=("Arial", "16", "bold"),
                                          bg=background_color,
                                          padx=10, pady=10)
        self.temp_convertor_label.grid(row=0)

        # Export Button (row 1)
        self.export_button = Button(self.convertor_frame, text="Export", 
                                  font=("Arial", "14"),
                                  padx=10, pady=10, 
                                  borderless=1, command=self.export)
        self.export_button.grid(row=1)

    def export(self):
        get_export = Export(self)

class Export:
    def __init__(self, partner):

        background = "LightCyan2"

        # disable export button
        partner.export_button.config(state=DISABLED)

        # Set up child window (i.e. export box)
        self.export_box = Toplevel()

        # If users press cross at top, closes export and 'releases' export button
        self.export_box.protocol('WM_DELETE_WINDOW', 
                                 partial(self.close_export, partner))

        # Set up GUI Frame
        self.export_frame = Frame(self.export_box, width = 300, bg=background)
        self.export_frame.grid()

        # Set up Export heading - row 0
        self.exp_heading = Label(self.export_frame, 
                                 text="Export / Instructions",
                                 font=("Arial", "14", "bold"), bg=background)
        self.exp_heading.grid(row=0)

        # Export Instructions (label, row 1)
        self.export_text = Label(self.export_frame,
                                  text="Enter a filename in the box below "
                                  "and press the Save button to save your "
                                  "calculation history to a text file. ",
                                  wrap = 250,
                                  justify=LEFT, width=40, bg=background)
        self.export_text.grid(row=1)

        # Export text (label, row 2)
        self.export_text = Label(self.export_frame, text="If the filename you enter below already exists."
                                 "It's contents will be replaced with your calculation history",
                                 justify=LEFT, bg="#ffafaf", fg="maroon",
                                 font="Arial 10 italic", wrap=225, padx=10)
        self.export_text.grid(row=2, pady=10)

        # File Entry Box (row 3)
        self.filename_entry = Entry(self.export_frame, width=20,
                                    font="Arial 14 bold", justify=CENTER)
        self.filename_entry.grid(row=3, pady=10) # used to be 2

        # Save / Cancel Frame (row 4)
        self.save_cancel_frame = Frame(self.export_frame)
        self.save_cancel_frame.grid(row=5, pady=10)

        # Save and Cancel Buttons (row 0 of save_cancel_frame)
        self.save_button = Button(self.save_cancel_frame, borderless=1, text="Save")
        self.save_button.grid(row=0, column=0)

        self.cancel_button = Button(self.save_cancel_frame, text="Cancel", borderless=1,
                                    command=partial(self.close_export, partner))
        self.cancel_button.grid(row=0, column=1)
    
    def close_export(self, partner):
        # Put export button back to normal...
        partner.export_button.config(state=NORMAL)
        self.export_box.destroy()

# main routine
if __name__== "__main__":
    root = Tk()
    root.title("Temperature Convertor")
    something = Convertor()
    root.mainloop()