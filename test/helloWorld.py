print ("hello world")

import pandas as pd
import os

path = 'C:\\Masterarbeit\\Programmieren\\Dateien'
os.chdir(path)

dataname = 'pokemon_data'

pokemondata = path+'\\'+str(dataname)+'.csv'

print pokemondata

df = pd.read_csv(pokemondata)

print df