import tkinter as tk
from algoritmo.elipse import midpoint_ellipse  # Certifique-se de que essa função está disponível


# Função para resetar os campos de entrada para os valores padrão
def reset_fields(entry_a, entry_b, entry_x_center, entry_y_center, entry_color):
    entry_a.delete(0, tk.END)
    entry_b.delete(0, tk.END)
    entry_x_center.delete(0, tk.END)
    entry_y_center.delete(0, tk.END)
    entry_color.delete(0, tk.END)

    entry_a.insert(0, "100")  # Valor padrão para semi-eixo maior
    entry_b.insert(0, "50")   # Valor padrão para semi-eixo menor
    entry_x_center.insert(0, "0")  # Valor padrão para centro X
    entry_y_center.insert(0, "0")  # Valor padrão para centro Y
    entry_color.insert(0, "black")  # Valor padrão para cor


# Função para plotar a elipse no canvas
def plot_ellipse_midpoint(canvas, entry_a, entry_b, entry_x_center, entry_y_center, entry_color, canvas_width, canvas_height):
    a = int(entry_a.get())
    b = int(entry_b.get())
    x_center = int(entry_x_center.get())
    y_center = int(entry_y_center.get())
    valor = entry_color.get()
    
    # Limpar o canvas antes de desenhar a nova elipse
    canvas.delete("all")
    
    # Desenhar eixos x e y
    canvas.create_line(canvas_width // 2, 0, canvas_width // 2, canvas_height, fill="gray", width=1)  # Eixo Y
    canvas.create_line(0, canvas_height // 2, canvas_width, canvas_height // 2, fill="gray", width=1)  # Eixo X

    # Ajustar o centro da elipse para coordenadas do canvas
    adjusted_x_center = canvas_width // 2 + x_center
    adjusted_y_center = canvas_height // 2 - y_center

    # Chamar a função para desenhar a elipse
    midpoint_ellipse(a, b, adjusted_x_center, adjusted_y_center, valor, canvas)

# Função para configurar a interface gráfica
def setup_gui():
    root = tk.Tk()
    root.title("Algoritmo do Ponto Médio - Plotar Elipse")

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

    # Canvas para desenhar a elipse
    canvas_height = 600
    canvas_width = 600
    canvas = tk.Canvas(center_frame, width=canvas_width, height=canvas_height, bg="white")
    canvas.pack(padx=10, pady=10)

    # Desenhar eixos x e y
    canvas.create_line(canvas_width // 2, 0, canvas_width // 2, canvas_height, fill="gray", width=1)  # Eixo Y
    canvas.create_line(0, canvas_height // 2, canvas_width, canvas_height // 2, fill="gray", width=1)  # Eixo X

    # Inputs no frame esquerdo
    tk.Label(left_frame, text="Semi-eixo Maior (a):", bg="lightgray").pack(padx=10, pady=5, anchor='w')
    entry_a = tk.Entry(left_frame)
    entry_a.pack(padx=10, pady=5, anchor='w')

    tk.Label(left_frame, text="Semi-eixo Menor (b):", bg="lightgray").pack(padx=10, pady=5, anchor='w')
    entry_b = tk.Entry(left_frame)
    entry_b.pack(padx=10, pady=5, anchor='w')

    tk.Label(left_frame, text="Centro X (0-100):", bg="lightgray").pack(padx=10, pady=5, anchor='w')
    entry_x_center = tk.Entry(left_frame)
    entry_x_center.pack(padx=10, pady=5, anchor='w')

    tk.Label(left_frame, text="Centro Y (0-100):", bg="lightgray").pack(padx=10, pady=5, anchor='w')
    entry_y_center = tk.Entry(left_frame)
    entry_y_center.pack(padx=10, pady=5, anchor='w')

    tk.Label(left_frame, text="Cor:", bg="lightgray").pack(padx=10, pady=5, anchor='w')
    entry_color = tk.Entry(left_frame)
    entry_color.pack(padx=10, pady=5, anchor='w')
    entry_color.insert(0, "black")  # Valor padrão para cor

    # Botão para plotar a elipse
    button_plot = tk.Button(left_frame, text="Plotar Elipse", command=lambda: plot_ellipse_midpoint(
        canvas, entry_a, entry_b, entry_x_center, entry_y_center, entry_color, canvas_width, canvas_height))
    button_plot.pack(padx=10, pady=20)


    # Botão para resetar os campos
    button_reset = tk.Button(left_frame, text="Resetar Valores", command=lambda: reset_fields(
        entry_a, entry_b, entry_x_center, entry_y_center, entry_color))
    button_reset.pack(padx=10, pady=10)

    # Texto explicativo no frame direito
    explanation = """
    Algoritmo do Ponto Médio para Elipse:
    1. Inicializa os pontos e o valor de d.
    2. Itera para calcular e desenhar pontos da elipse em duas regiões.
    3. Utiliza simetria para desenhar todos os pontos.
    """
    tk.Label(right_frame, text=explanation, bg="lightgray", justify=tk.LEFT).pack(padx=10, pady=10, anchor='n')

    return root