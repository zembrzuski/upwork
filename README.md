
curl --header "Content-Type: application/json"  --request POST  --data '{"index":"project_1","payload":{"alfa": "a", "beta": "b", "counter": 666}}' 127.0.0.1:5000/ingest

Notes:
- it would be better to ingest initial data using bulk api. But id didn't do it.
- it would be better if I could generate random data to insert. But id din't do it.
- it would be better if I had made some erro handling. 
- it would be better to implement some validation at the http endpoint.