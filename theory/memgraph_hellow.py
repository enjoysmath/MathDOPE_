from gqlalchemy import Memgraph
import os

host = '54.193.63.96'
port = 7687
username = 'fruitfulapproach@gmail.com'
# Place your Memgraph password that was created during Project creation
password= os.environ['MEMGRAPH_PASSWORD']

db = Memgraph(host, port, username, password, encrypted=True)

# Delete all nodes and relationships
query = "MATCH (n) DETACH DELETE n"

## Execute the query
db.execute(query)

# Create a node with the label FirstNode and message property with the value "Hello, World!"
query = """CREATE (n:FirstNode)
           SET n.message = '{message}'
           RETURN 'Node '  + id(n) + ': ' + n.message AS result""".format(message="Hello, World!")

# Execute the query
results = db.execute_and_fetch(query)

# Print the first member
print(list(results)[0]['result'])