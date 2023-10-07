# Comparing Different Ways of Storing Embeddings


## Task Description
 
 Find an efficient way to query across ~2k documents each having ~20 embeddings in a Flask Web Application (for simplicity) using python primarily.

 **Goal**: Find the best 3 document matches and the corresponding text matched inside that document.

### Note: 

###### _This is just a comparision of various ways of handling embeddings inside a Flask App (or any app written in python I guess). A single file server and the default app structure suffices for this experiment._


## Try them out?

```
cd PerfTest

virtualenv venv

source venv/bin/activate.fish

pip install -r requirements.txt

docker run --name perdTest-redis -p 6379:6379 -d redis

python run_test.py --documents 2000 --parts 20 --words 200
```