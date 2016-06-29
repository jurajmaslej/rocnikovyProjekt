# coding=utf-8
import Tkinter, time, os

class Hrac:
    def __init__(self, r, s,x,y):
        self.x = x
        self.y = y
        self.r = r
        self.s = s
        self.robot=Tkinter.PhotoImage(file='robot1.png')
        self.robotSvieti=Tkinter.PhotoImage(file='robot.png')
        

    def kresli(self, canvas, vel, farba):
        self.canvas= canvas
        self.vel = vel
        x,y =40,0

        self.id=self.canvas.create_image(x,y,anchor="ne",image=self.robot)

    def vykresli(self, canvas, vel, farba):
        self.canvas= canvas
        self.vel = vel
       
        self.id=self.canvas.create_image(95,115,anchor="ne",image=self.robot)

    def posun(self, dr, ds):
        self.r += dr
        self.s += ds
        self.canvas.move(self.id, ds*self.vel, dr*self.vel)

    def posun2(self, dr, ds):
        self.x += dr
        self.y += ds
        self.canvas.move(self.id, dr, ds)
    def posunNaPovodne(self,ax,by):
        self.x = ax
        self.y = by
        self.canvas.move(self.id,ax,by)
    def je_klik(self, x, y):
        return self.x-40<x<=self.x and self.y<=y<self.y+40

class simpleapp():
    def __init__(self):
        
        self.g = Tkinter.Tk()
        self.g.geometry("750x470")
        self.premenne()
        self.vytvorenieMenu()
        self.vytvorenieLabelMenu()
        self.pathCanvas()
        self.zakladnyCanvas()
        self.zakladneMenu()
        self.UdalostiMenu()
        self.infoMenu()
        self.nacitajmapu()
        self.g.bind_all('<Up>', self.hore)
        self.g.bind_all('<Left>', self.vlavo)
        self.g.bind_all('<Right>', self.vpravo)
        self.g.bind_all('<Down>', self.dole)
        self.g.bind_all('<l>', self.zasviet)
        self.g.bind_all('<r>', self.pustipohyb)
        self.g.bind('<Button-1>', self.udalost_tahaj_start)
        

        self.g.mainloop()
        
    def premenne(self):
        self.up=Tkinter.PhotoImage(file='up1.png')
        self.down=Tkinter.PhotoImage(file='down1.png')
        self.left=Tkinter.PhotoImage(file='left1.png')
        self.right=Tkinter.PhotoImage(file='right1.png')
        self.light=Tkinter.PhotoImage(file='light1.png')
        self.svieti=False
        self.path=[]
        self.pis=30
        self.Ypis=15
        self.vstupnyText0=Tkinter.StringVar()
        self.vstupnyText1=Tkinter.StringVar()
        self.vstupnyText2=Tkinter.StringVar()
    def vytvorenieMenu(self):        
        self.labelframe=Tkinter.LabelFrame(self.g)
        self.labelframe.pack(fill="y",side="left")
        
    def vytvorenieLabelMenu(self):        
        self.label=Tkinter.Label(self.labelframe)
        self.label.pack(expand="yes",fill="both")
        
    def zakladnyCanvas(self):
        self.canvas=Tkinter.Canvas(self.g,bg='white',width=700,height=360)
        self.canvas.pack(expand="yes",fill="both",side="right")
        
    def pathCanvas(self):
        self.canvas1=Tkinter.Canvas(self.g,bg='white',width=120,height=70)
        self.canvas1.pack(expand="no",fill="x",side="top")
        #self.idmapa=self.canvas1.create_image(10,10,image=self.foto1)
        
    def zakladneMenu(self):
        self.text=Tkinter.Message(self.label,textvariable=self.vstupnyText0,relief="raised",anchor="w",width=130)
        self.text.pack(fill="x",pady=3,padx=8,side="top")
        self.vstupnyText0.set("Vitajte v hre LightBot, zdraví Vás Robot :) Pomôžte mu nájsť cestu na vyznačené políčko. Uchopte Robota a postavte ho na jedno zo zelených štartovacích políčok. ")
        
    def infoMenu(self):
        self.text1=Tkinter.Message(self.label,textvariable=self.vstupnyText1,relief="raised",anchor="w",width=130)
        self.text1.pack(fill="x",pady=3,padx=8,side="top")
        self.vstupnyText1.set("Ovládanie: šípakmi zvoľte cestu, \n 1 šípka znamená posunutie sa o jedno políčko. Nezabudni na konci robotovi prikázať aby zasvietil, spravíš tak sltačením L. Robot sa pohne podľa šípok po stlačení R")

    def UdalostiMenu(self):
        self.text2=Tkinter.Message(self.label,textvariable=self.vstupnyText2,relief="raised",anchor="w",width=130)
        self.text2.pack(fill="x",pady=3,padx=8,side="bottom")
        self.vstupnyText2.set("Pozor, robot sa po rozsvietení prestane hýbať. Ak sa robot rozsvieti mimo vyznačeného políčka, tak ste prehrali. Hra sa zavrie sama")
                
    def PosunHore(self,canvas1):
        self.idhore=canvas1.create_image(self.pis,self.Ypis,image=self.up)
        self.pis+=40
        self.over()
        
    def PosunDole(self,canvas1):
        self.iddole=canvas1.create_image(self.pis,self.Ypis,image=self.down)
        self.pis+=40
        self.over()
        
    def PosunLavo(self,canvas1):
        self.idlavo=canvas1.create_image(self.pis,self.Ypis,image=self.left)
        self.pis+=40
        self.over()
        
    def PosunPravo(self,canvas1):
        self.idpravo=canvas1.create_image(self.pis,self.Ypis,image=self.right)
        self.pis+=40
        self.over()
        
    def ZasvietKoniec(self,canvas1):
        self.idsvieti=canvas1.create_image(self.pis,self.Ypis,image=self.light)
        self.pis+=40
        self.over()
        
    def over(self):
        if self.pis>540:
            self.Ypis+=40
            self.pis=30

    def udalost_tahaj_start(self, e):
    
        if self.hrac.je_klik(e.x,e.y) ==True:
            print('klikol si')
            self.g.bind('<B1-Motion>', self.udalost_tahaj)
            self.g.bind('<ButtonRelease-1>', self.udalost_pusti)
        

    def udalost_tahaj(self, e):
        self.hrac.posun2(e.x-self.hrac.x, e.y-self.hrac.y)
    def udalost_pusti(self, e):
        self.g.unbind('<B1-Motion>')
        self.g.unbind('<ButtonRelease-1>')
        print(self.hrac.x, self.hrac.y)
        if ((80<=self.hrac.x <=100)and(100<=self.hrac.y <=120)):
            self.hrac.r=1
            self.hrac.s=1
        if ((80<=self.hrac.x <=100)and(240<=self.hrac.y <=260)):
            self.hrac.r=4
            self.hrac.s=1
        if ((480<=self.hrac.x <=502)and(100<=self.hrac.y <=120)):
            self.hrac.r=1
            self.hrac.s=9
        if ((340<=self.hrac.x <=360)and(340<=self.hrac.y <=360)):
            self.hrac.r=6
            self.hrac.s=6
        if (((80<=self.hrac.x <=100)and(100<=self.hrac.y <=120))== False)and((80<=self.hrac.x <=100)and(240<=self.hrac.y <=260))== False and((480<=self.hrac.x <=502)and(100<=self.hrac.y <=120))== False and ((340<=self.hrac.x <=360)and(340<=self.hrac.y <=360))== False:
            self.hrac=None
            self.canvas.update()
            self.hrac= Hrac(0,0,40,0)
            self.hrac.kresli(self.canvas, self.vel, self.farba[0])
            self.canvas.update()
        
    
    def pustipohyb(self,e):
        self.g.unbind_all('<Button-1>')
        self.g.unbind_all('<B1-Motion>')
        self.g.unbind_all('<ButtonRelease-1>')
        self.g.unbind_all('<Up>')
        self.g.unbind_all('<Left>')
        self.g.unbind_all('<Right>')
        self.g.unbind_all('<Down>')
        self.g.unbind_all('<l>')
        self.g.unbind_all('<r>')
        for i in range(len(self.path)):
            if self.path[i]=='0':
                self.posun(-1, 0)
                self.canvas.update()
                time.sleep(1)
            if self.path[i]=='1':
                self.posun(0, -1)
                time.sleep(1)
                self.canvas.update()
               
            if self.path[i]=='2':
                self.posun(0, 1)
                time.sleep(1)
                self.canvas.update()
            if self.path[i]=='3':
                self.posun(1, 0)
                time.sleep(1)
                self.canvas.update()
            if self.path[i]=='l':
                x,y = self.hrac.s*self.hrac.vel, self.hrac.r*self.hrac.vel
                self.svieti=True
                self.id=self.canvas.create_image(x+46,y+50,anchor="ne",image=self.hrac.robotSvieti)
                self.hrac.canvas.update()
                self.canvas.update()
                self.g.unbind_all('<Up>')
                self.g.unbind_all('<Left>')
                self.g.unbind_all('<Right>')
                self.g.unbind_all('<Down>')
                self.g.unbind_all('<l>')
                self.g.unbind_all('<r>')
                
                if ((self.pole[self.hrac.r][self.hrac.s] == '+')and  (self.svieti==True)):
                    self.canvas.create_text(320,100,text='Vyhral si ',fill='black',font='arial 90 bold')
                else:
                    self.canvas.create_text(320,100,text='Prehral si ',fill='black',font='arial 90 bold')
                self.hrac.canvas.update()
                time.sleep(2)
                os._exit(0)
            
    def kresli(self):
        for i in range(self.vyska):
            for j in range(self.sirka):
                x,y = j*self.vel, i*self.vel+50
                '''
                f = self.farba['*.+'.index(self.pole[i][j])+2]
                '''
                if self.pole[i][j]=='*':
                    f='gray'
                if self.pole[i][j]=='.':
                    f='white'
                if self.pole[i][j]=='l':
                    f='green'
                if self.pole[i][j]=='+':
                    f='red'
                self.canvas.create_rectangle(x,y,x+self.vel,y+self.vel,fill=f)
        self.hrac.kresli(self.canvas, self.vel, self.farba[0])
        
        
    def hore(self, e):
        self.PosunHore(self.canvas1)
        self.path.append('0')

    def vlavo(self, e):
        self.PosunLavo(self.canvas1)
        self.path.append('1')
      

    def vpravo(self, e):
        self.PosunPravo(self.canvas1)
        self.path.append('2')
   

    def dole(self, e):
        self.PosunDole(self.canvas1)
        self.path.append('3')

    def zasviet(self,e):
        print("chce svietit")
        self.ZasvietKoniec(self.canvas1)
        self.path.append('l')

    
    def posun(self, dr, ds):
        r = self.hrac.r + dr
        s = self.hrac.s + ds
        if r<0 or r>=self.vyska or s<0 or s>=self.sirka or self.pole[r][s]=='*':
            return
        self.hrac.posun(dr,ds)
        return
        
#nacita mapu, zavola metodu kresli, ktora ju nakresli
    def nacitajmapu(self):
        t = open('map.txt')
        self.vyska = int(t.readline().strip())
        self.pole = [None] * self.vyska
        for i in range(self.vyska):
            self.pole[i] = list(t.readline().strip())

        self.hrac=Hrac(0,0,40,0)
        self.vel = int(t.readline().strip())
        self.farba = t.readline().split()
        t.close()
        self.sirka = len(self.pole[0])
        self.kresli()
        

app=simpleapp()
