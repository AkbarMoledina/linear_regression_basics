# -*- coding: utf-8 -*-
"""
Created on Sun Jan 20 19:46:20 2019

@author: akbar
"""

def get_y(m, b, x):
  y = (m * x) + b
  return y


def calculate_error(m, b, point):
    x_point = point[0]
    y_point = point[1]
    y_value = get_y(m, b, x_point)
    distance = abs(y_value - y_point)
    return distance


def calculate_all_error(m, b, points):
    distances = 0
    for point in points:
        error = calculate_error(m, b, point)
        distances += error
    return distances


def calculate_smallest_error(m_range, b_range, points):
    smallest_error = float("inf")
    best_m = 0
    best_b = 0
    for m in m_range:
        for b in b_range:
            distances = calculate_all_error(m, b, points)
            if distances < smallest_error:
                smallest_error = distances
                best_m, best_b = m, b
    return best_m, best_b, smallest_error
            

possible_as = [a * 0.1 for a in range(-100, 100)]
possible_ms = [m * 0.1 for m in range(-100, 100)]
possible_bs = [b * 0.1 for b in range(-200, 200)]

datapoints = [(1, 2), (2, 0), (3, 4), (4, 4), (5, 3)]
best_m, best_b, smallest_error = calculate_smallest_error(possible_ms, possible_bs, datapoints)
print(best_m, best_b, smallest_error)

print(get_y(best_m, best_b, 6))
