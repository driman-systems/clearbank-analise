# ClearBank Análise Financeira

Projeto de análise de transações bancárias desenvolvido em Python, com foco em validação de dados, consolidação mensal de indicadores financeiros e identificação de movimentações potencialmente suspeitas.

## Visão Geral

O projeto processa o arquivo `transacoes.csv`, aplica regras de validação sobre os registros, separa transações válidas e inválidas, calcula métricas financeiras por mês e exporta um relatório estruturado em JSON.

A solução principal utiliza bibliotecas nativas do Python para leitura, tratamento e exportação dos dados. O notebook também inclui uma etapa complementar de análise exploratória com `pandas`, `numpy` e `matplotlib`.

## Execução

O notebook pode ser aberto no Google Colab ou no Jupyter Notebook. A análise utiliza o arquivo `transacoes.csv` na raiz do repositório e gera os arquivos `relatorio.json` e `grafico.png` no mesmo diretório.

## Escopo da Análise

- Leitura de transações em formato CSV.
- Validação de campos obrigatórios.
- Conversão e validação de datas.
- Conversão e validação de valores monetários.
- Classificação de transações válidas e inválidas.
- Agrupamento mensal das movimentações.
- Cálculo de totais, saldo, média, maior valor e menor valor.
- Marcação de transações acima de R$ 10.000,00 como suspeitas.
- Exportação do relatório final em JSON.
- Geração de gráfico de saldo mensal.

## Tecnologias

- Python 3.10+
- Google Colab
- csv
- json
- datetime
- pandas
- numpy
- matplotlib

## Estrutura do Projeto

| Arquivo | Descrição |
| --- | --- |
| `desafio-final.ipynb` | Notebook principal da análise financeira. |
| `transacoes.csv` | Base de entrada com as transações bancárias. |
| `relatorio.json` | Relatório consolidado gerado pela análise. |
| `grafico.png` | Gráfico de saldo mensal. |
| `analise_pandas.py` | Versão complementar da análise com pandas. |
| `README.md` | Documentação do projeto. |

## Pipeline de Processamento

1. Carregamento dos registros do arquivo CSV.
2. Validação dos campos `id`, `data`, `cliente_id`, `tipo` e `valor`.
3. Separação entre registros válidos e inválidos.
4. Enriquecimento dos dados válidos com mês de referência e indicador de suspeita.
5. Consolidação mensal das métricas financeiras.
6. Cálculo do período total analisado.
7. Exportação do relatório em `relatorio.json`.
8. Análise complementar com DataFrame e visualização gráfica.

## Resultados

A base analisada contém 200 registros:

| Indicador | Valor |
| --- | ---: |
| Linhas lidas | 200 |
| Linhas válidas | 185 |
| Linhas inválidas | 15 |
| Transações suspeitas | 4 |
| Período analisado | 2026-01-01 a 2026-06-30 |

## Saídas

O processamento gera os seguintes artefatos:

- Relatório financeiro mensal exibido no notebook.
- `relatorio.json` com resumo mensal, totais e transações suspeitas.
- `grafico.png` com a evolução do saldo mensal.
