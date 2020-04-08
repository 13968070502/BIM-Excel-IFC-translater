print ("hello world")

import pandas as pd
import os

path = 'C:\\Masterarbeit\\Programmieren\\Dateien'
os.chdir(path)

pokemondata = path+'\\pokemon_data.csv'

df = pd.read_csv(pokemondata)

print df