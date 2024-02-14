import numpy as np
import matplotlib.pyplot as plt

# Definir la función constructor
def constructor(x):
    return x - 2 - 2 * np.floor((x - 1) / 2)

# Definir la función para el corazón
def draw_heart():
    t = np.linspace(0, 2 * np.pi, 100)
    x = 16 * np.sin(t)**3
    y = 13 * np.cos(t) - 5 * np.cos(2 * t) - 2 * np.cos(3 * t) - np.cos(4 * t)
    return x, y

# Definir la función para la rosa
def draw_flower():
    t = np.linspace(0, 12 * np.pi, 1000)
    x = 3 * np.cos(t) * (np.abs(6 * constructor(9 * t / (4 * np.pi))) - 4.5)
    y = 3 * np.sin(t) * (np.abs(6 * constructor(9 * t / (4 * np.pi))) - 4.5)
    return x, y

# Escalar la rosa para que esté más en línea con el tamaño del corazón
flower_scale_factor = 0.5
flower_x, flower_y = draw_flower()
flower_x *= flower_scale_factor
flower_y *= flower_scale_factor

# Dibujar la rosa
plt.plot(flower_x, flower_y, color='green')

# Dibujar y rellenar el corazón con rosa
heart_x, heart_y = draw_heart()
plt.fill(heart_x, heart_y, color='pink')

# Agregar las iniciales "CR" debajo de la rosa
plt.text(0, np.min(flower_y) - 3, "I ❤️ You", color='red', fontsize=22, ha='center')

# Configuración del gráfico
plt.gca().set_facecolor('#202020')
plt.axis('equal')
plt.axis('off')

plt.show()
