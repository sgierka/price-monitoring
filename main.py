import tkinter as tk
from tkinter import ttk, messagebox
import requests
from bs4 import BeautifulSoup
from shops import *
import os


class GUI(tk.Tk):
    def __init__(self):
        super().__init__()
        # configure window
        self.title('Price Monitoring')
        self.geometry("850x500")
        self.container = tk.Frame(border=2)
        self.resizable(False, False)
        # set the data
        self.products = []
        self.insert_list = []
        self.shops = ['Select shop', 'Hebe', 'Rossman', 'Natura', 'Xkom']
        # methods
        self.SetGUI()

    def CheckInputs(self):
        """ check if all inputs are given
            and create an object;
            var data (list) contains:
            [[name, regular price, sale price, sale%, url]]"""

        if len(self.t_link.get()) != 0:
            if self.combo.get() == 'Hebe':
                obj = Hebe()
                obj.GetURL(self.t_link.get())
                obj.ShortenUrl()
                data = obj.GetInfo()
                self.AddToList(data)
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
            self.t_link.delete('0', tk.END)
        else:
            tk.messagebox.showinfo('Error', 'Please enter the product URL')

    def AddToList(self, data):
        """ add product to the list of products
            @param data: (list) [[name, regular price,
            sale price, sale%, url]] """
        for elem in data:
            if elem not in self.products:
                self.products.append(elem)
                self.InsertText()
            else:
                tk.messagebox.showinfo('Error', 'This product exists on the ' +
                                       'list or in the file')

    def InsertText(self):
        """show products info in the window"""
        message = """| %30s | %6s | %9s | %8s| %10s"""

        for elem in self.products:
            if elem not in self.insert_list:
                self.t_field.insert(tk.END, '\n')
                self.t_field.insert(tk.END, message %
                                    (elem[0], elem[1], elem[2], elem[3],
                                     elem[4]))
                self.insert_list.append(elem)

    def ClearFile(self):
        """ clear products data saved in the file"""
        with open('product_data.txt', 'w+') as f:
            f.truncate()

    def ClearList(self):
        """clear products list"""
        self.products.clear()

    def ClearScreen(self):
        """ clear all the products in the window"""
        self.insert_list.clear()
        self.t_field.delete("2.0", tk.END)

    def SaveToFile(self):
        """saving products data to a file"""
        with open('product_data.txt', 'w+') as f:
            for i in range(len(self.products)):
                f.write('\n')
                for j in range(len(self.products[i])):
                    f.write(str(self.products[i][j])+'\t')
        tk.messagebox.showinfo('Success', 'The product has been saved to file')

    def LoadFromFile(self):
        """loading products data from a file"""
        self.ClearList()
        self.ClearScreen()
        with open('product_data.txt', 'r+') as f:
            if os.path.getsize('product_data.txt') != 0:
                data = f.read()
                data = data.split('\n')
                rows = [elem.split('\t') for elem in data][1:]
                for elem in rows:
                    del elem[-1]
                self.AddToList(rows)
            else:
                tk.messagebox.showinfo('Error', 'File is empty')

    def SetGUI(self):
        """setting and packing frames, labels, buttons etc."""
        # frames
        f_top = tk.Frame(self, width=450, height=100, bg='#95a5a6', bd=0,
                         highlightbackground='white', highlightthickness=2)
        f_top.pack(side='top', fill='both')
        f_right = tk.Frame(self, width=150, height=400,  bg='#2c3e50',
                           highlightbackground='white', highlightthickness=2)
        f_right.pack(side='right', fill='both')
        f_bottom = tk.Frame(self, width=300, height=400,  bg='azure2',
                            highlightbackground='white', highlightthickness=2)
        f_bottom.pack(side='top', fill='both')

        # create text field with header
        self.t_field = tk.Text(f_bottom, width=10, height=50)
        self.t_field.pack(side='top', fill='both')
        message_headers = """| %30s | %6s | %9s | %8s| %10s"""
        self.t_field.insert(tk.END, message_headers %
                            ('Name', 'Price', 'Sale', 'Sale[%]', 'Link\n'))
        # create labels and texts
        l1 = tk.Label(f_top, text='Paste the link below', bg='#95a5a6')
        l1.pack(side='top', fill='both')
        self.t_link = tk.Entry(f_top, width=90)
        self.t_link.pack(side='top')
        t_info = tk.Label(f_right, text='Version: 1.0' +
                          '\nmade by sgierka', font=('Arial', 7, 'bold'),
                          bg='white')
        t_info.pack(side='bottom')

        # create combobox
        self.combo = ttk.Combobox(f_top, text='Choose shop', values=self.shops,
                                  width=30, state='readonly')
        self.combo.set('Select shop')
        self.combo.pack(side='top')

        # create buttons
        b_search = tk.Button(f_top, text="Search", width=10,
                             command=self.CheckInputs)
        b_search.pack(side='top', padx=10, pady=2)
        b_load = tk.Button(f_right, text='Load', width=10,
                           command=self.LoadFromFile)
        b_load.pack(side='top', padx=10, pady=10)
        b_save = tk.Button(f_right, text='Save', width=10,
                           command=self.SaveToFile)
        b_save.pack(side='top', padx=10, pady=10)
        b_clear_f = tk.Button(f_right, text='Clear file', width=10,
                              command=self.ClearFile)
        b_clear_f.pack(side='top', padx=10, pady=10)
        b_clear_sc = tk.Button(f_right, text='Clear window', width=10,
                               command=self.ClearScreen)
        b_clear_sc.pack(side='top', padx=10, pady=10)


def main():
    gui = GUI()
    gui.mainloop()

if __name__ == '__main__':
    main()
