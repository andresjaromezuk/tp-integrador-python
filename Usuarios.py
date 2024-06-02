import pandas as pd
from datetime import datetime

class Usuario:
    def __init__(self, occupation, active_since, id = None):
        self.occupation = occupation
        self.active_since = active_since
        self.id = id

    def __repr__(self):
        return f"Usuario({self.occupation}, {self.active_since}, {self.id})"

    def write_df(self, df_usuarios):
        # Este método recibe el dataframe de usuarios y agrega el usuario
        # Si el id es None, toma el id más alto del DF y le suma uno. Si el
        # id ya existe, no lo agrega y devuelve un error.
        if self.id in df_usuarios['id'].values:
            raise ValueError("El ID ya existe")
        if self.id is None:
            self.id = 1 + df_usuarios['id'].max()
        
        usuario = {
            "id": self.id,
            "Occupation": self.occupation,
            "Active Since": self.active_since
        }
        
        usuario_df = pd.DataFrame([usuario])
        df_usuarios = pd.concat([df_usuarios, usuario_df], ignore_index=True)
        return df_usuarios

    def remove_from_df(self, df_usuarios):
        # Borra del DataFrame el objeto contenido en esta clase.
        # Para realizar el borrado todas las propiedades del objeto deben coincidir
        # con la entrada en el DF. Caso contrario imprime un error.

        query = (
            (df_usuarios['id'] == self.id)
            & (df_usuarios['Occupation'] == self.occupation)
            & (df_usuarios['Active Since'] == self.active_since)
        )
        
        filtrado = df_usuarios[query]
      
        if filtrado.empty:
            raise ValueError("NO existe el usuario")

        # Si llegaste aquí, entonces el usuario existe
        # Acciones para borrar el usuario
        indice = filtrado.index
        df_usuarios = df_usuarios.drop(indice)
        return df_usuarios