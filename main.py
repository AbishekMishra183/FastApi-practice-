from fastapi import FastAPI
from pydantic import BaseModel
import joblib 
import numpy as np
app=FastAPI() 
model=joblib.load('Saved/DecisionTreePrediction.pkl')


#GUlcose
 #Bloddpresure
 #dfp
#age
class Patient(BaseModel):
    gulcose:float
    bloodpressure:int
    dfp:float
    age:int

@app.get('/')         # @ is used to make the route

def show():
    return{'message:','Hello guys'}

@app.get('about')
def about():
    return{'Display:','Broad AI is the educational sector'}





@app.post('/predict')
async def predict(data:Patient):
    input_data=np.array([[
        data.gulcose,
        data.bloodpressure,
        data.dfp,
        

    ]])
    predict=await model.predict(input_data)[0]
    return{'prediction':int(predict)}


    #GUlcose
    #Bloddpresure
    #dfp
    #age









'''
to run this code we use the 
 in the cmd =>   uvicorn file name: app 
 uvicorn main:app --reload  


 to see the documentation 

http://127.0.0.1:8000/docs in the url / docs is used 

to give the data to the fastapi pydantic

'''

