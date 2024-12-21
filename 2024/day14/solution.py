from functools import reduce
import re
import pygame

with open("input.txt") as file:
    robots = [[int(n) for n in re.findall(r"(-*\d+)", line)] for line in file.readlines()]

xSize = 101
ySize = 103

def part1():
    
    for _ in range(100):

        for robot in robots:
            x, y, vx, vy = robot

            robot[0] = (x + vx) % xSize
            robot[1] = (y + vy) % ySize

    totals = [0, 0, 0, 0]

    mx, my = xSize // 2, ySize // 2
    for robot in robots:
        x, y, _, _ = robot

        if x == mx or y == my:
            continue
        
        quad = 1 if x > mx else 0
        quad <<= 1
        quad += 1 if y > my else 0

        totals[quad] += 1

    print(totals)
    print(reduce(lambda x, y: x * y, totals))


def part2():
    # pygame setup
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    running = True
    dt = 0

    mx, my = xSize // 2, ySize // 2

    sizeScale = 4
    robotCount = len(robots)
    seconds = 0
    pygame.font.init()
    font = pygame.font.SysFont("Comic Sans MS", 30)
    paused = False
    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    paused = False

        # fill the screen with a color to wipe away anything from last frame
        if not paused:
            screen.fill("white")

        nearCount = 0
        for robot in robots:
            x, y, vx, vy = robot

            if not paused:

                robot[0] = nx = (x + vx) % xSize
                robot[1] = ny = (y + vy) % ySize

            r = pygame.Vector2(nx * sizeScale, ny * sizeScale)
            pygame.draw.circle(screen, "green", r, sizeScale)

            nearCenter = mx - 20 < nx < mx + 20
            nearCount += nearCenter

        if not paused:
            seconds += 1

        if nearCount >= robotCount // 2 and seconds not in tried:
            paused = True
        
        text = font.render(f"{seconds} seconds", False, (0, 0, 0))
        screen.blit(text, (600, 600))

        # flip() the display to put your work on screen
        pygame.display.flip()

        # limits FPS to 60
        # dt is delta time in seconds since last frame, used for framerate-
        # independent physics.
        clock.tick(1000)

    pygame.quit()

part2()