import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import tkinter as tk
import time
import datetime
import timeit
import threading
import xlrd
import re

TITLE_FONT= ("Verdana", 18)

file_location=r"nutrition.xls"
workbook=xlrd.open_workbook(file_location)
sheet=workbook.sheet_by_index(0)
lista=[]
d={}
for i in range(1,sheet.nrows):
	lista.append(sheet.cell_value(i,0))
	l=[]
	l.append(sheet.cell_value(i,1))
	l.append(sheet.cell_value(i,3))
	l.append(sheet.cell_value(i,4)) 	
	d[sheet.cell_value(i,0)]=l

class Application(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.geometry("1000x700")
        #self.geometry("{0}x{1}+0+0".format(self.winfo_screenwidth(), self.winfo_screenheight()))

        container = tk.Frame(self)
        container.pack(fill="both", expand=True)
        container.rowconfigure(0, weight=1)
        container.columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, PageDiet, PageFitness, PageMental, PageOverall):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
            frame.configure(background="#1ecbe1")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()
        
class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        self.pack(fill="both", expand=True)
        self.rowconfigure(0, pad=5, weight=1)
        self.rowconfigure(1, pad=100)
        self.rowconfigure(2, pad=100)
        self.columnconfigure(0, pad=5, weight=1)
        self.columnconfigure(1, pad=5, weight=1)
        self.columnconfigure(2, pad=5, weight=1)

        tk.Label(self, text="LOGO").grid(row=0, column=1, padx=5)

        tk.Button(self, text="Fitness", width=20, height=2, command=lambda: controller.show_frame(PageFitness)).grid(row=1, column=0, padx=5)
        tk.Button(self, text="Diet", width=20, height=2, command=lambda: controller.show_frame(PageDiet)).grid(row=1, column=1, padx=5)
        tk.Button(self, text="Mental", width=20, height=2, command=lambda: controller.show_frame(PageMental)).grid(row=1, column=2, padx=5)

        tk.Button(self, text="Overall Health", width=40, height=2, font=("Verdana", 24), command=lambda: controller.show_frame(PageOverall)).grid(row=2, padx=5, columnspan=3)


class AutocompleteEntry(tk.Entry):
    def __init__(self, lista, *args, **kwargs):
        
        tk.Entry.__init__(self, *args, **kwargs)
        self.lista = lista        
        self.var = self["textvariable"]
        if self.var == '':
            self.var = self["textvariable"] = tk.StringVar()

        self.var.trace('w', self.changed)
        self.bind("<Right>", self.selection)
        self.bind("<Up>", self.up)
        self.bind("<Down>", self.down)
        
        self.lb_up = False

    def changed(self, name, index, mode):  

        if self.var.get() == '':
        	self.lb.destroy()
        	self.lb_up = False
        else:
            words = self.comparison()
            if words:            
                if not self.lb_up:
                    self.lb = tk.Listbox()
                    self.lb.bind("<Double-Button-1>", self.selection)
                    self.lb.bind("<Right>", self.selection)
                    self.lb.place(x=self.winfo_x(), y=self.winfo_y()+self.winfo_height())
                    self.lb_up = True
                
                self.lb.delete(0, tk.END)
                for w in words:
                    self.lb.insert(tk.END,w)
            else:
                if self.lb_up:
                    self.lb.destroy()
                    self.lb_up = False
        
    def selection(self, event):

        if self.lb_up:
            self.var.set(self.lb.get(tk.ACTIVE))
            self.lb.destroy()
            self.lb_up = False
            self.icursor(tk.END)

    def up(self, event):

        if self.lb_up:
            if self.lb.curselection() == ():
                index = '0'
            else:
                index = self.lb.curselection()[0]
            if index != '0':                
                self.lb.selection_clear(first=index)
                index = str(int(index)-1)                
                self.lb.selection_set(first=index)
                self.lb.activate(index) 

    def down(self, event):

        if self.lb_up:
            if self.lb.curselection() == ():
                index = '0'
            else:
                index = self.lb.curselection()[0]
            if index != tk.END:                        
                self.lb.selection_clear(first=index)
                index = str(int(index)+1)        
                self.lb.selection_set(first=index)
                self.lb.activate(index) 

    def comparison(self):
        pattern = re.compile('.*' + self.var.get() + '.*')
        return [w for w in self.lista if re.match(pattern, w)]

class PageDiet(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.rowconfigure(1, pad=5)
        self.rowconfigure(2, pad=5)
        self.rowconfigure(3, pad=5)
        self.columnconfigure(0, weight=1)

        fm1 = tk.Frame(self, bg="blue")
        fm1.columnconfigure(1, weight=1)
        icon1 = tk.PhotoImage(file="icon_hamburger.png")
        b1= tk.Button(fm1, text="Back", image=icon1, command=lambda: controller.show_frame(StartPage))
        b1.img= icon1
        b1.grid(row=0, column=0, sticky="w")
        tk.Label(fm1, text="Diet", font=TITLE_FONT, fg="white", bg="blue").grid(row=0, column=1)
        tk.Label(fm1, text="LOGO").grid(row=0, column=2)
        fm1.grid(row=0, sticky="ewsn")

        fm2 = tk.Frame(self, bg="white")
        fm2.columnconfigure(0, weight=1)
        fm2.columnconfigure(1, weight=1)
        fm2.columnconfigure(2, weight=1)
        rv = tk.IntVar()
        rv.set(1)
        self.rv= rv
        wrad1 = tk.Radiobutton(fm2, text='Easy', bg="white", value=1, variable=self.rv, command=self.show_graph)
        wrad2 = tk.Radiobutton(fm2, text='Medium', bg="white", value=2, variable=self.rv, command=self.show_graph)
        wrad3 = tk.Radiobutton(fm2, text='Hard', bg="white", value=3, variable=self.rv, command=self.show_graph)
        wrad1.grid(row=1, column=0, padx=5)
        wrad2.grid(row=1, column=1, padx=5)
        wrad3.grid(row=1, column=2, padx=5)
        fm2.grid(row=2, pady=20, padx=200, sticky="ewsn")
        
        fm3 = tk.Frame(self, bg="white")
        fm3.columnconfigure(0, weight=1)
        self.graphframe = fm3
        self.show_graph()
        fm3.grid(row=3, pady=20, padx=200, sticky="ewsn")
        
        f2 = tk.Frame(self, bg="white")
        tk.Label(f2, text = " How many servings did you eat today?",bg='#ff7580').grid(row = 0, column = 0)
        self.Servings = tk.Entry(f2)
        self.Servings.config(bg='#ff7580')
        self.Servings.grid(row = 1, column = 0,sticky='e,w')
        self.Servings.insert(0, "0")       
        tk.Button(f2, text = "Submit",command=lambda:self.serve(),bg='#a0010e').grid(row=3,column=0)
        self.f2 = f2
        f2.grid(row=1, pady=20, padx=200, sticky="ewsn")

        
    def serve(self):

        serve = int(self.Servings.get())
        temp=1
        tserv=serve

        servelist=[]
        while serve>0:
            serve=serve-1
            tk.Label(self.f2, text = "Food "+str(tserv-serve),bg='#ff7580').grid(row = 5+temp, column = 0)
            Serving = AutocompleteEntry(lista, self.f2)
            Serving.config(bg='#ff7580')
            Serving.grid(row = 6+temp, column = 0,sticky='e,w')
            Serving.insert(0, "")
            servelist.append(Serving)
            temp=temp+2
        tk.Button(self.f2, text = "Enter",command=lambda:self.calcal(servelist,temp),bg='#a0010e').grid(row=5+temp,column=0)	

    def calcal(self,servelist,temp):

        kcal=0
        prot=0
        fat=0

        for i in servelist: 
            kcal=kcal+int(d[i.get()][0])

        for i in servelist: 
            prot=prot+int(d[i.get()][1])
            
        for i in servelist: 
            fat=fat+int(d[i.get()][2])		

        tk.Label(self.f2, text = ("Kcal=",kcal)).grid(row = 6+temp, column = 0)
        tk.Label(self.f2, text = ("Protein=",prot,'g')).grid(row = 7+temp, column = 0)
        tk.Label(self.f2, text = ("Fats=",fat,'g')).grid(row = 8+temp, column = 0)


    def show_graph(self):
        x=np.array ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        v= np.array ([16,16.31925,17.6394,16.003,17.2861,17.3131,19.1259,18.9694,22.0003,22.81226])
        p= np.array ([16.23697,     17.31653,     17.22094,     17.68631,     17.73641 ,    18.6368,
            19.32125,     19.31756 ,    21.20247  ,   22.41444   ,  22.11718  ,   22.12453])
        if self.rv.get()==2 :
            v= np.array ([26,16.31925,27.6394,26.003,27.2861,27.3131,29.1259,18.9694,32.0003,22.81226])
            p= np.array ([16.23697,     17.31653,     17.22094,     17.68631,     17.73641 ,    18.6368,
                19.32125,     19.31756 ,    21.20247  ,   22.41444   ,  22.11718  ,   22.12453])
        elif self.rv.get()==3 :
            v= np.array ([6,16.31925,7.6394,6.003,7.2861,7.3131,9.1259,8.9694,2.0003,2.81226])
            p= np.array ([16.23697,     7.31653,     7.22094,     7.68631,     7.73641 ,    8.6368,
                9.32125,     9.31756 ,    11.20247  ,   2.41444   ,  2.11718  ,   2.12453])
        
        fig = Figure(figsize=(6,6))
        a = fig.add_subplot(111)
        a.scatter(v,x,color='red')
        a.plot(p, range(2 +max(x)),color='blue')
        a.invert_yaxis()

        a.set_title ("Estimation Grid", fontsize=16)
        a.set_ylabel("", fontsize=14)
        a.set_xlabel("X", fontsize=14)

        canvas = FigureCanvasTkAgg(fig, master=self.graphframe)
        canvas.get_tk_widget().grid(row=0, sticky="ewsn")
        canvas.draw()

class PageFitness(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        self.rowconfigure(1, pad=5)
        self.rowconfigure(2, pad=5)
        self.rowconfigure(3, pad=5)
        self.columnconfigure(0, weight=1)

        fm1 = tk.Frame(self, bg="blue")
        fm1.columnconfigure(1, weight=1)
        icon1 = tk.PhotoImage(file="icon_hamburger.png")
        b1= tk.Button(fm1, text="Back", image=icon1, command=lambda: controller.show_frame(StartPage))
        b1.img= icon1
        b1.grid(row=0, column=0, sticky="w")
        tk.Label(fm1, text="Fitness", font=TITLE_FONT, fg="white", bg="blue").grid(row=0, column=1)
        tk.Label(fm1, text="LOGO").grid(row=0, column=2)
        fm1.grid(row=0, sticky="ewsn")

        fm2 = tk.Frame(self, bg="white")
        fm2.columnconfigure(0, pad=5, weight=1)
        fm2.columnconfigure(1, pad=5, weight=1)
        fm2.columnconfigure(2, pad=5, weight=1)
        tk.Label(fm2, text="Workouts", justify=tk.CENTER, fg="white", bg="blue").grid(row=0, columnspan=3, sticky="ewsn")
        fvar = tk.IntVar()
        self.fvar = fvar
        wrad1 = tk.Radiobutton(fm2, text='Easy', bg="white", value=1, variable=self.fvar, command=self.showinfo)
        wrad2 = tk.Radiobutton(fm2, text='Medium', bg="white", value=2, variable=self.fvar, command=self.showinfo)
        wrad3 = tk.Radiobutton(fm2, text='Hard', bg="white", value=3, variable=self.fvar, command=self.showinfo)
        wrad1.grid(row=1, column=0, padx=5)
        wrad2.grid(row=1, column=1, padx=5)
        wrad3.grid(row=1, column=2, padx=5)
        fm2.grid(row=1, pady=20, padx=200, sticky="ewsn")

        fm3 = tk.Frame(self, bg="white")
        fm3.columnconfigure(0, pad=5, weight=1)
        fm3.columnconfigure(1, pad=5, weight=1)
        tk.Label(fm3, text="Graph", justify=tk.CENTER, fg="white", bg="blue").grid(row=0, columnspan=2, sticky="ewsn")
        grad1 = tk.Radiobutton(fm3, text='Daily', bg="white", value=1)
        grad2 = tk.Radiobutton(fm3, text='Weekly', bg="white", value=2)
        grad3 = tk.Radiobutton(fm3, text='Monthly', bg="white", value=3)
        grad1.grid(row=1, column=0, padx=5, sticky="w")
        grad2.grid(row=2, column=0, padx=5, sticky="w")
        grad3.grid(row=3, column=0, padx=5, sticky="w")
        photo1 = tk.PhotoImage(file="photo_sample.png")
        pl1= tk.Label(fm3, image=photo1)
        pl1.img= photo1
        pl1.grid(row=1, column=1, rowspan=3, sticky="ewsn")
        fm3.grid(row=2, pady=20, padx=200, sticky="ewsn")

        fm4 = tk.Frame(self, bg="white")
        fm4.columnconfigure(0, weight=1)
        tk.Label(fm4, text="News", justify=tk.CENTER, fg="white", bg="blue").grid(row=0, sticky="ewsn")
        tk.Label(fm4, text="Whether fresh, frozen or canned, the nutritional benefits of produce will be received no matter how you buy them – as long as you eat them! And if buying them frozen, means you’re more likely to eat those green beans, then go for it! What’s key is being able to have produce at your fingertips for any meal or snack without having to run to the supermarket every time you want a fruit or veggie.", bg="white", height=10).grid(row=1, rowspan=4, sticky="ewsn")
        fm4.grid(row=3, pady=20, padx=200, sticky="ewsn") 
    
    def showinfo(self):
        if self.fvar.get() == 1 :
            tk.messagebox.showinfo("Fitness", "10 pushups, 10 situps and 10 burpees ")
        elif self.fvar.get() == 2:
            tk.messagebox.showinfo("Fitness", "20 pushups, 20 situps and 20 burpees ")
        else:
            tk.messagebox.showinfo("Fitness", "30 pushups, 30 situps and 30 burpees ")


class PageMental(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.rowconfigure(1, pad=5)
        self.rowconfigure(2, pad=5)
        self.rowconfigure(3, pad=5)
        self.columnconfigure(0, weight=1, pad=30)

        fm1 = tk.Frame(self, bg="blue")
        fm1.columnconfigure(1, weight=1)
        icon1 = tk.PhotoImage(file="icon_hamburger.png")
        b1= tk.Button(fm1, text="Back", image=icon1, command=lambda: controller.show_frame(StartPage))
        b1.img= icon1
        b1.grid(row=0, column=0, sticky="w")
        tk.Label(fm1, text="Mental", font=TITLE_FONT, fg="white", bg="blue").grid(row=0, column=1)
        tk.Label(fm1, text="LOGO").grid(row=0, column=2)
        fm1.grid(row=0, sticky="ewsn")

        fm3 = tk.Frame(self, bg="white")
        fm3.columnconfigure(0, pad=5, weight=1)
        fm3.columnconfigure(1, pad=5, weight=1)
        tk.Label(fm3, text = "Timer", font=("Helvetica", 16)).grid(row=0,columnspan = 2)

        tvar = tk.StringVar()
        tvar.set("30 Seconds") # initial value
        toption = tk.OptionMenu(fm3, tvar, "30 Seconds", "1 Minute", "5 Minutes")
        toption.config(width=50)
        toption.grid(row=1,column = 0)
        self.tvar = tvar
        tbutton = tk.Button(fm3, text="Start", width= 10, command=self.countdown_timer)
        tbutton.grid(row=1,column = 1)

        tcvar = tk.StringVar()
        tcvar.set("0:00:00")
        self.tcvar = tcvar
        tclabel = tk.Label(fm3, text="0:00:00", font=("Helvetica", 32), height=2)
        tclabel.grid(row=2, columnspan = 2)
        self.tclabel = tclabel
        fm3.grid(row=1, sticky="ewsn")

        fm3 = tk.Frame(self, bg="white")
        fm3.columnconfigure(0, weight=1)
        tk.Label(fm3, text="News", justify=tk.CENTER, fg="white", bg="blue").grid(row=0, sticky="ewsn")
        tk.Label(fm3, text="1.Sit or lie comfortably. You may even want to invest in a meditation chair or cushion. \n 2. Close your eyes. We recommend using one of our Cooling Eye Masks or Restorative Eye Pillows if lying down.\n 3. Make no effort to control the breath; simply breathe naturally.\n 4. Focus your attention on the breath and on how the body moves with each inhalation and exhalation. Notice the movement of your body as you breathe. Observe your chest, shoulders, rib cage, and belly. Simply focus your attention on your breath without controlling its pace or intensity. If your mind wanders, return your focus back to your breath.", bg="white", height=10).grid(row=1, rowspan=4, sticky="ewsn")
        fm4.grid(row=3, pady=20, padx=200, sticky="ewsn")


    def countdown_timer(self):
        threading.Thread(target=self.update_label).start()

    def update_label(self):
        x = 30
        if self.tvar.get() == "1 Minute" :
            x = 60
        elif self.tvar.get() == "5 Minutes":
            x = 300
        while x >= 0 :
            x -= 1
            self.tcvar = str(datetime.timedelta(seconds=x))
            self.tclabel.config(text=self.tcvar)
            time.sleep(1)

class PageOverall(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.rowconfigure(1, pad=5)
        self.rowconfigure(2, pad=5)
        self.rowconfigure(3, pad=5)
        self.columnconfigure(0, weight=1)

        fm1 = tk.Frame(self, bg="blue")
        fm1.columnconfigure(1, weight=1)
        icon1 = tk.PhotoImage(file="icon_hamburger.png")
        b1= tk.Button(fm1, text="Back", image=icon1, command=lambda: controller.show_frame(StartPage))
        b1.img= icon1
        b1.grid(row=0, column=0, sticky="w")
        tk.Label(fm1, text="Overall", font=TITLE_FONT, fg="white", bg="blue").grid(row=0, column=1)
        tk.Label(fm1, text="LOGO").grid(row=0, column=2)
        fm1.grid(row=0, sticky="ewsn")

        f3 = tk.Frame(self, bg="#2ff8ff")
        tk.Label(f3, text = "BMI Calculator",bg='#f73848',font=("Helvetica", 16)).grid(row=0,columnspan = 6)

        tk.Label(f3, text = "Height (ft)",bg="#2ff8ff").grid(row = 1, column = 0)
        txtHeightFt = tk.Entry(f3)
        txtHeightFt.grid(row = 1, column = 1)
        txtHeightFt.insert(0, "0")
        self.txtHeightFt=txtHeightFt

        tk.Label(f3, text = "  Height (in)",bg="#2ff8ff").grid(row = 1, column = 3)
        txtHeightIn = tk.Entry(f3)
        txtHeightIn.grid(row = 1, column = 4)
        txtHeightIn.insert(0, "0")
        self.txtHeightIn=txtHeightIn

        tk.Label(f3, text = "Weight (lbs)",bg="#2ff8ff").grid(row = 2, column = 0)
        txtWeight = tk.Entry(f3)
        txtWeight.grid(row = 2, column = 1)
        txtWeight.insert(0, "0")
        self.txtWeight=txtWeight

        tk.Label(f3, text = "Your BMI:",bg="#2ff8ff").grid(row = 5, column = 0)
        f3.lblBMI = tk.Label(f3, bg = "#2ff8ff",relief = "groove")
        f3.lblBMI.grid(row = 5, column = 1, sticky = "we")
        tk.Label(f3, text = "You are:",bg="#2ff8ff").grid(row = 5, column = 3)
        f3.lblBMIStatus = tk.Label(f3)
        f3.lblBMIStatus.grid(row = 5, column = 4)

        tk.Label(f3, text = "____________________________________________________________________________________",bg='#f73848').grid(row = 11, columnspan = 10)
        tk.Label(f3, text = " Suggestions:",bg="#2ff8ff").grid(row = 12, column = 0, sticky='w')
        tk.Label(f3, text = " Weight:",bg="#2ff8ff").grid(row = 13, columnspan = 1,sticky='w')
        tk.Label(f3, text = " Calorie intake: ",bg="#2ff8ff").grid(row = 14, columnspan = 1,sticky='w')
        tk.Label(f3, text = " Protein intake: ",bg='#2ff8ff').grid(row = 15, columnspan = 1,sticky='w')
        f3.SWeight=tk.Label(f3)
        f3.SWeight.grid(row = 13,column=1, columnspan = 3,sticky='w')
        f3.SCalorie=tk.Label(f3)
        f3.SCalorie.grid(row = 14,column=1, columnspan = 3,sticky='w')
        f3.SProtein=tk.Label(f3)
        f3.SProtein.grid(row = 15,column=1, columnspan = 3,sticky='w')

        f3.btnCalc = tk.Button(f3, text = "Calculate BMI",bg='#ffffff',command=lambda:self.calcBMI())
        f3.btnCalc.grid(row = 10, columnspan = 5)
        f3.grid(row=1, sticky="ewsn")
        self.f3 =f3

    def calcBMI(self):
        #calculate BMI
        feet = int(self.txtHeightFt.get())
        inches = int(self.txtHeightIn.get())
        totalHeight = (12 * feet) + inches
        weight = float(self.txtWeight.get())
        #BMI needs to be a float, int * float is float
        bmi = weight * 703 / (totalHeight * totalHeight)
        f3= self.f3
        f3.lblBMI["text"] = "%.2f" % bmi


        #label for BMI status
        if bmi < 18.5:
            f3.lblBMIStatus["text"] = "Underweight"
            f3.SWeight["text"] = "Gain: 2 kg"
            f3.SCalorie["text"] = "3000 Calorie if MALE, 2500 if FEMALE"
            f3.SProtein["text"] = weight*0.48
        elif bmi < 24.9:
            f3.lblBMIStatus["text"] = "Normal"
            f3.SWeight["text"] = "Maintain"
            f3.SCalorie["text"] = "2500 Calorie if MALE, 2000 if FEMALE"
            f3.SProtein["text"] = weight*0.38
        elif bmi < 29.9:
            f3.lblBMIStatus["text"] = "Overweight"
            f3.SWeight["text"] = "Lose: 2 kg"
            f3.SCalorie["text"] = "2000 Calorie if MALE, 1500 if FEMALE"
            f3.SProtein["text"] = weight*0.48
        else:
            f3.lblBMIStatus["text"] = "Obese"
            f3.SWeight["text"] = "Lose: 4 kg"
            f3.SCalorie["text"] = "1600 Calorie if MALE, 1200 if FEMALE"
            f3.SProtein["text"] = weight*0.48
        #f3.btnCalc["command"] = f3.calcBMI


app = Application()
app.mainloop()
