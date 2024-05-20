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
        
    
    
    
    def create_df_from_csv(cls, filename):
        # Este class method recibe el nombre de un archivo csv, valida su 
        # estructura y devuelve un DataFrame con la información cargada del
        # archivo 'filename'.
        ###
        #Código
        ###
        return df_mov
    def get_from_df(cls, df_mov, id=None, nombre = None, anios = None, generos = None):
        # Este class method devuelve una lista de objetos 'Pelicula' buscando por:
        # id: id
        # nombre: nombre de la película
        # anios: [desde_año, hasta_año]
        # generos: [generos]
        return lista_peliculas
     def get_stats(cls,df_mov, anios=None, generos=None):
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