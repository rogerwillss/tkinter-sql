from conexao import conectar

def inserir_produto(descricao, valor):
    conexao = conectar()
    if conexao:
        cursor = conexao.cursor()
        sql = "INSERT INTO produtos (descricao, valor) VALUES (%s, %s)"
        valores = (descricao,valor)
        cursor.execute(sql, valores)
        conexao.commit()
        cursor.close()
        conexao.close()

# Função para listar produtos
def listar_produtos():
    con = conectar()
    cursor = con.cursor()
    cursor.execute("SELECT descricao, valor FROM produtos")
    resultado = cursor.fetchall()  # retorna lista de tuplas
    cursor.close()
    con.close()
    return resultado

def excluir_produto(id_produto):
    con = conectar()
    cursor = con.cursor()
    cursor.execute("DELETE FROM produtos WHERE id_produtos = %s", (id_produto,))
    con.commit()
    cursor.close()
    con.close()