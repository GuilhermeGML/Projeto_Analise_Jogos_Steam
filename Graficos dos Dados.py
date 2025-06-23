import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carrega os dados
df = pd.read_csv("todos_os_jogos.csv")

# Converte a coluna para datetime
df['data_lancamento'] = pd.to_datetime(df['data_lancamento'], format='mixed', errors='coerce')

# Cria a coluna com o ano
df['ano_lancamento'] = df['data_lancamento'].dt.year

# === Gráfico 1: Jogos únicos por ano ===
jogos_por_ano = df.groupby('ano_lancamento')['nome'].nunique()
plt.figure(figsize=(12, 6))
sns.barplot(x=jogos_por_ano.index, y=jogos_por_ano.values, color='skyblue')
plt.title('Número de jogos únicos lançados por ano')
plt.xlabel('Ano de Lançamento')
plt.ylabel('Quantidade de Jogos')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# === Gráfico 2: Jogos únicos por desenvolvedora ===
jogos_por_desenvolvedora = df.groupby('desenvolvedor')['nome'].nunique().sort_values(ascending=False).head(15)
plt.figure(figsize=(12, 6))
sns.barplot(x=jogos_por_desenvolvedora.values, y=jogos_por_desenvolvedora.index, palette='viridis')
plt.title('Top 15 Desenvolvedoras com mais jogos únicos')
plt.xlabel('Quantidade de Jogos')
plt.ylabel('Desenvolvedora')
plt.tight_layout()
plt.show()

# === Gráfico 3: Jogos únicos por categoria ===
jogos_por_categoria = df.groupby('categorias')['nome'].nunique().sort_values(ascending=False).head(15)
plt.figure(figsize=(12, 6))
sns.barplot(x=jogos_por_categoria.values, y=jogos_por_categoria.index, palette='magma')
plt.title('Top 15 Categorias com mais jogos únicos')
plt.xlabel('Quantidade de Jogos')
plt.ylabel('Categoria')
plt.tight_layout()
plt.show()

# === Gráfico 4: Jogos únicos por gênero ===
jogos_por_genero = df.groupby('generos')['nome'].nunique().sort_values(ascending=False).head(15)
plt.figure(figsize=(12, 6))
sns.barplot(x=jogos_por_genero.values, y=jogos_por_genero.index, palette='coolwarm')
plt.title('Top 15 Gêneros com mais jogos únicos')
plt.xlabel('Quantidade de Jogos')
plt.ylabel('Gênero')
plt.tight_layout()
plt.show()

# === Gráfico 5: JJogos por Ano e Desenvolvedora ===
top_devs = df['desenvolvedor'].value_counts().head(5).index
df_top = df[df['desenvolvedor'].isin(top_devs)]
pivot = df_top.pivot_table(index='ano_lancamento', columns='desenvolvedor', values='nome', aggfunc='nunique')
pivot.plot(kind='bar', figsize=(12,6))
plt.title('Jogos por Ano e Desenvolvedora')
plt.xlabel('Ano')
plt.ylabel('Quantidade de Jogos')
plt.tight_layout()
plt.show()

# === Gráfico 6: Jogos por Ano e Publicadora ===
top_devs = df['desenvolvedor'].value_counts().head(5).index
df_top = df[df['desenvolvedor'].isin(top_devs)]
pivot = df_top.pivot_table(index='ano_lancamento', columns='publicadora', values='nome', aggfunc='nunique')
pivot.plot(kind='bar', figsize=(12,6))
plt.title('Jogos por Ano e Publicadora')
plt.xlabel('Ano')
plt.ylabel('Quantidade de Jogos')
plt.tight_layout()
plt.show()

# === Gráfico 7: Jogos por Ano e Generos ===
top_devs = df['desenvolvedor'].value_counts().head(5).index
df_top = df[df['desenvolvedor'].isin(top_devs)]
pivot = df_top.pivot_table(index='ano_lancamento', columns='generos', values='nome', aggfunc='nunique')
pivot.plot(kind='bar', figsize=(12,6))
plt.title('Jogos por Ano e Generos')
plt.xlabel('Ano')
plt.ylabel('Quantidade de Jogos')
plt.tight_layout()
plt.show()

# === Gráfico 8: Jogos por Ano e Plataformas ===
top_devs = df['desenvolvedor'].value_counts().head(5).index
df_top = df[df['desenvolvedor'].isin(top_devs)]
pivot = df_top.pivot_table(index='ano_lancamento', columns='plataformas', values='nome', aggfunc='nunique')
pivot.plot(kind='bar', figsize=(12,6))
plt.title('Jogos por Ano e Plataformas')
plt.xlabel('Ano')
plt.ylabel('Quantidade de Jogos')
plt.tight_layout()
plt.show()

# === Gráfico 9: Jogos por Desenvolvedor e Generos ===
tabela = df.groupby(['desenvolvedor', 'generos'])['nome'].nunique().unstack().fillna(0)
tabela = tabela.loc[:, tabela.sum().sort_values(ascending=False).head(5).index]
tabela.head(10).plot(kind='bar', stacked=True, figsize=(12,6))
plt.title('Desenvolvedor x Generos')
plt.xlabel('Desenvolvedor')
plt.ylabel('Qtd de Jogos')
plt.tight_layout()
plt.show()

# === Gráfico 10: Jogos por Desenvolvedor e Plataformas ===
tabela = df.groupby(['desenvolvedor', 'plataformas'])['nome'].nunique().unstack().fillna(0)
tabela = tabela.loc[:, tabela.sum().sort_values(ascending=False).head(5).index]
tabela.head(10).plot(kind='bar', stacked=True, figsize=(12,6))
plt.title('Desenvolvedor x Plataformas')
plt.xlabel('Desenvolvedor')
plt.ylabel('Qtd de Jogos')
plt.tight_layout()
plt.show()

# === Gráfico 11: Jogos por Publicadora e Generos ===
tabela = df.groupby(['publicadora', 'generos'])['nome'].nunique().unstack().fillna(0)
tabela = tabela.loc[:, tabela.sum().sort_values(ascending=False).head(5).index]  # top 5 gêneros
tabela.head(10).plot(kind='bar', stacked=True, figsize=(12,6))
plt.title('Publicadora x Gêneros')
plt.xlabel('Publicadora')
plt.ylabel('Qtd de Jogos')
plt.tight_layout()
plt.show()

# === Gráfico 12: Jogos por Publicadora e Plataformas ===
tabela = df.groupby(['publicadora', 'plataformas'])['nome'].nunique().unstack().fillna(0)
tabela = tabela.loc[:, tabela.sum().sort_values(ascending=False).head(5).index]  # top 5 gêneros
tabela.head(10).plot(kind='bar', stacked=True, figsize=(12,6))
plt.title('Publicadora x Plataformas')
plt.xlabel('Publicadora')
plt.ylabel('Qtd de Jogos')
plt.tight_layout()
plt.show()
