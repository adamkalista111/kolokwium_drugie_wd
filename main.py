import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('cars.csv', header=0, sep=';')
df['Weight'] = df['Weight'].astype(int)
waga = df[(df['Weight']<2200)]
print(waga)
df['Horsepower'] = df['Horsepower'].astype(int)
df['Model year'] = df['Model year'].astype(int)
moc = (df.groupby(['Model year', 'Horsepower'], as_index=False).mean().groupby('Model year')['Horsepower'].mean())
print(moc)
wykres = moc.plot.bar(subplots=True, legend=False)
plt.xlabel('Lata')
plt.ylabel('Średnia')
plt.title('Średnia moc silnika w poszczególnych latach')
plt.savefig('wykres.png')
plt.show()
