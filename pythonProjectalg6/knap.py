#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches


def solve_fractional_knapsack(items, capacity):
    items.sort(key=lambda x: x[1] / x[2], reverse=True)
    selected_items = {}
    total_value = 0
    total_weight = 0

    for item in items:
        remaining_capacity = capacity - total_weight
        if remaining_capacity / item[2] > 1:
            selected_items[item[0]] = item[2]
            total_weight += item[2]
            total_value += item[1]
        else:
            selected_items[item[0]] = remaining_capacity
            total_value += item[1] / item[2] * remaining_capacity
            break

    return selected_items, total_value


if __name__ == '__main__':
    num_items = 10
    items_list = [[i, random.randint(1, 100), random.randint(3, 20)]
                  for i in range(num_items)]
    backpack_capacity = 30

    print("│ {:^10} │ {:^10} │ {:^10} │".format('Элемент', 'Стоимость', 'Вес'))
    for item in items_list:
        print("├{:^12}┼{:^12}┼{:^12}┤".format('', '', ''))
        print("│ {:^10} │ {:^10} │ {:^10} │".format(*item))

    selected_items, total_value = solve_fractional_knapsack(items_list, backpack_capacity)

    print("\nРешение:")
    for item, weight in selected_items.items():
        print("Элемент", item, "был взят весом", weight)
    print("Стоимость рюкзака = ", total_value)

    fig, ax = plt.subplots()

    ax.add_patch(patches.Rectangle((0, -0.5), backpack_capacity, 1, facecolor='gray'))

    x_position = 0
    y_position = 0.5

    text_properties = {'verticalalignment': 'center', 'horizontalalignment': 'center'}

    for item, value, weight in items_list:
        if item in selected_items:
            ax.add_patch(patches.Rectangle((x_position, y_position), weight, 1))
            ax.text(x_position + weight / 2, 1, str(value), **text_properties)
            if selected_items[item] == weight:
                ax.text(x_position + weight / 2, -0.5, str(selected_items[item]), **text_properties)
                ax.text(x_position + weight / 2, 0, str(value), **text_properties)
            else:
                ax.text((backpack_capacity + x_position) / 2, -0.5, str(selected_items[item]), **text_properties)
                ax.text((backpack_capacity + x_position) / 2, 0,
                        f"{value / weight * selected_items[item]:.2f}", **text_properties)

            ax.text(x_position + weight / 2, 2, str(item), **text_properties)
            ax.text(x_position + weight / 2, 1.5, str(weight), **text_properties)
            if x_position > 0:
                ax.axvline(x=x_position, ymin=0, ymax=2, color='red')
            x_position += weight

    ax.text(-10, 2, "Элементы", **text_properties)
    ax.text(-10, 1.5, "Вес", **text_properties)
    ax.text(-10, 1, "Цена", **text_properties)
    ax.text(-10, 0, "Цена в рюкзаке", **text_properties)
    ax.text(-10, -0.5, "Вес в рюкзаке", **text_properties)
    plt.xlim(-8, x_position)
    plt.ylim(-1, 2)

    ax.axis('off')

    plt.show()
