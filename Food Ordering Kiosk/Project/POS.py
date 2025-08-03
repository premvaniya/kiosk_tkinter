from tkinter import *
import tkinter as tk
from tkinter impor

class POS:
    
    def __init__(self, root):
        self.root = root
        self.root.title("Point of Sale")
        self.root.geometry("1500x700+0+0")
        self.root.configure(background="cadetblue")

        # ===============Define StringVars===================
        self.change_input = StringVar()
        self.cash_input = StringVar()
        self.tax_input = StringVar()
        self.subtotal_input = StringVar()
        self.total_input = StringVar()
        self.item = StringVar()
        self.qty = StringVar()
        self.amount = StringVar()
        self.choice = StringVar()
        #=========================image paths=======================================================================
        self.coke = PhotoImage(file=r"images\coke.png")
        self.coke2 = PhotoImage(file=r"images\coke2.png")
        self.coke3 = PhotoImage(file=r"images\coke3.png")
        self.coke4 = PhotoImage(file=r"images\coke4.png")
        self.coke5 = PhotoImage(file=r"images\coke5.png")
        self.coke6 = PhotoImage(file=r"images\coke6.png")

        self.cafe1 = PhotoImage(file=r"images\cafe1.png")
        self.cafe2 = PhotoImage(file=r"images\cafe2.png")
        self.cafe3 = PhotoImage(file=r"images\cafe3.png")
        self.cafe4 = PhotoImage(file=r"images\cafe4.png")
        self.cafe5 = PhotoImage(file=r"images\cafe5.png")
        self.cafe6 = PhotoImage(file=r"images\cafe6.png")

        self.cond1 = PhotoImage(file=r"images\cond1.png")
        self.cond2 = PhotoImage(file=r"images\cond2.png")
        self.cond3 = PhotoImage(file=r"images\cond3.png")
        self.cond4 = PhotoImage(file=r"images\cond4.png")
       

        self.burger1 = PhotoImage(file=r"images\burger1.png")
        self.burger2 = PhotoImage(file=r"images\burger2.png")
        self.burger3 = PhotoImage(file=r"images\burger3.png")
        self.burger4 = PhotoImage(file=r"images\burger4.png")
        self.burger5 = PhotoImage(file=r"images\burger5.png")
        self.burger6 = PhotoImage(file=r"images\burger6.png")
        self.burger7 = PhotoImage(file=r"images\burger7.png")
        self.burger8 = PhotoImage(file=r"images\burger8.png")
        self.burger9 = PhotoImage(file=r"images\burger9.png")
        self.burger10= PhotoImage(file=r"images\burger10.png")
        self.burger11= PhotoImage(file=r"images\burger11.png")
        self.burger12= PhotoImage(file=r"images\burger12.png")
        self.burger13= PhotoImage(file=r"images\burger13.png")
        self.burger14= PhotoImage(file=r"images\burger14.png")
        self.burger15= PhotoImage(file=r"images\burger15.png")
        self.burger16= PhotoImage(file=r"images\burger16.png")
        self.burger17= PhotoImage(file=r"images\burger17.png")
        self.burger18= PhotoImage(file=r"images\burger18.png")
        #====================================FUNCTIONS=====================================================

        def delete():
            ItemCost = 0
            Tax = 2.5
            for child in self.POS_records.get_children():
                try:
                    item_cost = float(self.POS_records.item(child, "values")[2])
                    ItemCost += item_cost
                except _tkinter.TclError:
                    continue  # Skip if the item is not found
            
            self.subtotal_input.set(str('₹%.2f' % (ItemCost)))
            self.tax_input.set(str('₹%.2f' % ((ItemCost * Tax) / 100)))
            self.total_input.set(str('₹%.2f' % (ItemCost + (ItemCost * Tax) / 100)))
            
            selected_item = self.POS_records.selection()  # Corrected line
            if selected_item:  # Check if there is a selected item
                try:
                    item_values = self.POS_records.item(selected_item[0], "values")
                    item_cost = float(item_values[2])
                    
                    # Delete the selected item
                    self.POS_records.delete(selected_item[0])
                    
                    # Update ItemCost, subtotal, tax, and total after removing the selected item
                    ItemCost -= item_cost
                    ItemCost = max(ItemCost, 0)  # Ensure ItemCost doesn't go negative
                    self.subtotal_input.set(str('₹%.2f' % (ItemCost)))
                    self.tax_input.set(str('₹%.2f' % ((ItemCost * Tax) / 100)))
                    self.total_input.set(str('₹%.2f' % (ItemCost + (ItemCost * Tax) / 100)))
                except :
                    print("sorry! start over again.")


        def giveChange():
                ItemCost = 0
                Tax = 2.5
                cash_input = float(self.cash_input.get())  # Correctly retrieve the cash input
                
                for child in self.POS_records.get_children():
                    ItemCost += float(self.POS_records.item(child, "values")[2])
                
                total_cost = ItemCost + (ItemCost * Tax) / 100
                change = cash_input - total_cost
                
                self.change_input.set('₹%.2f' % change)
                
                if cash_input == 0:
                    self.change_input.set("")
                    paymeth()
                    
                
                self.subtotal_input.set('₹%.2f' % ItemCost)
                self.tax_input.set('₹%.2f' % ((ItemCost * Tax) / 100))
                self.total_input.set('₹%.2f' % total_cost)


        def exit():
                self.root.destroy()  # Assuming 'root' is your main Tkinter window

        def reset():
                # Clear all entries in the Treeview
                for child in self.POS_records.get_children():
                     self.POS_records.delete(child)
    
# Reset all input fields
                self.subtotal_input.set("")
                self.tax_input.set("")
                self.total_input.set("")
                self.cash_input.set("")
                self.change_input.set("")


        def paymeth():
            if(Choice.get() == "cash"):
                self.txt_cost.focus()
            elif(Choice.get()==""):
                cash_input.set("0")
                change_input.set("")


                
 #============================================ Main Frame=========================================================
        main_frame = Frame(self.root, bg='cadetblue')
        main_frame.grid(padx=8, pady=5)

        # Button Frame
        button_frame = Frame(main_frame, bg='cadetblue', bd=5, width=1348, height=160, padx=2, pady=4, relief=RIDGE)
        button_frame.pack(side=BOTTOM)

        # Data Frame
        data_frame = Frame(main_frame, bg='cadetblue', bd=5, width=800, height=300, padx=4, pady=4, relief=RIDGE)
        data_frame.pack(side=LEFT)

        # Data Frame Left Cover
        data_frame_left_cover = LabelFrame(data_frame, bg='cadetblue', font=('arial', 12, 'bold'), text="Point Of Sale", bd=5, width=800, height=300, padx=4, pady=4, relief=RIDGE)
        data_frame_left_cover.pack(side=LEFT)

        # Change Button Frame
        change_button_frame = Frame(data_frame_left_cover, bd=5, width=300, height=460, pady=4, relief=RIDGE)
        change_button_frame.pack(side=LEFT, padx=4)

        # Receipt Frame
        receipt_frame = Frame(data_frame_left_cover, bd=5, width=200, height=400, padx=1, pady=5, relief=RIDGE)
        receipt_frame.pack(side=RIGHT, padx=4)

        # Food Item Frame
        food_item_frame = LabelFrame(data_frame, bg='cadetblue', font=('arial', 12, 'bold'), text="ITEMS", bd=5, width=450, height=500, padx=5, pady=2, relief=RIDGE)
        food_item_frame.pack(side=RIGHT)

        # Calculation Frame
        cal_frame = Frame(button_frame, bd=5, width=432, height=140, relief=RIDGE)
        cal_frame.grid(row=0, column=0, padx=5)

        # Change Frame
        change_frame = Frame(button_frame, bd=5, width=400, height=140, pady=2, relief=RIDGE)
        change_frame.grid(row=0, column=1, padx=5)

        # Remove Frame
        remove_frame = Frame(button_frame, bd=5, width=400, height=140, pady=4, relief=RIDGE)
        remove_frame.grid(row=0, column=2, padx=5)

        # Entry & Label Widgets in Calculation Frame================================================================
        self.lbl_subtotal = Label(cal_frame, font=('arial', 14, 'bold'), text="Sub Total", bd=5)
        self.lbl_subtotal.grid(row=0, column=0, sticky=W, padx=5)
        self.txt_subtotal = Entry(cal_frame, font=('arial', 14, 'bold'), textvariable=self.subtotal_input, bd=2, width=24)
        self.txt_subtotal.grid(row=0, column=1, sticky=W, padx=5)

        self.lbl_tax = Label(cal_frame, font=('arial', 14, 'bold'), text="Tax", bd=5)
        self.lbl_tax.grid(row=1, column=0, sticky=W, padx=5)
        self.txt_tax = Entry(cal_frame, font=('arial', 14, 'bold'), textvariable=self.tax_input, bd=2, width=24)
        self.txt_tax.grid(row=1, column=1, sticky=W, padx=5)

        self.lbl_total = Label(cal_frame, font=('arial', 14, 'bold'), text="Total", bd=5)
        self.lbl_total.grid(row=2, column=0, sticky=W, padx=5)
        self.txt_total = Entry(cal_frame, font=('arial', 14, 'bold'), textvariable=self.total_input, bd=2, width=24)
        self.txt_total.grid(row=2, column=1, sticky=W, padx=5)

        # Entry & Label Widgets in Change Frame======================================================================
        self.lbl_mop = Label(change_frame, font=('arial', 14, 'bold'), text="Method Of Payment", bd=5)
        self.lbl_mop.grid(row=0, column=0, sticky=W, padx=5)
        self.cbo_mop = ttk.Combobox(change_frame, font=('arial', 14, 'bold'), width=36, state='readonly', textvariable=self.choice, justify=RIGHT)
        self.cbo_mop['values'] = ('', 'Cash', 'Visa Card', 'Master Card')
        self.cbo_mop.current(0)
        self.cbo_mop.grid(row=0, column=1)

        self.lbl_cost = Label(change_frame, font=('arial', 14, 'bold'), text="Cash", bd=5)
        self.lbl_cost.grid(row=1, column=0, sticky=W, padx=5)
        self.txt_cost = Entry(change_frame, font=('arial', 14, 'bold'), textvariable=self.cash_input, bd=2, width=38)
        self.txt_cost.grid(row=1, column=1, sticky=W, padx=5)

        self.lbl_change = Label(change_frame, font=('arial', 14, 'bold'), text="Change", bd=5)
        self.lbl_change.grid(row=2, column=0, sticky=W, padx=5)
        self.txt_change = Entry(change_frame, font=('arial', 14, 'bold'), textvariable=self.change_input, bd=2, width=38)
        self.txt_change.grid(row=2, column=1, sticky=W, padx=5)

        # Buttons in Remove Frame============================================================
        self.btnPay = Button(remove_frame, padx=2, font=('arial', 15, 'bold'), text='Pay', bd=2, width=10, height=1,command=giveChange)
        self.btnPay.grid(row=0, column=0, pady=2, padx=4)
        
        self.btnExit = Button(remove_frame, padx=2, font=('arial', 15, 'bold'), text='Exit', bd=2, width=10, height=1,command=exit)
        self.btnExit.grid(row=0, column=1, pady=2, padx=4)

        self.btnReset = Button(remove_frame, padx=2, font=('arial', 15, 'bold'), text='Reset', bd=2, width=10, height=1,command = reset)
        self.btnReset.grid(row=1, column=0, pady=2, padx=4)
        
        self.btnRemoveItem = Button(remove_frame,  padx=2, font=('arial',15,'bold'), text='Remove Item',bd=2, width=10, height=1,command=delete)
        self.btnRemoveItem.grid(row=1, column=1, pady=2, padx=4)
#==================================image click Function=================================================

        def coke1():
            ItemCost = 20
            Tax = 2
            self.POS_records.insert("", tk.END, values=("coka cola", "1", "20"))
            for child in self.POS_records.get_children():
                    ItemCost += float(self.POS_records.item(child,"values")[2])
                    self.subtotal_input.set(str('₹%.2f'%(ItemCost - 20)))
                    self.tax_input.set((str('₹%.2f'%(((ItemCost - 20)*Tax)/100))))
                    self.total_input.set((str('₹%.2f'%((ItemCost - 20)+((ItemCost-20)*Tax)/100))))

        
        def coke2():
            ItemCost = 40
            Tax = 4
            self.POS_records.insert("", tk.END, values=("Mango Maza", "1", "40"))
            for child in self.POS_records.get_children():
                    ItemCost += float(self.POS_records.item(child,"values")[2])
                    self.subtotal_input.set(str('₹%.2f'%(ItemCost - 40)))
                    self.tax_input.set(str('₹%.2f'%(((ItemCost - 40)*Tax)/100)))
                    self.total_input.set(str('₹%.2f'%((ItemCost - 40)+((ItemCost-40)*Tax)/100)))

        
        def coke3():
            ItemCost = 40
            Tax = 4
            self.POS_records.insert("", tk.END, values=("Orange Maza", "1", "40"))
            for child in self.POS_records.get_children():
                    ItemCost += float(self.POS_records.item(child,"values")[2])
                    self.subtotal_input.set(str('₹%.2f'%(ItemCost - 40)))
                    self.tax_input.set(str('₹%.2f'%(((ItemCost - 40)*Tax)/100)))
                    self.total_input.set(str('₹%.2f'%((ItemCost - 40)+((ItemCost-40)*Tax)/100)))

        
        
        def coke4():
            ItemCost = 35
            Tax = 3.5
            self.POS_records.insert("", tk.END, values=("Mountain Dew", "1", "35"))
            for child in self.POS_records.get_children():
                    ItemCost += float(self.POS_records.item(child,"values")[2])
                    self.subtotal_input.set(str('₹%.2f'%(ItemCost - 35)))
                    self.tax_input.set(str('₹%.2f'%(((ItemCost - 35)*Tax)/100)))
                    self.total_input.set(str('₹%.2f'%((ItemCost - 35)+((ItemCost-35)*Tax)/100)))


        
        def coke5():
            ItemCost = 30
            Tax = 3
            self.POS_records.insert("", tk.END, values=("Kiwi drink", "1", "30"))
            for child in self.POS_records.get_children():
                    ItemCost += float(self.POS_records.item(child,"values")[2])
                    self.subtotal_input.set(str('₹%.2f'%(ItemCost - 30)))
                    self.tax_input.set(str('₹%.2f'%(((ItemCost - 30)*Tax)/100)))
                    self.total_input.set(str('₹%.2f'%((ItemCost - 30)+((ItemCost-30)*Tax)/100)))


        
        def coke6():
            ItemCost = 20
            Tax = 2
            self.POS_records.insert("", tk.END, values=("Thumb's UP", "1", "20"))
            for child in self.POS_records.get_children():
                    ItemCost += float(self.POS_records.item(child,"values")[2])
                    self.subtotal_input.set(str('₹%.2f'%(ItemCost - 20)))
                    self.tax_input.set((str('₹%.2f'%(((ItemCost - 20)*Tax)/100))))
                    self.total_input.set((str('₹%.2f'%((ItemCost - 20)+((ItemCost-20)*Tax)/100))))

        def cond1():
            ItemCost = 4
            Tax = 1
            self.POS_records.insert("", tk.END, values=("Chilli Sauce", "1", "4"))
            for child in self.POS_records.get_children():
                    ItemCost += float(self.POS_records.item(child,"values")[2])
                    self.subtotal_input.set(str('₹%.2f'%(ItemCost - 4)))
                    self.tax_input.set((str('₹%.2f'%(((ItemCost - 4)*Tax)/100))))
                    self.total_input.set((str('₹%.2f'%((ItemCost - 4)+((ItemCost-4)*Tax)/100))))
                    
        def cond2():
            ItemCost = 4
            Tax = 1
            self.POS_records.insert("", tk.END, values=("saczhuwan sauce", "1", "4"))
            for child in self.POS_records.get_children():
                    ItemCost += float(self.POS_records.item(child,"values")[2])
                    self.subtotal_input.set(str('₹%.2f'%(ItemCost - 4)))
                    self.tax_input.set((str('₹%.2f'%(((ItemCost - 4)*Tax)/100))))
                    self.total_input.set((str('₹%.2f'%((ItemCost - 4)+((ItemCost-4)*Tax)/100))))

        def cond3():
            ItemCost = 10
            Tax = 2
            self.POS_records.insert("", tk.END, values=("vanila swirl", "1", "10"))
            for child in self.POS_records.get_children():
                    ItemCost += float(self.POS_records.item(child,"values")[2])
                    self.subtotal_input.set(str('₹%.2f'%(ItemCost - 10)))
                    self.tax_input.set((str('₹%.2f'%(((ItemCost - 10)*Tax)/100))))
                    self.total_input.set((str('₹%.2f'%((ItemCost - 10)+((ItemCost-10)*Tax)/100))))

        def cond4():
            ItemCost = 15
            Tax = 1.5
            self.POS_records.insert("", tk.END, values=("dark vanila swirl", "1", "15"))
            for child in self.POS_records.get_children():
                    ItemCost += float(self.POS_records.item(child,"values")[2])
                    self.subtotal_input.set(str('₹%.2f'%(ItemCost - 15)))
                    self.tax_input.set((str('₹%.2f'%(((ItemCost - 15)*Tax)/100))))
                    self.total_input.set((str('₹%.2f'%((ItemCost - 15)+((ItemCost-15)*Tax)/100))))

        def burger1():
            ItemCost = 300
            Tax = 24
            self.POS_records.insert("", tk.END, values=("INFERNO SPICY BURGER", "1", "300"))
            for child in self.POS_records.get_children():
                    ItemCost += float(self.POS_records.item(child,"values")[2])
                    self.subtotal_input.set(str('₹%.2f'%(ItemCost - 300)))
                    self.tax_input.set((str('₹%.2f'%(((ItemCost - 300)*Tax)/100))))
                    self.total_input.set((str('₹%.2f'%((ItemCost - 300)+((ItemCost-300)*Tax)/100))))
                    
        def burger2():
            ItemCost = 100
            Tax = 8
            self.POS_records.insert("", tk.END, values=("VAGGIE GIANT BURGER", "1", "100"))
            for child in self.POS_records.get_children():
                    ItemCost += float(self.POS_records.item(child,"values")[2])
                    self.subtotal_input.set(str('₹%.2f'%(ItemCost - 100)))
                    self.tax_input.set((str('₹%.2f'%(((ItemCost - 100)*Tax)/100))))
                    self.total_input.set((str('₹%.2f'%((ItemCost - 100)+((ItemCost- 100)*Tax)/100))))
                    
        def burger3():
            ItemCost = 180
            Tax = 15
            self.POS_records.insert("", tk.END, values=("CHEESY KABAB BURGER", "1", "180"))
            for child in self.POS_records.get_children():
                    ItemCost += float(self.POS_records.item(child,"values")[2])
                    self.subtotal_input.set(str('₹%.2f'%(ItemCost - 180)))
                    self.tax_input.set((str('₹%.2f'%(((ItemCost - 180)*Tax)/100))))
                    self.total_input.set((str('₹%.2f'%((ItemCost - 180)+((ItemCost-180)*Tax)/100))))
        def burger4():
            ItemCost = 150
            Tax = 12
            self.POS_records.insert("", tk.END, values=("EGG VAGGIE BURGER", "1", "150"))
            for child in self.POS_records.get_children():
                    ItemCost += float(self.POS_records.item(child,"values")[2])
                    self.subtotal_input.set(str('₹%.2f'%(ItemCost -150 )))
                    self.tax_input.set((str('₹%.2f'%(((ItemCost -150 )*Tax)/100))))
                    self.total_input.set((str('₹%.2f'%((ItemCost -150 )+((ItemCost-150)*Tax)/100))))
                    
        def burger5():
            ItemCost = 170
            Tax = 11
            self.POS_records.insert("", tk.END, values=("MAXICAN SPICY BURGER", "1", "170"))
            for child in self.POS_records.get_children():
                    ItemCost += float(self.POS_records.item(child,"values")[2])
                    self.subtotal_input.set(str('₹%.2f'%(ItemCost - 170)))
                    self.tax_input.set((str('₹%.2f'%(((ItemCost - 170)*Tax)/100))))
                    self.total_input.set((str('₹%.2f'%((ItemCost - 170)+((ItemCost-170)*Tax)/100))))
                    
        def burger6():
            ItemCost = 250
            Tax = 20
            self.POS_records.insert("", tk.END, values=("WHOPPER BURGER", "1", "250"))
            for child in self.POS_records.get_children():
                    ItemCost += float(self.POS_records.item(child,"values")[2])
                    self.subtotal_input.set(str('₹%.2f'%(ItemCost - 250)))
                    self.tax_input.set((str('₹%.2f'%(((ItemCost - 250)*Tax)/100))))
                    self.total_input.set((str('₹%.2f'%((ItemCost - 250)+((ItemCost-250)*Tax)/100))))

        def burger7():
            ItemCost = 480
            Tax = 18
            self.POS_records.insert("", tk.END, values=("WHOPPER FAMILY", "2", "480"))
            for child in self.POS_records.get_children():
                    ItemCost += float(self.POS_records.item(child,"values")[2])
                    self.subtotal_input.set(str('₹%.2f'%(ItemCost - 480)))
                    self.tax_input.set((str('₹%.2f'%(((ItemCost - 480)*Tax)/100))))
                    self.total_input.set((str('₹%.2f'%((ItemCost - 480)+((ItemCost-480)*Tax)/100))))
                    
        def burger8():
            ItemCost = 100
            Tax = 8
            self.POS_records.insert("", tk.END, values=("PIZZA PUFF", "5", "100"))
            for child in self.POS_records.get_children():
                    ItemCost += float(self.POS_records.item(child,"values")[2])
                    self.subtotal_input.set(str('₹%.2f'%(ItemCost - 100)))
                    self.tax_input.set((str('₹%.2f'%(((ItemCost - 100)*Tax)/100))))
                    self.total_input.set((str('₹%.2f'%((ItemCost - 100)+((ItemCost-100)*Tax)/100))))
                    
        def burger9():
            ItemCost = 70
            Tax = 5.6
            self.POS_records.insert("", tk.END, values=("FRENCH FRIES", "1", "70"))
            for child in self.POS_records.get_children():
                    ItemCost += float(self.POS_records.item(child,"values")[2])
                    self.subtotal_input.set(str('₹%.2f'%(ItemCost - 70)))
                    self.tax_input.set((str('₹%.2f'%(((ItemCost - 70)*Tax)/100))))
                    self.total_input.set((str('₹%.2f'%((ItemCost -70 )+((ItemCost-70)*Tax)/100))))

        def burger10():
            ItemCost = 80
            Tax = 6.4
            self.POS_records.insert("", tk.END, values=("VEG NUGGETS", "4", "80"))
            for child in self.POS_records.get_children():
                    ItemCost += float(self.POS_records.item(child,"values")[2])
                    self.subtotal_input.set(str('₹%.2f'%(ItemCost - 80 )))
                    self.tax_input.set((str('₹%.2f'%(((ItemCost -80 )*Tax)/100))))
                    self.total_input.set((str('₹%.2f'%((ItemCost - 80)+((ItemCost-80)*Tax)/100))))
                    
        def burger11():
            ItemCost = 100
            Tax = 8
            self.POS_records.insert("", tk.END, values=("PERI PERI FRIES", "1", "100"))
            for child in self.POS_records.get_children():
                    ItemCost += float(self.POS_records.item(child,"values")[2])
                    self.subtotal_input.set(str('₹%.2f'%(ItemCost -100 )))
                    self.tax_input.set((str('₹%.2f'%(((ItemCost - 100)*Tax)/100))))
                    self.total_input.set((str('₹%.2f'%((ItemCost - 100)+((ItemCost- 100)*Tax)/100))))
                    
        def burger12():
            ItemCost = 50
            Tax = 4
            self.POS_records.insert("", tk.END, values=("CAPPUCHINO", "1", "50"))
            for child in self.POS_records.get_children():
                    ItemCost += float(self.POS_records.item(child,"values")[2])
                    self.subtotal_input.set(str('₹%.2f'%(ItemCost - 50)))
                    self.tax_input.set((str('₹%.2f'%(((ItemCost - 50)*Tax)/100))))
                    self.total_input.set((str('₹%.2f'%((ItemCost - 50)+((ItemCost-50)*Tax)/100))))

        def burger13():
            ItemCost = 30
            Tax = 2.4
            self.POS_records.insert("", tk.END, values=("SMOOTHIE", "1", "30"))
            for child in self.POS_records.get_children():
                    ItemCost += float(self.POS_records.item(child,"values")[2])
                    self.subtotal_input.set(str('₹%.2f'%(ItemCost - 30)))
                    self.tax_input.set((str('₹%.2f'%(((ItemCost - 30)*Tax)/100))))
                    self.total_input.set((str('₹%.2f'%((ItemCost - 30)+((ItemCost-30)*Tax)/100))))
                    
        def burger14():
            ItemCost = 70
            Tax = 5.6
            self.POS_records.insert("", tk.END, values=("AMERICANO", "1", "70"))
            for child in self.POS_records.get_children():
                    ItemCost += float(self.POS_records.item(child,"values")[2])
                    self.subtotal_input.set(str('₹%.2f'%(ItemCost -70 )))
                    self.tax_input.set((str('₹%.2f'%(((ItemCost -70 )*Tax)/100))))
                    self.total_input.set((str('₹%.2f'%((ItemCost - 70)+((ItemCost-70)*Tax)/100))))
                    
        def burger15():
            ItemCost = 120
            Tax = 9.6
            self.POS_records.insert("", tk.END, values=("ICED COFFEE", "1", "120"))
            for child in self.POS_records.get_children():
                    ItemCost += float(self.POS_records.item(child,"values")[2])
                    self.subtotal_input.set(str('₹%.2f'%(ItemCost - 120)))
                    self.tax_input.set((str('₹%.2f'%(((ItemCost - 120)*Tax)/100))))
                    self.total_input.set((str('₹%.2f'%((ItemCost - 120)+((ItemCost-120)*Tax)/100))))

        def burger16():
            ItemCost = 50
            Tax = 4
            self.POS_records.insert("", tk.END, values=("MUDPIE CAKE", "1", "50"))
            for child in self.POS_records.get_children():
                    ItemCost += float(self.POS_records.item(child,"values")[2])
                    self.subtotal_input.set(str('₹%.2f'%(ItemCost -50 )))
                    self.tax_input.set((str('₹%.2f'%(((ItemCost - 50)*Tax)/100))))
                    self.total_input.set((str('₹%.2f'%((ItemCost - 50)+((ItemCost-50)*Tax)/100))))
                    
        def burger17():
            ItemCost = 50
            Tax = 4
            self.POS_records.insert("", tk.END, values=("HOT COFFIE", "1", "50"))
            for child in self.POS_records.get_children():
                    ItemCost += float(self.POS_records.item(child,"values")[2])
                    self.subtotal_input.set(str('₹%.2f'%(ItemCost - 50)))
                    self.tax_input.set((str('₹%.2f'%(((ItemCost - 50)*Tax)/100))))
                    self.total_input.set((str('₹%.2f'%((ItemCost - 50)+((ItemCost-50)*Tax)/100))))
                    
        def burger18():
            ItemCost = 40
            Tax = 3.2
            self.POS_records.insert("", tk.END, values=("SAMOSA", "2", "40"))
            for child in self.POS_records.get_children():
                    ItemCost += float(self.POS_records.item(child,"values")[2])
                    self.subtotal_input.set(str('₹%.2f'%(ItemCost -40 )))
                    self.tax_input.set((str('₹%.2f'%(((ItemCost - 40)*Tax)/100))))
                    self.total_input.set((str('₹%.2f'%((ItemCost -40 )+((ItemCost-40)*Tax)/100))))

        def burger19():
            ItemCost = 200
            Tax = 16
            self.POS_records.insert("", tk.END, values=("KIMCHI", "1", "200"))
            for child in self.POS_records.get_children():
                    ItemCost += float(self.POS_records.item(child,"values")[2])
                    self.subtotal_input.set(str('₹%.2f'%(ItemCost - 200)))
                    self.tax_input.set((str('₹%.2f'%(((ItemCost - 200)*Tax)/100))))
                    self.total_input.set((str('₹%.2f'%((ItemCost - 200)+((ItemCost-200)*Tax)/100))))
                    
        def burger20():
            ItemCost = 150
            Tax = 12
            self.POS_records.insert("", tk.END, values=("MAXICAN ROLLS", "5", "150"))
            for child in self.POS_records.get_children():
                    ItemCost += float(self.POS_records.item(child,"values")[2])
                    self.subtotal_input.set(str('₹%.2f'%(ItemCost - 150)))
                    self.tax_input.set((str('₹%.2f'%(((ItemCost -150 )*Tax)/100))))
                    self.total_input.set((str('₹%.2f'%((ItemCost - 150)+((ItemCost-150)*Tax)/100))))
                    
        def burger21():
            ItemCost = 140
            Tax = 11.2
            self.POS_records.insert("", tk.END, values=("NOODLES", "1", "140"))
            for child in self.POS_records.get_children():
                    ItemCost += float(self.POS_records.item(child,"values")[2])
                    self.subtotal_input.set(str('₹%.2f'%(ItemCost - 140)))
                    self.tax_input.set((str('₹%.2f'%(((ItemCost -140 )*Tax)/100))))
                    self.total_input.set((str('₹%.2f'%((ItemCost - 140)+((ItemCost-140)*Tax)/100))))


        def burger22():
            ItemCost = 150 
            Tax = 12
            self.POS_records.insert("", tk.END, values=("MANCHURIAN", "1", "150"))
            for child in self.POS_records.get_children():
                    ItemCost += float(self.POS_records.item(child,"values")[2])
                    self.subtotal_input.set(str('₹%.2f'%(ItemCost - 150)))
                    self.tax_input.set((str('₹%.2f'%(((ItemCost - 150)*Tax)/100))))
                    self.total_input.set((str('₹%.2f'%((ItemCost - 150)+((ItemCost-150)*Tax)/100))))
                    
        def burger23():
            ItemCost = 150
            Tax = 12
            self.POS_records.insert("", tk.END, values=("TACOS", "3", "150"))
            for child in self.POS_records.get_children():
                    ItemCost += float(self.POS_records.item(child,"values")[2])
                    self.subtotal_input.set(str('₹%.2f'%(ItemCost - 150)))
                    self.tax_input.set((str('₹%.2f'%(((ItemCost - 150)*Tax)/100))))
                    self.total_input.set((str('₹%.2f'%((ItemCost - 150)+((ItemCost-150)*Tax)/100))))

        def burger24():
            ItemCost = 150
            Tax = 12
            self.POS_records.insert("", tk.END, values=("BIG MAC BURGER", "1", "150"))
            for child in self.POS_records.get_children():
                    ItemCost += float(self.POS_records.item(child,"values")[2])
                    self.subtotal_input.set(str('₹%.2f'%(ItemCost - 150)))
                    self.tax_input.set((str('₹%.2f'%(((ItemCost - 150)*Tax)/100))))
                    self.total_input.set((str('₹%.2f'%((ItemCost - 150)+((ItemCost-150)*Tax)/100))))                    

                    
#=====================================TreeView  widget=======================================================================

        scroll_x1 = Scrollbar(receipt_frame, orient = HORIZONTAL)
        scroll_y1 = Scrollbar(receipt_frame, orient =VERTICAL)

        self.POS_records=ttk.Treeview(receipt_frame, height=20, columns=("Item", "Qty", "Amount"), xscrollcommand=scroll_x1.set, yscrollcommand=scroll_y1.set)

        scroll_x1.pack(side=BOTTOM, fill=X)
        scroll_y1.pack(side=RIGHT,fill=Y)

        scroll_x1.config(command=self.POS_records.xview)
        scroll_y1.config(command=self.POS_records.yview)


        self.POS_records.heading("Item", text="Item")
        self.POS_records.heading("Qty", text="Qty")
        self.POS_records.heading("Amount", text="Amount")

        self.POS_records['show'] = 'headings'

        self.POS_records.column("Item",width=120)
        self.POS_records.column("Qty", width=100)
        self.POS_records.column("Amount", width=100)

        self.POS_records.pack(fill=BOTH, expand=1)
        self.POS_records.bind("<ButtonRelease-1>")
      

  
#==================================================images========================================
        self.btncoke = Button(change_button_frame, padx=2, image=self.coke, width=104, height=104, bd=2, command=coke1)
        self.btncoke.grid(row=0, column=0, pady=2, padx=4)

        self.btncoke2 = Button(change_button_frame, padx=2, image=self.coke2, width=104, height=104, bd=2, command=coke2)
        self.btncoke2.grid(row=0, column=1, pady=2, padx=4)

        self.btncoke3 = Button(change_button_frame, padx=2, image=self.coke3, width=104, height=104, bd=2, command=coke3)
        self.btncoke3.grid(row=1, column=0, pady=2, padx=4)

        self.btncoke4 = Button(change_button_frame, padx=2, image=self.coke4, width=104, height=104, bd=2, command=coke4)
        self.btncoke4.grid(row=1, column=1, pady=2, padx=4)

        self.btncoke5 = Button(change_button_frame, padx=2, image=self.coke5, width=104, height=104, bd=2, command=coke5)
        self.btncoke5.grid(row=2, column=0, pady=2, padx=4)

        self.btncoke6 = Button(change_button_frame, padx=2, image=self.coke6, width=104, height=104, bd=2,command=coke6)
        self.btncoke6.grid(row=2, column=1, pady=2, padx=4)
#================================food item frame images===============================================
        self.btnitem1 = Button(food_item_frame, padx=2, image=self.burger1, width=104, height=104, bd=2,command=burger1)
        self.btnitem1.grid(row=0, column=0, pady=2, padx=4)

        self.btnitem2 = Button(food_item_frame, padx=2, image=self.burger2, width=104, height=104, bd=2,command=burger2)
        self.btnitem2.grid(row=0, column=1, pady=2, padx=4)

        self.btnitem3 = Button(food_item_frame, padx=2, image=self.burger3, width=104, height=104, bd=2,command=burger3)
        self.btnitem3.grid(row=0, column=2, pady=2, padx=4)

        self.btnitem4 = Button(food_item_frame, padx=2, image=self.burger4, width=104, height=104, bd=2,command=burger4)
        self.btnitem4.grid(row=0, column=3, pady=2, padx=4)

        self.btnitem5 = Button(food_item_frame, padx=2, image=self.burger5, width=104, height=104, bd=2,command=burger24)
        self.btnitem5.grid(row=0, column=4, pady=2, padx=4)

        self.btnitem6 = Button(food_item_frame, padx=2, image=self.burger6, width=104, height=104, bd=2,command=burger5)
        self.btnitem6.grid(row=0, column=5, pady=2, padx=4)

        self.btnitem7 = Button(food_item_frame, padx=2, image=self.burger7, width=104, height=104, bd=2,command=burger6)
        self.btnitem7.grid(row=1, column=0, pady=2, padx=4)

        self.btnitem8 = Button(food_item_frame, padx=2, image=self.burger8, width=104, height=104, bd=2,command=burger7)
        self.btnitem8.grid(row=1, column=1, pady=2, padx=4)

        self.btnitem9 = Button(food_item_frame, padx=2, image=self.burger9, width=104, height=104, bd=2,command=burger8)
        self.btnitem9.grid(row=1, column=2, pady=2, padx=4)

        self.btnitem10 = Button(food_item_frame, padx=2, image=self.burger10, width=104, height=104, bd=2,command=burger9)
        self.btnitem10.grid(row=1, column=3, pady=2, padx=4)

        self.btnitem11 = Button(food_item_frame, padx=2, image=self.burger11, width=104, height=104, bd=2,command=burger10)
        self.btnitem11.grid(row=1, column=4, pady=2, padx=4)

        self.btnitem12 = Button(food_item_frame, padx=2, image=self.burger12, width=104, height=104, bd=2,command=burger11)
        self.btnitem12.grid(row=1, column=5, pady=2, padx=4)      

        self.btnitem13 = Button(food_item_frame, padx=2, image=self.cafe1, width=104, height=104, bd=2,command=burger12)
        self.btnitem13.grid(row=2, column=0, pady=2, padx=4)

        self.btnitem14 = Button(food_item_frame, padx=2, image=self.cafe2, width=104, height=104, bd=2,command=burger13)
        self.btnitem14.grid(row=2, column=1, pady=2, padx=4)

        self.btnitem15 = Button(food_item_frame, padx=2, image=self.cafe3, width=104, height=104, bd=2,command=burger14)
        self.btnitem15.grid(row=2, column=2, pady=2, padx=4)

        self.btnitem16 = Button(food_item_frame, padx=2, image=self.cafe4, width=104, height=104, bd=2,command=burger15)
        self.btnitem16.grid(row=2, column=3, pady=2, padx=4)

        self.btnitem17 = Button(food_item_frame, padx=2, image=self.cafe5, width=104, height=104, bd=2,command=burger16)
        self.btnitem17.grid(row=2, column=4, pady=2, padx=4)

        self.btnitem18 = Button(food_item_frame, padx=2, image=self.cafe6, width=104, height=104, bd=2,command=burger17)
        self.btnitem18.grid(row=2, column=5, pady=2, padx=4)

        self.btnitem19 = Button(food_item_frame, padx=2, image=self.burger13, width=104, height=104, bd=2,command=burger18)
        self.btnitem19.grid(row=3, column=0, pady=2, padx=4)

        self.btnitem20 = Button(food_item_frame, padx=2, image=self.burger14, width=104, height=104, bd=2,command=burger19)
        self.btnitem20.grid(row=3, column=1, pady=2, padx=4)

        self.btnitem21 = Button(food_item_frame, padx=2, image=self.burger15, width=104, height=104, bd=2,command=burger20)
        self.btnitem21.grid(row=3, column=2, pady=2, padx=4)

        self.btnitem22 = Button(food_item_frame, padx=2, image=self.burger16, width=104, height=104, bd=2,command=burger21)
        self.btnitem22.grid(row=3, column=3, pady=2, padx=4)

        self.btnitem23 = Button(food_item_frame, padx=2, image=self.burger17, width=104, height=104, bd=2,command=burger22)
        self.btnitem23.grid(row=3, column=4, pady=2, padx=4)

        self.btnitem24= Button(food_item_frame, padx=2, image=self.burger18, width=104, height=104, bd=2,command=burger23)
        self.btnitem24.grid(row=3, column=5, pady=2, padx=4)
#============================condiments=================================================
        self.btncond1 = Button(food_item_frame, padx=2, image=self.cond1, width=104, height=104, bd=2,command=cond1)
        self.btncond1.grid(row=0, column=6, pady=2, padx=4)

        self.btncond2 = Button(food_item_frame, padx=2, image=self.cond2, width=104, height=104, bd=2,command=cond2)
        self.btncond2.grid(row=1, column=6, pady=2, padx=4)

        self.btncond3 = Button(food_item_frame, padx=2, image=self.cond3, width=104, height=104, bd=2, command=cond3)
        self.btncond3.grid(row=2, column=6, pady=2, padx=4)

        self.btncond4= Button(food_item_frame, padx=2, image=self.cond4, width=104, height=104, bd=2,command=cond4)
        self.btncond4.grid(row=3, column=6, pady=2, padx=4) 
        
if __name__ == '__main__':
    root = Tk()
    application = POS(root)
    root.mainloop()






