import numpy as np
from flask import Flask, request, jsonify, render_template
import string
from model_svr_1 import SvrModel1
from model_svr_7 import SvrModel7
from model_svr_15 import SvrModel15
from model_svr_30 import SvrModel30
from model_lr_1 import PriceModel1
from model_lr_7 import PriceModel7
from model_lr_15 import PriceModel15
from model_lr_30 import PriceModel30



app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html') 

@app.route('/1day')
def day1():
    return render_template('1day.html') 

@app.route('/7day')
def day7():
    return render_template('7day.html')   
    

@app.route('/15day')
def day15():
    return render_template('15day.html')  

@app.route('/30day')
def day30():
    return render_template('30day.html')




@app.route('/start_lr_prediction_1day')
def lr_prediction1():
    return render_template('LR_prediction_1day.html')
    

@app.route('/lr_predict_1day' , methods=['POST'])
def predict1():

    model_lr_1 = PriceModel1()
    result = ''
    price0 = (request.form['price00'])
    
    price5 = float(request.form['price05'])
    price6 = float(request.form['price06'])
    price7 = float(request.form['price07'])
    price8 = float(request.form['price08'])

    price_array = [price5, price6, price7, price8]

    result = model_lr_1.model_predict(price0, price5, price6, price7, price8)
    
    return render_template('LR_prediction_1day.html' , result=f'The Prediction Price According to given input : {result}' , price_array=price_array)




@app.route('/start_lr_prediction_7day')
def lr_prediction7():
    return render_template('LR_prediction_7day.html')
    

@app.route('/lr_predict_7day' , methods=['POST'])
def predict7():

    model_lr_7 = PriceModel7()
    result = ''
    price0 = (request.form['price00'])
    
    price5 = float(request.form['price05'])
    price6 = float(request.form['price06'])
    price7 = float(request.form['price07'])
    price8 = float(request.form['price08'])

    price_array = [ price5, price6, price7, price8]

    result = model_lr_7.model_predict(price0, price5, price6, price7, price8)
    
    return render_template('LR_prediction_7day.html' , result=f'The Prediction Price According to given input : {result}' , price_array=price_array)





@app.route('/start_lr_prediction_15day')
def lr_prediction15():
    return render_template('LR_prediction_15day.html')
    

@app.route('/lr_predict_15day' , methods=['POST'])
def predict15():

    model_lr_15 = PriceModel15()
    result = ''
    price0 = (request.form['price00'])
    
    price5 = float(request.form['price05'])
    price6 = float(request.form['price06'])
    price7 = float(request.form['price07'])
    price8 = float(request.form['price08'])

    price_array = [ price5, price6, price7, price8]

    result = model_lr_15.model_predict(price0, price5, price6, price7, price8)
    
    return render_template('LR_prediction_15day.html' , result=f'The Prediction Price According to given input : {result}' , price_array=price_array)

@app.route('/start_lr_prediction_30day')
def lr_prediction30():
    return render_template('LR_prediction_30day.html')
    

@app.route('/lr_predict_30day' , methods=['POST'])
def predict30():

    model_lr_30 = PriceModel30()
    result = ''
    price0 = (request.form['price00'])
    
    price5 = float(request.form['price05'])
    price6 = float(request.form['price06'])
    price7 = float(request.form['price07'])
    price8 = float(request.form['price08'])

    price_array = [ price5, price6, price7, price8]

    result = model_lr_30.model_predict(price0, price5, price6, price7, price8)
    
    return render_template('LR_prediction_30day.html' , result=f'The Prediction Price According to given input : {result}' , price_array=price_array)



@app.route('/start_svr_prediction_1day')
def svr_prediction1():
    return render_template('SVR_prediction_1day.html')

@app.route('/svr_predict_1day' , methods=['POST'])
def prediction1():

    model_svr_1 = SvrModel1()
    result = ''
    price0 = (request.form['price00'])
    
    price5 = float(request.form['price05'])
    price6 = float(request.form['price06'])
    price7 = float(request.form['price07'])
    price8 = float(request.form['price08'])

    price_array = [price5, price6, price7, price8]

    result = model_svr_1.model_svrpredict(price0, price5, price6, price7, price8)
    
    return render_template('SVR_prediction_1day.html' , result=f'The Prediction Price According to given input : {result}' , price_array=price_array)





@app.route('/start_svr_prediction_7day')
def svr_prediction7():
    return render_template('SVR_prediction_7day.html')

@app.route('/svr_predict_7day' , methods=['POST'])
def prediction7():

    model_svr_7 = SvrModel7()
    result = ''
    price0 = (request.form['price00'])
    
    price5 = float(request.form['price05'])
    price6 = float(request.form['price06'])
    price7 = float(request.form['price07'])
    price8 = float(request.form['price08'])

    price_array = [ price5, price6, price7, price8]

    result = model_svr_7.model_svrpredict(price0, price5, price6, price7, price8)
    
    return render_template('SVR_prediction_7day.html' , result=f'The Prediction Price According to given input : {result}' , price_array=price_array)





@app.route('/start_svr_prediction_15day')
def svr_prediction15():
    return render_template('SVR_prediction_15day.html')

@app.route('/svr_predict_15day' , methods=['POST'])
def prediction15():

    model_svr_15 = SvrModel15()
    result = ''
    price0 = (request.form['price00'])
    
    price5 = float(request.form['price05'])
    price6 = float(request.form['price06'])
    price7 = float(request.form['price07'])
    price8 = float(request.form['price08'])

    price_array = [ price5, price6, price7, price8]

    result = model_svr_15.model_svrpredict(price0, price5, price6, price7, price8)
    
    return render_template('SVR_prediction_15day.html' , result=f'The Prediction Price According to given input : {result}' , price_array=price_array)

@app.route('/start_svr_prediction_30day')
def svr_prediction30():
    return render_template('SVR_prediction_30day.html')

@app.route('/svr_predict_30day' , methods=['POST'])
def prediction30():

    model_svr_30 = SvrModel30()
    result = ''
    price0 = (request.form['price00'])
    
    price5 = float(request.form['price05'])
    price6 = float(request.form['price06'])
    price7 = float(request.form['price07'])
    price8 = float(request.form['price08'])

    price_array = [ price5, price6, price7, price8]

    result = model_svr_30.model_svrpredict(price0, price5, price6, price7, price8)
    
    return render_template('SVR_prediction_30day.html' , result=f'The Prediction Price According to given input : {result}' , price_array=price_array)

if __name__ == "__main__":
    app.run(debug=True)


    