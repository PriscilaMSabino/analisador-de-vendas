# 📊 Analisador de Vendas

Ferramenta de análise de dados de vendas desenvolvida com **Python, Pandas e SQL**, utilizando **SQLite** para armazenamento e consultas dos dados.

## 🎯 Sobre o projeto

Este projeto foi desenvolvido como prática de análise de dados, com o objetivo de transformar dados de vendas em informações resumidas para facilitar a análise do faturamento.

O programa lê os dados de um arquivo CSV, realiza cálculos com Pandas, armazena os dados em um banco SQLite e executa consultas SQL para gerar diferentes análises.

## 🔎 Análises realizadas

O programa apresenta:

* Faturamento total
* Faturamento por produto
* Faturamento por categoria
* Faturamento por cliente

Os resultados são organizados em ordem decrescente de faturamento para facilitar a visualização.

## 🛠️ Tecnologias utilizadas

* Python
* Pandas
* SQL
* SQLite
* Git e GitHub

## 📁 Estrutura do projeto

```text
analisador-de-vendas/
├── analisador.py
├── vendas.csv
├── README.md
└── .gitignore
```

> O banco de dados SQLite é criado automaticamente quando o programa é executado.

## ▶️ Como executar

### 1. Clonar o repositório

```bash
git clone URL_DO_REPOSITORIO
```

### 2. Criar e ativar o ambiente virtual

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Instalar as dependências

```bash
python -m pip install pandas
```

### 4. Executar o programa

```bash
python analisador.py
```

## 📚 Aprendizados

Este projeto foi desenvolvido para praticar:

* Manipulação de dados com Pandas
* Leitura de arquivos CSV
* Criação de cálculos a partir dos dados
* Utilização de banco de dados SQLite
* Consultas SQL com `SELECT`, `SUM`, `GROUP BY` e `ORDER BY`
* Integração entre Python, Pandas e SQL
* Versionamento utilizando Git e GitHub

## 👩‍💻 Sobre

Projeto desenvolvido por **Priscila Sabino** como parte dos estudos em Ciência da Computação e prática de análise de dados.
