import sqlite3

con = sqlite3.connect("flashcards.db")
con.execute("PRAGMA foreign_keys = ON") #liga a checagem de FK por padrão, sem isso o cascade não roda

cur = con.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS pastas(id INTEGER PRIMARY KEY, titulo)")

cur.execute("CREATE TABLE IF NOT EXISTS cards(id INTEGER PRIMARY KEY, conteudo_frente, conteudo_verso, pasta_id, " \
            "FOREIGN KEY (pasta_id) REFERENCES pastas(id) ON DELETE CASCADE)")
con.commit()

def criar_pasta(con, titulo):
    con.execute(" INSERT INTO pastas (titulo) VALUES(?)",(titulo,))
    con.commit()
    return con.execute("SELECT last_insert_rowid()").fetchone()[0]

def criar_card(con, conteudo_frente, conteudo_verso, pasta_id):
    con.execute("INSERT INTO cards (conteudo_frente, conteudo_verso, pasta_id) VALUES(?,?,?)", (conteudo_frente, conteudo_verso, pasta_id))
    con.commit()
    return con.execute("SELECT last_insert_rowid()").fetchone()[0]

def listar_pastas(con):
    return con.execute("SELECT * FROM pastas").fetchall()

def listar_cards(con, pasta_id):
    return con.execute("SELECT * FROM cards WHERE pasta_id = ? ORDER BY id", (pasta_id,)).fetchall()

def editar_card(con, card_id, nova_frente, novo_verso):
    con.execute("UPDATE cards SET conteudo_frente = ? , conteudo_verso = ? WHERE id = ?",(nova_frente, novo_verso, card_id))
    con.commit()

def editar_pasta(con, pasta_id,novo_titulo):
    con.execute("UPDATE pastas SET titulo = ? WHERE id = ?",(novo_titulo, pasta_id))
    con.commit()

def deletar_pasta(con, pasta_id):
    con.execute("DELETE FROM pastas WHERE id = ?", (pasta_id,))
    con.commit()

def buscar_pasta(con, pasta_id):
    return con.execute("SELECT titulo FROM pastas WHERE id = ?", (pasta_id,)).fetchone()[0]

def buscar_card(con, card_id):
    return con.execute("SELECT conteudo_frente, conteudo_verso FROM cards WHERE id = ?", (card_id,)).fetchone()