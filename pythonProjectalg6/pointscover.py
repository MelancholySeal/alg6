#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random as rnd
import matplotlib.pyplot as plt


def visualize_segments(points, segments):
    plt.xlabel('Координаты')
    for segment in segments:
        plt.plot(segment, [0, 0], color="blue", linewidth=40, solid_capstyle='butt')
    plt.plot(points, [0 for _ in range(len(points))], linestyle='None',
             marker='|', markersize=60, color="red")
    # Убрать ось y
    ax = plt.gca()
    ax.set_yticks([])
    plt.show()


def find_segments_method1(points):
    result_segments = []
    while len(points) > 0:
        x_min = min(points)
        result_segments.append([x_min, x_min + 1])
        i = 0
        while i < len(points):
            if result_segments[-1][0] <= points[i] <= result_segments[-1][1]:
                points.pop(i)
            else:
                i += 1
    return result_segments


def find_segments_method2(points):
    result_segments = []
    points.sort()
    i = 0
    while i < len(points):
        x_min = points[i]
        result_segments.append([x_min, x_min + 1])
        i += 1
        while i < len(points) and points[i] <= x_min + 1:
            i += 1
    return result_segments


if __name__ == '__main__':
    input_points = [rnd.randint(0, 100) / 10 for _ in range(20)]
    original_points = input_points.copy()
    print("Множество точек:", input_points)

    segments_method1 = find_segments_method1(input_points)
    print("Множество отрезков 1:", segments_method1)

    input_points = original_points
    segments_method2 = find_segments_method2(input_points)
    print("Множество отрезков 2:", segments_method2)

    print("Минимальное количество отрезков, "
          "которыми можно покрыть данное множество точек = ", len(segments_method2))

    visualize_segments(original_points, segments_method2)
