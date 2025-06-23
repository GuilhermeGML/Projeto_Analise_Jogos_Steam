import pandas as pd

df = pd.read_csv("todos_os_jogos.csv")

#Converte para formato DataTime
df['data_lancamento'] = pd.to_datetime(df['data_lancamento'], format='mixed', errors='coerce')

#Agrupa as datas por ano
df['ano_lancamento'] = df['data_lancamento'].dt.year
jogos_por_ano = df.groupby('ano_lancamento')['nome'].nunique()
print(jogos_por_ano)

#Agrupa por desenvolvedora
jogos_por_desenvolvedora = df.groupby('desenvolvedor')['nome'].nunique()
print(jogos_por_desenvolvedora)

#Agrupa por categoria
jogos_por_categoria = df.groupby('categorias')['nome'].nunique()
print(jogos_por_categoria)

#Agrupa por genero
jogos_por_genero = df.groupby('generos')['nome'].nunique()
print(jogos_por_genero)