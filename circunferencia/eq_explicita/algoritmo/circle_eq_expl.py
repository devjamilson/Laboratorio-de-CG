# algoritmo/dda.py
import math

def draw_point(x, y, valor, canvas):
    """Desenha um ponto no canvas."""
    canvas_width = int(canvas['width']) // 2
    canvas_height = int(canvas['height']) // 2
    canvas_x = canvas_width + x
    canvas_y = canvas_height - y
    canvas.create_rectangle(canvas_x, canvas_y, canvas_x + 1, canvas_y + 1, fill=valor)

def explicit_circle(raio, x_center, y_center, valor, canvas):
    """Desenha uma circunferência usando a equação explícita x^2 + y^2 = r^2."""
    for x in range(-raio, raio + 1):
        y = int(math.sqrt(raio**2 - x**2))
        draw_point(x_center + x, y_center + y, valor, canvas)  # Ponto superior
        draw_point(x_center + x, y_center - y, valor, canvas)  # Ponto inferior
