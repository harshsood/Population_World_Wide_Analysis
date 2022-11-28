from tkinter import *
import tkinter.ttk as ttk
import csv

class view_dataset(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)

        width = 1300
        height = 700
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width/2) - (width/2)
        y = (screen_height/2) - (height/2)
        self.geometry("%dx%d+%d+%d" % (width, height, x, y))
        self.configure(bg='#f07167')
        self.resizable(False, False)

        TableMargin = Frame(self, width=700)
        TableMargin.pack(side=TOP)
        scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
        scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
        tree = ttk.Treeview(TableMargin, columns=("Code", "Country", "Population", "Density"), height=400, selectmode="extended", yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
        scrollbary.config(command=tree.yview)
        scrollbary.pack(side=RIGHT, fill=Y)
        scrollbarx.config(command=tree.xview)
        scrollbarx.pack(side=BOTTOM, fill=X)
        tree.heading('Code', text="Code", anchor=W)
        tree.heading('Country', text="Country", anchor=W)
        tree.heading('Population', text="Population", anchor=W)
        tree.heading('Density', text="Density(per sq km)", anchor=W)
        tree.column('#0', stretch=NO, minwidth=0, width=0)
        tree.column('#1', stretch=NO, minwidth=0, width=200)
        tree.column('#2', stretch=NO, minwidth=0, width=200)
        tree.column('#3', stretch=NO, minwidth=0, width=300)
        tree.column('#4', stretch=NO, minwidth=0, width=300)
        tree.pack()

        with open('2022_population.csv') as f:
            reader = csv.DictReader(f, delimiter=',')
            for row in reader:
                code = row['iso_code']
                country = row['country']
                population = row['2022_last_updated']
                density = row['density_sq_km']
                tree.insert("", 0, values=(code, country, population, density))