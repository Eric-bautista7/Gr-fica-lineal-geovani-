# Importa la librería Matplotlib para crear gráficas
import matplotlib.pyplot as plt

# Define los valores del eje X
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

# Define los valores del eje Y
y = [10, 15, 13, 18, 22, 25, 35, 45, 24, 59, 7, 33, 22, 2, 12, 52, 39, 17, 40, 9]

# Crea una gráfica lineal de color morado con círculos en los puntos
plt.plot(x, y, color="red", marker="o", linestyle="-", linewidth=2)

# Agrega un título a la gráfica
plt.title("Gráfica lineal de ejemplo")

# Coloca el nombre del eje X
plt.xlabel("Eje X")

# Coloca el nombre del eje Y
plt.ylabel("Eje Y")

# Activa la cuadrícula para facilitar la lectura de los datos
plt.grid(True)

# Muestra la gráfica en pantalla
plt.show()