# interface/gui.py
import tkinter as tk
from algoritmo.circle_eq_expl import explicit_circle

class CircleApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Algoritmo Explícito - Plotar Circunferência")
        
        # Configuração do frame principal
        self.main_frame = tk.Frame(root)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        # Configuração dos frames
        self.setup_left_frame()
        self.setup_center_frame()
        self.setup_right_frame()

    def setup_left_frame(self):
        """Configuração do frame esquerdo para inputs."""
        self.left_frame = tk.Frame(self.main_frame, bg="lightgray", width=200)
        self.left_frame.pack(side=tk.LEFT, fill=tk.Y)

        tk.Label(self.left_frame, text="Raio (0-100):", bg="lightgray").pack(padx=10, pady=5, anchor='w')
        self.entry_raio = tk.Entry(self.left_frame)
        self.entry_raio.pack(padx=10, pady=5, anchor='w')

        tk.Label(self.left_frame, text="Centro X (0-100):", bg="lightgray").pack(padx=10, pady=5, anchor='w')
        self.entry_x_center = tk.Entry(self.left_frame)
        self.entry_x_center.pack(padx=10, pady=5, anchor='w')

        tk.Label(self.left_frame, text="Centro Y (0-100):", bg="lightgray").pack(padx=10, pady=5, anchor='w')
        self.entry_y_center = tk.Entry(self.left_frame)
        self.entry_y_center.pack(padx=10, pady=5, anchor='w')

        tk.Label(self.left_frame, text="Cor:", bg="lightgray").pack(padx=10, pady=5, anchor='w')
        self.entry_color = tk.Entry(self.left_frame)
        self.entry_color.pack(padx=10, pady=5, anchor='w')
        self.entry_color.insert(0, "black")  # Valor padrão para cor

        self.button_plot = tk.Button(self.left_frame, text="Plotar Circunferência", command=self.plot_circle)
        self.button_plot.pack(padx=10, pady=10)
        
        self.button_reset = tk.Button(self.left_frame, text="Resetar", command=self.reset_inputs)
        self.button_reset.pack(padx=10, pady=10)

    def setup_center_frame(self):
        """Configuração do frame central para o canvas."""
        self.center_frame = tk.Frame(self.main_frame, bg="white")
        self.center_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.canvas_width = 600
        self.canvas_height = 600
        self.canvas = tk.Canvas(self.center_frame, width=self.canvas_width, height=self.canvas_height, bg="white")
        self.canvas.pack(padx=10, pady=10)

    def setup_right_frame(self):
        """Configuração do frame direito para explicações."""
        self.right_frame = tk.Frame(self.main_frame, bg="lightgray", width=200)
        self.right_frame.pack(side=tk.RIGHT, fill=tk.Y)

        explanation = """
        Algoritmo Explícito para Circunferência:
        1. Calcula pontos diretamente da equação x^2 + y^2 = r^2.
        2. Não utiliza simetria para desenhar.
        3. Útil para demonstrar o conceito básico de círculo.
        """
        tk.Label(self.right_frame, text=explanation, bg="lightgray", justify=tk.LEFT).pack(padx=10, pady=10, anchor='n')

    def plot_circle(self):
        """Captura os valores dos inputs e desenha a circunferência."""
        raio = int(self.entry_raio.get())
        x_center = int(self.entry_x_center.get())
        y_center = int(self.entry_y_center.get())
        valor = self.entry_color.get()

        # Limpar o canvas antes de desenhar o novo círculo
        self.canvas.delete("all")
        
        # Desenhar eixos x e y
        self.canvas.create_line(self.canvas_width // 2, 0, self.canvas_width // 2, self.canvas_height, fill="gray")  # Eixo Y
        self.canvas.create_line(0, self.canvas_height // 2, self.canvas_width, self.canvas_height // 2, fill="gray")  # Eixo X

        # Chamar a função para desenhar a circunferência
        explicit_circle(raio, x_center, y_center, valor, self.canvas)

    def reset_inputs(self):
        """Reseta os campos de entrada para os valores padrões."""
        self.entry_raio.delete(0, tk.END)
        self.entry_raio.insert(0, "0")
        self.entry_x_center.delete(0, tk.END)
        self.entry_x_center.insert(0, "0")
        self.entry_y_center.delete(0, tk.END)
        self.entry_y_center.insert(0, "0")
        self.entry_color.delete(0, tk.END)
        self.entry_color.insert(0, "black")
        self.canvas.delete("all")  # Opcional: Limpa o canvas ao resetar

if __name__ == "__main__":
    root = tk.Tk()
    app = CircleApp(root)
    root.mainloop()
