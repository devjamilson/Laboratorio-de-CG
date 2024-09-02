import tkinter as tk
from algoritmo.ponto_medio import midpoint_circle

def plot_circle_midpoint():
    raio = int(entry_raio.get())
    x_center = int(entry_x_center.get())
    y_center = int(entry_y_center.get())
    valor = entry_color.get()
    
    # Limpar o canvas antes de desenhar o novo círculo
    canvas.delete("all")
    
    # Desenhar eixos x e y
    canvas.create_line(canvas_width // 2, 0, canvas_width // 2, canvas_height, fill="gray", width=1)  # Eixo Y
    canvas.create_line(0, canvas_height // 2, canvas_width, canvas_height // 2, fill="gray", width=1)  # Eixo X

    # Chamar a função para desenhar a circunferência
    midpoint_circle(raio, x_center, y_center, valor, canvas)

def reset_parameters():
    # Limpa as entradas e o canvas
    entry_raio.delete(0, tk.END)
    entry_x_center.delete(0, tk.END)
    entry_y_center.delete(0, tk.END)
    entry_color.delete(0, tk.END)
    canvas.delete("all")
    
    # Redesenha os eixos no canvas
    canvas.create_line(canvas_width // 2, 0, canvas_width // 2, canvas_height, fill="gray", width=1)  # Eixo Y
    canvas.create_line(0, canvas_height // 2, canvas_width, canvas_height // 2, fill="gray", width=1)  # Eixo X

def setup_gui():
    global canvas, entry_raio, entry_x_center, entry_y_center, entry_color
    root = tk.Tk()
    root.title("Algoritmo do Ponto Médio - Plotar Circunferência")

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

    # Canvas para desenhar o círculo
    global canvas_width, canvas_height
    canvas_width = 600
    canvas_height = 600
    canvas = tk.Canvas(center_frame, width=canvas_width, height=canvas_height, bg="white")
    canvas.pack(padx=10, pady=10)

    # Desenhar eixos x e y (reajustar para garantir visibilidade)
    canvas.create_line(canvas_width // 2, 0, canvas_width // 2, canvas_height, fill="gray", width=1)  # Eixo Y
    canvas.create_line(0, canvas_height // 2, canvas_width, canvas_height // 2, fill="gray", width=1)  # Eixo X

    # Inputs no frame esquerdo
    tk.Label(left_frame, text="Raio (0-100):", bg="lightgray").pack(padx=10, pady=5, anchor='w')
    entry_raio = tk.Entry(left_frame)
    entry_raio.pack(padx=10, pady=5, anchor='w')

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

    # Botão para plotar o círculo
    button_plot = tk.Button(left_frame, text="Plotar Circunferência", command=plot_circle_midpoint)
    button_plot.pack(padx=10, pady=10)

    # Botão para resetar os parâmetros
    button_reset = tk.Button(left_frame, text="Resetar Parâmetros", command=reset_parameters)
    button_reset.pack(padx=10, pady=10)

    # Texto explicativo no frame direito
    explanation = """
    Algoritmo do Ponto Médio:
    1. Inicializa os pontos e o valor de d.
    2. Itera para calcular e desenhar pontos do círculo.
    3. Utiliza simetria para desenhar todos os pontos.
    """
    tk.Label(right_frame, text=explanation, bg="lightgray", justify=tk.LEFT).pack(padx=10, pady=10, anchor='n')

    return root