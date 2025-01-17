import pandas as pd

# Store A data
data_a = {
    "Brand": ["Budweiser", "Budweiser", "Budweiser", "Stella Artois", "Stella Artois", "Stella Artois", "Competitor", "Competitor", "Competitor"],
    "Package Type": ["Can (6-pack)", "Bottle (6-pack)", "Can (12-pack)", "Can (6-pack)", "Bottle (6-pack)", "Can (12-pack)", "Can (6-pack)", "Bottle (6-pack)", "Can (12-pack)"],
    "Units": [20, 6, 8, 123, 108, 78, 68, 37, 12],
    "Brand Share %": [7.4, None, None, 67.3, None, None, 25.3, None, None],
    "Format Share %": [9.2, 2.8, 3.7, 56.7, 49.8, 35.9, 31.3, 17.1, 5.5]
}

df_store_a = pd.DataFrame(data_a)

# Store B data
data_b = {
    "Brand": ["Budweiser", "Budweiser", "Budweiser", "Stella Artois", "Stella Artois", "Stella Artois", "Competitor", "Competitor", "Competitor"],
    "Package Type": ["Can (6-pack)", "Bottle (6-pack)", "Can (12-pack)", "Can (6-pack)", "Bottle (6-pack)", "Can (12-pack)", "Can (6-pack)", "Bottle (6-pack)", "Can (12-pack)"],
    "Units": [65, 35, 24, 163, 105, 28, 274, 143, 53],
    "Brand Share %": [12.5, None, None, 29.8, None, None, 47.7, None, None],
    "Format Share %": [12.9, 7.0, 4.8, 32.4, 20.9, 5.6, 54.7, 28.5, 10.6]
}

df_store_b = pd.DataFrame(data_b)


data_c = {
    "Brand": ["Budweiser", "Budweiser", "Budweiser", "Stella Artois", "Stella Artois", "Stella Artois", "Competitor", "Competitor", "Competitor"],
    "Package Type": ["Can (6-pack)", "Bottle (6-pack)", "Can (12-pack)", "Can (6-pack)", "Bottle (6-pack)", "Can (12-pack)", "Can (6-pack)", "Bottle (6-pack)", "Can (12-pack)"],
    "Units": [163, 82, 74, 32, 10, 5, 11, 8, 8],
    "Brand Share %": [80.2, None, None, 11.8, None, None, 8.0, None, None],
    "Format Share %": [51.1, 25.7, 23.2, 10.0, 3.1, 1.6, 3.4, 2.5, 2.5]
}

df_store_c = pd.DataFrame(data_c)

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


data_a = {
    "Brand": ["Budweiser", "Budweiser", "Budweiser", "Stella Artois", "Stella Artois", "Stella Artois", "Competitor", "Competitor", "Competitor"],
    "Package Type": ["Can (6-pack)", "Bottle (6-pack)", "Can (12-pack)", "Can (6-pack)", "Bottle (6-pack)", "Can (12-pack)", "Can (6-pack)", "Bottle (6-pack)", "Can (12-pack)"],
    "Units": [20, 6, 8, 123, 108, 78, 68, 37, 12],
    "Brand Share %": [7.4, None, None, 67.3, None, None, 25.3, None, None],
    "Format Share %": [9.2, 2.8, 3.7, 56.7, 49.8, 35.9, 31.3, 17.1, 5.5]
}
df_store_a = pd.DataFrame(data_a)


data_b = {
    "Brand": ["Budweiser", "Budweiser", "Budweiser", "Stella Artois", "Stella Artois", "Stella Artois", "Competitor", "Competitor", "Competitor"],
    "Package Type": ["Can (6-pack)", "Bottle (6-pack)", "Can (12-pack)", "Can (6-pack)", "Bottle (6-pack)", "Can (12-pack)", "Can (6-pack)", "Bottle (6-pack)", "Can (12-pack)"],
    "Units": [65, 35, 24, 163, 105, 28, 274, 143, 53],
    "Brand Share %": [12.5, None, None, 29.8, None, None, 47.7, None, None],
    "Format Share %": [12.9, 7.0, 4.8, 32.4, 20.9, 5.6, 54.7, 28.5, 10.6]
}
df_store_b = pd.DataFrame(data_b)


data_c = {
    "Brand": ["Budweiser", "Budweiser", "Budweiser", "Stella Artois", "Stella Artois", "Stella Artois", "Competitor", "Competitor", "Competitor"],
    "Package Type": ["Can (6-pack)", "Bottle (6-pack)", "Can (12-pack)", "Can (6-pack)", "Bottle (6-pack)", "Can (12-pack)", "Can (6-pack)", "Bottle (6-pack)", "Can (12-pack)"],
    "Units": [163, 82, 74, 32, 10, 5, 11, 8, 8],
    "Brand Share %": [80.2, None, None, 11.8, None, None, 8.0, None, None],
    "Format Share %": [51.1, 25.7, 23.2, 10.0, 3.1, 1.6, 3.4, 2.5, 2.5]
}
df_store_c = pd.DataFrame(data_c)


