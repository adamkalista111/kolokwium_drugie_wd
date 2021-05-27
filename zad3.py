import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
data = {'a': np.random.randint(0, 100, 100),
        'b': np.random.randint(0, 100, 100),
        'c': np.random.randint(0, 8, 100)}
data['tmp'] = data['a'] - data['b']
data['d'] = np.abs(data['tmp'])

df = pd.DataFrame(data)

wykres = sns.relplot(data=df, x='a', y='b',size = 'd', palette='Set2', hue='c')
plt.legend(loc='lower left')
plt.xlabel("os x")
plt.ylabel("os y")
plt.title("Wykres")
wykres.fig.set_size_inches(10, 10)
plt.show()