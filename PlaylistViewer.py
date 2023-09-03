import sys
from tabulate import tabulate
import pandas as pd

filename = nombre_archivo = sys.argv[1]
df = pd.read_table(filename ,encoding="utf-16")
print(tabulate(df.iloc[:,0:2], tablefmt='psql'))