

import pandas as pd
import matplotlib.pyplot as plt

info = pd.read_excel('students_info.xlsx')
results = pd.read_html('results_ejudge.html')[0]



results['solved_tasks'] = results.iloc[:, 2:].apply(lambda row: (row > 0).sum(), axis=1)
merged_data = pd.merge(results[['User', 'solved_tasks']], info, left_on='User', right_on='login')

faculty_avg = merged_data.groupby('group_faculty')['solved_tasks'].mean()
faculty_avg.plot(kind='bar', title="Среднее количество решённых задач по факультетским группам")
plt.xlabel("Факультетская группа")
plt.ylabel("Среднее количество решённых задач")
plt.show()
group_avg = merged_data.groupby('group_out')['solved_tasks'].mean()
group_avg.plot(kind='bar', title="Среднее количество решённых задач по группам по информатике")
plt.xlabel("Группа по информатике")
plt.ylabel("Среднее количество решённых задач")
plt.show()

tasksGH = results[['User', 'G', 'H']]
passedGH = tasksGH[(tasksGH['G'] > 10) | (tasksGH['H'] > 10)]['User'].unique()



filtered_data = merged_data[merged_data['User'].isin(passedGH)]
faculty_count = filtered_data['group_faculty'].value_counts()
groups_count = filtered_data['group_out'].value_counts()

print("Факультетские группы студентов, прошедших более одного теста в задачах G или H:")
print(faculty_count)
print("\nГруппы по информатике, в которые попали студенты, прошедшие более одного теста в задачах G или H:")
print(groups_count)
