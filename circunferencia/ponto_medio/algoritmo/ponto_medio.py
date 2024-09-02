import math

def draw_point(x, y, valor, canvas):
    """Desenha um ponto no canvas."""
    canvas_width = int(canvas['width']) // 2
    canvas_height = int(canvas['height']) // 2
    canvas_x = canvas_width + x
    canvas_y = canvas_height - y
    canvas.create_rectangle(canvas_x, canvas_y, canvas_x + 1, canvas_y + 1, fill=valor)

def midpoint_circle(raio, x_center, y_center, valor, canvas):
    """Desenha uma circunferência usando o algoritmo do ponto médio."""
    x = 0
    y = raio
    d = 1 - raio  # Ponto inicial do círculo
    
    # Desenha os pontos nos octantes
    draw_circle_points(x_center, y_center, x, y, valor, canvas)
    
    while x < y:
        if d < 0:
            d += 2 * x + 3
        else:
            d += 2 * (x - y) + 5
            y -= 1
        x += 1
        draw_circle_points(x_center, y_center, x, y, valor, canvas)

def draw_circle_points(x_center, y_center, x, y, valor, canvas):
    """Desenha os pontos simétricos da circunferência para o ponto (x, y)."""
    draw_point(x_center + x, y_center + y, valor, canvas)  # Octante E
    draw_point(x_center - x, y_center + y, valor, canvas)  # Octante W
    draw_point(x_center + x, y_center - y, valor, canvas)  # Octante S
    draw_point(x_center - x, y_center - y, valor, canvas)  # Octante N
    draw_point(x_center + y, y_center + x, valor, canvas)  # Octante NE
    draw_point(x_center - y, y_center + x, valor, canvas)  # Octante NW
    draw_point(x_center + y, y_center - x, valor, canvas)  # Octante SE
    draw_point(x_center - y, y_center - x, valor, canvas)  # Octante SW
