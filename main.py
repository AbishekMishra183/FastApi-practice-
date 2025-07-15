from fastapi import FastAPI

app=FastAPI()

@app.get('/')         # @ is used to make the route

def show():
    return{'message:','Hello guys'}

@app.get('about')
def about():
    return{'Display:','Broad AI is the educational sector'}

'''
to run this code we use the 
 in the cmd =>   uvicorn file name: app 
 uvicorn main:app --reload  


 to see the documentation 

http://127.0.0.1:8000/docs in the url / docs is used 

'''

