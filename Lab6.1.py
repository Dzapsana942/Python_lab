import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Wczytanie danych
df_so2 = pd.read_excel('lol.xlsx', sheet_name='SO2').drop(0)
df_pm10 = pd.read_excel('lol.xlsx', sheet_name='PM10').drop(0)

# Konwersja liczb
kolumny_liczbowe = ['Rok', 'Średnia', 'Min', 'Maks', 'Liczba pomiarów', 'Kompletność ']
for kol in kolumny_liczbowe:
    df_so2[kol] = pd.to_numeric(df_so2[kol], errors='coerce')
    df_pm10[kol] = pd.to_numeric(df_pm10[kol], errors='coerce')

# Dodanie amplitudy
df_so2['Amplituda'] = df_so2['Maks'] - df_so2['Min']
df_pm10['Amplituda'] = df_pm10['Maks'] - df_pm10['Min']

sns.set(style="whitegrid")  # Ustawienia stylu seaborn

# 1. WYKRES LINIOWY - średnia amplituda PM10 i SO2 w latach
plt.figure(figsize=(10,6))
amplituda_so2 = df_so2.groupby('Rok')['Amplituda'].mean()
amplituda_pm10 = df_pm10.groupby('Rok')['Amplituda'].mean()

plt.plot(amplituda_so2.index, amplituda_so2.values, marker='o', label='SO2 - Amplituda')
plt.plot(amplituda_pm10.index, amplituda_pm10.values, marker='s', label='PM10 - Amplituda')

plt.title('Średnia amplituda pomiarów w latach')
plt.xlabel('Rok')
plt.ylabel('Średnia Amplituda')
plt.legend()
plt.tight_layout()
plt.show()


# 2. WYKRES SŁUPKOWY - liczba pomiarów na województwo dla PM10
plt.figure(figsize=(12,6))
woj_pomiary_pm10 = df_pm10.groupby('Województwo')['Liczba pomiarów'].sum().sort_values()

sns.barplot(x=woj_pomiary_pm10.values, y=woj_pomiary_pm10.index, palette='viridis')

plt.title('Liczba pomiarów PM10 w poszczególnych województwach')
plt.xlabel('Liczba pomiarów')
plt.ylabel('Województwo')
plt.tight_layout()
plt.show()


# 3. HEATMAPA - korelacje między zmiennymi w PM10
plt.figure(figsize=(10,8))
korelacje = df_pm10[['Średnia', 'Min', 'Maks', 'Liczba pomiarów', 'Kompletność ', 'Amplituda']].corr()

sns.heatmap(korelacje, annot=True, cmap='coolwarm', fmt=".2f")

plt.title('Macierz korelacji dla metryk PM10')
plt.tight_layout()
plt.show()
