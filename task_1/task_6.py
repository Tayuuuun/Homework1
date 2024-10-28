def main():
    x, y = 0, 0
    n = int(input("Введите количество ходов: "))
    for i in range(n):
        # Считываем количество шагов и направление
        steps, direction = input("Введите количество шагов и направление (вверх, вниз, влево, вправо): ").split()

        steps = int(steps)

        if direction == "вправо":
            x += steps
        elif direction == "влево":
            x -= steps
        elif direction == "вверх":
            y += steps
        elif direction == "вниз":
            y -= steps
        else:
            print("Некорректное направление.")

    shortest_distance = abs(x) + abs(y)
    print(f"Кратчайшее расстояние от начальной точки: {shortest_distance}")


if __name__ == "__main__":
    main()

