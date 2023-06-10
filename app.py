
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



    
@app.post('/api/clients')

def Post_add_new_clients():
    username = request.json.get('username')
    password = request.json.get('password')
    results = dbhelper.run_procedure('CAll add_new_client(?,?)',[username,password])
    if(type(results)==list):
        client_json= json.dumps(results,default=str)
        return client_json
    else:
        return "sorry please try again"




@app.patch('/api/clients')

def new_loyalty_input():
    username = request.json.get('username')
    new_loyalty_input = request.json.get('new_loyalty_input')
    results = dbhelper.run_procedure('CAll add_new_point(?,?)',[username,new_loyalty_input])
    if(type(results)==list):
        client_json= json.dumps(results,default=str)
        return client_json
    else:
        return "sorry please try again" 

@app.delete('/api/clients')

def delete_client():
    username = request.json.get('username')
    password_input = request.json.get('password_input')
    results = dbhelper.run_procedure('CAll delete_client(?,?)',[username,password_input])
    if(results==[]):
        return "successfully deleted client "
    else:
        return "sorry please try again"  

app.run(debug=True)





