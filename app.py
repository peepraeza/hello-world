from flask import Flask, render_template
import pandas as pd
from pandas import DataFrame

app = Flask(__name__)

@app.route('/')
def index():
    df = pd.read_csv("station.csv")
    a = df.values.tolist()
    
    return render_template('index.html', station = a)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
