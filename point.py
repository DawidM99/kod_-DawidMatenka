# -*- coding: utf-8 -*-
import math


def normalize_angle(angle):
    if angle >= 0:
        return angle
    else:
        return 400 + angle


def radians_to_grads(angle_in_radians):
    return angle_in_radians * (200/math.pi)


class Point(object):

    def __init__(self, name, x, y, z=0):
        self.name = name
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f'Point(nr="{self.name}", x={self.x}, y={self.y}, z={self.z})'

    def get_length(self, other, _3d=False):
        if not _3d:
            # długość 2d
            return ((other.x - self.x) ** 2 + (other.y - self.y) ** 2) ** 0.5
        else:
            # długość 3d
            return ((other.x - self.x) ** 2 + (other.y - self.y) ** 2 + (other.z - self.z) ** 2) ** 0.5

    def get_azimuth(self, other):
        delta_x = other.x - self.x
        delta_y = other.y - self.y
        angle = radians_to_grads(math.atan2(delta_y, delta_x))
        return normalize_angle(angle)

    def get_angle(self, left, right):
        azimuth_left = self.get_azimuth(left)
        azimuth_right = self.get_azimuth(right)
        angle = azimuth_right - azimuth_left
        return normalize_angle(angle)

    def get_dlugosc(self, other):
        return((other.x - self.x) ** 2 + (other.y - self.y) ** 2) ** 0,5

    def get_azymut(self, other):
        delta_x = other.x - self.x
        delta_y = other.y - self.y
        angle = radians_to_grads(math.atan2(delta_y, delta_x))
        return normalize_angle(angle)

    def get_kat(self, left, right):
        azimuth_left = self.get_azimuth(left)
        azimuth_right = self.get_azimuth(right)
        angle = azimuth_right - azimuth_left
        return normalize_angle(angle)



