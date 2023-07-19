import pygame
from pyvidplayer2 import VideoCollection

PATH1 = "demos\\vids\\vid.mp4"
PATH2 = "demos\\vids\\ep2.mp4"

win = pygame.display.set_mode((1066, 744))
pygame.display.set_caption("parallel video v demo")
clock = pygame.time.Clock()

v = VideoCollection()

v.add_video(PATH2, (0, 0, 426, 240))
v.add_video(PATH1, (426, 0, 256, 144))
v.add_video(PATH2, (682, 0, 256, 144))
v.add_video(PATH2, (426, 144, 640, 360))
v.add_video(PATH1, (0, 240, 256, 144))
v.add_video(PATH2, (0, 384, 426, 240))
v.add_video(PATH1, (426, 504, 426, 240))

v.play()

while True:
    key = None
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            v.close()
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            key = pygame.key.name(event.key)
    
    clock.tick(60)
    
    win.fill("black")
    v.draw(win)

    pygame.display.update()