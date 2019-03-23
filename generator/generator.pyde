def setup():
    
    frameRate(1000000)
    size(320,240)
    
    global x, y, w, h, Xo, frame, start
    global r, g, b
    x=0; y=0; w=1; h=1; Xo=1
    start = 0; count=1
    r=int(random(0,255)); g=int(random(0,255)); b=int(random(0,255))

    loadPixels()
    
    f = open('frames_count.txt', "r")
    fh = open('frames_count.txt')
    for line in fh:
        frame=int(line)+1
    fh.close()
    
    
def draw():

    global x, y, w, h, Xo, frame, start
    global r, g, b

    rgb=[r,g,b]
    rgb_row=[r,g,b]
    rgb_col=[r,g,b]
    
    if(start==0):
        rgb_row[0]=int(random(0,256))
        rgb_row[1]=int(random(0,256))
        rgb_row[2]=int(random(0,256))
        
        rgb_col[0]=int(random(0,256))
        rgb_col[1]=int(random(0,256))
        rgb_col[2]=int(random(0,256))
        
    elif (y>0):
        
        if(y*320+x<len(pixels)):
    
            rgb_col[0]=int(red(color(pixels[((y-1)*320+x)])))
            rgb_col[1]=int(green(color(pixels[((y-1)*320+x)])))
            rgb_col[2]=int(blue(color(pixels[((y-1)*320+x)])))
            
            rgb_row[0]=int(red(color(pixels[(y*320+x)-1])))
            rgb_row[1]=int(green(color(pixels[(y*320+x)-1])))
            rgb_row[2]=int(blue(color(pixels[(y*320+x)-1])))
 
    if(start==0):
        for i in range(0,3):
            rgb[i] = int((((rgb_row[i]+rgb_row[i]/2)+random(-150,150))))    # zmieniając wartość '2' oraz -150 i 150 otrzymamy inne efekty
            if (rgb[i]>256):
                rgb[i]=0
            if (rgb[i]<0):
                rgb[i]=0
    if(start==1):
        for i in range(0,3):
            rgb[i] = int((((rgb_row[i]+rgb_col[i])/2)+random(-50,50)))    # zmieniając wartość '2' oraz -30 i 30 otrzymamy inne efekty
            if (rgb[i]>256):
                rgb[i]=0
            if (rgb[i]<0):
                rgb[i]=0
    
    noStroke()
    fill(rgb[0], rgb[1], rgb[2])
    rect(x, y, w, h)
    
    if(start==0):
        if(y==0):
            x=x+1
            if(x==320):
                x=0
                y=y+1
        if(y>0):
            y=y+1
            if(y==240):
                x=0
                y=1
                start=1
    
    if(start==1):        
        if(x==320):
            x=0
            y=y+1
        if(Xo==1):
            x=x+1
        if(x==320 and y==240):
            saveFrame('frame_' + str(frame) + '.png');
            background(255)
            x=0; y=0
            if(frame>0):
                f = open('frames_count.txt', 'a')
                f.write(str(frame)+'\n')
                f.close()
            frame=frame+1
            r=int(random(0,255)); g=int(random(0,255)); b=int(random(0,255))
            start=0
        loadPixels()
        updatePixels()
   
    
