# %%
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("auxiliar/BTD6 Rounds RBE - Rounds.csv")

x = df["Round"][0:100]
y = df["Bloon RBE"][0:100]

plt.figure(dpi=400)
plt.plot(x, y)
plt.show()