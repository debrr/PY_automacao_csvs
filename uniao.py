from pathlib import Path
import pandas as pd
import re

# Definição dos caminhos
BASE_DIR = Path(__file__).resolve().parent
INPUT_DIR = BASE_DIR / "Inputs"
OUTPUT_DIR = BASE_DIR / "Outputs"

# Verificação de diretórios
if not INPUT_DIR.exists():
    raise FileNotFoundError(f"Pasta não encontrada: {INPUT_DIR}")

if not OUTPUT_DIR.exists():
    raise FileNotFoundError(f"Pasta não encontrada: {OUTPUT_DIR}")

# Listagem de arquivos
arquivos_csv = [
    f for f in INPUT_DIR.iterdir()
    if f.is_file() and f.suffix.lower() == ".csv"
]

if not arquivos_csv:
    raise FileNotFoundError(
        f"Nenhum arquivo CSV encontrado em: {INPUT_DIR}"
    )

# Função para extração de número do nome do arquivo
def extrair_numero(nome_arquivo):
    match = re.search(r"(\d+)", nome_arquivo.stem)
    if match:
        return int(match.group(1))
    return -1

# Ordenação dos arquivos
arquivos_ordenados = sorted(
    arquivos_csv,
    key=extrair_numero
)

dataframes = []

# Leitura dos arquivos com tratamento de encoding
for arquivo in arquivos_ordenados:
    try:
        df = pd.read_csv(
            arquivo,
            sep=";",
            encoding="utf-8"
        )
    except UnicodeDecodeError:
        df = pd.read_csv(
            arquivo,
            sep=";",
            encoding="latin1"
        )
    dataframes.append(df)

# Concatenação dos dados
df_final = pd.concat(
    dataframes,
    ignore_index=True
)

colunas_data = [
    "Data de abertura",
    "Última atualização"
]

# Formatação das colunas de data
for col in colunas_data:
    if col in df_final.columns:
        df_final[col] = pd.to_datetime(
            df_final[col],
            dayfirst=True,
            errors="coerce"
        ).dt.strftime("%d/%m/%Y")

arquivo_saida = OUTPUT_DIR / "tabela_unificada.xlsx"

# Remoção do arquivo antigo, se existir
if arquivo_saida.exists():
    arquivo_saida.unlink()

# Salvando o resultado em Excel
with pd.ExcelWriter(
    arquivo_saida,
    engine="openpyxl"
) as writer:
    df_final.to_excel(
        writer,
        index=False,
        sheet_name="Dados"
    )

print(f"Arquivo gerado com sucesso: {arquivo_saida}")