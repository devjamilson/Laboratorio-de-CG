import math

def draw_point(x, y, valor, canvas):
    """Desenha um ponto no canvas."""
    canvas_width = int(canvas['width']) // 2
    canvas_height = int(canvas['height']) // 2
    canvas_x = canvas_width + x
    canvas_y = canvas_height - y
    canvas.create_rectangle(canvas_x, canvas_y, canvas_x + 1, canvas_y + 1, fill=valor)

def midpoint_ellipse(a, b, x_center, y_center, valor, canvas):
    """Desenha uma elipse usando o algoritmo do ponto médio."""
    x = 0
    y = b
    a_squared = a * a
    b_squared = b * b
    a_squared_2 = 2 * a_squared
    b_squared_2 = 2 * b_squared
    x_squared = x * x
    y_squared = y * y
    d1 = b_squared - (a_squared * b) + (0.25 * a_squared)
    dx = b_squared_2 * x
    dy = a_squared_2 * y

    # Desenha os pontos iniciais
    draw_ellipse_points(x_center, y_center, x, y, valor, canvas)

    # Região 1
    while dx < dy:
        x += 1
        x_squared += b_squared
        dx += b_squared_2
        if d1 < 0:
            d1 += dx + b_squared
        else:
            y -= 1
            y_squared -= a_squared
            dy -= a_squared_2
            d1 += dx - dy + b_squared
        draw_ellipse_points(x_center, y_center, x, y, valor, canvas)

    # Região 2
    d2 = b_squared * (x + 0.5) * (x + 0.5) + a_squared * (y - 1) * (y - 1) - a_squared * b_squared
    while y >= 0:
        y -= 1
        y_squared -= a_squared
        dy -= a_squared_2
        if d2 > 0:
            d2 += a_squared - dy
        else:
            x += 1
            x_squared += b_squared
            dx += b_squared_2
            d2 += a_squared - dx + dy
        draw_ellipse_points(x_center, y_center, x, y, valor, canvas)

def draw_ellipse_points(x_center, y_center, x, y, valor, canvas):
    """Desenha os pontos simétricos da elipse para o ponto (x, y)."""
    draw_point(x_center + x, y_center + y, valor, canvas)  # Quadrante I
    draw_point(x_center - x, y_center + y, valor, canvas)  # Quadrante II
    draw_point(x_center + x, y_center - y, valor, canvas)  # Quadrante III
    draw_point(x_center - x, y_center - y, valor, canvas)  # Quadrante IV
