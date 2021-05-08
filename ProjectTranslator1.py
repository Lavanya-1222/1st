from tkinter import *
from tkinter.ttk import Combobox
from googletrans import Translator, LANGUAGES
from pyttsx3 import *


root = Tk()

root.geometry('1080x400')

root.resizable(0,0)

root.config(bg = 'ghost white')

root.title("Project--Language Translator")


Label(root, text = "LANGUAGE TRANSLATOR", font = "arial 20 bold", bg='white smoke').pack()

Label(root,text ="Translator", font = 'arial 15 bold', bg ='white smoke' ,
      width = '20').pack(side="bottom")

Label(root,text ="Enter Text", font = 'arial 13 bold', bg ='white smoke').place(x=200,y=60)

Label(root,text ="Output", font = 'arial 13 bold', bg ='white smoke').place(x=780,y=60)


Input_text = Text(root,font = 'arial 10',
                  height = 11, padx=5, pady=5, width = 60)
Input_text.place(x=30,y = 100)

Output_text = Text(root,font = 'arial 10',
                   height = 11, wrap = WORD, padx=5, pady= 5, width =60)
Output_text.place(x = 600 , y = 100)

print(list(LANGUAGES.values()))

language = list(LANGUAGES.values())
# print(language)

src_lang =Combobox(root, values=language, width =22)

x=language[21]

src_lang.place(x=20,y=60)

src_lang.set(x)

dest_lang = Combobox(root, values= list(LANGUAGES.values()), width =22)

dest_lang.place(x=890,y=60)

dest_lang.set("Choose the language")



def Translate():
    t=Translator()

    translated=t.translate(text= Input_text.get(1.0,END)
                           , src = src_lang.get(), dest = dest_lang.get())

    Output_text.delete(1.0, END)

    Output_text.insert(END, translated.text)

trans_btn = Button(root, text='Translate', font='arial 12 bold',

                   pady=5, command=Translate, bg='royal blue1',
                       activebackground="Black")



def speech():
  text=Input_text.get(1.0,END)

  en=init()

  en.say(text)

  en.runAndWait()

trans_btn1 = Button(root, text='Speak', font='arial 12 bold', pady=10, command=speech, bg='royal blue1',
                       activebackground="Black")

trans_btn.place(x=490, y=120)

trans_btn1.place(x=495, y=220)

root.mainloop()