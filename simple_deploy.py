from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def read_main():
    return {'message': 'Hello World. I am here'}