import json
import pickle
import math
__data_columns = None
__model = None


def get_estimated_price(bedroom,area,bathroom):

    return math.ceil(__model.predict([[bedroom,area,bathroom]])[0])

def get_col_names():
    return __data_columns


def load_saved_artifacts():
    print("loading saved artifacts .. start")
    global __data_columns

    with open("./artifacts/columns.json",'r') as f:
        __data_columns = json.load(f)['data_columns']
    global __model
    with open("./artifacts/ahmedabad_model",'rb') as f:
        __model = pickle.load(f)

    print("loading saved artifacts..done")







if __name__ == "__main__":
    load_saved_artifacts()
    print(get_col_names())
    print(get_estimated_price(2,1500,2))