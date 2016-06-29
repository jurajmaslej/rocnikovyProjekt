import tkinter, random

class Obdlznik:
    def __init__(self, x, y, sirka, vyska, farba='red'):
        self.x = x
        self.y = y
        self.sirka = sirka
        self.vyska = vyska
        self.farba = farba

    def kresli(self, g):
        self.g = g
        self.id = self.g.create_rectangle(self.x,self.y,
                      self.x+self.sirka,self.y+self.vyska,
                      fill=self.farba)

    def posun(self, dx=0, dy=0):
        self.x += dx
        self.y += dy
        self.g.move(self.id, dx, dy)

    def zmen(self, sirka, vyska):
        self.sirka = sirka
        self.vyska = vyska
        self.g.coords(self.id, self.x,self.y,
                      self.x+self.sirka,self.y+self.vyska)

    def prefarbi(self, farba):
        self.farba = farba
        self.g.itemconfig(self.id, fill=farba)
    def je_klik(self, x, y):
        return self.x<=x<self.x+self.sirka and self.y<=y<self.y+self.vyska
class Hrac:
    def __init__(self,x,y):
        self.x = x
        self.y = y

        self.robot=tkinter.PhotoImage(file='robot1.png')
        self.robotSvieti=tkinter.PhotoImage(file='robot.png')
        
    def kresli(self, canvas, vel):
        self.canvas= canvas
        self.vel = vel
        self.id=self.canvas.create_image(self.x,self.y,anchor="ne",image=self.robot)

    def vykresli(self, canvas, vel):
        self.id=self.canvas.create_image(95,115,anchor="ne",image=self.robot)

    def posun(self, dr, ds):
        self.x += dr
        self.y += ds
        self.canvas.move(self.id, dr, ds)

    def posun2(self, dx=0, dy=0):
       
        self.x += dx
        self.y += dy
        self.g.move(self.id, dx, dy)
    def je_klik(self, x, y):
        return self.x-40<x<=self.x and self.y<=y<self.y+40



class Skupina:
    def __init__(self, g):
        self.pole = []
        self.g = g

    def pridaj(self, utvar):
        self.pole.append(utvar)
        utvar.kresli(g)
class Program:
    def __init__(self):
        self.pole = []
        self.g = tkinter.Canvas(bg='white', width=400, height=400)
        self.g.pack()
        for i in range(5):
            self.pridaj(Obdlznik(random.randint(50, 350),random.randint(50, 350), 40, 30))
        self.hrac=Hrac(40,40)
        self.hrac.kresli(self.g,70)
        self.pole.append(self.hrac)
        self.g.bind('<Button-1>', self.udalost_tahaj_start)
        self.g.bind('<Button-3>', self.udalost_pravy_klik)
        self.g.mainloop()

    def udalost_pravy_klik(self, e):
        if random.randrange(2):
            self.pridaj(Kruh(e.x, e.y, 30, nahodna_farba()))
        else:
            self.pridaj(Obdlznik(e.x, e.y, 30, 40, nahodna_farba()))
    def pridaj(self,utvar):
        self.pole.append(utvar)
        utvar.kresli(self.g)

    def udalost_tahaj_start(self, e):
        ix = len(self.pole)-1
        while ix >= 0 and not self.pole[ix].je_klik(e.x, e.y):
            ix -= 1
        if ix < 0:
            self.utvar = None
            return
        self.utvar = self.pole[ix]
        self.ex, self.ey = e.x, e.y
        self.g.bind('<B1-Motion>', self.udalost_tahaj)
        self.g.bind('<ButtonRelease-1>', self.udalost_pusti)

    def udalost_tahaj(self, e):
        self.utvar.posun(e.x-self.ex, e.y-self.ey)
        self.ex, self.ey = e.x, e.y

    def udalost_pusti(self, e):
        self.g.unbind('<B1-Motion>')
        self.g.unbind('<ButtonRelease-1>')
        self.utvar = None
        
Program()
