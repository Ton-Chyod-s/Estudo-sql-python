import psycopg2 as db
import csv
import os

#configuração inicial do servidor --recomendado criar um jason para incluir os dados
class Config:
    def __init__(self):
        self.config = {
            "postgres": {
                "user": "postgres",
                "password": "123",
                "host": "localhost",
                "port": "5432",
                "database": "myframe"
            }
        }

#configurando a biblioteca para ter essa conecção
class Conection(Config):
    def __init__(self):
        Config.__init__(self)
        try:
            self.conn = db.connect(**self.config["postgres"])
            self.cur = self.conn.cursor()
        except Exception as e:
            print("erro na conecção", e)
            exit(1)

    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.commit()
        self.cur.close()
        self.conn.close()

    @property
    def conection(self):
        return self.conn
    
    @property
    def cursor(self):
        return self.cur
    
    def commit(self):
        self.conn.commit()

    def fetchall(self):
        return self.cursor.fetchall()
    
    def execute(self, sql, params=None):
        self.cursor.execute(sql, params or ())

    def query(self, sql, params=None):
        self.cursor.execute(sql, params or ())
        return self.fetchall()


class Person(Conection):
    def __init__(self):
        Conection.__init__(self)
    
    #inserir pelo nome
    def insert(self, *args):
        try:
            sql = "INSERT INTO person (name) VALUES (%s)"
            self.execute(sql, args)
            self.commit()
        except Exception as e:
            print("Erro ao inserir", e)

    #inserir por arquivo csv
    def insert_csv(self,filename):
        try:
            data = csv.DictReader(open(filename, encoding="utf-8"))
            for row in data:
                self.insert(row["name"])
            print("Registro inserido")
        except Exception as e:
            print("Erro ao inserir", e)

    #deletar uma linha por id
    def delete(self, id):
        try:
            sql_s = f"SELECT * FROM person WHERE id = {id}"
            if not self.query(sql_s):
                return "Registro não encontrado para deletar"
            sql_d = f"DELETE FROM person WHERE id = {id}"
            self.execute(sql_d)
            self.commit()
            return "Registro deletado"
        
        except Exception as e:
            print("Erro ao deletar", e)

    #fazer atualização de valores
    def update(self, id, *args):
        try:
            sql = f"UPDATE person SET name = %s WHERE id = {id}"
            self.execute(sql, args)
            self.commit()
            print("Registro atualizado")

        except Exception as e:
            print("Erro ao atualizar", e)

    #procurar por um indice no banco de dados
    def search(self, *args, type_s="name"):
        sql = "SELECT * FROM person WHERE name LIKE %s"
        if type_s == "id":
            sql = "SELECT * FROM person WHERE id = %s"
        data =  self.query(sql, args)
        if data:
            return data
        return "Registro não encontrado"


if __name__ == "__main__":
    person = Person()
    print(person.query("SELECT * FROM person"))
    #person.insert("josé") Adicionando um nome na tabela ja feita no sgbd
    #person.insert_csv(os.path.abspath("data.csv")) Inserirndo nomes pelo arquivo csv
    #print(person.delete(7)) Deletando pelo id
    #person.update(9, "lavinha oliveira") Fazendo a atualização de valores
    print(person.search("lavinha")) #Procurando pelo nome ou id

    