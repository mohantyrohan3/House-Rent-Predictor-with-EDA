import json
import pickle
import math
__data_columns = None
__ahmedabadmodel = None
__delhimodel = None
__mumbaimodel = None
__kolkatamodel = None
__bangaloremodel=None


def get_estimated_price_ahmedabad(bedroom,area,bathroom):

    return math.ceil(__ahmedabadmodel.predict([[bedroom,area,bathroom]])[0])

def get_estimated_price_kolkata(bedroom,area,bathroom):

    return math.ceil(__kolkatamodel.predict([[bedroom,area,bathroom]])[0])

def get_estimated_price_mumbai(bedroom,area,bathroom):

    return math.ceil(__mumbaimodel.predict([[bedroom,area,bathroom]])[0])

def get_estimated_price_delhi(bedroom,area,bathroom):

    return math.ceil(__delhimodel.predict([[bedroom,area,bathroom]])[0])

def get_estimated_price_bangalore(bedroom,area,bathroom):

    return math.ceil(__bangaloremodel.predict([[bedroom,area,bathroom]])[0])




def get_col_names():
    return __data_columns


def load_saved_artifacts():
    print("loading saved artifacts .. start")
    global __data_columns

    with open("./artifacts/columns.json",'r') as f1:
        __data_columns = json.load(f1)['data_columns']
    global __ahmedabadmodel
    with open("./artifacts/ahmedabad_model",'rb') as f2:
        __ahmedabadmodel = pickle.load(f2)
    global  __delhimodel
    with open("./artifacts/Delhi_model",'rb') as f3:
        __delhimodel = pickle.load(f3)
    global __kolkatamodel
    with open("./artifacts/Kolkata_model",'rb') as f4:
        __kolkatamodel = pickle.load(f4)
    global __bangaloremodel
    with open("./artifacts/Bangalore_model",'rb') as f5:
        __bangaloremodel = pickle.load(f5)
    global __mumbaimodel
    with open("./artifacts/Mumbai_model",'rb') as f6:
        __mumbaimodel = pickle.load(f6)


    print("loading saved artifacts..done")







if __name__ == "__main__":
    load_saved_artifacts()
    print(get_col_names())
    print(get_estimated_price_ahmedabad(2,1500,2))
    print(get_estimated_price_kolkata(2,1500,2))
    print(get_estimated_price_delhi(2, 1500, 2))
    print(get_estimated_price_bangalore(2, 1500, 2))
    print(get_estimated_price_mumbai(2, 1500, 2))