import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg")#1
    kk_img = pg.image.load("ex01/fig/3.png")#2
    kk_img = pg.transform.flip(kk_img,True,False)#2
    bg_img1 = pg.transform.flip(bg_img,True,False)
    kk_imgs = [pg.transform.rotozoom(kk_img,i,1.0)for i in range(11)]#ex1
    cnt=[0,1,2,3,4,5,6,7,8,9,10,9,8,7,6,5,4,3,2,1]#ex1
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        x=tmr%3200#6
        screen.blit(bg_img, [-x, 0])#4
        screen.blit(bg_img1, [1600-x, 0])#ex2
        screen.blit(bg_img, [3200-x, 0])#ex2
        screen.blit(kk_imgs[cnt[tmr%20]],[300,200])#ex1
        pg.display.update()
        tmr += 1        
        clock.tick(100)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()