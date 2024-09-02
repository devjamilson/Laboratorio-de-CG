# algoritmo/dda.py

def dda(x1, y1, x2, y2, valor, canvas):
    """
    Função que implementa o algoritmo DDA para desenhar uma linha no canvas.

    Args:
        x1, y1 (int): Coordenadas do ponto inicial.
        x2, y2 (int): Coordenadas do ponto final.
        valor (str): Cor da linha.
        canvas (tk.Canvas): Objeto canvas do Tkinter onde a linha será desenhada.
    """
    length = abs(x2 - x1)
    if abs(y2 - y1) > length:
        length = abs(y2 - y1)

    Xinc = (x2 - x1) / length
    Yinc = (y2 - y1) / length

    X = x1
    Y = y1

    set_pixel(round(X), round(Y), valor, canvas)

    for _ in range(int(length)):
        X += Xinc
        Y += Yinc
        set_pixel(round(X), round(Y), valor, canvas)

def set_pixel(x, y, valor, canvas):
    """
    Função para desenhar um pixel no canvas.

    Args:
        x, y (int): Coordenadas do pixel.
        valor (str): Cor do pixel.
        canvas (tk.Canvas): Objeto canvas do Tkinter onde o pixel será desenhado.
    """
    # Ajustar a origem para o centro do canvas
    canvas_width = int(canvas['width']) // 2
    canvas_height = int(canvas['height']) // 2

    # Converter coordenadas cartesianas para coordenadas de canvas
    canvas_x = canvas_width + x
    canvas_y = canvas_height - y

    # Desenha um pequeno ponto (ou quadrado) no canvas
    canvas.create_rectangle(canvas_x, canvas_y, canvas_x + 1, canvas_y + 1, fill=valor)
