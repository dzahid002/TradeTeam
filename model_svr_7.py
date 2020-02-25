import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
from sklearn import preprocessing,svm # Preprocessing for scaling data,Accuracy,Processing speed ,cross validation for training and testing
from sklearn import model_selection
from sklearn.model_selection import train_test_split

class SvrModel7():
    # arrayd = [[p1,p2,p3,p4,p5,p6,p7,p8]]
    def model_svrpredict(self,p0,p5,p6,p7,p8):
        dataset = pd.read_csv('for 7day.csv')
        dataset_a=dataset[dataset['symbol']== p0]

        x = dataset_a.loc[:,'7day_closing_price':'volume']
        y = dataset_a.loc[:,'closing_price']
        from sklearn.model_selection import train_test_split
        x_train,x_test,y_train,y_test=model_selection.train_test_split(x,y,test_size=0.1,random_state =200)
        clf=svm.SVR()
        clf.fit(x_train,y_train)
        accuracy=clf.score(x_test,y_test)
        # Test_data = [[26.5,26.5,25.9,25.9,26.3,639,21.744,831790]]
        Test_data = [[p5,p6,p7,p8]]
        forecast_set=clf.predict(Test_data)
        print (forecast_set)

        return forecast_set
