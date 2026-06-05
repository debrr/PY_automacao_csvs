# União CSVs

Script em Python que consolida múltiplos arquivos CSV em um único arquivo Excel.

## O que faz

- Lê todos os arquivos CSV da pasta `Inputs`
- Assume separador `;` e tenta encoding UTF-8 (fallback para Latin-1)
- Ordena os arquivos pelo número presente no nome do arquivo
- Concatena todas as tabelas (mesma estrutura de colunas)
- Converte as colunas "Data de abertura" e "Última atualização" para o formato `dd/mm/aaaa`
- Gera um arquivo `tabela_unificada.xlsx` na pasta `Outputs`

## Estrutura
```text
projeto/
├── Inputs/      # Coloque os CSVs aqui
├── Outputs/     # Onde o arquivo unificado será salvo
├── uniao.py     # Script principal
└── README.md
```


## Formato dos arquivos

Os arquivos CSV devem ter:
- Separador: `;`
- Mesma estrutura de colunas
- Nomes no formato: `nome(1).csv`, `nome(2).csv`, `nome(3).csv` (o número entre parênteses define a ordem de concatenação)

## Como usar
1. Instalar dependências:
   ```bash
   pip install pandas openpyxl
2. Colocar os CSVs na pasta Inputs
3. Executar script
4. Obter resultado em Outputs/tabela_unificada.xlsx
