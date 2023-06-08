
from flask import Flask,request
import dbhelper
import json

app=Flask(__name__)

@app.get('/clients')
def get_all_clients():
    results = dbhelper.run_procedure('CAll get_endpoint_info()',[])
    if(type(results)==list):
        client_json= json.dumps(results,default=str)
        return client_json
    else:
        return "sorry please try again"
    
@app.get('/api/loyal_clients')
def get_loyalty_points():
    max_points = request.args.get('max_points')
    results = dbhelper.run_procedure('CAll get_clients_loyal_point(?)',[max_points])
    if(type(results)==list):
        client_json= json.dumps(results,default=str)
        return client_json
    else:
        return "sorry please try again"
app.run(debug=True)


