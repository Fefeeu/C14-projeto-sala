# %%
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("auxiliar/BTD6 Rounds RBE - Rounds.csv")

x = df["Round"][0:100]
y = df["Bloon RBE"][0:100]

# %%
descricao_rbe = df["Bloon RBE"].describe()
print(descricao_rbe)

# %%
plt.figure(dpi=500)

plt.plot(x, y)
plt.show()
