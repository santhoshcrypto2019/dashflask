from pymongo import MongoClient
import ssl
from bson import json_util
# import json
import os
from dash import Dash, Input, Output, dash_table,dcc,html
import dash_bootstrap_components as dbc

app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

mongo_uri=f"mongodb://{os.environ['MONGODB_DATABASE_HOSTNAME']}:{os.environ['MONGODB_DATABASE_PORT']}"
print(f"Trying to connect to the database: {mongo_uri}")
client = MongoClient(mongo_uri)


collection_ticker = client['trading']['ticker']
system_collection_ticker = client['trading']['system.buckets.ticker']
print(client.server_info())
print("Database connection is successful.")

app.layout = html.Div([
    dbc.Label('helloworld')
    #  html.Div(id='mongo-datatable', children=[]),
     
     
     
     
     
     ])

if __name__ == '__main__':
    app.run_server(debug=True)
    
