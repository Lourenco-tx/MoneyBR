import sqlite3
import random

# Lista de nomes e dados fictícios para evitar dependências externas complexas
nomes_pf = [
    "Ana Silva", "Bruno Costa", "Carlos Souza", "Daniela Lima", "Eduardo Rocha",
    "Fernanda Montes", "Gabriel Neves", "Helena Farias", "Igor Guimarães", "Julia Paiva",
    "Kevin Oliveira", "Larissa Duarte", "Márcio Terra", "Nádia Sol", "Otávio Luna"
]

sobrenomes = ["Oliveira", "Santos", "Pereira", "Ferreira", "Alves", "Machado", "Ribeiro"]

nomes_pj = [
    "Tecnologia Global Ltda", "Logística Expressa S.A.", "Construções Alvorada",
    "Papelaria Central", "Supermercado Horizonte", "Auto Peças União",
    "Consultoria Prime", "Restaurante Sabor Real", "Farmácia Vida", "Oficina Mecânica Precision"
]


def gerar_documento(tipo):
    if tipo == 1:  # CPF fictício
        return f"{random.randint(100, 999)}.{random.randint(100, 999)}.{random.randint(100, 999)}-{random.randint(10, 99)}"
    else:  # CNPJ fictício
        return f"{random.randint(10, 99)}.{random.randint(100, 999)}.{random.randint(100, 999)}/0001-{random.randint(10, 99)}"


def popular_tabela():
    conn = sqlite3.connect('entidades.db')
    cursor = conn.cursor()

    print("Iniciando a inserção de 50 registros...")

    for i in range(50):
        # Define o Tipo (1 ou 2)
        tipo = random.choice([1, 2])

        # Define a Classificação (1 a 5)
        classificacao = random.choice([1, 2, 3, 4, 5])

        # Define o Nome baseado no Tipo
        if tipo == 1:
            nome = random.choice(nomes_pf) + " " + random.choice(sobrenomes)
        else:
            nome = random.choice(nomes_pj) + " " + str(random.randint(1, 100))

        documento = gerar_documento(tipo)
        endereco = f"Rua {random.choice(sobrenomes)}, nº {random.randint(1, 2000)}, Brasília-DF"
        email = f"{nome.lower().replace(' ', '.')}@exemplo.com.br"
        celular = f"(61) 9{random.randint(8000, 9999)}-{random.randint(1000, 9999)}"
        fixo = f"(61) 3{random.randint(3000, 3999)}-{random.randint(1000, 9999)}"

        try:
            cursor.execute('''
                           INSERT INTO entidades (classificacao, tipo, nome, documento, endereco, email, celular,
                                                  telefone_fixo)
                           VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                           ''', (classificacao, tipo, nome, documento, endereco, email, celular, fixo))
        except sqlite3.IntegrityError:
            # Caso o documento repetido (raro), apenas pula
            continue

    conn.commit()
    conn.close()
    print("50 registros inseridos com sucesso no banco 'entidades.db'!")


if __name__ == "__main__":
    popular_tabela()