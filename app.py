
from flask import Flask
import dbhelper
import json

app=Flask(__name__)

@app.get('/clients')
def get_endpoint_info():
    results = dbhelper.run_procedure('CAll get_endpoint_info()',[])
    if(type(results)==list):
        client_json= json.dumps(results,default=str)
        return client_json
    else:
        return "sorry please try again"
app.run(debug=True)


