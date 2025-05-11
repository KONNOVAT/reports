import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Параметры модели
a = 0.2   # коэффициент прироста жертв
b = 0.5  # коэффициент смертности жертв из-за хищников
c = 0.05  # коэффициент прироста хищников из-за жертв
d = 0.02   # коэффициент смертности хищников

# Сист. ур.
def model(populations, t):
    x, y = populations  # x - популяция жертв, y - популяция хищников
    dxdt = -a * x + c * x * y  # изменение популяции жертв
    dydt = -d * x * y + b * y   # изменение популяции хищников
    return [dxdt, dydt]

# Нач. условия
initial_conditions = [40, 9]  # начальные значения (жертвы, хищники)
t = np.linspace(0, 100, 100)  # временной интервал

# Решение дифф. ур.
solution = odeint(model, initial_conditions, t)

# Извлечение значений популяций
x_population = solution[:, 0]  # популяция жертв
y_population = solution[:, 1]  # популяция хищников

plt.figure(figsize=(10, 5))
plt.plot(t, x_population, label='Популяция жертв (x)', color='green')
plt.plot(t, y_population, label='Популяция хищников (y)', color='red')
plt.xlabel('Время')
plt.ylabel('Численность')
plt.title('Динамика численности популяций по времени')
plt.legend()
plt.grid()
plt.show()
