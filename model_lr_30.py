import pandas as pd #For data related tasks
import matplotlib.pyplot as plt #for data visualization 
#import quandl #Stock market API for fetching Data
from sklearn.linear_model import LinearRegression
from matplotlib import pyplot as plt
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np

class PriceModel30():
    # arrayd = [[p1,p2,p3,p4,p5,p6,p7,p8]]
    def model_predict(self,p0,p5,p6,p7,p8):
        dataset = pd.read_csv('for 30day.csv')
        dataset_a=dataset[dataset['symbol']== p0]

        x = dataset_a.loc[:,'30d_closing_price':'volume']
        y = dataset_a.loc[:,'closing_price']
        from sklearn.model_selection import train_test_split
        x_train, x_test, y_train, y_test = train_test_split(x , y ,test_size = 0.1,random_state =0 )

        LR = LinearRegression()
        LR.fit(x_train, y_train)
        LR.score(x_test, y_test)
        # Test_data = [[26.5,26.5,25.9,25.9,26.3,639,21.744,831790]]
        Test_data = [[p5,p6,p7,p8]]
        prediction = LR.predict(Test_data)
        print (prediction)

        return prediction
