# %%
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("auxiliar/BTD6 Rounds RBE - Rounds.csv")

x = df["Round"][0:90]
y = df["Bloon RBE"][0:90]

plt.figure(dpi=300)
plt.plot(x, y)
plt.show()