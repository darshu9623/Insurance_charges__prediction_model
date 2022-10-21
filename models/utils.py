import pandas as pd 
import numpy as np 
import pickle  
import json 
import config

class MedInc():
    def __init__(self,age,sex,bmi,children,smoker,region):
        self.age = age
        self.sex =  sex
        self.bmi = bmi
        self.children = children
        self.smoker = smoker
        self.region = 'region_'+region

    def load_model(self):
        with open(config.JSON_FILE_PATH,'r') as f:
            self.json_data = json.load(f)

        with open(config.MODEL_FILE_PATH,'rb') as f:
            self.linear_reg_model = pickle.load(f) 
    
    def get_insurance_charges(self):
        self.load_model() 

        array = np.zeros(len(self.json_data['columns']))

        region_index = self.json_data['columns'].index(self.region)

        array[0] = self.age 
        array[1] = self.json_data['sex'][self.sex]
        array[2] = self.bmi
        array[3] = self.children
        array[4] = self.json_data['smoker'][self.smoker]
        array[region_index] = 1
        print(array)

        predicted_charges = self.linear_reg_model.predict([array])[0]
        return np.around(predicted_charges,2)

if __name__ == "__main__":
    age = 67
    sex = "male"
    bmi = 27.9
    children = 3
    smoker = "yes"
    region = "southeast"

    Ins_charg = MedInc(age, sex, bmi, children, smoker, region)
    charges = Ins_charg.get_insurance_charges()
    print(f"Predicted car price is {charges} Rs. only")

