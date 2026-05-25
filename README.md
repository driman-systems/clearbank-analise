# ClearBank Análise Financeira

Projeto desenvolvido em Python para leitura, validação e análise de transações bancárias a partir de um arquivo CSV.

## Descrição

O objetivo do projeto é processar um arquivo `transacoes.csv`, validar os dados, descartar registros inválidos, agrupar as transações por mês, calcular métricas financeiras e identificar transações potencialmente suspeitas.

O relatório final é exibido no notebook e também exportado para o arquivo `relatorio.json`.

## Tecnologias utilizadas

- Python 3.10+
- Google Colab
- csv
- json
- datetime

## Arquivos do projeto

- `desafio-final.ipynb`: notebook principal com a análise.
- `transacoes.csv`: arquivo de entrada com as transações bancárias.
- `relatorio.json`: arquivo gerado com o resultado da análise.
- `README.md`: documentação do projeto.

## Como executar

1. Abra o arquivo `desafio-final.ipynb` no Google Colab ou Jupyter Notebook.
2. Certifique-se de que o arquivo `transacoes.csv` está disponível no caminho configurado no notebook.
3. Execute todas as células em ordem.
4. Ao final da execução, o relatório será exibido no terminal do notebook.
5. O arquivo `relatorio.json` será gerado automaticamente.

## Funcionalidades

- Leitura de arquivo CSV com `csv.DictReader`.
- Tratamento de erro caso o arquivo CSV não seja encontrado.
- Validação de campos obrigatórios.
- Conversão de datas com `datetime`.
- Conversão e validação de valores numéricos.
- Agrupamento mensal das transações.
- Cálculo de total de créditos, total de débitos, saldo, média, maior e menor valor.
- Identificação de transações suspeitas acima de R$ 10.000,00.
- Exportação do resultado em JSON.

## Saídas geradas

O notebook gera:

- Relatório financeiro mensal exibido no terminal.
- Arquivo `relatorio.json` com os dados processados.