# algoritmo/trigonometrico.py
import math

def draw_circle_points_trig(x_center, y_center, raio, valor, canvas):
    # Ajustar a origem para o centro do canvas
    canvas_width = int(canvas['width']) // 2
    canvas_height = int(canvas['height']) // 2

    # Converter coordenadas cartesianas para coordenadas do canvas
    canvas_x_center = canvas_width + x_center
    canvas_y_center = canvas_height - y_center

    # Desenhar o círculo usando trigonometria
    for angle in range(0, 360):
        radian = math.radians(angle)
        x = int(raio * math.cos(radian))
        y = int(raio * math.sin(radian))
        px, py = canvas_x_center + x, canvas_y_center - y
        canvas.create_rectangle(px, py, px + 1, py + 1, fill=valor)
