import pandas as pd
import matplotlib.pyplot as plt

# Dados fictícios de consumo de energia
data = {
    'Hora': ['00:00', '01:00', '02:00', '03:00', '04:00', '05:00', '06:00', '07:00', '08:00', '09:00', '10:00', '11:00'],
    'Consumo (kWh)': [5, 4, 3, 4, 5, 6, 8, 10, 15, 20, 18, 16]
}

df = pd.DataFrame(data)

# Visualização do consumo de energia
plt.figure(figsize=(10, 6))
plt.plot(df['Hora'], df['Consumo (kWh)'], marker='o')
plt.title('Consumo de Energia ao Longo do Dia')
plt.xlabel('Hora')
plt.ylabel('Consumo (kWh)')
plt.grid(True)
plt.show()
