from flask import *  
import numpy as np
import cv2
import keras
from keras.models import  load_model
import pandas as pd
import os

app = Flask(__name__)  
UPLOAD_FOLDER = '[your path]/Upload_Folder'
@app.route('/')  
def upload():  
    return render_template("file_upload_form.html")  
 
@app.route('/success', methods = ['POST'])  
def success():  
    if request.method == 'POST':  
        f = request.files['file']
        filename = f.filename  
        path = os.path.join(UPLOAD_FOLDER,f.filename)

        model = load_model('model1.h5')
        image = cv2.imread(path)

        image =cv2.resize(image, dsize=(100,75), interpolation=cv2.INTER_CUBIC)
        image = np.asarray([image])

        c =model.predict(image)
        c = c.flatten()
        c = c.astype(int)
        c = list(c)
        if c.index(max(c)) != 5:
        	result = 'Low Risk'
            return render_template("success.html",result=result)
        else:
        	result = 'Melanoma'
        	return render_template("success.html",result=result)
        

if __name__ == '__main__':  
    app.run(debug = False,threaded=False)

