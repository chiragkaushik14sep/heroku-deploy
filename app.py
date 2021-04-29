import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))
print(model)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [int(x) for x in request.form.values()]
    print("int_features",int_features)
    final_features = [np.array(int_features)]
    print("final_features",final_features)
    prediction = model.predict(final_features)
    print(prediction)

    output = round(prediction[0], 2)
    print("output",output)

    return render_template('index.html', prediction_text='Employee Salary should be $ {}'.format(output))


if __name__ == "__main__":
    app.run(debug=True)
