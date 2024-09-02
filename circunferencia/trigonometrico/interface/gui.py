import tkinter as tk
from algoritmo.trigonometrico import draw_circle_points_trig

def plot_circle_trig(canvas, entry_raio, entry_x_center, entry_y_center, entry_color):
    raio = int(entry_raio.get())
    x_center = int(entry_x_center.get())
    y_center = int(entry_y_center.get())
    valor = entry_color.get()
    
    # Limpar o canvas antes de desenhar o novo círculo
    canvas.delete("all")
    
    # Desenhar eixos x e y
    canvas_width = int(canvas['width'])
    canvas_height = int(canvas['height'])
    canvas.create_line(canvas_width // 2, 0, canvas_width // 2, canvas_height, fill="gray")  # Eixo Y
    canvas.create_line(0, canvas_height // 2, canvas_width, canvas_height // 2, fill="gray")  # Eixo X

    # Chamar a função para desenhar a circunferência
    draw_circle_points_trig(x_center, y_center, raio, valor, canvas)

def clear_inputs(entry_raio, entry_x_center, entry_y_center, entry_color, canvas):
    """Função para limpar os campos de entrada e o canvas."""
    entry_raio.delete(0, tk.END)
    entry_x_center.delete(0, tk.END)
    entry_y_center.delete(0, tk.END)
    entry_color.delete(0, tk.END)
    canvas.delete("all")

def iniciar_interface():
    # Configuração da interface do tkinter
    root = tk.Tk()
    root.title("Algoritmo Trigonométrico - Plotar Circunferência")

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
    canvas_width = 600
    canvas_height = 600
    canvas = tk.Canvas(center_frame, width=canvas_width, height=canvas_height, bg="white")
    canvas.pack(padx=10, pady=10)

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
    button_plot = tk.Button(left_frame, text="Plotar Circunferência", 
                            command=lambda: plot_circle_trig(canvas, entry_raio, entry_x_center, entry_y_center, entry_color))
    button_plot.pack(padx=10, pady=20)

    # Botão para limpar entradas e canvas
    button_clear = tk.Button(left_frame, text="Limpar", 
                             command=lambda: clear_inputs(entry_raio, entry_x_center, entry_y_center, entry_color, canvas))
    button_clear.pack(padx=10, pady=5)

    # Texto explicativo no frame direito
    explanation = """
    Algoritmo Trigonométrico:
    1. Calcula pontos usando seno e cosseno.
    2. Desenha a circunferência usando ângulos de 0 a 360 graus.
    3. Método direto para plotar formas baseadas em ângulos.
    """
    tk.Label(right_frame, text=explanation, bg="lightgray", justify=tk.LEFT).pack(padx=10, pady=10, anchor='n')

    # Executa a interface gráfica
    root.mainloop()
