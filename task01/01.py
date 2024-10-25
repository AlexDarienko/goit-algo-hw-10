import pulp

# Створення моделі
model = pulp.LpProblem("Maximize_Drink_Production", pulp.LpMaximize)

# Змінні для кількості виробництва лимонаду та фруктового соку
lemonade = pulp.LpVariable("Lemonade", lowBound=0, cat='Integer')
fruit_juice = pulp.LpVariable("Fruit_Juice", lowBound=0, cat='Integer')

# Цільова функція: максимізація загальної кількості напоїв
model += lemonade + fruit_juice, "Total_Drinks"

# Обмеження на ресурси
model += 2 * lemonade + 1 * fruit_juice <= 100, "Water_Constraint"
model += 1 * lemonade <= 50, "Sugar_Constraint"
model += 1 * lemonade <= 30, "Lemon_Juice_Constraint"
model += 2 * fruit_juice <= 40, "Fruit_Puree_Constraint"

# Розв'язання моделі
model.solve()

# Виведення результатів
print("Статус розв'язку:", pulp.LpStatus[model.status])
print("Оптимальна кількість лимонаду:", lemonade.varValue)
print("Оптимальна кількість фруктового соку:", fruit_juice.varValue)
print("Максимальна кількість вироблених напоїв:", pulp.value(model.objective))
