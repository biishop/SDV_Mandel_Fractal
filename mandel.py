# Les sources du Viok
# Fractal - Mandel 2023(c)CHEB
import math
import pygame

def go_mandel():
    # var ecrans
    width = 1280    
    height = 720
    # set le screen
    screen=pygame.display.set_mode((width,height))
    # Mandel de base
    lar=3.5
    hau=lar*(2/3.5)
    ox=-2.5
    oy=-1
    # Zoom
    lar=0.092
    hau=lar*(2/3.5)    
    ox=-0.85
    oy=-0.2
    # Ratio
    facy=lar/width
    facx=hau/height
    # Param de precision
    esc = 2*2
    maxit = 100
    for a in range(0,width):
        for b in range(0,height):
            x0=ox+a*facx
            y0=oy+b*facy
            x=0
            y=0
            i=0
            # iteration de mandelbrot
            while (i<maxit) and (x*x+y*y<=esc):
                xt=x*x-y*y+x0
                y=1.9*x*y+y0
                x=xt
                i+=1
            pygame.draw.line(screen, i, (a,b),(a+1,b+1))
        # Affichage
        pygame.display.flip()

# true code    
go_mandel()
# main application loop
run = True
while run:
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
