import tkinter as tk
from tkinter import ttk, messagebox
import requests, webbrowser
from bs4 import BeautifulSoup
from os import path
from shops import *
from functools import partial
from tkHyperlinkManager import HyperlinkManager



class GUI(tk.Tk):
    def __init__(self):
        super().__init__()
        #configure window
        self.title('Price checker')
        self.geometry("850x500")
        self.container = tk.Frame(border=2)
        self.resizable(False, False)
        #set the data
        self.products = []
        self.urls = []
        self.shops = ['Select shop', 'Hebe', 'Rossman','Natura','Xkom']
        #methods
        self.SetGUI()


    def callback(url):
        webbrowser.open_new_tab(self.url)

    def CheckInputs(self):
        if len(self.t_link.get()) != 0:
            if self.combo.get() == 'Hebe':
                obj = Hebe()
                obj.GetURL(self.t_link.get())
                obj.ShortenUrl()
                dane = obj.GetPrices()
                self.InsertText(dane)

            elif self.combo.get() == 'Rossman':
                obj = Rossman()
                obj.GetURL(self.t_link.get())
            elif self.combo.get() == 'Natura':
                obj = Natura()
                obj.GetURL(self.t_link.get())
            elif self.combo.get() == 'Xkom':
                obj = Xkom()
                obj.GetURL(self.t_link.get())
            elif self.combo.get() == 'Select shop':
                tk.messagebox.showinfo('Error', 'Please select the shop')
        else:
            tk.messagebox.showinfo('Error', 'Please enter the product URL')    

    # def AddingToLists(self, dane, url):
    #     print(dane)
    #     print(url)
    #     for elem in dane:
    #         if elem not in self.products:
    #             self.products.append(elem)
    #         else:
    #             tk.messagebox.showinfo('Error', 'This product is already on the list')
    #     if url not in self.urls:
    #         self.urls.append(url)

        self.InsertText()

    def hyperlink(self, event):
        webbrowser.open_new(url)

    def InsertText(self, dane): #name, value_before, value_now, sale_pct, url
        for elem in dane:
            if elem not in self.products:
                self.products.append(elem)
          

                message = """| %30s | %6s | %9s | %8s|""" 
                self.t_field.insert(tk.END, message % (self.products[-1][0],self.products[-1][1], self.products[-1][2], self.products[-1][3])) 
                message2 ="""%10s"""
                hyperlink = HyperlinkManager(self.t_field)
                self.t_field.insert(tk.END, message2 %(self.products[-1][4])), hyperlink.add(partial(webbrowser.open, self.products[-1][4]))
                self.t_field.tag_add('nwm', '2.65', '2.90')
                self.t_field.tag_config('nwm', background='yellow')
                self.t_field.insert(tk.END,'\n')
            else:
                tk.messagebox.showinfo('Error', 'This product is already on the list')
        
    def SaveToFile(self): 
        """saving data to a file"""
        with open('product_data.txt', 'w+') as f:
            for i in range (len(self.products)):
                f.write('\n')
                for j in range (len(self.products[i])):
                    f.write(str(self.products[i][j])+'\t')
        tk.messagebox.showinfo('', 'The file has been saved')

    def test(self, lista):
        print(lista)

    def LoadFile(self):
        """loading data from a file"""
        with open('product_data.txt', 'r+') as f:
            dane = f.read()
            dane = dane.split('\n')
            rows = [elem.split('\t') for elem in dane][1:]
            for elem in rows:
                del elem [-1]
        print(rows)
        self.InsertText(rows)    
    
    def SetGUI(self):
        """setting and packing frames, labels, buttons etc."""
        #frames
        f_top = tk.Frame(self, width=450, height= 100, bg='#95a5a6', bd = 0, highlightbackground='white', highlightthickness=2)
        f_top.pack(side='top', fill = 'both')
        f_right = tk.Frame(self, width=150,height= 400,  bg='#2c3e50', highlightbackground='white', highlightthickness=2)
        f_right.pack(side='right', fill = 'both')
        f_bottom = tk.Frame(self, width=300, height= 400,  bg ='azure2', highlightbackground='white', highlightthickness=2)
        f_bottom.pack(side='top', fill='both')

        self.t_field= tk.Text(f_bottom,width=10, height= 50)
        self.t_field.pack(side ='top', fill='both')  
        message_headers = """| %30s | %6s | %9s | %8s| %10s"""
        self.t_field.insert(tk.END, message_headers % ('Name', 'Price', 'Sale', 'Sale[%]', 'Link\n'))
    
        #create labels and texts
        l1 = tk.Label(f_top, text='Paste the link below', bg='#95a5a6')
        l1.pack(side='top', fill='both')
        self.t_link = tk.Entry(f_top, width=90)
        self.t_link.pack(side='top')
        t_info = tk.Label(f_right, text='Info:\nthe first & the last version\nmade by Shadoqie', font = ('Arial',7, 'bold'), bg='white')
        t_info.pack(side='bottom')

        #create combobox
        self.combo = ttk.Combobox(f_top, text= 'Choose shop', values = self.shops, width=30, state='readonly')
        self.combo.set('Select shop')
        self.combo.pack(side = 'top')

        #create buttons
        b_search = tk.Button(f_top, text="Search", width=10, command= self.CheckInputs)
        b_search.pack(side='top', padx=10, pady=2)
        b_load = tk.Button(f_right, text= 'Load', width=10, command = self.LoadFile)
        b_load.pack(side= 'top', padx=10, pady=10)
        b_save = tk.Button(f_right, text= 'Save', width=10, command= self.SaveToFile)
        b_save.pack(side= 'top', padx=10, pady=10)
        b_delete = tk.Button(f_right, text= 'Delete', width=10)
        b_delete.pack(side= 'top', padx=10, pady=10)

def main(): 
    gui = GUI()
    gui.mainloop()

if __name__ == '__main__':
    main()