import pandas as pd
import glob
import os

# Caminho da pasta com os arquivos CSV
pasta = r"C:\Users\Adriano\Desktop\Programação\Projeto\2 - Análise de Video Game"

# Encontra arquivos com extensão .csv e .CSV e remove duplicados
csv_files = list(set(
    glob.glob(os.path.join(pasta, "*.csv")) + glob.glob(os.path.join(pasta, "*.CSV"))
))

# Mostrar os arquivos encontrados
print("Arquivos encontrados:")
for f in csv_files:
    print("-", os.path.basename(f))

# Lista para armazenar os DataFrames
dataframes = []

# Lê os arquivos CSV
for file in csv_files:
    try:
        df = pd.read_csv(file)
        dataframes.append(df)
    except Exception as e:
        print(f"Erro ao ler {file}: {e}")

# Verifica se conseguiu ler arquivos
if dataframes:
    # Junta todos os DataFrames
    df_final = pd.concat(dataframes, ignore_index=True)

    # Salva o resultado
    df_final.to_csv("todos_os_jogos.csv", index=False, encoding="utf-8-sig")
    print(f"{len(csv_files)} arquivos combinados com sucesso!")
    print(f"Total de linhas no CSV final: {len(df_final)}")
else:
    print("Nenhum arquivo CSV foi carregado.")
