def setup():
    frameRate(60)
    size(1280,720)

    global a, b, c, d, Vx, dir
    a = 0
    b = 300
    c = 120
    d = 120
    Vx = 5
    dir = 1
    
def draw():
    global a, b, c, d, Vx, dir
    rgb=[0,0,0]
    
    background(255)
    
    noStroke()
    for i in range(0,3):
        rgb[i] = random(0,255)
    fill(rgb[0], rgb[1], rgb[2])
    rect(a, b, c, d)
    
    if(a == 1160):
        dir=0
    elif(a == 0):
        dir=1
        
    if (dir == 1):
        a=a+Vx
    else:
        a=a-Vx
    



    
