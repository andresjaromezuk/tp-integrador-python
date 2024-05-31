

import pandas as pd
from datetime import datetime
from helper import save_one

ATRIBUTOS_VALIDOS = [
    "id",
    "Name",
    "Release Date",
    "IMDB URL",
    "unknown",
    "Action",
    "Adventure",
    "Animation",
    "Children's",
    "Comedy",
    "Crime",
    "Documentary",
    "Drama",
    "Fantasy",
    "Film-Noir",
    "Horror",
    "Musical",
    "Mystery",
    "Romance",
    "Sci-Fi",
    "Thriller",
    "War",
    "Western",
]
GENEROS_VALIDOS = ATRIBUTOS_VALIDOS[4:]
# Dict-comprehension: creamos en 1 linea un diccionario a partir de un iterador
DICT_GENEROS_DEFAULT = {genero: 0 for genero in GENEROS_VALIDOS}

class Pelicula:

    def __init__(self, nombre, anio, generos, imdb_url = None, id = None):
        self.nombre = nombre
        self.anio = anio
        self.generos = generos
        self.imdb_url = imdb_url
        self.id = id

    def __repr__(self):
        return f"Pelicula({self.nombre}, {self.anio}, {self.generos}, {self.id})"

    def write_df(self, df_movies):
        # Este método recibe el dataframe de películas y agrega la película
        # Si el id es None, toma el id más alto del DF y le suma uno. Si el
        # id ya existe, no la agrega y devuelve un error.
        if self.id in df_movies['id'].values:
            raise ValueError("El ID ya existe")
        if self.id is None:
            self.id = 1 + df_movies['id'].max()
        pelicula_id = {
            "id": self.id,
            "Name": self.nombre,
            "Release Date": self.anio,
            "IMDB URL": self.imdb_url,
            }
        pelicula_generos = DICT_GENEROS_DEFAULT.copy()
        for genero in self.generos:
            if genero in GENEROS_VALIDOS:
                pelicula_generos[genero] = 1
            else:
                pelicula_generos['unknown'] = 1
        # Union de diccionarios
        pelicula = pelicula_id | pelicula_generos
        film_df = pd.DataFrame([pelicula])
        df_movies = pd.concat([df_movies, film_df], ignore_index=True)
        # Guardar en el csv corresponde a otro metodo (save)
        # new_df.to_csv('peliculas.csv', index = False)
        return df_movies

    @classmethod
    def create_df_from_csv(cls, filename):
        # Este class method recibe el nombre de un archivo csv, valida su
        # estructura y devuelve un DataFrame con la información cargada del
        # archivo 'filename'.
        df_movies = pd.read_csv(filename)
        if list(df_movies.columns) != ATRIBUTOS_VALIDOS:
            raise ValueError("NO tiene la estructura de 'Peliculas'")
        return df_movies

    @classmethod
    def get_from_df(cls, df_movies, id=None, nombre=None, anios=None, generos=None):
        # Este class method devuelve una lista de objetos 'Pelicula' buscando por:
        # id: id
        # nombre: nombre de la película
        # anios: [desde_año, hasta_año]
        # generos: [generos]
        lista_peliculas = []

        # salida temprana en caso de que todos los args. sean "None"
        if all([id, nombre, anios, generos]) is None:
            return lista_peliculas
        if id is not None:
            df = df_movies[df_movies['id'] == id]
        if nombre is not None:
            df = df_movies[df_movies['Name'] == nombre]
        if anios is not None:
            desde_anio, hasta_anio = anios
            desde_anio = datetime.strptime(desde_anio, '%d-%b-%Y')
            hasta_anio = datetime.strptime(hasta_anio, '%d-%b-%Y')
            index_anios = [index for index, anio in enumerate(df_movies['Release Date']) if str(anio) != 'nan' and desde_anio <= datetime.strptime(anio, '%d-%b-%Y') <= hasta_anio ]
            df = df_movies.iloc[index_anios]
        if generos is not None:
            df= [df_movies[df_movies[x] == 1] for x in generos][0]
        
        #Bloque para devolver en formato lista
        for index, movie in enumerate(df.values):
            id = df['id'].values[index]
            nombre = df['Name'].values[index]
            fecha_completa = df['Release Date'].values[index]
            bool_indexer = df.iloc[0, 4:] == 1
            generos = df.columns[4:][bool_indexer].tolist()
            lista_peliculas.append(Pelicula(nombre, fecha_completa, generos, id=id))
        return lista_peliculas

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
        )
        
        filtrado = df_mov[query]
      
        if filtrado.empty:
            raise ValueError("NO existe la pelicula")
        
        genres = filtrado[self.generos]
     
        if False in (genres.values == 1):
            raise ValueError("NO existe la pelicula")

        # Si llegaste aquí, entonces la película existe
        # Acciones para borrar la película
        indice = filtrado.index
        df_mov = df_mov.drop(indice)
        return df_mov
    
    @classmethod
    def save(cls, df):
        save_one('peliculas.csv', df)

