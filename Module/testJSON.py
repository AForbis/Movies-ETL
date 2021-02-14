#%%
import json
import pandas as pd
import numpy as np
# %%
file_dir = 'C://Users/alexf/Desktop/Bootcamp/Movies-ETL/'
# %%
with open(f'{file_dir}/wikipedia-movies.json', mode='r') as file:
    wiki_movies_raw = json.load(file)
# %%
len(wiki_movies_raw)
# %%
# First 5 records
wiki_movies_raw[:5]
# %%
# Last 5 records
wiki_movies_raw[-5:]
# %%
# Some records in the middle
wiki_movies_raw[3600:3605]