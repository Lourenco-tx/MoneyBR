import sqlite3

def inicializar_banco():
    # Conecta ao arquivo (ele será criado se não existir)
    conexao = sqlite3.connect('moneybr.db')
    cursor = conexao.cursor()

    # Criando a tabela com as colunas da sua imagem
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS transacoes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            data TEXT NOT NULL,
            favorecido TEXT NOT NULL,
            categoria_id INTEGER,
            subcategoria_id INTEGER,
            descricao TEXT,
            tipo_cd INTEGER, -- 1 para Crédito, 0 para Débito
            valor REAL NOT NULL
        )
    ''')

    conexao.commit()
    conexao.close()
    print("Banco de dados 'moneybr.db' atualizado com sucesso!")

if __name__ == "__main__":
    inicializar_banco()