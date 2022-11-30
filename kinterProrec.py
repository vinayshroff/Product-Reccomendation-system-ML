import pickle 
import pandas as pd
import numpy as np



from tkinter import *
from tkinter import ttk
#creating the application main window.   
top = Tk()
top.title("Prorec Software")


WIDTH =900
HEIGHT = 400

x = int((top.winfo_screenwidth() / 2) - (WIDTH / 2))
y = int((top.winfo_screenheight() / 2) - (HEIGHT / 2))

top.geometry(f'{WIDTH}x{HEIGHT}+{x}+{y}')



new_df=pickle.load(open("new_df.pkl",'rb')) # Readind the binary file from pickle file
product_list_tuple = tuple(set(new_df['name'].values))

similarity=pickle.load(open("similarity.pkl",'rb'))


options = product_list_tuple
# Combobox creation
n = StringVar()
monthchoosen = ttk.Combobox(top, width = 27, textvariable = n, state="readonly",)
  
# Adding combobox drop down list
monthchoosen['values'] = product_list_tuple

monthchoosen.grid(column = 1, row = 0,padx=10)
monthchoosen.current()
  

#Text box

inputtxt = Text(top, height = 10,
                width = 68,
                bg = "light yellow",relief="ridge")
inputtxt.grid(row=0,column=6,rowspan=10,pady=10,padx=10)

# Product Reccomensation Function from similarities
def recommend(prod,num):
    prod_index=new_df[new_df['name']== prod].index[0]
    distances= similarity[prod_index]
    prod_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:num+1]
    
    l=[]
    inputtxt.delete("1.0", "end")
    for i in prod_list:
        l.append(new_df.iloc[i[0]]['name'])
    for x in range(len(l)):
        inputtxt.insert(END,str(x+1)+" : "+l[x]+'\n')
        

#------------------------#
new_df=pickle.load(open("new_df.pkl",'rb')) # Readind the binary file from pickle file
product_list_tuple = tuple(set(new_df['name'].values))

similarity=pickle.load(open("similarity.pkl",'rb'))

#------------------------
#Entering the event main loop
name_var=StringVar()
s=Spinbox(top, from_= 1, to = 10,relief="ridge") 
s.grid(column = 1, row = 1,padx=10)

b1=Button(top, text = "Get Reccomendation",command=lambda: recommend(n.get(),int(s.get())))
b1.grid(column = 3, row = 0,pady=5)

top.mainloop() 
