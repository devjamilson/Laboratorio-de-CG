def draw_point(x, y, valor, canvas):
    """Desenha um ponto no canvas."""
    canvas.create_rectangle(x, y, x + 1, y + 1, fill=valor)


def draw_ellipse_points(x_center, y_center, x, y, valor, canvas):
    """Desenha os pontos simétricos da elipse para o ponto (x, y)."""
    draw_point(x_center + x, y_center + y, valor, canvas)  # Quadrante I
    draw_point(x_center - x, y_center + y, valor, canvas)  # Quadrante II
    draw_point(x_center + x, y_center - y, valor, canvas)  # Quadrante III
    draw_point(x_center - x, y_center - y, valor, canvas)  # Quadrante IV


def midpoint_ellipse(a, b, x_center, y_center, valor, canvas):
    """Desenha uma elipse usando o algoritmo do ponto médio."""
    x = 0
    y = b
    a_squared = a * a
    b_squared = b * b
    a_squared_2 = 2 * a_squared
    b_squared_2 = 2 * b_squared
    d1 = b_squared - (a_squared * b) + (0.25 * a_squared)
    dx = b_squared_2 * x
    dy = a_squared_2 * y

    # Região 1
    while dx < dy:
        draw_ellipse_points(x_center, y_center, x, y, valor, canvas)
        if d1 < 0:
            x += 1
            dx += b_squared_2
            d1 += dx + b_squared
        else:
            x += 1
            y -= 1
            dx += b_squared_2
            dy -= a_squared_2
            d1 += dx - dy + b_squared

    # Região 2
    d2 = b_squared * (x + 0.5) * (x + 0.5) + a_squared * (y - 1) * (y - 1) - a_squared * b_squared
    while y >= 0:
        draw_ellipse_points(x_center, y_center, x, y, valor, canvas)
        if d2 > 0:
            y -= 1
            dy -= a_squared_2
            d2 += a_squared - dy
        else:
            y -= 1
            x += 1
            dx += b_squared_2
            dy -= a_squared_2
            d2 += dx - dy + a_squared