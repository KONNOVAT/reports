import numpy as np
import matplotlib.pyplot as plt

# Параметры модели
alpha = 0.1  # коэффициент размножения жертв
beta = 0.02  # коэффициент смертности жертв от хищников
delta = 0.01  # коэффициент размножения хищников
gamma = 0.1   # коэффициент смертности хищников

# Начальные условия
prey_initial = 40   # начальное количество жертв
predator_initial = 9  # начальное количество хищников
time_steps = 200     # количество временных шагов

# Временная сетка
t = np.linspace(0, time_steps, time_steps)

# Массивы для хранения значений популяций
prey_population = np.zeros(time_steps)
predator_population = np.zeros(time_steps)

# Установка начальных условий
prey_population[0] = prey_initial
predator_population[0] = predator_initial

# Моделирование динамики популяций
for i in range(1, time_steps):
    prey_population[i] = prey_population[i-1] + (alpha * prey_population[i-1] - beta * prey_population[i-1] * predator_population[i-1])
    predator_population[i] = predator_population[i-1] + (delta * prey_population[i-1] * predator_population[i-1] - gamma * predator_population[i-1])

# Визуализация результатов
plt.figure(figsize=(12, 6))
plt.plot(t, prey_population, label='Жертвы (Prey)', color='green')
plt.plot(t, predator_population, label='Хищники (Predators)', color='red')
plt.title('Модель Хищник-Жертва')
plt.xlabel('Время')
plt.ylabel('Популяция')
plt.legend()
plt.grid()
plt.show()
