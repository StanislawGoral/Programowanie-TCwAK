def setup():
    frameRate(60)
    size(1280,720)

    global a, b, c, d, Vx, DirX, DirY
    a = 0
    b = 300
    c = 120
    d = 120
    Vx = 5
    Vy = 5
    DirX = 1
    DirY = 1
def draw():
    global a, b, c, d, Vx, DirX, DirY
    rgb=[0,0,0]
    
    background(255)
    
    noStroke()
    for i in range(0,3):
        rgb[i] = random(0,255)
    fill(rgb[0], rgb[1], rgb[2])
    rect(a, b, c, d)
    
    if(a == 1160):
        DirX=0
    elif(a == 0):
        DirX=1
    
    if(b == 600):
        DirY=0
    elif(b == 0):
        DirY=1
        
    if (DirX == 1):
        a=a+Vx
    else:
        a=a-Vx
    
    if (DirY == 1):
        b=b+Vx
    else:
        b=b-Vx
    
    



    
