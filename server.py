from flask import Flask, jsonify, render_template
import pandas as pd



df = pd.read_csv("multinational_company_sales_data.csv")
df['Profit'] = df['Profit'].sort_values()


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get-datachart')
def get_datachart():
    classes = df["Product"].value_counts().index
    values = df["Product"].value_counts().values

    data = []
    for i in range(len(classes)):
        data.append({"class": classes[i], "value": int(values[i])})

    return jsonify(data)

@app.route('/get-datatable')
def get_datatable():
    classes = df["Branch"].value_counts().index
    values = df["Branch"].value_counts().values

    data = []
    for i in range(len(classes)):
        data.append({"class": classes[i], "value": int(values[i])})

    return jsonify(data)



@app.route('/get-datavalue')
def get_datavalue():
  
    unique_ratings = df['Customer Satisfaction Rating'].drop_duplicates()
 
    top_ratings = unique_ratings.sort_values(ascending=False).head(9)
    
    data = []
    
    for rating in top_ratings:

        color = df[df['Customer Satisfaction Rating'] == rating]['Color'].values[0]
        data.append({"color": color, "value": int(rating)})

    return jsonify(data)



@app.route('/get_datademo')
def get_datademo():
    classes = df["Product"][:5]
    values = df["Sales Quantity"][:9]

    data = [{"class": class_val, "value": int(value)} for class_val, value in zip(classes, values)]

    return jsonify(data)

 
if __name__=='__main__':
    app.run(debug=True)