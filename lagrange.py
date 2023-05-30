from matplotlib import pyplot as plt


def draw_picture(x_list, y_list, node, name):
    plt.title(f"newton-{name}")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.plot(x_list, y_list, color="red")
    for i in range(len(x_list)):
        plt.scatter(x_list[i], y_list[i], color="purple", linewidths=2)
    plt.scatter(node[0], node[1], color="blue", linewidth=2)
    plt.show()


def lagrange_interpolation(x, y, x_interp):
    n = len(x)
    if n != len(y):
        raise ValueError("Input arrays must have the same length.")
    res = 0.0
    for i in range(n):
        num, den = 1.0, 1.0
        for j in range(n):
            if i != j:
                num *= (x_interp - x[j])
                den *= (x[i] - x[j])
        res += y[i] * num / den
    return res


def func(x):
    return x ** 3


if __name__ == "__main__":
    c, d = int(input("Enter c (start number): ")), int(input("Enter d (end number): "))

    # Example usage
    x = [i for i in range(c, d)]
    y = [func(i) for i in x]

    for i in x:
        print(f"Истинное значение для функции для x = {i}: {func(i)}")
        interp_val = lagrange_interpolation(x, y, i)
        print(f"Интерполяция Лагранжа для x = {i}: {interp_val}\n")

        draw_picture(x, y, (i, interp_val), "lagrange")
