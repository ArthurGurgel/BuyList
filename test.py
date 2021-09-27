import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
from pymongo import MongoClient
import pprint   

#Create screen informations
root = Tk()
root.title('BUY LIST')
root.geometry('400x400')
#Connect to DB
client = MongoClient('localhost', 27017)
#Create a DB
db = client.test
#Create a principal screen
class PrincipalGUI:
	def __init__(self, master=None):

		self.frame1=Frame(master)
		self.frame2=Frame(master)
		
		self.label = Label(self.frame1, text = 'Welcome to buy list',)
		self.label.pack(side='left')
		#Create btns and set commands
		self.button_add = Button(self.frame2, text = 'Add item', command = AddGUI)
		self.button_inventory = Button(self.frame2, text = 'Inventory', command = InventoryGUI)
		self.button_list = Button(self.frame2, text = 'Buy list', command = BuyListGUI)
		
		self.button_add.pack(side = 'left')
		self.button_inventory.pack(side = 'left')
		self.button_list.pack(side='left')
		
		self.button_add.pack()
		self.button_inventory.pack()
		self.button_list.pack()
		
		self.frame1.pack()
		self.frame2.pack()
		
class AddGUI:
    #Funcction of btn
    def add(self):
        #Connect a Data Base
        client = MongoClient('localhost', 27017)

        #Insert into a Table
        db.itens.insert_one(
               {
                    'item': self.item.get(),
                    'amount': self.amount.get(),
                    'minimum': self.minimum.get(),
                    'unity': self.combo.get()                                 
               }
        )

        #Clear the text
        self.item.delete(0, END)
        self.amount.delete(0, END)
        self.minimum.delete(0, END)
                
    def __init__(self, master=None):
        
        self.frame1 = Frame(master)
        self.frame2 = Frame(master)
        self.frame3 = Frame(master)
        self.frame4 = Frame(master)
        
        self.label = Label(self.frame1, text = 'Insert item:  ')
        self.item = Entry(self.frame1, width = 30)

        self.label.pack(side = 'left')
        self.item.pack(side = 'left')
        
        self.label1 = Label(self.frame2, text = 'Insert the amount:  ')
        self.amount = Entry(self.frame2, width = 25)

        self.label1.pack(side = 'left')
        self.amount.pack(side = 'left')

        self.label2 = Label(self.frame3, text = 'Insert the minimum amount: ')
        self.minimum = Entry(self.frame3, width = 18)

        self.label2.pack(side = 'left')
        self.minimum.pack(side = 'left')
        
                        
        self.combo = Combobox (self.frame4)
        if self.amount.get() == '1':
        	self.combo['values']= ('KG', 'Liter', 'UN', 'Pct' )
        else:
        	self.combo['values']= ('KG', 'Liters', 'UNs', 'Pcts' )
        self.combo.current(0)
        self.combo.pack( )

        self.button = Button(self.frame4, text = 'Add',  command  = self.add)
        self.button_exit = Button(self.frame4, text = 'Exit',  command = root.destroy)

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
            self.frame2= Frame(master)

            client = MongoClient('localhost', 27017)  # Conectando ao banco
            db = client.teste  # selecionando o banco de dados
            collection = db.itens.find()

            self.stock = Listbox (self.frame1)
            for document in collection:
                self.stock.insert(END, document)
            
            self.button_exit = Button(self.frame2, text = 'Exit',  command = root.destroy)

                       
            self.stock.pack()
            self.button_exit.pack()
            self.frame1.pack()
            self.frame2.pack()
		
class BuyListGUI:
	def __init__(self, master=None):
		self.frame1= Frame(master)
		self.frame2= Frame(master)
        
		
		self.frame1.pack()
		self.frame2.pack()
		

PrincipalGUI(root)
root.mainloop()
