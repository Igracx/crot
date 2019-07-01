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
def get_center_color():
    return (np.random.randint(0, 255), np.random.randint(0, 255), np.random.randint(0, 255))

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

centers = [[(290, 20), get_center_color()]]
for i in range(11):
    rotated_coordinates = rotate(centers[i][0], (300, 300), np.pi/6, 1)
    next_center = [(rotated_coordinates[0], rotated_coordinates[1]), get_center_color()]
    centers.append(next_center)

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

    for i in range(len(centers)):
        centers[i][0] = rotate(centers[i][0], (300, 300), 0.001, 1)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.fill((0, 0, 0))
    for center in centers:
        pygame.draw.circle(screen, center[1], 
                           (int(center[0][0]), int(center[0][1])), 20)
    pygame.display.flip()