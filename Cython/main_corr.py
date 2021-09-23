from time import time

from corre_pastas import RAIZ, correr_pastas

ini = time()
print(correr_pastas())
print(f"TEMPO CORRIDO PARA PERCORRER {RAIZ} {round(time() - ini, 2)} SEGUNDOS")
