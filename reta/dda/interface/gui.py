# interface/gui.py
import tkinter as tk
from algoritmo.dda import dda

# Função para capturar os valores dos inputs e desenhar a linha
def plot_line(canvas, entry_x1, entry_y1, entry_x2, entry_y2, entry_color):
    x1 = int(entry_x1.get())
    y1 = int(entry_y1.get())
    x2 = int(entry_x2.get())
    y2 = int(entry_y2.get())
    valor = entry_color.get()
    
    # Limpar o canvas antes de desenhar a nova linha
    canvas.delete("all")
    
    # Desenhar eixos x e y
    canvas_width = int(canvas['width'])
    canvas_height = int(canvas['height'])
    canvas.create_line(canvas_width // 2, 0, canvas_width // 2, canvas_height, fill="gray")  # Eixo Y
    canvas.create_line(0, canvas_height // 2, canvas_width, canvas_height // 2, fill="gray")  # Eixo X

    # Chamar a função DDA para desenhar a linha
    dda(x1, y1, x2, y2, valor, canvas)

# Função para limpar os parâmetros de entrada e o canvas
def clear_inputs(entries, canvas):
    for entry in entries:
        entry.delete(0, tk.END)
    entries[-1].insert(0, "black")  # Valor padrão para cor
    canvas.delete("all")  # Limpar o canvas

# Configuração da interface do tkinter
def iniciar_interface():
    root = tk.Tk()
    root.title("Algoritmo DDA - Plotar Linha no Plano Cartesiano")

    # Frame principal para organizar os layouts
    main_frame = tk.Frame(root)
    main_frame.pack(fill=tk.BOTH, expand=True)

    # Frame esquerdo para inputs
    left_frame = tk.Frame(main_frame, bg="lightgray", width=200)
    left_frame.pack(side=tk.LEFT, fill=tk.Y)

    # Frame central para o canvas
    center_frame = tk.Frame(main_frame, bg="white")
    center_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    # Frame direito para explicações
    right_frame = tk.Frame(main_frame, bg="lightgray", width=200)
    right_frame.pack(side=tk.RIGHT, fill=tk.Y)

    # Canvas para desenhar a linha
    canvas_width = 600
    canvas_height = 600
    canvas = tk.Canvas(center_frame, width=canvas_width, height=canvas_height, bg="white")
    canvas.pack(padx=10, pady=10)

    # Inputs no frame esquerdo
    entry_x1 = tk.Entry(left_frame)
    entry_y1 = tk.Entry(left_frame)
    entry_x2 = tk.Entry(left_frame)
    entry_y2 = tk.Entry(left_frame)
    entry_color = tk.Entry(left_frame)
    entry_color.insert(0, "black")  # Valor padrão para cor

    entries = [entry_x1, entry_y1, entry_x2, entry_y2, entry_color]

    labels = ["Valor X1:", "Valor Y1:", "Valor X2:", "Valor Y2:", "Cor:"]
    for label_text, entry in zip(labels, entries):
        tk.Label(left_frame, text=label_text, bg="lightgray").pack(padx=10, pady=5, anchor='w')
        entry.pack(padx=10, pady=5, anchor='w')

    # Botão para plotar a linha
    button_plot = tk.Button(left_frame, text="Plotar Linha", command=lambda: plot_line(canvas, entry_x1, entry_y1, entry_x2, entry_y2, entry_color))
    button_plot.pack(padx=10, pady=10)

    # Botão para limpar os parâmetros de entrada e o canvas
    button_clear = tk.Button(left_frame, text="Limpar", command=lambda: clear_inputs(entries, canvas))
    button_clear.pack(padx=10, pady=10)

    # Texto explicativo no frame direito
    explanation = """
    Algoritmo DDA (Digital Differential Analyzer):
    1. Calcula os incrementos Xinc e Yinc.
    2. Desenha a linha ponto a ponto.
    3. Baseado na diferença de coordenadas.
    """
    tk.Label(right_frame, text=explanation, bg="lightgray", justify=tk.LEFT).pack(padx=10, pady=10, anchor='n')

    # Executa a interface gráfica
    root.mainloop()
