
### How to run this applications:

You need `docker` and `docker-compose` in order to be able to run this application.

### How to run it:

Type `docker-compose up -d` in your terminal. In my machine, with ubuntu, it runs very well.
If you have some other linux distribution, it may run well. If you us MacOS it also may run well.

### What does this do:

It starts an elasticsearch cluster with two nodes. When the status of the 
cluster is green, it runs the python script that populates 3 indices, reindex
all indexes to a new `target_index`, and update the new index with the current
datetime.

I hope you guys don't have any timezone issue. It may happen, but I haven't
payed so much attention to that issue.

After running the script, docker-compose will launch another container
with a flask application that allows you to index new documents to 
elasticsearch. The flask app is extremely simple. It assumes that all 
clients are going to send json payloads in a a valid format. 
Be kind with this application, and use a command like this: 

`curl --header "Content-Type: application/json"  --request POST  --data '{"index":"project_1","payload":{"alfa": "a", "beta": "b", "counter": 123}}' localhost:5000/ingest`

Thank you so much.
