import tkinter as tk           # Main GUI Module
import tkinter.messagebox      # Tkinter messagebox module
import time                    # For real time clock
from functions import *        # Importing all user-defined functions from functions.py file



#____________________Global Variables____________________#
InputDate = getTodaysDate()
InputTime = getCurrentTime()
Selection = ""
#____________________Global Variables____________________#



#____________________FONTS____________________#
LARGEFONT = ("Calibri", 25)
FONT = ("Calibri", 18)
SMALLFONT = ("Calibri", 13)
#____________________FONTS____________________#



class MiniProject(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        
        self.winfo_toplevel().title("NTU Canteen Menu System")
        
        # Setting the application to an unresizable 800x600 resolution window
        self.geometry("800x600") 
        self.resizable(False, False)

        # Dictionary of all frames in the application
        # Each frame is its own class
        self.frames = {}
        for F in (StartPage, ChooseAStore, StoreFrame, ViewOperatingHours, ChooseADate, ChooseAStore_UserDateAndTime,StoreFrame_UserDateAndTime):

            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    # Function to bind to button that raises frame to the top of the window
    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()
        
class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)



        #______________________________Background Image______________________________#
        photo = tk.PhotoImage(file="StartPage.png")
        label1 = tk.Label(self, image=photo)
        label1.image = photo
        label1.place(x=0,y=0)
        #______________________________Background Image______________________________#



        #______________________________Function for real time clock______________________________#
        def tick():
            time_string = time.strftime("%A, %d %B, %Y, %H:%M:%S")
            clock.config(text=time_string)
            clock.after(100, tick)
        clock = tk.Label(self, fg="white", bg="#303030", font=FONT)
        clock.place(anchor="n", x=400 ,y=0, width=800, height=40)
        tick()
        #______________________________Function for real time clock______________________________#



        Button1 = tk.Button(self, text="View Today's stores", fg="black", bg="#bababa", font=SMALLFONT, command=lambda: controller.show_frame(ChooseAStore))
        Button1.place(anchor="n", x=400 ,y=280, width=380, height=35)
        
        Button2 = tk.Button(self, text="View stores by other dates", fg="black", bg="#bababa", font=SMALLFONT, command=lambda: controller.show_frame(ChooseADate))
        Button2.place(anchor="n", x=400 ,y=315, width=380, height=35)

        Button3 = tk.Button(self, text="View stores' operating hours", fg="black", bg="#bababa", font=SMALLFONT, command=lambda: controller.show_frame(ViewOperatingHours))
        Button3.place(anchor="n", x=400 ,y=350, width=380, height=35)
        
        Button4 = tk.Button(self, text="Quit", fg="white", bg="red", font=FONT, command=lambda: exit())
        Button4.place(anchor="n", x=400, y=550, width=800, height=50)
        
class ChooseAStore(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)



        #______________________________Background Image______________________________#
        photo = tk.PhotoImage(file="ChooseAStore.png")
        label1 = tk.Label(self, image=photo)
        label1.image = photo
        label1.place(x=0,y=0)
        #______________________________Background Image______________________________#



        #______________________________Function for real time clock______________________________#
        def tick():
            time_string = time.strftime("%A, %d %B, %Y, %H:%M:%S")
            clock.config(text=time_string)
            clock.after(100, tick)
        clock = tk.Label(self, fg="white", bg="#303030", font=FONT)
        clock.place(anchor="n", x=400 ,y=0, width=800, height=40)
        tick()
        #______________________________Function for real time clock______________________________#



        #______________________________Change global variable "Selection" upon button presses______________________________#
        def b1():
            global Selection
            Selection = "McDonalds"
        def b2():
            global Selection
            Selection = "Malay Food"
        def b3():
            global Selection
            Selection = "Subway"
        def b4():
            global Selection
            Selection = "Chicken Rice"
        def b5():
            global Selection
            Selection = "Western Food"  
        #______________________________Change global variable "Selection" upon button presses______________________________#



        # Check stores availability using isRestaurantAvailable() and place the button for the stores if return is True
        # Stores are checked against getTodaysDate() and getCurrentTime()
        def CheckStores():  
            n = 200
            if isRestaurantAvailable("McDonalds",getTodaysDate(),getCurrentTime()):
                Button1 = tk.Button(self, text="Mcdonald's", fg="black", bg="#bababa", font=FONT, command=lambda:[b1(),controller.show_frame(StoreFrame)])
                Button1.place(anchor="n", x=400 ,y=n, width=400, height=40)
                n += 40
            
            if isRestaurantAvailable("Malay Food",getTodaysDate(),getCurrentTime()):
                Button2 = tk.Button(self, text="Malay Food", fg="black", bg="#bababa", font=FONT, command=lambda:[b2(),controller.show_frame(StoreFrame)])
                Button2.place(anchor="n", x=400 ,y=n, width=400, height=40)
                n += 40

            if isRestaurantAvailable("Subway",getTodaysDate(),getCurrentTime()):
                Button3 = tk.Button(self, text="Subway", fg="black", bg="#bababa", font=FONT, command=lambda:[b3(),controller.show_frame(StoreFrame)])
                Button3.place(anchor="n", x=400 ,y=n, width=400, height=40)
                n += 40
                
            if isRestaurantAvailable("Chicken Rice",getTodaysDate(),getCurrentTime()):
                Button4 = tk.Button(self, text="Chicken Rice", fg="black", bg="#bababa", font=FONT, command=lambda:[b4(),controller.show_frame(StoreFrame)])
                Button4.place(anchor="n", x=400 ,y=n, width=400, height=40)
                n += 40

            if isRestaurantAvailable("Western Food",getTodaysDate(),getCurrentTime()):
                Button5 = tk.Button(self, text="Western Food", fg="black", bg="#bababa", font=FONT, command=lambda:[b5(),controller.show_frame(StoreFrame)])
                Button5.place(anchor="n", x=400 ,y=n, width=400, height=40)

        
        # "Reset" by placing a white empty label over the buttons when "Back" button is pressed
        def ResetStores():
            emptylabel = tk.Label(self, bg="white")
            emptylabel.place(anchor="n", x=400 ,y=200, width=400, height=200)


        CheckStoresButton = tk.Button(self, text="Check Available Stores", fg = "black", bg = "#adffb1", font=FONT, command=lambda: CheckStores())
        CheckStoresButton.place(anchor="n", x=400, y=500, width=800, height=50)

        BackButton = tk.Button(self, text="Back", fg = "black", bg = "#96bfff", font=FONT, width=40, command=lambda: [ResetStores(), controller.show_frame(StartPage)])
        BackButton.place(anchor="n", x=400, y=550, width=800, height=50)

class StoreFrame(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)



        #______________________________Background Image______________________________#
        photo = tk.PhotoImage(file="StoreFrame.png")
        label1 = tk.Label(self, image=photo)
        label1.image = photo
        label1.place(x=0,y=0)
        #______________________________Background Image______________________________#



        #______________________________Function for real time clock______________________________#
        def tick():
            time_string = time.strftime("%A, %d %B, %Y, %H:%M:%S")
            clock.config(text=time_string)
            clock.after(100, tick)
        clock = tk.Label(self, fg="white", bg="#303030", font=FONT)
        clock.place(anchor="n", x=400 ,y=0, width=800, height=40)
        tick()
        #______________________________Function for real time clock______________________________#



        #______________________________Function for displaying selected store______________________________#
        def SelectionTick():
            global Selection
            label.config(text=Selection)
            label.after(100,SelectionTick)
        label = tk.Label(self, fg = "black", bg = "grey", font=LARGEFONT)
        label.place(anchor="n", x=400 ,y=40, width=800, height=50)
        SelectionTick()
        #______________________________Function for displaying selected store______________________________#


        # Function to display the operating hours of the currently selected store using popup tkinter.messagebox
        def OperatingHoursButton():
            global Selection
            tkinter.messagebox.showinfo("Operating Hours", getOperatingHours(Selection))


        # Function to generate a new tkinter window to calculate waiting time for the currently selected store
        def WaitingTimeButton():
            global Selection
            window = tk.Tk()

            window.winfo_toplevel().title("Waiting Time")
            tk.Label(window, text="Enter the number of people in the queue:").grid(row=0)

            tk.Button(window, text='Quit', command=window.destroy).grid(row=1, column=0)

            e1 = tk.Entry(window)
            e1.grid(row=0, column=1)

            def Calculate():
                try:
                    pax = int(e1.get())
                    if pax < 0:
                        tkinter.messagebox.showerror("Error","Please enter a positive integer value for the number of people in the queue!")
                    else:
                        tkinter.messagebox.showinfo("Waiting Time","Estimated waiting time is "+ str(calculateWaitingTime(Selection, pax))+" minutes.")
                except:
                    tkinter.messagebox.showerror("Error","Please enter an integer value for the number of people in the queue!")

            button = tk.Button(window, text="Calculate", command=Calculate)
            button.grid(row=1,column=1)

            window.mainloop()


        # Get a dictionary of menu item, prices using getMenu() based on getTodaysDate() and getCurrentTime()
        # Place the items using a for loop
        def ViewMenu():
            n = 210
            for item,price in getMenu(Selection, getTodaysDate(), getCurrentTime()).items():
                
                item1 = tk.Label(self, text=item, bg="white", font=FONT)
                item1.place(anchor="n", x=320 ,y=n, width=250, height=40)

                item2 = tk.Label(self, text=price, bg="white", font=FONT)
                item2.place(anchor="n", x=530 ,y=n, width=100, height=40)

                n += 40
        

        # "Reset" by placing a white empty label over the menu when "Back" button is pressed
        def ResetSelection():
            global Selection
            Selection = ""
            emptylabel = tk.Label(self, bg="white")
            emptylabel.place(anchor="n", x=400 ,y=210, width=400, height=200)


        button1 = tk.Button(self, text="Operating Hours", font=FONT, command = OperatingHoursButton)
        button1.place(anchor="n", x=200 ,y=90, width=400, height=40)

        button2 = tk.Button(self, text="Waiting Time", font=FONT, command = WaitingTimeButton)
        button2.place(anchor="n", x=600 ,y=90, width=400, height=40)

        ViewMenuButton = tk.Button(self, text="View Menu", fg = "black", bg = "#adffb1", font=FONT, command=ViewMenu)
        ViewMenuButton.place(anchor="n", x=400, y=500, width=800, height=50)

        BackButton = tk.Button(self, text="Back", fg = "black", bg = "#96bfff", font=FONT, width=40, command=lambda: [ResetSelection(),controller.show_frame(ChooseAStore)])
        BackButton.place(anchor="n", x=400, y=550, width=800, height=50)

class ViewOperatingHours(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        


        #______________________________Background Image______________________________#
        photo = tk.PhotoImage(file="ViewOperatingHours.png")
        label1 = tk.Label(self, image=photo)
        label1.image = photo
        label1.place(x=0,y=0)
        #______________________________Background Image______________________________#



        #______________________________Function for real time clock______________________________#
        def tick():
            time_string = time.strftime("%A, %d %B, %Y, %H:%M:%S")
            clock.config(text=time_string)
            clock.after(100, tick)
        clock = tk.Label(self, fg="white", bg="#303030", font=FONT)
        clock.place(anchor="n", x=400 ,y=0, width=800, height=40)
        tick()
        #______________________________Function for real time clock______________________________#


        
        BackButton = tk.Button(self, text="Back", fg = "black", bg = "#96bfff", font=FONT, width=40, command=lambda: controller.show_frame(StartPage))
        BackButton.place(anchor="n", x=400, y=550, width=800, height=50)

class ChooseADate(tk.Frame):
    
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        


        #______________________________Background Image______________________________#
        photo = tk.PhotoImage(file="ChooseADate.png")
        label1 = tk.Label(self, image=photo)
        label1.image = photo
        label1.place(x=0,y=0)
        #______________________________Background Image______________________________#



        #______________________________Function for real time clock______________________________#
        def tick(): 
            time_string = time.strftime("%A, %d %B, %Y, %H:%M:%S")
            clock.config(text=time_string)
            clock.after(100, tick)
        clock = tk.Label(self, fg="white", bg="#303030", font=FONT)
        clock.place(anchor="n", x=400 ,y=0, width=800, height=40)
        tick()
        #______________________________Function for real time clock______________________________#



        label1 = tk.Label(self, text="Choose A Date:", bg="white", font=LARGEFONT)
        label1.place(anchor="n", x=400 ,y=120, width=250, height=50)

        label2 = tk.Label(self, text="Choose A Time:", bg="white", font=LARGEFONT)
        label2.place(anchor="n", x=400 ,y=280, width=300, height=50)



        #______________________________DATE AND TIME SELECTION______________________________#
        variable_date = tk.StringVar(self)
        variable_date.set(time.strftime("%d"))
        ChooseDate = tk.OptionMenu(self, variable_date, "01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31")
        ChooseDate.config(font=FONT, bg="white")
        menu = self.nametowidget(ChooseDate.menuname)
        menu.config(font=FONT, bg="white")        

        slash1 = tk.Label(self, text="/", bg="white", font=FONT)   

        variable_month = tk.StringVar(self)
        variable_month.set(time.strftime("%m"))
        ChooseMonth = tk.OptionMenu(self, variable_month, "01","02","03","04","05","06","07","08","09","10","11","12")
        ChooseMonth.config(font=FONT, bg="white")
        menu = self.nametowidget(ChooseMonth.menuname)
        menu.config(font=FONT, bg="white")

        slash2 = tk.Label(self,text="/", bg="white", font=FONT)       
        
        variable_year = tk.StringVar(self)
        variable_year.set(time.strftime("%Y"))
        ChooseYear = tk.OptionMenu(self, variable_year, "2019","2020","2021","2022","2023","2024","2025","2026","2027","2028","2029","2030")
        ChooseYear.config(font=FONT, bg="white")
        menu = self.nametowidget(ChooseYear.menuname)
        menu.config(font=FONT, bg="white")

        variable_hour = tk.StringVar(self)
        variable_hour.set(time.strftime("%H"))
        ChooseHour = tk.OptionMenu(self, variable_hour, "00","01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23")
        ChooseHour.config(font=FONT, bg="white")
        menu = self.nametowidget(ChooseHour.menuname)
        menu.config(font=FONT, bg="white")

        colon1 = tk.Label(self,text=":", bg="white", font=FONT)
    
        variable_minute = tk.StringVar(self)
        variable_minute.set(time.strftime("%M"))
        ChooseMinute = tk.OptionMenu(self, variable_minute, "00","05","10","15","20","25","30","35","40","45","50","55")
        ChooseMinute.config(font=FONT, bg="white")
        menu = self.nametowidget(ChooseMinute.menuname)
        menu.config(font=FONT, bg="white")
        #______________________________DATE AND TIME SELECTION______________________________#



        #______________________________Placing the selection widgets______________________________#
        ChooseDate.place(anchor="n", x=280 ,y=180, width=100, height=50)
        slash1.place(anchor="n", x=340 ,y=180, width=20, height=50)
        ChooseMonth.place(anchor="n", x=400 ,y=180, width=100, height=50)
        slash2.place(anchor="n", x=460 ,y=180, width=20, height=50)
        ChooseYear.place(anchor="n", x=520 ,y=180, width=100, height=50)
        ChooseHour.place(anchor="n", x=350 ,y=340, width=80, height=50)
        colon1.place(anchor="n", x=400 ,y=340, width=20, height=50)
        ChooseMinute.place(anchor="n", x=450 ,y=340, width=80, height=50)
        #______________________________Placing the selection widgets______________________________#



        # We can use global keyword to change the assignment of global variables InputDate and InputTime
        def pressed():
            global InputDate
            global InputTime
            InputDate = variable_date.get() + "/" + variable_month.get() + "/" + variable_year.get()
            InputTime = variable_hour.get() + ":" + variable_minute.get()
        

        ConfirmButton = tk.Button(self, text="Next", bg = "#adffb1", font=FONT, command=lambda:[pressed(),controller.show_frame(ChooseAStore_UserDateAndTime)])
        ConfirmButton.place(anchor="n", x=400, y=500, width=800, height=50)

        BackButton = tk.Button(self, text="Back", fg = "black", bg = "#96bfff", font=FONT, width=40, command=lambda: controller.show_frame(StartPage))
        BackButton.place(anchor="n", x=400, y=550, width=800, height=50)

class ChooseAStore_UserDateAndTime(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)



        #______________________________Background Image______________________________#
        photo = tk.PhotoImage(file="ChooseAStore.png")
        label1 = tk.Label(self, image=photo)
        label1.image = photo
        label1.place(x=0,y=0)
        #______________________________Background Image______________________________#



        #______________________________Function of date input by user______________________________#
        def tick():
            DATE, MONTH, YEAR = (int(x) for x in InputDate.split('/')) 
            try: # Check for invalid date given
                time_string = datetime.date(YEAR, MONTH, DATE).strftime("%A, %d %B, %Y") + ", " + InputTime
            except: # Show "INPUT DATE IS INVALID" when invalid date is given
                time_string = "INPUT DATE IS INVALID"
            clock.config(text=time_string)
            clock.after(100, tick)
        clock = tk.Label(self, fg="white", bg="#303030", font=FONT)
        clock.place(anchor="n", x=400 ,y=0, width=800, height=40)
        tick()
        #______________________________Function of date input by user______________________________#



        #______________________________Change global variable "Selection" upon button presses______________________________#
        def b1():
            global Selection
            Selection = "McDonalds"
        def b2():
            global Selection
            Selection = "Malay Food"
        def b3():
            global Selection
            Selection = "Subway"
        def b4():
            global Selection
            Selection = "Chicken Rice"
        def b5():
            global Selection
            Selection = "Western Food"  
        #______________________________Change global variable "Selection" upon button presses______________________________#



        # Check stores availability using isRestaurantAvailable() and place the button for the stores if return is True
        # Stores are checked against global variables InputDate and InputTime
        def CheckStores():
            n = 200
            if isDateValid(InputDate):

                if isRestaurantAvailable("McDonalds",InputDate,InputTime):
                    Button1 = tk.Button(self, text="Mcdonald's", fg="black", bg="#bababa", font=FONT, command=lambda:[b1(),controller.show_frame(StoreFrame_UserDateAndTime)])
                    Button1.place(anchor="n", x=400 ,y=n, width=400, height=40)
                    n += 40
                
                if isRestaurantAvailable("Malay Food",InputDate,InputTime):
                    Button2 = tk.Button(self, text="Malay Food", fg="black", bg="#bababa", font=FONT, command=lambda:[b2(),controller.show_frame(StoreFrame_UserDateAndTime)])
                    Button2.place(anchor="n", x=400 ,y=n, width=400, height=40)
                    n += 40

                if isRestaurantAvailable("Subway",InputDate,InputTime):
                    Button3 = tk.Button(self, text="Subway", fg="black", bg="#bababa", font=FONT, command=lambda:[b3(),controller.show_frame(StoreFrame_UserDateAndTime)])
                    Button3.place(anchor="n", x=400 ,y=n, width=400, height=40)
                    n += 40
                    
                if isRestaurantAvailable("Chicken Rice",InputDate,InputTime):
                    Button4 = tk.Button(self, text="Chicken Rice", fg="black", bg="#bababa", font=FONT, command=lambda:[b4(),controller.show_frame(StoreFrame_UserDateAndTime)])
                    Button4.place(anchor="n", x=400 ,y=n, width=400, height=40)
                    n += 40

                if isRestaurantAvailable("Western Food",InputDate,InputTime):
                    Button5 = tk.Button(self, text="Western Food", fg="black", bg="#bababa", font=FONT, command=lambda:[b5(),controller.show_frame(StoreFrame_UserDateAndTime)])
                    Button5.place(anchor="n", x=400 ,y=n, width=400, height=40)
            
            else: # Prompts user to re-enter a valid date when an invalid date is input
                labelinvalid = tk.Label(self, text="INPUT DATE IS INVALID \n Please go back and enter a valid date!", fg="white", bg="red", font=FONT)
                labelinvalid.place(anchor="n", x=400 ,y=260, width=400, height=65)


        # "Reset" by placing a white empty label over the buttons when "Back" button is pressed
        # Global variables InputDate and InputTime are also reset to the default
        def ResetDateAndTime():
            global InputDate 
            global InputTime
            InputDate = getTodaysDate()
            InputTime = getCurrentTime()
            emptylabel = tk.Label(self, bg="white")
            emptylabel.place(anchor="n", x=400 ,y=200, width=400, height=200)


        CheckStoresButton = tk.Button(self, text="Check Available Stores", fg = "black", bg = "#adffb1", font=FONT, command=lambda: CheckStores())
        CheckStoresButton.place(anchor="n", x=400, y=500, width=800, height=50)

        BackButton = tk.Button(self, text="Back", fg = "black", bg = "#96bfff", font=FONT, width=40, command=lambda: [ResetDateAndTime(), controller.show_frame(ChooseADate)])
        BackButton.place(anchor="n", x=400, y=550, width=800, height=50)

class StoreFrame_UserDateAndTime(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)



        #______________________________Background Image______________________________#
        photo = tk.PhotoImage(file="StoreFrame.png")
        label1 = tk.Label(self, image=photo)
        label1.image = photo
        label1.place(x=0,y=0)
        #______________________________Background Image______________________________#



        #______________________________Function of date input by user______________________________#
        def tick():
            DATE, MONTH, YEAR = (int(x) for x in InputDate.split('/'))  
            try: 
                time_string = datetime.date(YEAR, MONTH, DATE).strftime("%A, %d %B, %Y") + ", " + InputTime
            except: 
                time_string = "INPUT DATE IS INVALID"
            clock.config(text=time_string)
            clock.after(100, tick)
        clock = tk.Label(self, fg="white", bg="#303030", font=FONT)
        clock.place(anchor="n", x=400 ,y=0, width=800, height=40)
        tick()
        #______________________________Function of date input by user______________________________#



        #______________________________Function for displaying selected store______________________________#
        def SelectionTick():
            global Selection
            label.config(text=Selection)
            label.after(100,SelectionTick)
        label = tk.Label(self, fg = "black", bg = "grey", font=LARGEFONT)
        label.place(anchor="n", x=400 ,y=40, width=800, height=50)
        SelectionTick()
        #______________________________Function for displaying selected store______________________________#



        # Function to display the operating hours of the currently selected store using popup tkinter.messagebox
        def OperatingHoursButton():
            global Selection
            tkinter.messagebox.showinfo("Operating Hours", getOperatingHours(Selection))


        # Function to generate a new tkinter window to calculate waiting time for the currently selected store
        def WaitingTimeButton():
            global Selection
            window = tk.Tk()

            window.winfo_toplevel().title("Waiting Time")
            
            tk.Label(window, text="Enter the number of people in the queue:").grid(row=0)

            tk.Button(window, text='Quit', command=window.destroy).grid(row=1, column=0)

            e1 = tk.Entry(window)
            e1.grid(row=0, column=1)

            def Calculate():
                try:
                    pax = int(e1.get())
                    tkinter.messagebox.showinfo("Waiting Time","Estimated waiting time is "+ str(calculateWaitingTime(Selection, pax))+" minutes.")
                except:
                    tkinter.messagebox.showerror("Error","Please enter an integer value for the number of people in the queue!")

            button = tk.Button(window, text="Calculate", command=Calculate)
            button.grid(row=1,column=1)

            window.mainloop()


        # Get a dictionary of menu item, prices using getMenu() based on InputDate and InputTime
        # Place the items using a for loop 
        def ViewMenu():
            n = 210
            for item,price in getMenu(Selection, InputDate, InputTime).items():
                
                item1 = tk.Label(self, text=item, bg="white", font=FONT)
                item1.place(anchor="n", x=320 ,y=n, width=250, height=40)

                item2 = tk.Label(self, text=price, bg="white", font=FONT)
                item2.place(anchor="n", x=530 ,y=n, width=100, height=40)

                n += 40
        

        # "Reset" by placing a white empty label over the menu when "Back" button is pressed
        def ResetSelection():
            global Selection
            Selection = ""
            emptylabel = tk.Label(self, bg="white")
            emptylabel.place(anchor="n", x=400 ,y=210, width=400, height=200)

        button1 = tk.Button(self, text="Operating Hours", font=FONT, command = OperatingHoursButton)
        button1.place(anchor="n", x=200 ,y=90, width=400, height=40)

        button2 = tk.Button(self, text="Waiting Time", font=FONT, command = WaitingTimeButton)
        button2.place(anchor="n", x=600 ,y=90, width=400, height=40)

        ViewMenuButton = tk.Button(self, text="View Menu", fg = "black", bg = "#adffb1", font=FONT, command=ViewMenu)
        ViewMenuButton.place(anchor="n", x=400, y=500, width=800, height=50)

        BackButton = tk.Button(self, text="Back", fg = "black", bg = "#96bfff", font=FONT, width=40, command=lambda: [ResetSelection(),controller.show_frame(ChooseAStore_UserDateAndTime)])
        BackButton.place(anchor="n", x=400, y=550, width=800, height=50)


app = MiniProject()
app.mainloop()
