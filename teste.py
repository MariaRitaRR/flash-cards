from database import con

con.execute("DELETE FROM pastas")
con.commit()
from database import criar_pasta
criar_pasta(con, "Biologia")
criar_pasta(con, "História")


from database import listar_pastas, deletar_pasta
print("antes:", listar_pastas(con))
deletar_pasta(con, 1)          # troca 1 por um id que exista
print("depois:", listar_pastas(con))