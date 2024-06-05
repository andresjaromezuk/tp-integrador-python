import pandas as pd

class Persona:

    def __init__(self, full_name, year_of_birth, gender, zipcode, id = None):
        self.full_name = full_name
        self.year_of_birth = year_of_birth
        self.gender = gender
        self.zipcode = zipcode
        self.id = id

    def __repr__(self):
        return f"Persona({self.id}, {self.full_name}, {self.year_of_birth}, {self.gender}, {self.zipcode})"

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
            'Full Name': self.full_name,
            'year of birth': self.year_of_birth,
            'Gender': self.gender,
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
        df_personas = pd.read_csv(filename)
        if list(df_personas.columns) != ['id','Full Name','year of birth','Gender','Zip Code']:
            raise ValueError("NO tiene la estructura de Persona")
        return df_personas
        
    def remove_from_df(self, df_personas):
        # Borra del DataFrame el objeto contenido en esta clase.
        # Para realizar el borrado todas las propiedades del objeto deben coincidir
        # con la entrada en el DF. Caso contrario imprime un error.

        query = (
            (df_personas['id'] == self.id)
            & (df_personas['Full Name'] == self.full_name)
            & (df_personas['year of birth'] == self.year_of_birth)
            & (df_personas['Gender'] == self.gender)
            & (df_personas['Zip Code'] == self.zipcode)
        )
        
        filtrado = df_personas[query]
      
        if filtrado.empty:
            raise ValueError("NO existe el usuario")

        # Si llegaste aquí, entonces el usuario existe
        # Acciones para borrar el usuario
        indice = filtrado.index
        df_personas = df_personas.drop(indice)
        return df_personas