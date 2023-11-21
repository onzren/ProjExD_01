import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg")#1
    kk_img = pg.image.load("ex01/fig/3.png")#2
    kk_img = pg.transform.flip(kk_img,True,False)#2
    kk_imgs = [kk_img,pg.transform.rotozoom(kk_img,2,1.0),
               pg.transform.rotozoom(kk_img,4,1.0),
               pg.transform.rotozoom(kk_img,6,1.0),
               pg.transform.rotozoom(kk_img,8,1.0),
               pg.transform.rotozoom(kk_img,10,1.0),
               pg.transform.rotozoom(kk_img,8,1.0),
               pg.transform.rotozoom(kk_img,6,1.0),
               pg.transform.rotozoom(kk_img,4,1.0),
               pg.transform.rotozoom(kk_img,2,1.0),]
    # kk_img1 = [kk_img,pg.transform.rotozoom(kk_img,5,1.0)]
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        x=tmr%1600#6
        screen.blit(bg_img, [-x, 0])#4
        screen.blit(bg_img, [1600-x, 0])#6
        # screen.blit(kk_img1[tmr%2],[300,200])#5
        screen.blit(kk_imgs[tmr%10],[300,200])
        pg.display.update()
        tmr += 1        
        clock.tick(100)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()