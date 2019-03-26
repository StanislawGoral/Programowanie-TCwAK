def setup():
    size(1280, 720)
    frameRate(60)
   
    global select, w, h
    select = 0; h = height/2; w=width/2
    
    textAlign(CENTER)
    textMode(CENTER)
    background(255)

def draw():
    global select, w, h
    
    if keyPressed:
        if (key == 's' or keyCode == 37):
            select=1
        elif (key == 'g' or keyCode == 39):
            select=2
            
    if get(mouseX, mouseY)!=g.backgroundColor and mouseX<w:
        select=1
    elif  get(mouseX, mouseY)!=g.backgroundColor and mouseX>w:
        select=2
    
    if select==0:
        textSize(150)
        fill(50, 50, 150)
        text("S", w-100, h)
        text("G", w+100, h)
        
    elif select==1:
        background(255)
    
        textSize(200)   
        fill(0, 150, 255)
        text("S", w-100, h)
            
        textSize(150)
        fill(50, 50, 150)
        text("G", w+100, h)
        
    elif select==2:
        background(255)
        
        textSize(200)
        fill(0, 150, 255)
        text("G", w+100, h)
        
        textSize(150)
        fill(0, 50, 150)
        text("S", w-100, h)
    
    sh = createShape()
    sh.beginShape()
    sh.fill(0,150,200)
    sh.noStroke()
    
    sh.vertex(108, h+100)
    sh.vertex(216, h+316)
    sh.vertex(324, h+100)
    sh.vertex(432, h+316)
    sh.vertex(540, h+100)
    sh.vertex(648, h+316)
    sh.vertex(756, h+100)
    sh.vertex(864, h+316)
    sh.vertex(984, h+100)
    sh.vertex(1080, h+316)
    sh.vertex(1188, h+100)

    sh.endShape(CLOSE)
    shape(sh, 0 ,0)

            
