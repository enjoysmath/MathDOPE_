from gqlalchemy import Memgraph
import os

host = '54.193.63.96'
port = 7687
username = 'fruitfulapproach@gmail.com'
# Place your Memgraph password that was created during Project creation
password= os.environ['MEMGRAPH_PASSWORD']

db = Memgraph(host, port, username, password, encrypted=True)