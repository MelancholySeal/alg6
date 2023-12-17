#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from random import randint
import matplotlib.pyplot as plt


def visualize_solution(segments, selected_segments):
    plt.xlabel('Координаты')
    plt.ylabel('Отрезки')
    offset1 = 40
    for segment in segments:
        plt.plot(segment, [offset1, offset1], color="blue", linewidth=10, solid_capstyle='butt')
        offset1 -= 10
    offset2 = 50
    for selected_segment in selected_segments:
        plt.plot(selected_segment, [offset2, offset2], color="red", linewidth=10, solid_capstyle='butt')
    ax = plt.gca()
    ax.set_yticks([])


def select_segments_method1(segments):
    solution = []
    while len(segments) > 0:
        min_right = min(x[1] for x in segments)
        min_index = next(i for i in range(len(segments)) if min_right == segments[i][1])
        current_segment = segments[min_index]
        solution.append(current_segment)
        i = 0
        while i < len(segments):
            if segments[i][0] <= current_segment[1]:
                segments.pop(i)
            else:
                i += 1
    return solution


def select_segments_method2(segments):
    segments.sort(key=lambda x: x[1])
    solution = [segments[0]]
    for segment in segments:
        if segment[0] > solution[-1][1]:
            solution.append(segment)
    return solution


if __name__ == '__main__':
    segments = [[a, randint(a+1, 1100)] for a in (randint(0, 1000) for _ in range(20))]
    original_segments = segments.copy()

    plt.figure(1)
    plt.title("обычный алгоритм")
    print("Массив отрезков: ", segments)
    selected_segments_method1 = select_segments_method1(segments)
    segments = original_segments.copy()
    print("\nНепересекающиеся отрезки: ", selected_segments_method1)
    visualize_solution(segments, selected_segments_method1)

    print("\n\t\t-------------------------\t\t\n")
    segments = original_segments.copy()
    plt.figure(2)
    plt.title("улучшенный алгоритм")
    selected_segments_method2 = select_segments_method2(segments)
    print("Массив сортированных отрезков: ", segments)
    print("\nНепересекающиеся сортированные отрезки: ", selected_segments_method2)
    visualize_solution(segments, selected_segments_method2)

    plt.show()
