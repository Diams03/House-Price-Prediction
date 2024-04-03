import json
import pickle
import numpy as np

__locations=None
__data_columns=None
__model=None

def get_estimated_price(location,sqft,bhk,bath):
    try:
        loc_index=__data_columns.index(location.lower())
    except:
        loc_index=-1
    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index] = 1
    return round(__model.predict([x])[0],2)

def get_locations_name():
    return __locations

def loads_artifacts():
    print("Load saved artifact...")
    global __locations
    global __data_columns
    global __model

    with open("server\\artifacts\\column.json","r") as f:
        __data_columns=json.load(f)["data_columns"]
        __locations=__data_columns[3:]
    with open("server\\artifacts\\banglore_home_prices_model.pickle","rb") as f:
        __model=pickle.load(f)
    
    print("Load successfully.")



if __name__=="__main__":
    loads_artifacts()
    print(get_estimated_price('2nd Phase Judicial Layout',1000, 2, 2))