import sqlite3

def criar_banco_entidades():
    # Conecta ou cria o arquivo do banco de dados
    conn = sqlite3.connect('entidades.db')
    cursor = conn.cursor()

    # Criação da tabela com chaves numéricas
    # 1. classificacao: 1=Func., 2=Fornec., 3=Cli., 4=Ent.Públ., 5=Outros
    # 2. tipo: 1=PF, 2=PJ
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS entidades (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            classificacao INTEGER NOT NULL, 
            tipo INTEGER NOT NULL,          
            nome TEXT NOT NULL,
            documento TEXT UNIQUE,       -- CPF ou CNPJ (apenas números)
            endereco TEXT,
            email TEXT,
            celular TEXT,
            telefone_fixo TEXT,
            data_cadastro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    conn.commit()
    conn.close()
    print("Sucesso: Banco 'entidades.db' configurado com classificações numéricas.")

if __name__ == "__main__":
    criar_banco_entidades()