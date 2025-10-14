import sqlite3
from pathlib import Path

conexao = sqlite3.connect(ROOT_PATH / "clientes.db")
print(conexao)
