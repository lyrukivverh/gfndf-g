from tkinter import *
import random as r
from numpy import*
from random import randint
a=r.choice(['1','2','3']) 
de=0
def ra ():
  global de
  de=de+1
  if de % 2==1:
    global a
    if a=='1':
     hol.create_oval(randint(1,200),randint(1,200),randint(1,200),randint(1,200))
    elif a=='2':
     hol.create_rectangle(randint(1,200),randint(1,200),randint(1,200),randint(1,200))
    else:
      hol.create_polygon(randint(1,200),randint(1,200),randint(1,200),randint(1,200),randint(1,200),randint(1,200))
  else:
    hol.delete('all')
    
    
okno=Tk()
okno.geometry('300x300')
kn=Button(width=5,height=3,command=ra)
kn.pack(side=BOTTOM)
hol=Canvas(okno)
hol.pack(side=TOP)
okno.mainloop