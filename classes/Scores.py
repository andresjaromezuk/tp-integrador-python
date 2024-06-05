import pandas as pd


class Score():
    def __init__(self, user_id, movie_id, rating, date, id=None):
      self.user_id = user_id 
      self.movie_id = movie_id 
      self.rating = rating 
      self.date = date  
      self.id = id  

    def __repr__(self):
        return f"Score({self.id}, {self.user_id}, {self.movie_id}, {self.rating}, {self.date})"

    def write_df(self, df_scores):
        # Este método recibe el dataframe de usuarios y agrega el usuario
        # Si el id es None, toma el id más alto del DF y le suma uno. Si el
        # id ya existe, no lo agrega y devuelve un error.
        
        if self.id in df_scores['id'].values:
            raise ValueError("El ID ya existe")
        if self.id is None:
            self.id = 1 + df_scores['id'].max()
        
        score = {
          'id': self.id,
          'user_id': self.user_id,
          'movie_id': self.movie_id,
          'rating':self.rating,
          'Date':self.date
        }
        
        score_df = pd.DataFrame([score])
        df_scores = pd.concat([df_scores, score_df], ignore_index=True)
        return df_scores
    
    @classmethod
    def create_df_from_csv(cls, filename):
        # Este class method recibe el nombre de un archivo csv, valida su
        # estructura y devuelve un DataFrame con la información cargada del
        # archivo 'filename'.
        df_scores = pd.read_csv(filename)
        if list(df_scores.columns) != ['id','user_id','movie_id','rating','Date']:
          raise ValueError("NO tiene la estructura de Scores")
        else:
          df_scores.columns = ['id','user_id','movie_id','rating','Date']
        return df_scores
    
    @classmethod
    def get_stats(cls, df_movies, df_scores, df_people, df_users):
      merged_df = pd.merge(df_scores, df_movies, left_on='movie_id', right_on='id')

      #Scores agrupados por año
      merged_df['Release Date'] = merged_df['Release Date'].str[-4:]
      df_group_by_year = merged_df.groupby('Release Date')['rating'].mean()

      df_people_users = pd.merge(df_people, df_users, left_on='id', right_on='id')
      df_scores_people_users = pd.merge(df_people_users, df_scores, left_on='id', right_on='user_id')
      df_all_related = pd.merge(df_scores_people_users, df_movies, left_on='movie_id', right_on='id')
      
      #Scores agrupados por género (sexo)
      df_group_by_gender = df_all_related.groupby(['Name','Gender'])['rating'].mean()

      #Scores agrupados por ocupación
      df_group_by_occupation = df_all_related.groupby(['Name','Occupation'])['rating'].mean()

      return df_group_by_year, df_group_by_gender, df_group_by_occupation


    def remove_from_df(self, df_scores):
        # Borra del DataFrame el objeto contenido en esta clase.
        # Para realizar el borrado todas las propiedades del objeto deben coincidir
        # con la entrada en el DF. Caso contrario imprime un error.

        query = (
            (df_scores['id'] == self.id)
            & (df_scores['user_id'] == self.user_id)
            & (df_scores['movie_id'] == self.movie_id)
            & (df_scores['rating'] == self.rating)
            & (df_scores['Date'] == self.date)
        )
        
        filtrado = df_scores[query]
      
        if filtrado.empty:
            raise ValueError("NO existe el usuario")

        # Si llegaste aquí, entonces el usuario existe
        # Acciones para borrar el usuario
        indice = filtrado.index
        df_scores = df_scores.drop(indice)
        return df_scores