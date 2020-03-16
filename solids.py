import math

size = 500
pixels = []
for i in range(size):
    pixels.append([])
    for j in range(size):
        pixels[i].append([255,255,255])

def line(x1,y1,x2,y2,r,g,b):
    x1 = round(x1)
    x2 = round(x2)
    y1 = round(y1)
    y2 = round(y2)
    if(x1==x2):
        for i in range(min(y1,y2),max(y1,y2)+1):
            pixels[(x1+size)%size][(i+size)%size]=[r,g,b]
        return
    if(y1==y2):
        for i in range(min(x1,x2),max(x1,x2)+1):
            pixels[(i+size)%size][(y1+size)%size]=[r,g,b]
        return
    m = (y1-y2)/(x1-x2)
    #print(m)
    if(abs(m)<1):
        if(x1>x2):
            line(x2,y2,x1,y1,r,g,b)
            return
        extra = 0
        shift = 0

        for i in range(x1,x2):
            pixels[(i+size)%size][(y1+shift)%size]=[r,g,b]
            extra += m
            shift=round(extra)
    if(abs(m)>1):
        m = 1/m
        if(y1>y2):
            line(x2,y2,x1,y1,r,g,b)
            return
        extra = 0
        shift = 0

        for i in range(y1,y2):
            pixels[(x1+shift)%size][(i+size)%size]=[r,g,b]
            extra += m
            shift=round(extra)

def parametricEllipse(x,y,z,rx,ry=-1,trate=100):
    if(ry==-1):
        ry = rx
    for i in range(trate):
        x1=x+rx*math.cos(2*math.pi*i/trate)
        y1=y+ry*math.sin(2*math.pi*i/trate)
        z1=0
        addLine(x1,y1,z1,x1,y1,z1)

def parametricEllipsePoints(x,y,z,rx,ry=-1,trate=100):
    if(ry==-1):
        ry = rx
    ans = []
    for i in range(trate):
        x1=x+rx*math.cos(2*math.pi*i/trate)
        y1=y+ry*math.sin(2*math.pi*i/trate)
        z1=0
        ans.append([x1,y1,z1,1])
    return ans

def bezier(x1,y1,x2,y2,x3,y3,x4,y4,trate=1000):
    ax = (-x1 + 3 * x2 - 3*x3 + x4)
    bx = (3*x1-6*x2+3*x3)
    cx = -3*x1+3*x2
    dx = x1
    ay = (-y1 + 3 * y2 - 3*y3 + y4)
    by = (3*y1-6*y2+3*y3)
    cy = -3*y1+3*y2
    dy = y1
    for i in range(trate):
        t=i/trate
        p1x = ax*t**3+bx*t**2+cx*t+dx
        p1y = ay*t**3+by*t**2+cy*t+dy
        p1z = 0
        s = t + 1/trate
        p2x = ax*(s)**3+bx*(s)**2+cx*(s)+dx
        p2y = ay*(s)**3+by*(s)**2+cy*(s)+dy
        p2z = 0
        addLine(p1x,p1y,p1z,p2x,p2y,p2z)

def hermite(x1,y1,x2,y2,x3,y3,x4,y4,trate=1000):
    ax = 2*x1-2*x2+x3+x4
    bx = -3*x1+3*x2-2*x3-x4
    cx = x3
    dx = x1
    ay = 2*y1-2*y2+y3+y4
    by = -3*y1+3*y2-2*y3-y4
    cy = y3
    dy = y1
    for i in range(trate):
        t=i/trate
        p1x = ax*t**3+bx*t**2+cx*t+dx
        p1y = ay*t**3+by*t**2+cy*t+dy
        p1z = 0
        s = t + 1/trate
        p2x = ax*(s)**3+bx*(s)**2+cx*(s)+dx
        p2y = ay*(s)**3+by*(s)**2+cy*(s)+dy
        p2z = 0
        addLine(p1x,p1y,p1z,p2x,p2y,p2z)

def matrixMult(a,b):
    for i in range(len(b)):
        temp = []
        for j in range(len(a)):
            sum = 0
            for k in range(len(a[0])):
                sum+=a[k][j]*b[i][k]
            temp.append(sum)
        b[i] = temp
    return b

def matrixPrint(a):
    for i in range(len(a[0])):
        stri = ""
        for j in range(len(a)):
            stri+=str(a[j][i])+" "
        print(stri)
    print("")

def altitude(p1x,p1y,p2x,p2y,p3x,p3y,r,g,b):
    m23 = (p3y-p2y)/(p3x-p2x)

    Dx = (p2y-p1y-m23*p2x-p1x/m23)/(-m23-1/m23)
    Dy = p2y+m23*(Dx-p2x)
    Dx = int(Dx)
    Dy = int(Dy)
    lineMatrix.append([p1x,p1y,0,1])
    lineMatrix.append([Dx,Dy,0,1])
    crosshair(Dx,Dy,5,255,0,0)



def crosshair(x1,y1,radius,r,g,b):
    lineMatrix.append([x1-radius,y1,0,1])
    lineMatrix.append([x1+radius,y1,0,1])
    lineMatrix.append([x1,y1-radius,0,1])
    lineMatrix.append([x1,y1+radius,0,1])


def median(p1x,p1y,p2x,p2y,p3x,p3y,r,g,b):
    lineMatrix.append([p1x,p1y,0,1])
    lineMatrix.append([int((p2x+p3x)/2),int((p2y+p3y)/2),0,1])
    crosshair(int((p2x+p3x)/2),int((p2y+p3y)/2),5,255,0,0)

def circle(centerx,centery,pointx,pointy):
    lineMatrix = []
    rotAngle = math.pi/720
    rotMatrix = [
    [math.cos(rotAngle),math.sin(rotAngle),0,0],
    [-math.sin(rotAngle),math.cos(rotAngle),0,0],
    [0,0,1,0],
    [-centerx*math.cos(rotAngle)+centery*math.sin(rotAngle)+centerx,-centerx*math.sin(rotAngle)-centery*math.cos(rotAngle)+centery,0,1]]
    lineMatrix.append([pointx,pointy,0,1])
    lineMatrix.append([pointx,pointy,0,1])

    for i in range(1440):
        matrixDraw(lineMatrix)
        # if(i%360==0):
        #     print("Multiplied line matrix that is actually a dot by rot matrix "+str(i)+" times")
        #     matrixPrint(lineMatrix)

        matrixMult(rotMatrix,lineMatrix)
        #matrixPrint(lineMatrix)
    matrixDraw()

def sphere(x,y,z,r):
    n = 50
    finalPs = []
    ident()

    for i in range(n):
        roty(180/n)
        p = parametricEllipsePoints(x,y,z,r)
        matrixMult(transformMatrix,p)
        for i in range(len(p)):
            addLine(p[i][0],p[i][1],p[i][2],p[i][0],p[i][1],p[i][2])
    ident()

def torus(x,y,z,r,R):
    n = 100
    finalPs = []
    ident()

    for i in range(n):
        roty(360/n)
        p = parametricEllipsePoints(x+R,y,z,r)
        matrixMult(transformMatrix,p)
        for i in range(len(p)):
            addLine(p[i][0],p[i][1],p[i][2],p[i][0],p[i][1],p[i][2])
    ident()

def matrixDraw():
    for i in range(len(lineMatrix)):
        if(i%2==0):
            line(lineMatrix[i][0],lineMatrix[i][1],lineMatrix[i+1][0],lineMatrix[i+1][1],0,0,0)

def matrixClear():
    for i in range(len(lineMatrix)):
        lineMatrix.pop()

def ident():
    transformMatrix[0] = [1,0,0,0]
    transformMatrix[1] = [0,1,0,0]
    transformMatrix[2] = [0,0,1,0]
    transformMatrix[3] = [0,0,0,1]


def rotz(deg):
    rotAngle = deg/180 * math.pi
    rotMatrix = [
    [math.cos(rotAngle),math.sin(rotAngle),0,0],
    [-math.sin(rotAngle),math.cos(rotAngle),0,0],
    [0,0,1,0],
    [0,0,0,1]]
    matrixMult(rotMatrix,transformMatrix)

def roty(deg):
    rotAngle = deg/180 * math.pi
    rotMatrix = [
    [math.cos(rotAngle),0,-math.sin(rotAngle),0],
    [0,1,0,0],
    [math.sin(rotAngle),0,math.cos(rotAngle),0],
    [0,0,0,1]]
    matrixMult(rotMatrix,transformMatrix)

def rotx(deg):
    rotAngle = deg/180 * math.pi
    rotMatrix = [
    [1,0,0,0],
    [0,math.cos(rotAngle),math.sin(rotAngle),0],
    [0,-math.sin(rotAngle),math.cos(rotAngle),0,0],
    [0,0,0,1]]
    matrixMult(rotMatrix,transformMatrix)

def translateMatrix(a,b,c):
    tMatrix = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[a,b,c,1]]
    matrixMult(tMatrix,transformMatrix)

def dilate(x,y,z):
    dMatrix = [[x,0,0,0],[0,y,0,0],[0,0,z,0],[0,0,0,1]]
    matrixMult(dMatrix,transformMatrix)

def applyM():
    matrixMult(transformMatrix,lineMatrix)

def addLine(x1,y1,z1,x2,y2,z2):
    lineMatrix.append([x1,y1,z1,1])
    lineMatrix.append([x2,y2,z2,1])

def box(x,y,z,a,b,c):
    #Near corner
    addLine(x,y,z,x+a,y,z)
    addLine(x,y,z,x,y+b,z)
    addLine(x,y,z,x,y,z+c)

    addLine(x+a,y,z,x+a,y+b,z)
    addLine(x+a,y,z,x+a,y,z+c)
    addLine(x,y+b,z,x+a,y+b,z)
    addLine(x,y+b,z,x,y+b,z+c)
    addLine(x,y,z+c,x,y+b,z+c)
    addLine(x,y,z+c,x+a,y,z+c)
    # addLine(x+a,y,z,x+a,y,z+b)
    # addLine(x,y+b,z,x+a,y+b,z)
    # addLine(x,y+b,z,x,y+b,z+c)
    # addLine(x,y,z+c,x,y+b,z+c)

    #Far corner
    addLine(x+a,y,z+c,x+a,y+b,z+c)
    addLine(x,y+b,z+c,x+a,y+b,z+c)
    addLine(x+a,y+b,z,x+a,y+b,z+c)

def drawlines():
    i = 0
    #print(lineMatrix)
    while(i<len(lineMatrix)):
        #print(lineMatrix[i][0],lineMatrix[i][1],lineMatrix[i+1][0],lineMatrix[i+1][1],0,0,0)
        line(lineMatrix[i][0],lineMatrix[i][1],lineMatrix[i+1][0],lineMatrix[i+1][1],0,0,0)
        i+=2

def display(name):
    drawlines()
    fout = open(name,"w")
    fout.write("P3\n"+str(size)+" "+str(size)+"\n255\n")
    for i in range(size):
        for j in range(size):
            fout.write(str(pixels[j][i][0])+" "+str(pixels[j][i][1])+" "+str(pixels[j][i][2])+" ")
            pixels[j][i]=[255,255,255]
        fout.write("\n")
    print("The image file is "+name)
    fout.close()

def readScript(filename):
    displaycount = 0
    fin = open(filename,"r")
    coms = fin.read()
    coms = coms.split("\n")
    #print(coms)
    while(len(coms)>0):
        #print(len(coms),coms[0])
        #matrixPrint(transformMatrix)
        if(coms[0]=="line"):
            coms[1]=coms[1].split(" ")
            addLine(int(coms[1][0]),int(coms[1][1]),int(coms[1][2]),int(coms[1][3]),int(coms[1][4]),int(coms[1][5]))
            coms.pop(0)
            coms.pop(0)
        elif(coms[0]=="display"):
            display("pic"+str(displaycount)+".ppm")
            displaycount+=1
            coms.pop(0)
        elif(coms[0]=="ident"):
            ident()
            coms.pop(0)
        elif(coms[0]=="scale"):
            coms[1]=coms[1].split(" ")
            dilate(float(coms[1][0]),float(coms[1][1]),float(coms[1][2]))
            coms.pop(0)
            coms.pop(0)
        elif(coms[0]=="move"):
            coms[1]=coms[1].split(" ")
            translateMatrix(int(coms[1][0]),int(coms[1][1]),int(coms[1][2]))
            coms.pop(0)
            coms.pop(0)
        elif(coms[0]=="rotate"):
            coms[1]=coms[1].split(" ")
            if(coms[1][0]=="z"):
                rotz(int(coms[1][1]))
            if(coms[1][0]=="y"):
                roty(int(coms[1][1]))
            if(coms[1][0]=="x"):
                rotx(int(coms[1][1]))
            coms.pop(0)
            coms.pop(0)
        elif(coms[0]=="apply"):
            applyM()
            coms.pop(0)
        elif(coms[0]=="circle"):
            coms[1]=coms[1].split(" ")
            parametricEllipse(int(coms[1][0]),int(coms[1][1]),int(coms[1][2]),int(coms[1][3]))
            coms.pop(0)
            coms.pop(0)
        elif(coms[0]=="hermite"):
            coms[1]=coms[1].split(" ")
            hermite(int(coms[1][0]),int(coms[1][1]),int(coms[1][2]),int(coms[1][3]),int(coms[1][4]),int(coms[1][5]),int(coms[1][6]),int(coms[1][7]))
            coms.pop(0)
            coms.pop(0)
        elif(coms[0]=="bezier"):
            coms[1]=coms[1].split(" ")
            bezier(int(coms[1][0]),int(coms[1][1]),int(coms[1][2]),int(coms[1][3]),int(coms[1][4]),int(coms[1][5]),int(coms[1][6]),int(coms[1][7]))
            coms.pop(0)
            coms.pop(0)
        elif(coms[0]=="sphere"):
            coms[1]=coms[1].split(" ")
            sphere(int(coms[1][0]),int(coms[1][1]),int(coms[1][2]),int(coms[1][3]))
            coms.pop(0)
            coms.pop(0)
        elif(coms[0]=="box"):
            coms[1]=coms[1].split(" ")
            box(int(coms[1][0]),int(coms[1][1]),int(coms[1][2]),int(coms[1][3]),int(coms[1][4]),int(coms[1][5]))
            coms.pop(0)
            coms.pop(0)
        elif(coms[0]=="clear"):
            print(len(lineMatrix))
            matrixClear()
            print(len(lineMatrix))
            coms.pop(0)
        elif(coms[0]=="torus"):
            coms[1]=coms[1].split(" ")
            torus(int(coms[1][0]),int(coms[1][1]),int(coms[1][2]),int(coms[1][3]),int(coms[1][4]))
            coms.pop(0)
            coms.pop(0)
        elif(coms[0]=="save"):

            display(coms[1])

            coms.pop(0)
            coms.pop(0)
            #print(coms)
        else:
            coms.pop(0)

lineMatrix = []
transformMatrix = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]



readScript("script")