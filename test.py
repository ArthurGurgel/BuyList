import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *

inventory = [ ]
buy_list = [ ]
class PrincipalGUI:
	def __init__(self, master=None):

		self.frame1=Frame(master)
		self.frame2=Frame(master)
		
		self.label = Label(self.frame1, text = 'Welcome to buy list',)
		self.label.pack(side='left')
		
		self.button_add = Button(self.frame2, text = 'Add item', command = AddGUI)
		self.button_inventory = Button(self.frame2, text = 'Inventory', command = InventoryGUI)
		self.button_list = Button(self.frame2, text = 'Buy list')
		
		self.button_add.pack(side = 'left')
		self.button_inventory.pack(side = 'left')
		self.button_list.pack(side='left')
		
		self.button_add.pack()
		self.button_inventory.pack()
		self.button_list.pack()
		
		self.frame1.pack()
		self.frame2.pack()
		
class AddGUI:

    def add(self):
        inventory.append([self.entry.get(), self.inventory.get(), self.minimum.get(), self.combo.get()])
        messagebox.showinfo('Inventory',self.entry.get() + ' has been add on inventory')

    def __init__(self, master=None):
        
        self.frame1 = Frame(master)
        self.frame2 = Frame(master)
        self.frame3 = Frame(master)
        self.frame4 = Frame(master)
        
        self.label = Label(self.frame1, text = 'Insert item:  ')
        self.entry = Entry(self.frame1, width = 30)

        self.label.pack(side = 'left')
        self.entry.pack(side = 'left')
        
        self.label1 = Label(self.frame2, text = 'Insert the amount:  ')
        self.inventory = Entry(self.frame2, width = 25)

        self.label1.pack(side = 'left')
        self.inventory.pack(side = 'left')

        self.label2 = Label(self.frame3, text = 'Insert the minimum amount: ')
        self.minimum = Entry(self.frame3, width = 19)

        self.label2.pack(side = 'left')
        self.minimum.pack(side = 'left')
        
                        
        self.combo = Combobox (self.frame4)
        self.combo['values']= ('KG', 'Liter', 'UND', 'Pct' )
        self.combo.current(0)
        self.combo.pack( )

        self.button = Button(self.frame4, text = 'Add',  command  = self.add)
        self.button_exit = Button(self.frame4, text = 'Exit',  command = PrincipalGUI)

        self.button.pack(side = 'left')
        self.button_exit.pack(side = 'left')

        self.button.pack()
        self.button_exit.pack()

        self.frame1.pack()
        self.frame2.pack()
        self.frame3.pack()
        self.frame4.pack()

class InventoryGUI:
	def __init__(self, master=None):
		self.frame1= Frame(master)
		
		self.frame1.pack()
		
root = Tk()
PrincipalGUI(root)
root.mainloop()

