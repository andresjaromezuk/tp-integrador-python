#%%
import pandas as pd

class Pelicula:
    def __init__(self, nombre, anio, generos, id = None):
        self.nombre = nombre
        self.anio = anio
        self.generos = generos
        self.id = id

    def __repr__(self):
        return f"Pelicula({self.nombre}, {self.anio}, {self.generos}, {self.id})"

    def write_df(self, df_mov):
        # Este método recibe el dataframe de películas y agrega la película
        # Si el id es None, toma el id más alto del DF y le suma uno. Si el 
        # id ya existe, no la agrega y devuelve un error.

        # if self.id is None:
        #     self.id = df_mov['id'].max() + 1
        # if self.id in df_mov['id'].values:
        #     raise ValueError("El ID ya existe.")
        # df_mov = df_mov.append({
        #     'id': self.id, 
        #     'nombre': self.nombre, 
        #     'anio': self.anio, 
        #     'generos': self.generos
        # }, ignore_index=True)
        # return df_mov

        pelicula = {
            'id': self.id,
            'Name': self.nombre,
            'Release Date': self.anio,
            'IMDB URL': '',
            'unknown': 0,
            'Action': 0,
            'Adventure': 0,
            'Animation': 0,
            'Children\'s': 0,
            'Comedy': 0,
            'Crime': 0,
            'Documentary': 0,
            'Drama': 0,
            'Fantasy': 0,
            'Film-Noir': 0,
            'Horror': 0,
            'Musical': 0,
            'Mystery': 0,
            'Romance': 0,
            'Sci-Fi': 0,
            'Thriller': 0,
            'War': 0,
            'Western': 0,
        }

        for g in self.generos:
            pelicula[g] = 1

        if self.id is None:
            pelicula['id'] = int(df_mov['id'].max()) + 1
            print(pelicula['id'])
        elif self.id in df_mov['id'].values:
            raise ValueError("El ID ya existe.")
        film_df = pd.DataFrame([pelicula])
        print(film_df)
        new_df = pd.concat([df_mov, film_df], ignore_index=True)
        #df_mov.loc[len(df_mov)] = [self.id, self.nombre, self.anio, self.generos]
        new_df.to_csv('peliculas.csv', index = False)
        return df_mov  
    
    @classmethod
    def create_df_from_csv(cls, filename):
        # Este class method recibe el nombre de un archivo csv, valida su 
        # estructura y devuelve un DataFrame con la información cargada del
        # archivo 'filename'.
        ###
        df_mov = pd.read_csv(filename)
        ###
        return df_mov
    #def get_from_df(cls, df_mov, id=None, nombre = None, anios = None, generos = None):
    #     # Este class method devuelve una lista de objetos 'Pelicula' buscando por:
    #     # id: id
    #     # nombre: nombre de la película
    #     # anios: [desde_año, hasta_año]
    #     # generos: [generos]
        #return lista_peliculas
     
     #def get_stats(cls,df_mov, anios=None, generos=None):
        # Este class method imprime una serie de estadísticas calculadas sobre
        # los resultados de una consulta al DataFrame df_mov. 
        # Las estadísticas se realizarán sobre las filas que cumplan con los requisitos de:
        # anios: [desde_año, hasta_año]
        # generos: [generos]
        # Las estadísticas son:
        # - Datos película más vieja
        # - Datos película más nueva
        # - Bar plots con la cantidad de películas por año/género.
    def remove_from_df(self, df_mov):
        # Borra del DataFrame el objeto contenido en esta clase.
        # Para realizar el borrado todas las propiedades del objeto deben coincidir
        # con la entrada en el DF. Caso contrario imprime un error.
        query = (
            (df_mov['id'] == self.id) 
            & (df_mov['Name'] == self.nombre) 
            & (df_mov['Release Date'] == self.anio)
            #& (df_mov['Release Date'] == self.anio)
        )
        filtrado = df_mov[query].index
        df_mov = df_mov.drop(filtrado)
        if filtrado == True:
            raise ValueError("El dato no tiene errores")
        return df_mov
        #Qué hace este método??? Borra en True o False???

#%%

pelicula = Pelicula("Película", "1960", ['Action', 'Drama'])
peliculas = Pelicula.create_df_from_csv('peliculas.csv')

#pelicula.write_df(peliculas)
#peliculas

pelicula2 = Pelicula("Scream of Stone (Schrei aus Stein) (1991)", "08-Mar-1996","", 1682.0)
pelicula2.remove_from_df(peliculas)
# %%
