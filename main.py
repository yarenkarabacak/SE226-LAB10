from collections import Counter
from tkinter import *

myTk = Tk()
myTk.geometry("1000x500")
frame = Frame(myTk)
frame.pack()
bottomFrame = Frame(myTk)
bottomFrame.pack(side=BOTTOM)
title = myTk.title("my new gui")

myFile = open('//Users//yarenkarabacak//Desktop//Marvel.txt')


def fileReader():
    content = myFile.readlines()
    for i in content:
        text.insert('1.0',i)
    text.pack()
    myFile.close()


def calculateFreq():
    t2 = myFile.readlines()
    freq = {}
    words = []
    for line in t2:
        words.append(line.split())

    for item in words:
        for i in item:
            if (i in freq):
                freq[i] += 1
            else:
                freq[i] = 1
    for allKeys in freq:
        print("\"", allKeys, "\"", end=" ")
        print(freq[allKeys], end=" ")
        print()
        str_ = (allKeys, "=", (freq[allKeys]))
        text.insert(END, str_)
        text.insert(END, "\n")

    myFile.close()

def clearToTextInput():
   text.delete("1.0","end")

text = Text(frame,height=30,width=150,background='pink')
text2 = Text(frame,height=30,width=150,background='blue')

buttonR = Button(bottomFrame,text='Read', width=10, command=fileReader, font=('Comic Sans',16))
buttonR.pack()
buttonC = Button(bottomFrame,text='Calculate', width=10, command=calculateFreq, font=('Comic Sans',16))
buttonC.pack()
buttonCl=myTk.Button(myTk,height=1,width=10, text="Clear",command=clearToTextInput)
buttonCl.pack()



myTk.mainloop()
