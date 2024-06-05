import pandas as pd
from classes.Personas import Persona

class Trabajador(Persona):
    def __init__(self, full_name, year_of_birth, gender, zipcode, working_hours, position, category, start_date, id=None):
        super().__init__(full_name, year_of_birth, gender, zipcode,id)
        self.start_date = start_date
        self.position = position
        self.category = category
        self.working_hours = working_hours
    
    def __repr__(self):
        return f"Trabajador({self.id}, {self.position}, {self.category}, {self.working_hours}, {self.start_date})"

    def write_df(self, df_workers):
        # Este método recibe el dataframe de usuarios y agrega el usuario
        # Si el id es None, toma el id más alto del DF y le suma uno. Si el
        # id ya existe, no lo agrega y devuelve un error.
        if self.id in df_workers['id'].values:
            raise ValueError("El ID ya existe")
        if self.id is None:
            self.id = 1 + df_workers['id'].max()
        
        worker = {
          'id': self.id, 
          'Position': self.position,
          'Category': self.category,
          'Working Hours': self.working_hours,
          'Start Date': self.start_date
        }
        
        worker_df = pd.DataFrame([worker])
        df_workers = pd.concat([df_workers, worker_df], ignore_index=True)
        return df_workers
    
    @classmethod
    def create_df_from_csv(cls, filename):
        # Este class method recibe el nombre de un archivo csv, valida su
        # estructura y devuelve un DataFrame con la información cargada del
        # archivo 'filename'.
        df_workers = pd.read_csv(filename)
        if list(df_workers.columns) != ['id','Position','Category','Working Hours','Start Date']:
            raise ValueError("NO tiene la estructura de Trabajador")
        return df_workers

    def remove_from_df(self, df_workers):
        # Borra del DataFrame el objeto contenido en esta clase.
        # Para realizar el borrado todas las propiedades del objeto deben coincidir
        # con la entrada en el DF. Caso contrario imprime un error.

        query = (
            (df_workers['id'] == self.id)
            & (df_workers['Position'] == self.position)
            & (df_workers['Category'] == self.category)
            & (df_workers['Working Hours'] == self.working_hours)
            & (df_workers['Start Date'] == self.start_date)
        )
        
        filtrado = df_workers[query]
      
        if filtrado.empty:
            raise ValueError("NO existe el usuario")

        # Si llegaste aquí, entonces el usuario existe
        # Acciones para borrar el usuario
        indice = filtrado.index
        df_workers = df_workers.drop(indice)
        return df_workers