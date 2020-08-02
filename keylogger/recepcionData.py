import ast
import squarify
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import plotly.express as px
import urllib.request


datos = urllib.request.urlopen("https://sistemasop-fiis.herokuapp.com/data").read().decode()

dict_data=ast.literal_eval(datos[1:-1])
dict_data_=dict_data[-1]
dict_data_["keys"]

pd_data=pd.DataFrame(dict_data_["keys"])

label_value=pd_data["key"].value_counts().to_dict()

Data=pd.DataFrame(data=label_value.items(),columns=['Tecla', 'Frecuencia'])

fig = px.treemap(Data,
                 path=['Tecla'],
                 values='Frecuencia')
                 
fig.show()
