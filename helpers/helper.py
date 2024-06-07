import pandas as pd
from classes.Peliculas import Pelicula
from classes.Usuarios import Usuario
from classes.Personas import Persona
from classes.Scores import Score
from classes.Trabajadores import Trabajador

def load_all(
        file_peliculas,
        file_personas,
        file_scores,
        file_trabajadores,
        file_usuarios
    ):
    df_peliculas = Pelicula.create_df_from_csv(file_peliculas)
    df_personas = Persona.create_df_from_csv(file_personas)
    df_scores = Score.create_df_from_csv(file_scores)
    df_trabajadores = Trabajador.create_df_from_csv(file_trabajadores)
    df_usuarios = Usuario.create_df_from_csv(file_usuarios)
    return df_peliculas, df_personas, df_scores, df_trabajadores, df_usuarios

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