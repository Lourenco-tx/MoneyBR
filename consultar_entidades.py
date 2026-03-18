import sqlite3


def ver_cadastro_completo():
    try:
        conn = sqlite3.connect('entidades.db')
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()

        # Dicionários para traduzir os códigos numéricos para texto legível
        mapa_classificacao = {1: "Func.", 2: "Fornec.", 3: "Cliente", 4: "Ent. Públ.", 5: "Outros"}
        mapa_tipo = {1: "Pessoa Física (PF)", 2: "Pessoa Jurídica (PJ)"}

        cursor.execute("SELECT * FROM entidades")
        registros = cursor.fetchall()

        print("=" * 90)
        print(f"{'CADASTRO GERAL DE ENTIDADES - MONEYBR':^90}")
        print("=" * 90)

        for r in registros:
            # Tradução dos códigos
            txt_tipo = mapa_tipo.get(r['tipo'], "N/A")
            txt_class = mapa_classificacao.get(r['classificacao'], "N/A")

            # Bloco de Informações Principais
            print(f"ID: {r['id']:03} | {r['nome'].upper()}")
            print(f"TIPO: {txt_tipo:<20} | CLASSIFICAÇÃO: {txt_class}")
            print(f"DOC:  {r['documento']:<20} | E-MAIL: {r['email']}")

            # Bloco de Contato e Localização
            print(f"TEL:  {r['celular']} (Cel) / {r['telefone_fixo']} (Fixo)")
            print(f"END:  {r['endereco']}")
            print("-" * 90)

        conn.close()
    except sqlite3.Error as e:
        print(f"Erro ao acessar banco: {e}")


if __name__ == "__main__":
    ver_cadastro_completo()