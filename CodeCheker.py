import ast
import os

global ascii_art
ascii_art = """\033[32m
                          .-=-.          .--.
              __        .'     '.       /  " )
      _     .'  '.     /   .-.   \     /  .-'
     ( \   / .-.  \   /   /   \   \   /  /    
      \ `-` /   \  `-'   /     \   `-`  /
        `-.-`     '.____.'       `.____.'
▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
██ ▄▄▀██ ▄▄▄ ██ ▄▄▀██ ▄▄▄████ ▄▄ ██ ███ ████ ▄▄▀██ ██ ██ ▄▄▄██ █▀▄██ ▄▄▄██ ▄▄▀
██ █████ ███ ██ ██ ██ ▄▄▄████ ▀▀ ██▄▀▀▀▄████ █████ ▄▄ ██ ▄▄▄██ ▄▀███ ▄▄▄██ ▀▀▄
██ ▀▀▄██ ▀▀▀ ██ ▀▀ ██ ▀▀▀████ ███████ ██████ ▀▀▄██ ██ ██ ▀▀▀██ ██ ██ ▀▀▀██ ██ 
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
                                                                by Kevin Dev

\033[0m"""

def analizar_linea(linea, num_linea):
    try:
        exec(linea)
        print(f"\033[32m La línea {num_linea} está correctamente escrita.\033[0m")
    except Exception as e:
        print(f"\033[91m Error de sintaxis en la línea {num_linea} : {e}\033[0m")

def analizar_codigo():
    try:
        print(ascii_art)
        print("\033[34mIngrese su codigo (escriba exit para terminar):\033[0m")
        linea = input()
        codigo = []
        while linea != "exit":
            codigo.append(linea)
            linea = input()
        print("\033[33m|||||||  EJECUCION  |||||||\033[0m")
        for num_linea, linea in enumerate(codigo, start=1):
            analizar_linea(linea.strip(), num_linea)
        print("\033[33m|||||||  ANALISIS COMPLETO ||||||| \033[0m")
        input("Presione ENTER para continuar...")
        os.system('cls')
        analizar_codigo()

    except FileNotFoundError:
        print(f"Error: El archivo '{archivo}' no se encontró.")
        analizar_codigo()
        

analizar_codigo()
