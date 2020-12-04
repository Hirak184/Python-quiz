from tkinter import *
from tkinter import messagebox
import mysql.connector as mysql
root=Tk()
root.geometry("700x650")
rainfo=PhotoImage(file="rainforest1.png")
pl=PhotoImage(file="pl1.png")
gal=PhotoImage(file="galaxy.png")
hol=PhotoImage(file="hollywood.png")
fot=PhotoImage(file="champ.png")
game=PhotoImage(file="game.png")
olym=PhotoImage(file="olympic.png")
cric=PhotoImage(file="cricket.png")
fore=PhotoImage(file="forest.png")
frost=PhotoImage(file="frost.png")
photo1=PhotoImage(file="bg.png")
bglabel=Label(root,image=photo1)
bglabel.place(x=0,y=0)
photo=PhotoImage(file="quiz1.png")
alabel=Label(root,image=photo)
alabel.place(x=200,y=3)
gen=StringVar()
gen.set(-1)
name=Label(root,text="Name ").place(x=20,y=250)
gender=Label(root,text="Gender ").place(x=20,y=340)
radio1=Radiobutton(root,text="M",variable=gen,value="Male").place(x=70,y=340)
radio2=Radiobutton(root,text="F",variable=gen,value="Female").place(x=140,y=340)
age=Label(root,text="Age").place(x=20,y=430)
nameval=StringVar()
ageval=StringVar()

but=StringVar()
but.set("NEXT")
nameentry=Entry(root,textvariable=nameval).place(x=70,y=250)
ageentry=Entry(root,textvariable=ageval,width=10).place(x=70,y=430)
score= 0
def questions():
    if not nameval.get():
        messagebox.showinfo(title="Entry Details",message="Please enter your name properly ")
    elif not gen.get():
        messagebox.showinfo(title="Entry Details",message="Please select your gender ")
    elif not ageval.get():
        messagebox.showinfo(title="Entry Details",message="Please enter your age properly ")

    if nameval.get() and gen.get() and ageval.get():
        name1 = nameval.get()
        gen1 = gen.get()
        age1 = ageval.get()
        con=mysql.connect(host="localhost",charset="utf8",user="root",password="",database="basic_info")
        cursor=con.cursor()
        cursor.execute("insert into quiz (Name,Gender,Age) values('"+name1+"','"+gen1+"','"+age1+"')")
        cursor.execute("commit")
        con.close()
        messagebox.showinfo(message="Insertion successfull\nStart Quiz")
        que=Toplevel()
        que.geometry("500x500")
        root.withdraw()
        que.counter = 0
        l1 = Label(que, image=rainfo)
        l1.place(x=0, y=0)
        rain=IntVar()
        v=StringVar()
        Label(que,textvariable=v).place(x=50,y=50)
        v.set("Which rainforest produces the most amount of oxygen in the world?")
        r1=StringVar()
        r2 = StringVar()
        r3 = StringVar()
        r4 = StringVar()
        radio1=Radiobutton(que,textvariable=r1,variable=rain,value=1)
        radio1.place(x=70,y=100)
        radio2 = Radiobutton(que, textvariable=r2, variable=rain, value=2)
        radio2.place(x=220, y=100)
        radio3 = Radiobutton(que, textvariable=r3, variable=rain, value=3)
        radio3.place(x=70, y=150)
        radio4 = Radiobutton(que, textvariable=r4, variable=rain, value=4)
        radio4.place(x=220, y=150)
        r1.set("Congo Rainforest")
        r2.set("Amazon Rainforest")
        r3.set("Daintree Rainforest")
        r4.set("Kinabalu Rainforest")

        def desel():
            rain.set(-1)


        def nextquestions():
            global score
            que.counter +=1

            if que.counter==1:

                    l1.config(image=pl)
                    v.set("Who is the active player holding record of most UCL goals?")
                    r1.set("Neymar jr")
                    r2.set("Lionel Messi")
                    r3.set("Cristiano Ronaldo")
                    r4.set("Zlatan Ibrahimovic")
                    if rain.get() == 2:

                        score += 10
                        desel()
                    else:
                        score+=0
                        desel()


            elif que.counter==2:

                     l1.config(image=gal)
                     v.set("Which is the brightest star in the earth's night sky?")
                     r1.set("Alpha Centurai")
                     r2.set("Vega")
                     r3.set("Canopus")
                     r4.set("Sirius A")
                     if rain.get() == 3:
                        score += 10
                        desel()
                     else:
                        score += 0
                        desel()


            elif que.counter==3:



                     l1.config(image=hol)
                     v.set("Which movie was the highest grossing movie in the year 2015?")
                     r1.set("Furious 7")
                     r2.set("Avengers:Age of Ultron")
                     r3.set("Jurassic World")
                     r4.set("Inside Out")
                     if rain.get() == 4:
                        score += 10
                        desel()
                     else:
                        score += 0
                        desel()

            elif que.counter==4:


                     l1.config(image=fot)
                     v.set("Which active player holds the record of most goals in a year?")
                     r1.set("Lionel Messi")
                     r2.set("Cristiano Ronaldo")
                     r3.set("Luis Suarez")
                     r4.set("Neymar jr")
                     if rain.get() == 3:
                        score += 10
                        desel()
                     else:
                        score += 0
                        desel()

            elif que.counter == 5:



                     l1.config(image=game)
                     v.set("Which game won the game of the year award in 2016?")
                     r1.set("Fortnite")
                     r2.set("Hearthstone")
                     r3.set("Overwatch")
                     r4.set("Valorant")
                     if rain.get() == 1:
                        score += 10
                        desel()
                     else:
                        score += 0
                        desel()

            elif que.counter == 6:



                     l1.config(image=olym)
                     v.set("Who is considered as the fastest athlete in the world?")
                     r1.set("Tyson Gay")
                     r2.set("Yohan Blake")
                     r3.set("Asafa Powell")
                     r4.set("Usain Bolt")
                     if rain.get() == 3:
                        score += 10
                        desel()
                     else:
                        score += 0
                        desel()

            elif que.counter == 7:


                    l1.config(image=cric)
                    v.set("Who is the current best Batsman in the world ?")
                    r1.set("David warner")
                    r2.set("Virat Kohli")
                    r3.set("Steve Smith")
                    r4.set("Kane Williamson")
                    if rain.get() == 4:
                        score += 10
                        desel()
                    else:
                        score += 0
                        desel()

            elif que.counter == 8:



                    l1.config(image=fore)
                    v.set("Which country was 1st ever to ban deforestation?")
                    r1.set("Norway")
                    r2.set("Finland")
                    r3.set("Denmark")
                    r4.set("U.S.A")
                    if rain.get() == 3:
                         score += 10
                         desel()
                    else:
                         score += 0
                         desel()

            elif que.counter == 9:



                    l1.config(image=frost)
                    v.set("Which of the following is the best game development tool?")
                    r1.set("Unity")
                    r2.set("Torque")
                    r3.set("Frostbite Engine")
                    r4.set("Unreal Engine")
                    but.set("SUBMIT")
                    if rain.get() == 1:
                         score += 10
                         desel()
                    else:
                         score += 0
                         desel()

            elif que.counter==10:



                    if rain.get()==4:
                         score +=10
                         desel()
                         score=str(score)
                         con = mysql.connect(host="localhost", charset="utf8", user="root", password="",
                                             database="basic_info")
                         cursor = con.cursor()
                         cursor.execute("update quiz set Score='"+score+"' where Name='"+name1+"'")
                         cursor.execute("commit")
                         con.close()
                         messagebox.showinfo(message=f"Submited Successfully\n Your Score is {score}/100")
                         root.destroy()
                    else:
                         score += 0
                         desel()
                         score = str(score)
                         con = mysql.connect(host="localhost", charset="utf8", user="root", password="",
                                             database="basic_info")
                         cursor = con.cursor()
                         cursor.execute("update quiz set Score='"+score+"' where Name='"+name1+"'")
                         cursor.execute("commit")
                         con.close()
                         messagebox.showinfo(message=f"Submited Successfully\n Your Score is {score}/100")
                         root.destroy()
    Button(que,textvariable=but,font="times 10 bold",command=nextquestions).place(x=300,y=230)
Button(root,text="START",fg="blue",font="times 10 bold",command=questions).place(x=250,y=510)
root.mainloop()