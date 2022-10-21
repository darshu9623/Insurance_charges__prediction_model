from distutils.command.config import config
from flask import Flask,jsonify,render_template,request
from models.utils   import  MedInc
import config


# create instance for flask 
app = Flask(__name__)


############### Home API ############################# 


@app.route('/')             # flask decorator 
def hello_flask():
    print('Welcome to Insurance charges prediction')
    return render_template("index.html")                       ##### link with html file
    # return "success"


#################### Prediction charges API ################################


@app.route('/prediction_charges',methods = ['POST','GET'])        # Give appropriate method in html file 
def get_charges():

    if request.method == "GET":
        print("We are using GET Method")

        # data = request.form
        # print('Data ::',data)                                      ###### for testing on postman appication

        # age = eval(data['age'])
        # sex = data['sex']
        # bmi = eval(data['bmi'])
        # children = eval(data['children'])
        # smoker = data['smoker']
        # region = data['region']


        # get_method = request.args.get               ##### request use to store output from user...
        
        age = eval(request.args.get('age'))
        sex = request.args.get('sex')
        bmi = eval(request.args.get('bmi'))
        children = eval(request.args.get('children'))
        smoker = request.args.get('smoker')
        region = request.args.get('region')


        print("age, sex, bmi, children, smoker, region\n",age, sex, bmi, children, smoker, region)

        Ins_charg = MedInc(age, sex, bmi, children, smoker, region)
        charges = Ins_charg.get_insurance_charges()

        return render_template("index.html", prediction = charges)        #### connection to the html file
 
        # return jsonify({"Result" : f"Predicted Charges for Medical Insurance is {charges}/- Rs. Only"})


    else:
        print('we are in POST method')              ######## in post method args replace by form #############

        age = eval(request.form.get('age'))
        sex = request.form.get('sex')
        bmi = eval(request.form.get('bmi'))
        children = eval(request.form.get('children'))
        smoker = request.form.get('smoker')
        region = request.form.get('region')

        print("age, sex, bmi, children, smoker, region\n",age, sex, bmi, children, smoker, region)

        Ins_charg = MedInc(age, sex, bmi, children, smoker, region)
        charges = Ins_charg.get_insurance_charges()

        return render_template("index.html", prediction = charges)

        # return jsonify({"Result" : f"Predicted Charges for Medical Insurance is {charges}/- Rs. Only"})


if __name__ == "__main__":
    app.run(host = '0.0.0.0',port = config.PORT_NUMBER,debug = True)    #### instance for calling flask