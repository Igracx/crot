import pygame
import numpy as np

def transx(x, koordinates_of_O):
    return x - koordinates_of_O[0]

def transy(y, koordinates_of_O):
    return -y + koordinates_of_O[1]

def revers_transx(X, koordinates_of_O):
    return X + koordinates_of_O[0]

def reverse_transy(Y, koordinates_of_O):
    return -Y  + koordinates_of_O[1]

def multyply_complex_numbers(Z1, Z2):
    x = Z1[0] * Z2[0] * (Z1[1] * Z2[1] - Z1[2] * Z2[2])
    y = Z1[0] * Z2[0] * (Z1[2] * Z2[1] + Z1[1] * Z2[2])
    return (x, y)

def rotate(coordinates, center_of_rotation, angle_in_radians, r):
    translated_coordinates = (transx(coordinates[0], center_of_rotation), 
                              transy(coordinates[1], center_of_rotation))
    Z1 = (1, translated_coordinates[0], translated_coordinates[1])
    Z2 = (r, np.cos(angle_in_radians), np.sin(angle_in_radians))
    translated_rotated_coordinates = multyply_complex_numbers(Z1, Z2)
    rotated_coordinates = (revers_transx(translated_rotated_coordinates[0], center_of_rotation),
                           reverse_transy(translated_rotated_coordinates[1], center_of_rotation))
    return rotated_coordinates


pygame.init()
screen = pygame.display.set_mode((600, 600))

center1 = (290, 20)
center2 = (290, 580)

r1 = 0.9985
r2 = 1 / 0.9985
r = r1
iter_cnt = 2000
curr_iter = 1

done = False
while not done:
    if curr_iter == iter_cnt:
        curr_iter = 1
        if r == r1: 
            r = r2
        else:
            r = r1
    curr_iter += 1
    center1 = rotate(center1, (300, 300), 0.01, r)
    center2 = rotate(center2, (300, 300), 0.01, r)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, (0, 0, 255), (int(center1[0]), int(center1[1])), 20)
    pygame.draw.circle(screen, (255, 0, 0), (int(center2[0]), int(center2[1])), 20)
    pygame.display.flip()