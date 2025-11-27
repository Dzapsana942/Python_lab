import pandas as pd

# 1. Wczytaj dane z pliku Excel
df_so2 = pd.read_excel('lol.xlsx', sheet_name='SO2')
df_pm10 = pd.read_excel('lol.xlsx', sheet_name='PM10')

# 2. Usuń pierwszy wiersz z opisami
df_so2 = df_so2.drop(0)
df_pm10 = df_pm10.drop(0)

# 3. Konwersja kolumn liczbowych na typ numeryczny
kolumny_liczbowe_so2 = ['Rok', 'Średnia', 'Min', 'Maks', 'Liczba pomiarów', 'Kompletność ']
kolumny_liczbowe_pm10 = ['Rok', 'Średnia', 'Min', 'Maks', 'Liczba pomiarów', 'Kompletność ']

for kol in kolumny_liczbowe_so2:
    df_so2[kol] = pd.to_numeric(df_so2[kol], errors='coerce')

for kol in kolumny_liczbowe_pm10:
    df_pm10[kol] = pd.to_numeric(df_pm10[kol], errors='coerce')


# 4. Które stacje mają najniższą kompletność pomiarów
print("SO2 - Najniższa kompletność:")
print(df_so2[['Kod stacji', 'Kompletność ']].sort_values('Kompletność ').head())

print("\nPM10 - Najniższa kompletność:")
print(df_pm10[['Kod stacji', 'Kompletność ']].sort_values('Kompletność ').head())


# 5. Liczba pomiarów na województwa
print("\nSO2 - Liczba pomiarów na województwo:")
print(df_so2.groupby('Województwo')['Liczba pomiarów'].sum())

print("\nPM10 - Liczba pomiarów na województwo:")
print(df_pm10.groupby('Województwo')['Liczba pomiarów'].sum())


# 6. Najniższe i najwyższe średnie
print("\nSO2 - Najwyższe średnie:")
print(df_so2[['Kod stacji', 'Średnia']].sort_values('Średnia', ascending=False).head())

print("\nSO2 - Najniższe średnie:")
print(df_so2[['Kod stacji', 'Średnia']].sort_values('Średnia').head())

print("\nPM10 - Najwyższe średnie:")
print(df_pm10[['Kod stacji', 'Średnia']].sort_values('Średnia', ascending=False).head())

print("\nPM10 - Najniższe średnie:")
print(df_pm10[['Kod stacji', 'Średnia']].sort_values('Średnia').head())


# 7. Stacje z najwyższą amplitudą
df_so2['Amplituda'] = df_so2['Maks'] - df_so2['Min']
df_pm10['Amplituda'] = df_pm10['Maks'] - df_pm10['Min']

print("\nSO2 - Największa amplituda:")
print(df_so2[['Kod stacji', 'Amplituda']].sort_values('Amplituda', ascending=False).head())

print("\nPM10 - Największa amplituda:")
print(df_pm10[['Kod stacji', 'Amplituda']].sort_values('Amplituda', ascending=False).head())


# 8. Jak zmienia się amplituda na przestrzeni lat
print("\nSO2 - Amplituda w latach:")
print(df_so2.groupby('Rok')['Amplituda'].mean())

print("\nPM10 - Amplituda w latach:")
print(df_pm10.groupby('Rok')['Amplituda'].mean())
