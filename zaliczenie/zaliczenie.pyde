# === PRACA NA ZALICZENIE - INTERAKTYWNA ANIMACJA === #

# KLASA KOŁO ZĘBATE
class gear(object):
    def __init__(self):
        self.x = 0; self.y = 0; self.angle = 0; self.appearance = ''
    def rotation(self, angle):
        translate(self.x, self.y) # ZMIANA PUNKTU OSI OBROTU
        rotate(radians(self.angle)) # OBRÓT O KĄT PODANY W RADIANACH
        
# KLASA PRZYCISK
class Button(object):
    def __init__(self):
        self.x = 0; self.y = 0; self.state = 0
        self.sprite = ''; self.ext = '.png'; self.appearance = ''
    def highlight(self):
        self.appearance = loadImage(self.sprite + '_high' + self.ext); self.state = 1
    def click(self):
        self.appearance = loadImage(self.sprite + '_click' + self.ext); self.state = 2
    def release(self):
        self.appearance = loadImage(self.sprite + self.ext); self.state = 0
        
# USTAWIENIA
def setup():
    global state, speed, gear_1, gear_2, gear_3, bg, btn, distance, icons; state = 0# zmienne globalne
   
    # USTAWIENIA OKNA
    size(1280, 720)
    frameRate(60)
    
    # OBRAZ TŁA
    bg = loadImage("bg.png")
    image(bg, 0, 0)
    
    # TWORZENIE OBIEKTÓW
    # ================ #
    # KOŁA ZĘBATE
    imageMode(CENTER)
    gear_1 = gear()
    gear_1.appearance = loadImage("gear_small.png")
    gear_1.angle = 0; gear_1.x = 648.895; gear_1.y = 248.803
    
    gear_2 = gear()
    gear_2.appearance = loadImage("gear_medium.png")
    gear_2.angle = 0; gear_2.x = 789.582; gear_2.y = 249.403
    
    gear_3 = gear()
    gear_3.appearance = loadImage("gear_big.png")
    gear_3.angle = 0; gear_3.x = 529.017; gear_3.y = 368.709
    
    # PRZYCISKI
    # LISTA OBIEKTÓW - PRZYCISKI SĄ ROZMIESZCZONE RÓWNOMIERNIE, MAJĄ JEDEN SPRITE
    # I WIELKOŚĆ, WIĘC MOŻNA NADAĆ IM WARTOŚCI I JE WYŚWIETLIĆ W PĘTLI
    btn = [Button(), Button(), Button(), Button()]
    distance = 98 # ODLEGŁOŚĆ MIĘDZY PRZYCISKAMI
    for i in range(0,4):
        btn[i] = Button()
        btn[i].sprite = 'btn'
        btn[i].appearance = loadImage(btn[i].sprite + btn[i].ext)
        btn[i].x = 492+distance*i; btn[i].y = 580
    icons = loadImage('button_icons.png')
    
    # PRĘDKOŚĆ POCZĄTKOWA
    speed = 0
    
def draw():
    # ZMIENNE GLOBALNE
    global gear_1, gear_2, gear_3, bg, state, speed, btn, distance
    
    # OGRANICZENIE PRĘDKOŚCI
    if speed > 10:
        speed = 10
    elif speed < -10:
        speed = - 10
    
    # ZACHOWANIE ODPOWIEDNIEGO KĄTA OBROTU KIEDY ZATRZYMANE
    if state == 0:
        imageMode(CORNER)
        image(bg, 0 ,0)
        imageMode(CENTER)
        translate(gear_1.x, gear_1.y); rotate(radians(gear_1.angle)); image(gear_1.appearance, 0, 0)
        resetMatrix()
        translate(gear_2.x, gear_2.y); rotate(radians(gear_2.angle)); image(gear_2.appearance, 0, 0)
        resetMatrix()
        translate(gear_3.x, gear_3.y); rotate(radians(gear_3.angle));image(gear_3.appearance, 0, 0)
        resetMatrix()
    
    # KIEDY WŁĄCZONE, DEFINICJA OBROTU
    if state == 1:
        imageMode(CORNER)
        image(bg, 0 ,0)
        imageMode(CENTER)
        gear_1.rotation(gear_1.angle); gear_1.angle = (gear_1.angle - 1 * speed); image(gear_1.appearance, 0, 0)
        resetMatrix()
        gear_2.rotation(gear_2.angle); gear_2.angle = (gear_2.angle + 0.75  * speed); image(gear_2.appearance, 0, 0)
        resetMatrix()
        gear_3.rotation(gear_2.angle); gear_3.angle = (gear_3.angle + 0.5 * speed); image(gear_3.appearance, 0, 0)
        resetMatrix()
    
    # DEFINIOWANIE HITBOXÓW POSZCZEGÓLNYCH PRZYCISKÓW
    for i in range(0,4):
        if mouseX > btn[i].x - 42 and mouseX < btn[i].x + 42 and mouseY > btn[i].y - 27 and mouseY < btn[i].y + 27:
            btn[i].highlight()
            if mousePressed:
                btn[i].click()
        elif not(mouseX > btn[i].x - 42 and mouseX < btn[i].x + 42 and mouseY > btn[i].y - 27 and mouseY < btn[i].y + 27):
            btn[i].release()
    
    # RYSOWANIE PRZYCISKÓW
    for i in range(0,4):
        imageMode(CENTER)
        resetMatrix()
        image(btn[i].appearance, btn[i].x, btn[i].y)
        
    # RYSOWANIE IKONEK NA PRZYCISKACH I INFORMACJI O PRĘDKOŚCI
    image(icons, width/2, 580)
    textSize(34); fill(0, 102, 128); text('PREDKOSC: ' + str(int((speed))), 152, 112)

    # ZMIANA STANU ORAZ PRĘDKOŚCI
    if btn[2].state == 2:
        state = 1
    if btn[1].state == 2:
        state = 0
    if btn[3].state == 2:
        speed = speed + 0.1
    if btn[0].state == 2:
        speed = speed - 0.1
