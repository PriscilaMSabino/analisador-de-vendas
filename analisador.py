import pandas as pd
import sqlite3

# Ler os dados do arquivo CSV
vendas = pd.read_csv("vendas.csv")

# Calcular o valor total de cada venda
vendas["valor_total"] = vendas["quantidade"] * vendas["valor_unitario"]

# Criar/conectar ao banco de dados SQLite
conexao = sqlite3.connect("vendas.db")

# Salvar os dados no banco de dados
vendas.to_sql("vendas", conexao, if_exists="replace", index=False)


# ==========================================================
# 1. FATURAMENTO TOTAL
# ==========================================================

consulta_faturamento = """
SELECT SUM(valor_total)
FROM vendas
"""

resultado = conexao.execute(consulta_faturamento).fetchone()

print("\n=== FATURAMENTO TOTAL ===")
print(f"R$ {resultado[0]:.2f}")


# ==========================================================
# 2. FATURAMENTO POR PRODUTO
# ==========================================================

consulta_produtos = """
SELECT produto, SUM(valor_total) AS faturamento
FROM vendas
GROUP BY produto
ORDER BY faturamento DESC
"""

resultado_produtos = conexao.execute(consulta_produtos).fetchall()

print("\n=== FATURAMENTO POR PRODUTO ===")

for produto, faturamento in resultado_produtos:
    print(f"{produto}: R$ {faturamento:.2f}")


# ==========================================================
# 3. FATURAMENTO POR CATEGORIA
# ==========================================================

consulta_categorias = """
SELECT categoria, SUM(valor_total) AS faturamento
FROM vendas
GROUP BY categoria
ORDER BY faturamento DESC
"""

resultado_categorias = conexao.execute(consulta_categorias).fetchall()

print("\n=== FATURAMENTO POR CATEGORIA ===")

for categoria, faturamento in resultado_categorias:
    print(f"{categoria}: R$ {faturamento:.2f}")


# ==========================================================
# 4. FATURAMENTO POR CLIENTE
# ==========================================================

consulta_clientes = """
SELECT cliente, SUM(valor_total) AS faturamento
FROM vendas
GROUP BY cliente
ORDER BY faturamento DESC
"""

resultado_clientes = conexao.execute(consulta_clientes).fetchall()

print("\n=== FATURAMENTO POR CLIENTE ===")

for cliente, faturamento in resultado_clientes:
    print(f"{cliente}: R$ {faturamento:.2f}")


# Fechar a conexão com o banco
conexao.close()