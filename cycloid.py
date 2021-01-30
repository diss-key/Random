from turtle import *
from math import sin, radians



def draw(P,M) :
    colormode(255)
    

    R, G, B = 1, 0, 0
    r,g,b = 0, 0, 0
    T = Turtle()
    T.up()
    T.sety(-120)
    T.down()
    i = 360/P
    c = 0
    # while c<P:
    #     # T.dot(2, "pink")
    #     T.circle(200, i)
    #     c+=1
    T.circle(200)
    k = 0
    T.speed(10)
    colormode(255)
    step= 255//(P//2//3)
    while True:
        if k<(P//3):
            r+=step
            if r>=255:
                r=0
        elif (P//3)<=k<(2*(P//3)):
            r,b=0,0
            g+= step
            if g>=255:
                g=0
        else:
            r,g=0,0
            b+=step
            if b>=255:
                b=0
        


        print(r,g,b)
        T.pencolor(r,g,b)
        nexz = (k*M)%P
        angle = abs((nexz-k))*i
        dist = 2*200*sin(radians(angle//2))
        
        if nexz < k:
            T.left(180)
            T.right(angle//2)            
            T.forward(dist)
            T.back(dist)
            T.left(angle//2)
            T.right(180)
        else:
            T.left(angle//2)            
            T.forward(dist)
            T.back(dist)
            T.right(angle//2)
        T.up()
        T.circle(200, i)
        T.down()

        k+=1
        k %= P

    done()    

if __name__ == "__main__":
    draw(200, 6)