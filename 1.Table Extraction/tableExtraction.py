#Extracting table  from URL 

import pandas as pd

strangerThings = pd.read_html('https://en.wikipedia.org/wiki/List_of_Stranger_Things_episodes')

print(len(strangerThings))
print(strangerThings[0])