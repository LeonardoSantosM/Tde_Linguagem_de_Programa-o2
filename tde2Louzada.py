# =========================================
# Questão 1 — Importação das bibliotecas
# =========================================
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# =========================================
# Questão 2 — Leitura dos dados
# =========================================
df = pd.read_csv('vendas_brasil_clean_aula5.csv')

df.head()
df.shape
df.dtypes


# =========================================
# Questão 4 — Gráfico de barras (canal)
# =========================================
canal = df.groupby('canal_venda')['receita'].sum().sort_values()

plt.figure()
canal.plot(kind='barh')
plt.title('Receita por canal de venda')
plt.xlabel('Receita')
plt.ylabel('Canal')
plt.show()


# =========================================
# Questão 5 — Gráfico de linha (sazonalidade)
# =========================================
tempo = df.groupby('mes')['receita'].sum().sort_index()

plt.figure()
tempo.plot()
plt.title('Evolução da receita ao longo dos meses')
plt.xlabel('Mês')
plt.ylabel('Receita')
plt.xticks(rotation=45)
plt.show()


# =========================================
# Questão 6 — Boxplot (margem por categoria)
# =========================================
plt.figure()
sns.boxplot(x='categoria', y='margem_lucro', data=df)
plt.title('Distribuição da margem por categoria')
plt.show()


# =========================================
# Questão 7 — Scatter plot (receita x lucro)
# =========================================
plt.figure()
sns.scatterplot(x='receita', y='lucro', data=df, alpha=0.5)
plt.title('Relação entre receita e lucro')
plt.show()