import sqlite3
database = "Persona.db"
class DB:
    def ejecutar_consulta(self,consulta,parametros=()):
        with sqlite3.connect(persona) as conn:
            self.cursor = conn.cursor()
            result = self.cursor.execute(consulta, parametros)
            conn.commit()
            return result