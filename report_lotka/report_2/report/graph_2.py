import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Параметры модели
a = 0.2   # коэффициент прироста жертв
b = 0.5  # коэффициент смертности жертв из-за хищников
c = 0.05  # коэффициент прироста хищников из-за жертв
d = 0.02   # коэффициент смертности хищников

# Система уравнений
def model(populations, t):
    x, y = populations  # x - популяция жертв, y - популяция хищников
    dxdt = -a * x + c * x * y  # изменение популяции жертв
    dydt = -d * x * y + b * y   # изменение популяции хищников
    return [dxdt, dydt]

# Функция для построения графика
def plot_population_graph(initial_conditions, time_range):
    t = np.linspace(time_range[0], time_range[1], 1000)  # временной интервал
    solution = odeint(model, initial_conditions, t)

    x_population = solution[:, 0]  # популяция жертв
    y_population = solution[:, 1]  # популяция хищников

    # Построение графика
    plt.figure()
    plt.plot(x_population, y_population, label='Зависимости изменения численности', color='blue')
    plt.xlabel('Популяция жертв (x)')
    plt.ylabel('Популяция хищников (y)')
    plt.title('''Зависимости изменения численности хищников от
             изменения численности жертв с начальными значениями''')
    plt.grid()
    plt.legend()
    plt.show()

# Начальные условия
initial_conditions = [10, 5]  # начальные значения (жертвы, хищники)
time_range = (0, 400)  # временной диапазон

# Вызов функции для построения графика
plot_population_graph(initial_conditions, time_range)
