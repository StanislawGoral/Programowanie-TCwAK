def setup():
    frameRate(60)
    size(1280,720)

    global x, y, w, h, v, dirX, dirY
    x = random(0,1160); y = random(0,600); w = 120; h = 120; v=5
    dirX = int(random(0,2)); dirY = int(random(0,2))

def draw():
    global x, y, w, h, v, dirX, dirY
    rgb=[0,0,0]
    
    background(255)
    
    for i in range(0,3):
        rgb[i] = int(random(0,255))
    fill(rgb[0], rgb[1], rgb[2])
    for i in range(0,3):
        rgb[i] = int(random(0,255))
    strokeWeight(10)
    stroke(rgb[0], rgb[1], rgb[2])
    rect(x, y, w, h)
    
    if(x > 1160):
        dirX=0
    elif(x < 0):
        dirX=1
    
    if(y > 600):
        dirY=0
    elif(y < 0):
        dirY=1
        
    if (dirX == 1):
        x=x+v
    else:
        x=x-v
    
    if (dirY == 1):
        y=y+v
    else:
        y=y-v
