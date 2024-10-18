import pandas as pd

df = pd.read_csv('dz.csv')

# Удаляем строки, где зарплата отсутствует
df_cleaned = df.dropna(subset=['Salary'])

# Группируем по городам и вычисляем среднюю зарплату
average_salary_by_city = df_cleaned.groupby('City')['Salary'].mean()

# Выводим результат
print(average_salary_by_city)
