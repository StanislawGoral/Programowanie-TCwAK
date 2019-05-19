
# ====== GRACZ ======
class Gracz(object):
    def __init__(self):
        self.x = 640.0
        self.y = 600.0
        self.lewo = 0
        self.prawo = 0
        self.predkosc = 5
        self.rozmiar = [50, 50]
    def rysuj(self):
        rectMode(CENTER)
        noStroke()
        fill(0, 255, 0)
        rect(self.x, self.y, self.rozmiar[0], self.rozmiar[1])
    def ruch(self):
        self.x = self.x + (self.prawo-self.lewo)*self.predkosc


# ====== POCISK ======
class Pocisk(object):
    def __init__(self):
        self.x = G.x
        self.y = G.y
        self.predkosc = 10
        self.rozmiar = [10, 10]
        self.cooldown = False
    def rysuj(self):
        rectMode(CENTER)
        noStroke()
        fill(255, 255, 0)
        rect(self.x, self.y, self.rozmiar[0], self.rozmiar[1])
    def ruch(self):
        self.y = self.y - self.predkosc
    def zniszcz(self):
        if self.y < 0:
            self.x = G.x
            self.y = G.y

class Przeciwnik(object):
    def __init__(self):
        self.x = 640
        self.y = 100
        self.rozmiar = [50, 50]
    def rysuj(self):
        rectMode(CENTER)
        noStroke()
        fill(255, 0, 0)
        rect(self.x, self.y, self.rozmiar[0], self.rozmiar[1])
    # def ruch(self):
        
def setup():
    size(1280, 720)
    frameRate(60)
    global G, P, Prz
    G = Gracz()
    P = Pocisk()
    Prz = Przeciwnik()
def draw():
    background(0)
    G.rysuj()
    G.ruch()
    Prz.rysuj()
    if P.cooldown == True:
        P.rysuj() 
        P.ruch()
        P.zniszcz()
    if P.y < 1:
        P.cooldown = False

    
    print keyCode, P.cooldown, P.y

def keyPressed():
    if keyCode == LEFT:
        G.lewo = 1
    if keyCode == RIGHT:
        G.prawo = 1
    if keyCode == 32 and P.cooldown == False:
        P.cooldown = True
        
def keyReleased():
    if keyCode == LEFT:
        G.lewo = 0
    if keyCode == RIGHT:
        G.prawo = 0
    
