# bresenham.py

def bresenham(x0, y0, xEnd, yEnd, valor, canvas):
    dx = abs(xEnd - x0)
    dy = abs(yEnd - y0)
    p = 2 * dy - dx
    twoDy = 2 * dy
    twoDyMinusDx = 2 * (dy - dx)
    
    if x0 > xEnd:
        x, y = xEnd, yEnd
        xEnd = x0
    else:
        x, y = x0, y0

    set_pixel(x, y, valor, canvas)

    while x < xEnd:
        x += 1
        if p < 0:
            p += twoDy
        else:
            y += 1
            p += twoDyMinusDx

        set_pixel(x, y, valor, canvas)

def set_pixel(x, y, valor, canvas):
    # Ajustar a origem para o centro do canvas
    canvas_width = int(canvas['width']) // 2
    canvas_height = int(canvas['height']) // 2

    # Converter coordenadas cartesianas para coordenadas de canvas
    canvas_x = canvas_width + x
    canvas_y = canvas_height - y

    # Desenha um pequeno ponto (ou quadrado) no canvas
    canvas.create_rectangle(canvas_x, canvas_y, canvas_x + 1, canvas_y + 1, fill=valor)
