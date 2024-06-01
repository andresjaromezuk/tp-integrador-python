import pandas as pd
#from Peliculas import Pelicula

def load_all(
        file_personas,
        file_trabajadores,
        file_usuarios,
        file_peliculas,
        file_scores,
    ):
    df_personas = pd.read_csv(file_personas)
    df_trabajadores = pd.read_csv(file_trabajadores)
    df_usuarios = pd.read_csv(file_usuarios)
    df_peliculas = pd.read_csv(file_peliculas)
    df_scores = pd.read_csv(file_scores)
    return df_personas, df_trabajadores, df_usuarios, df_peliculas, df_scores

def save_one(file_name, df):
    return df.to_csv(file_name, index = False)

def save_all(
        df_personas,
        df_trabajadores, 
        df_usuarios, 
        df_peliculas, 
        df_scores, 
        file_personas="personas.csv", 
        file_trabajadores="trabajadores.csv", 
        file_usuarios="usuarios.csv", 
        file_peliculas="peliculas.csv", 
        file_scores="scores.csv"):
        try:
            save_one(file_personas, df_personas)
            save_one(file_trabajadores, df_trabajadores)
            save_one(file_usuarios, df_usuarios)
            save_one(file_peliculas, df_peliculas)
            save_one(file_scores, df_scores)

            return 0
        except Exception as err:
             print(f"Se detectó el siguiente error: #{err}")
             return -1