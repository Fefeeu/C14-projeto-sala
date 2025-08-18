# %%
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("auxiliar/BTD6 Rounds RBE - Rounds.csv")

x = df["Round"][0:120]
y = df["Bloon RBE"][0:120]

plt.figure(dpi=500)
plt.plot(x, y)
plt.show()