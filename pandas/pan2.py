import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv(r'C:\Users\Вержбицкая Полина\Downloads\flights.csv')
summary = data.groupby('CARGO').agg(
    flights_count=('CARGO', 'size'),
    total_price=('PRICE', 'sum'),
    total_weight=('WEIGHT', 'sum')
).reset_index()


fig, ax = plt.subplots(3, 1, figsize=(10, 15))


ax[0].bar(summary['CARGO'], summary['flights_count'], color='skyblue')
ax[0].set_title('Количество полетов авиакомпаниями', fontsize=12)
ax[0].set_ylabel('Количество полетов', fontsize=10)
ax[0].set_xticks(range(len(summary['CARGO'])))
ax[0].set_xticklabels(summary['CARGO'], rotation=0, ha='center', fontsize=10)

ax[1].bar(summary['CARGO'], summary['total_price'], color='salmon')
ax[1].set_title('Стоимость груза авиакомпаний', fontsize=12)
ax[1].set_ylabel('Стоимость груза', fontsize=10)
ax[1].set_xticks(range(len(summary['CARGO'])))
ax[1].set_xticklabels(summary['CARGO'], rotation=0, ha='center', fontsize=10)

ax[2].bar(summary['CARGO'], summary['total_weight'], color='lightgreen')
ax[2].set_title('Масса груза га бортах авиакомпаний', fontsize=12)
ax[2].set_ylabel('Масса груза', fontsize=10)
ax[2].set_xticks(range(len(summary['CARGO'])))
ax[2].set_xticklabels(summary['CARGO'], rotation=0, ha='center', fontsize=10)

plt.tight_layout(pad=3)  
plt.show()