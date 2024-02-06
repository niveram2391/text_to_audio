import tkinter
from tkinter import filedialog

from gtts import gTTS
from PyPDF2 import PdfReader
from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename, asksaveasfilename


def text_to_speech(text,filename):
    name = file_name.get()
    answer = tkinter.messagebox.askquestion("Save", "Do you want to save?")
    if answer == 'yes':
        file_path = tkinter.filedialog.asksaveasfilename(initialfile=name)
        speech = gTTS(text=text,lang="en",slow=False)
        speech.save(f'{file_path}.mp3')
    else:
        window.destroy()


def open_file():
    text = ""
    file = filedialog.askopenfilename(initialdir="/",
                                          title="Select a File",
                                          )
    with open(file, "rb") as file:
        reader = PdfReader(file)

        number_of_pages = len(reader.pages)

        for page in range(number_of_pages):
            text += reader.pages[page].extract_text()
    text_to_speech(text=text,filename=file_name)


window = Tk()
window.title("Text to speech Converter")
window.config(bg='#569DAA')
window.geometry('600x400')
window.columnconfigure(0, weight =1)
window.columnconfigure(4, weight =1)

description = Label(text = "Convert a PDF file to audio format", font= ("Arial",15,"bold"),
                    fg = "#577D86", bg="#B9EDDD", padx=90,pady=50)
description.grid(column=1,row=1,columnspan=3,pady=(50,50))

save_file = Label (text = "Save Audio File as ",font= ("Arial",15),fg="#B9EDDD", bg="#569DAA" )
save_file.grid(column = 1, row=3)

file_name = Entry(width = 20,font =("Arial",15) )
file_name.insert(0,"Enter File Name")
file_name.grid(column =2, row=3)

upload_button = Button(text="UPLOAD",height=2, width=10,font= ("Arial",10,"bold"),bg="#B9EDDD", fg="#569DAA",command=open_file )
upload_button.grid(column=3, row=3,padx=10)

window.mainloop()