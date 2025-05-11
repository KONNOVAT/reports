---
## Front matter
title: "Построение мат. модели «хищник–жертва» с помощью python"
subtitle: "Модель «хищник–жертва»"
author: "Коннова Татьяна Алексеевна"

## Generic otions
lang: ru-RU
toc-title: "Содержание"

## Bibliography
bibliography: bib/cite.bib
csl: pandoc/csl/gost-r-7-0-5-2008-numeric.csl

## Pdf output format
toc: true # Table of contents
toc-depth: 2
lof: true # List of figures
lot: false # List of tables
fontsize: 12pt
linestretch: 1.5
papersize: a4
documentclass: scrreprt
## I18n polyglossia
polyglossia-lang:
  name: russian
  options:
	- spelling=modern
	- babelshorthands=true
polyglossia-otherlangs:
  name: english
## I18n babel
babel-lang: russian
babel-otherlangs: english
## Fonts
mainfont: PT Serif
romanfont: PT Serif
sansfont: PT Sans
monofont: PT Mono
mainfontoptions: Ligatures=TeX
romanfontoptions: Ligatures=TeX
sansfontoptions: Ligatures=TeX,Scale=MatchLowercase
monofontoptions: Scale=MatchLowercase,Scale=0.9
## Biblatex
biblatex: true
biblio-style: "gost-numeric"
biblatexoptions:
  - parentracker=true
  - backend=biber
  - hyperref=auto
  - language=auto
  - autolang=other*
  - citestyle=gost-numeric
## Pandoc-crossref LaTeX customization
figureTitle: "Рис."
tableTitle: "Таблица"
listingTitle: "Листинг"
lofTitle: "Список иллюстраций"
lotTitle: "Список таблиц"
lolTitle: "Листинги"
## Misc options
indent: true
header-includes:
  - \usepackage{indentfirst}
  - \usepackage{float} # keep figures where there are in the text
  - \floatplacement{figure}{H} # keep figures where there are in the text
---

# Цель работы

Исследование динамики численности популяций хищников и жертв с течением времени, а также анализ зависимости изменения численности хищников от изменения численности жертв с заданными начальными условиями.

# Теоретическое введение

Модель Лотки-Вольтерры описывает взаимодействие двух видов в экосистеме [@lotka_1], [@lotka_2], [@lotka_3]:

- **Жертвы**: размножаются с постоянной скоростью, но их численность ограничивается хищниками
- **Хищники**: вымирают без жертв, но увеличивают популяцию за счет поедания жертв

Основные уравнения модели:

$$
\begin{cases}
  \dot x = ax - bxy \\
  \dot y = cxy - dy,
\end{cases}
$$

a, d, - коэффициенты смертности
b, c, - коэффициенты прироста популяции

**Код для построения графика динамики численности популяций по времени:**

```python
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
plt.title('Динамика численности популяций по времени.')
plt.legend()
plt.grid()
plt.show()
```
Результат:

![Динамика численности популяций по времени](./image/img_4.png)

Далее построим с помощью python график, отражающий зависимости изменения численности хищников от изменения численности жертв с начальными значениями:
```python
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
    plt.plot(x_population, y_population, label='''Зависимости изменения 
    численности''', color='blue')
    plt.xlabel('Популяция жертв (x)')
    plt.ylabel('Популяция хищников (y)')
    plt.title('''Зависимости изменения численности хищников 
    от изменения численности жертв с начальными значениями''')
    plt.grid()
    plt.legend()
    plt.show()

# Начальные условия
initial_conditions = [10, 5]  # начальные значения (жертвы, хищники)
time_range = (0, 400)  # временной диапазон

# Вызов функции для построения графика
plot_population_graph(initial_conditions, time_range)
```

Результат:

![Зависимости изменения численности хищников от изменения численности жертв с начальными значениями](./image/img_6.png)

# Выводы

В процессе выполнения данной лабораторной реализована модель "хищник-жертва" в python.

# Список литературы{.unnumbered}

::: {#refs}
:::