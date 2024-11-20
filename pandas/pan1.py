import pandas as pd
data = pd.read_csv('transactions.csv')

ok_payments = data[data['STATUS'] == 'OK']

top3_payments = ok_payments.nlargest(3, 'SUM')
data['CONTRACTOR'] = data['CONTRACTOR'].str.strip().str.replace('"', '')

total_sum = ok_payments[ok_payments['CONTRACTOR'] == 'Umbrella, Inc']['SUM'].sum()



print("Три самых крупных платежа с реальным статусом 'OK':")
print(top3_payments)
print("\nОбщая сумма платежей в адрес 'Umbrella, Inc.':", total_sum)
