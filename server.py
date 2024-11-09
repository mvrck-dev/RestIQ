from flask import Flask, jsonify
import mysql.connector
import pandas as pd
import random
from datetime import datetime, timedelta
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)

# Database connection function
def connect_to_database():
    return mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='student@123',
        database='restiq'
    )

# Fetch data for sleep monitoring (simulating REM, awake, light, deep phases)
@app.route('/sleep_data', methods=['GET'])
def get_sleep_data():
    sleep_data = [
        {"time": "22:00", "awake": 1, "rem": 0, "light": 0, "deep": 0},
        {"time": "23:00", "awake": 0.2, "rem": 0, "light": 0.8, "deep": 0},
        {"time": "00:00", "awake": 0, "rem": 0, "light": 0.3, "deep": 0.7},
        {"time": "01:00", "awake": 0, "rem": 0, "light": 0, "deep": 1},
        {"time": "02:00", "awake": 0, "rem": 0.6, "light": 0.4, "deep": 0},
        {"time": "03:00", "awake": 0, "rem": 0.8, "light": 0.2, "deep": 0},
        {"time": "04:00", "awake": 0, "rem": 0, "light": 0.5, "deep": 0.5},
        {"time": "05:00", "awake": 0, "rem": 0.7, "light": 0.3, "deep": 0},
        {"time": "06:00", "awake": 0.1, "rem": 0.9, "light": 0, "deep": 0},
        {"time": "07:00", "awake": 1, "rem": 0, "light": 0, "deep": 0},
    ]
    return jsonify(sleep_data)

# Fetch energy levels data
@app.route('/energy_data', methods=['GET'])
def get_energy_data():
    energy_data = [
        {"time": "06:00", "level": 3},
        {"time": "09:00", "level": 7},
        {"time": "12:00", "level": 6},
        {"time": "15:00", "level": 4},
        {"time": "18:00", "level": 5},
        {"time": "21:00", "level": 3}
    ]
    return jsonify(energy_data)

# Generate mock month data for mood and productivity
@app.route('/month_data', methods=['GET'])
def get_month_data():
    data = []
    now = datetime.now()
    for i in range(30):
        date = (now - timedelta(days=i)).strftime('%Y-%m-%d')
        data.insert(0, {
            "date": date,
            "mood": random.randint(1, 5),
            "productivity": random.randint(1, 5),
        })
    return jsonify(data)

# Prediction function for sleep requirements based on model
def generate_predictions():
    conn = connect_to_database()
    query = "SELECT * FROM sleep_details"  # Modify as needed
    df = pd.read_sql(query, conn)
    conn.close()

    # Preprocess and train a model, similar to previous setup
    features = df[['Stress Level (1-10)', 'Mood (1-10)', 'Heart Rate (Normal)',
                   'Worked Out (Hours)', 'Mental Work (Hours)', 'Number of Breaks']]
    target = df['Hours of Sleep']
    X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)
    
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    # Prepare data for JSON response
    results = [{"ActualSleepHours": actual, "PredictedSleepHours": pred} for actual, pred in zip(y_test, y_pred)]
    return results

# Endpoint for sleep predictions
@app.route('/predictions', methods=['GET'])
def predictions():
    results = generate_predictions()
    return jsonify(results)

if __name__ == "_main_":
    app.run(debug=True, port=5000)