# Cria uma lista de bancos de dados com os nomes presentes na lista dblist

import os

from util.dblist import dblist

if __name__ == "__main__":
    print("DB CREATION STARTED")
    for db in dblist:
        os.system("createdb --host localhost --username postgres --password postgres" + db)
    print("DB CREATION END WITH SUCCESS")
