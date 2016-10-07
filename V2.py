# Rubik's Cube V2

# This version allows interaction with the cube.

import pygame
import sys
import time
import math
from pygame.locals import *


class Cube:
    dimensions = 3

    def __init__(self, vertex):
        self.edge_length = 200
        self.vertex = vertex

        # distance_a is the distance in the plane to the nearest set of vertices which is equivalent to the
        # horizontal distance to the further corners
        distance_a = math.sqrt((2 / 3.0) * self.edge_length ** 2)

        self.center_vertex = vertex
        self.top_vertex = [vertex[0], vertex[1] - distance_a]
        self.top_right_vertex = [vertex[0] + distance_a * math.cos(math.pi / 6),
                                 vertex[1] - distance_a * math.sin(math.pi / 6)]
        self.bottom_right_vertex = [vertex[0] + distance_a * math.cos(math.pi / 6),
                                    vertex[1] + distance_a * math.sin(math.pi / 6)]
        self.bottom_vertex = [vertex[0], vertex[1] + distance_a]
        self.bottom_left_vertex = [vertex[0] - distance_a * math.cos(math.pi / 6),
                                   vertex[1] + distance_a * math.sin(math.pi / 6)]
        self.top_left_vertex = [vertex[0] - distance_a * math.cos(math.pi / 6),
                                vertex[1] - distance_a * math.sin(math.pi / 6)]

        self.white = Side(pygame.Color('white'), Cube.dimensions)
        self.yellow = Side(pygame.Color('yellow'), Cube.dimensions)
        self.blue = Side(pygame.Color('blue'), Cube.dimensions)
        self.green = Side(pygame.Color('green'), Cube.dimensions)
        self.red = Side(pygame.Color('red'), Cube.dimensions)
        self.orange = Side(pygame.Color(255, 130, 0), Cube.dimensions)

        self.sides = [self.white, self.yellow, self.blue, self.green, self.red, self.orange]

        self.top = self.white
        self.left = self.red
        self.right = self.blue
        self.bottom = self.yellow
        self.back_left = self.green
        self.back_right = self.orange

    def draw(self, surface):
        self.top.draw(surface, self.top_vertex, self.top_right_vertex, self.center_vertex, self.top_left_vertex)
        self.left.draw(surface, self.top_left_vertex, self.center_vertex, self.bottom_vertex, self.bottom_left_vertex)
        self.right.draw(surface, self.top_right_vertex, self.bottom_right_vertex, self.bottom_vertex, self.center_vertex)

    def rotate_cube_up_left(self):
        temp = self.top
        self.top = self.right
        self.right = self.bottom
        self.bottom = self.back_left
        self.back_left = temp

    def rotate_cube_up_right(self):
        temp = self.top
        self.top = self.left
        self.left = self.bottom
        self.bottom = self.back_right
        self.back_right = temp

    def rotate_cube_down_left(self):
        temp = self.top
        self.top = self.back_right
        self.back_right = self.bottom
        self.bottom = self.left
        self.left = temp

    def rotate_cube_down_right(self):
        temp = self.top
        self.top = self.back_left
        self.back_left = self.bottom
        self.bottom = self.right #
        self.right = temp

    def rotate_cube_left(self):
        temp = self.right
        self.right = self.back_right
        self.back_right = self.back_left
        self.back_left = self.left  #
        self.left = temp

    def rotate_cube_right(self):
        temp = self.left
        self.left = self.back_left
        self.back_left = self.back_right
        self.back_right = self.right  #
        self.right = temp

    def set_edge_length(self, length=False, increase=False):
        if length:
            self.edge_length = length
        elif increase:
            self.edge_length += increase
        distance_a = math.sqrt((2 / 3.0) * self.edge_length ** 2)
        self.center_vertex = self.vertex
        self.top_vertex = [self.vertex[0], self.vertex[1] - distance_a]
        self.top_right_vertex = [self.vertex[0] + distance_a * math.cos(math.pi / 6),
                                 self.vertex[1] - distance_a * math.sin(math.pi / 6)]
        self.bottom_right_vertex = [self.vertex[0] + distance_a * math.cos(math.pi / 6),
                                    self.vertex[1] + distance_a * math.sin(math.pi / 6)]
        self.bottom_vertex = [self.vertex[0], self.vertex[1] + distance_a]
        self.bottom_left_vertex = [self.vertex[0] - distance_a * math.cos(math.pi / 6),
                                   self.vertex[1] + distance_a * math.sin(math.pi / 6)]
        self.top_left_vertex = [self.vertex[0] - distance_a * math.cos(math.pi / 6),
                                self.vertex[1] - distance_a * math.sin(math.pi / 6)]

    def rotate_top(self, clockwise):
        if clockwise


class Side:
    def __init__(self, colour, dimensions):
        self.colour = colour  # of center piece
        self.dimensions = dimensions

        # Makes a 2D list of colours of stickers. self.side[row(up downwards)][column(left to right]
        self.side = [[Sticker(colour), Sticker(colour), Sticker(colour)],
                     [Sticker(colour), Sticker(colour), Sticker(colour)],
                     [Sticker(colour), Sticker(colour), Sticker(colour)]]

    def draw(self, surface, top_left_vertex, top_right_vertex, bottom_right_vertex, bottom_left_vertex):

        # horizontal distance from one sticker vertex to the one on its right
        x = int((top_right_vertex[0] - top_left_vertex[0]) / self.dimensions)

        # vertical distance from one sticker vertex to the one below
        y = int((bottom_left_vertex[1] - top_left_vertex[1]) / self.dimensions)

        # horizontal distance from one sticker to the one below
        cross = int((bottom_left_vertex[0] - top_left_vertex[0]) / self.dimensions)

        # vertical distance from one sticker vertex to the one on its right
        rise = int((top_right_vertex[1] - top_left_vertex[1]) / self.dimensions)

        vertices = [[(top_left_vertex[0], top_left_vertex[1]),
                     (top_left_vertex[0] + x, top_left_vertex[1] + rise),
                     (top_left_vertex[0] + 2 * x, top_left_vertex[1] + 2 * rise),
                     (top_right_vertex[0], top_right_vertex[1])],

                    [(top_left_vertex[0] + cross, top_left_vertex[1] + y),
                     (top_left_vertex[0] + x + cross, top_left_vertex[1] + y + rise),
                     (top_left_vertex[0] + 2 * x + cross, top_left_vertex[1] + y + 2 * rise),
                     (top_right_vertex[0] + cross, top_right_vertex[1] + y)],

                    [(top_left_vertex[0] + 2 * cross, top_left_vertex[1] + 2 * y),
                     (top_left_vertex[0] + x + 2 * cross, top_left_vertex[1] + 2 * y + rise),
                     (top_left_vertex[0] + 2 * x + 2 * cross, top_left_vertex[1] + 2 * y + 2 * rise),
                     (top_right_vertex[0] + 2 * cross, top_right_vertex[1] + 2 * y)],

                    [bottom_left_vertex,
                     (bottom_left_vertex[0] + x, bottom_left_vertex[1] + rise),
                     (bottom_left_vertex[0] + 2 * x, bottom_left_vertex[1] + 2 * rise),
                     bottom_right_vertex]]

        for rowInd in range(3):
            for colInd in range(3):
                self.side[rowInd][colInd].draw(surface,
                                               [vertices[rowInd][colInd], vertices[rowInd][colInd + 1],
                                                vertices[rowInd + 1][colInd + 1], vertices[rowInd + 1][colInd]]
                                               )


class Sticker:

    border_width = 5

    def __init__(self, colour):
        self.colour = colour

    def draw(self, surface, vertices):
        pygame.draw.polygon(surface, self.colour, vertices)
        pygame.draw.polygon(surface, pygame.Color('black'), vertices, Sticker.border_width)


# User-defined functions


def main():
    pygame.init()

    window_title = "Rubik's Cube"
    frame_delay = 0.2  # smaller is faster game
    pygame.display.set_caption(window_title)
    surface_size = (800, 600)
    surface = pygame.display.set_mode(surface_size, 0, 0)

    cube = Cube([400, 300]) # Creates the Rubik's Cube

    while True:
        # Handle events
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == pygame.K_KP7:
                    cube.rotate_cube_up_left()
                elif event.key == pygame.K_KP1:
                    cube.rotate_cube_down_left()
                elif event.key == pygame.K_KP9:
                    cube.rotate_cube_up_right()
                elif event.key == pygame.K_KP3:
                    cube.rotate_cube_down_right()
                elif event.key == pygame.K_KP4:
                    cube.rotate_cube_left()
                elif event.key == pygame.K_KP6:
                    cube.rotate_cube_right()
                elif event.key == pygame.K_KP8:
                    cube.set_edge_length(increase=2)
                elif event.key == pygame.K_KP2:
                    cube.set_edge_length(increase=-2)

        # Update and draw objects for the frame
        surface.fill(pygame.Color('light gray'))
        cube.draw(surface)
        pygame.display.update()
        time.sleep(frame_delay)

main()
