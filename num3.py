import pandas as pd
import matplotlib.pyplot as plt

# Чтение данных из файла с явным указанием разделителя
data = pd.read_csv(r'C:\Users\Вержбицкая Полина\Downloads\students.csv', sep=';', header=None, names=['Преподаватель', 'Группа', 'Оценка'])

# График распределения оценок по преподавателям
data.groupby(['Преподаватель', 'Оценка']).size().unstack().plot(kind='bar', stacked=True)
plt.title('Распределение оценок по преподавателям')
plt.xlabel('Преподаватель')
plt.ylabel('Количество')
plt.show()

# График распределения оценок по группам
data.groupby(['Группа', 'Оценка']).size().unstack().plot(kind='bar', stacked=True)
plt.title('Распределение оценок по группам')
plt.xlabel('Группа')
plt.ylabel('Количество')
plt.show()
