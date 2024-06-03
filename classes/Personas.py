import pandas as pd

class Persona:

    def __init__(self, nombre_completo, año_nacimiento, genero, zipcode, id = None):
        self.nombre_completo = nombre_completo
        self.año_nacimiento = año_nacimiento
        self.genero = genero
        self.zipcode = zipcode
        self.id = id

    def __repr__(self):
        return f"Persona({self.id}, {self.nombre_completo}, {self.año_nacimiento}, {self.genero}, {self.zipcode})"

    def write_df(self, df_personas):
        # Este método recibe el dataframe de usuarios y agrega el usuario
        # Si el id es None, toma el id más alto del DF y le suma uno. Si el
        # id ya existe, no lo agrega y devuelve un error.
        if self.id in df_personas['id'].values:
            raise ValueError("El ID ya existe")
        if self.id is None:
            self.id = 1 + df_personas['id'].max()
        
        persona = {
            'id': self.id,
            'Full Name': self.nombre_completo,
            'year of birth': self.año_nacimiento,
            'Gender': self.genero,
            'Zip Code': self.zipcode
        }
        
        persona_df = pd.DataFrame([persona])
        df_personas = pd.concat([df_personas, persona_df], ignore_index=True)
        return df_personas
    
    @classmethod
    def create_df_from_csv(cls, filename):
        # Este class method recibe el nombre de un archivo csv, valida su
        # estructura y devuelve un DataFrame con la información cargada del
        # archivo 'filename'.
        df_users = pd.read_csv(filename)
        if list(df_users.columns) != ['id','Full Name','year of birth','Gender','Zip Code']:
            raise ValueError("NO tiene la estructura de Usuarios")
        return df_users

    def remove_from_df(self, df_usuarios):
        # Borra del DataFrame el objeto contenido en esta clase.
        # Para realizar el borrado todas las propiedades del objeto deben coincidir
        # con la entrada en el DF. Caso contrario imprime un error.

        query = (
            (df_usuarios['id'] == self.id)
            & (df_usuarios['Full Name'] == self.nombre_completo)
            & (df_usuarios['year of birth'] == self.año_nacimiento)
            & (df_usuarios['Gender'] == self.genero)
            & (df_usuarios['Zip Code'] == self.zipcode)
        )
        
        filtrado = df_usuarios[query]
      
        if filtrado.empty:
            raise ValueError("NO existe el usuario")

        # Si llegaste aquí, entonces el usuario existe
        # Acciones para borrar el usuario
        indice = filtrado.index
        df_usuarios = df_usuarios.drop(indice)
        return df_usuarios