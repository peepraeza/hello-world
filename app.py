from flask import Flask, render_template, json
import pandas as pd
from pandas import DataFrame

app = Flask(__name__)

@app.route('/')
def index():
    df = pd.read_csv("station.csv")
    a = df.values.tolist()
    a = [[13.736717,100.523186],
         [15.5337283,101.0490618],
         [14.4344572,101.3382849],
         [14.1786371,101.6463547],
         [14.3223389,101.3168609],
         [11.7112437,99.5839528],
         [14.3118684,99.0696813],
         [14.2086742,98.7248681],
         [16.9228372,101.4344774],
         [15.8889687,104.7762545]]
    b = json.dumps([["กรุงเทพมหานคร","rain"],
                    ["วนอุทยานแห่งชาติพุม่วง","sunny"],
                    ["อุทยานแห่งชาติเขาใหญ่","hazy"],
                    ["อุทยานแห่งชาติทับลาน","rain"],
                    ["อุทยานแห่งชาตินางรอง","sunny"],
                    ["อุทยานแห่งชาติน้ำตกห้วยยาง","sunny"],
                    ["อุทยานแห่งชาติเอราวัณ","hazy"],
                    ["อุทยานแห่งชาติทองผาภูมิ","rain"],
                    ["อุทยานแห่งชาติภูกระดึง","sunny"],
                    ["วนอุทยานภูสิงห์-ภูผาผึ้ง","sunny"]])


    return render_template('index.html', station = a,ads=b)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
