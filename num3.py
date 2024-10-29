import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv(r'C:\Users\Вержбицкая Полина\Downloads\students.csv', sep=';', header=None, names=['Преподаватель', 'Группа', 'Оценка'])

data.groupby(['Преподаватель', 'Оценка']).size().unstack().plot(kind='bar', stacked=True)
plt.title('Распределение оценок по преподавателям')
plt.xlabel('Преподаватель')
plt.ylabel('Количество')
plt.show()
data.groupby(['Группа', 'Оценка']).size().unstack().plot(kind='bar', stacked=True)
plt.title('Распределение оценок по группам')
plt.xlabel('Группа')
plt.ylabel('Количество')
plt.show()
