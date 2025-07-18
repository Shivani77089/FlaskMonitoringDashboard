from flask import Flask, jsonify, render_template
from flask.globals import request
from apscheduler.schedulers.background import BackgroundScheduler
import random

app = Flask(__name__)

# Initialize scheduler
scheduler = BackgroundScheduler()

# Variable to track if scheduler is running
scheduler_running = False


# Function to generate and store data
def generate_and_store_data():
    # Generate random data
    data = {'random_number': random.randint(1, 100)}

    # Store data in text file
    with open('output.txt', 'w') as file:
        file.write(str(data))


# Route to get data
@app.route('/get_data', methods=['GET'])
def get_data():
    try:
        # Read data from file
        with open('output.txt', 'r') as file:
            data = eval(file.read())  # Convert string to dictionary
        return jsonify(data)
    except FileNotFoundError:
        return jsonify({'error': 'Data file not found.'})
    except Exception as e:
        return jsonify({'error': str(e)})


# Route to render template with buttons
@app.route('/')
def index():
    return render_template('index.html')


# Route to start scheduler
@app.route('/start', methods=['POST'])
def start_scheduler():
    global scheduler_running, scheduler
    if not scheduler_running:
        # Reinitialize scheduler
        scheduler = BackgroundScheduler()
        scheduler.add_job(generate_and_store_data, 'interval', seconds=10)
        scheduler.start()
        scheduler_running = True
        return jsonify({'message': 'Scheduler started.'})
    else:
        return jsonify({'message': 'Scheduler is already running.'})


# Route to stop scheduler
@app.route('/stop', methods=['POST'])
def stop_scheduler():
    global scheduler_running, scheduler
    if scheduler_running:
        scheduler.shutdown()
        scheduler_running = False
        return jsonify({'message': 'Scheduler stopped.'})
    else:
        return jsonify({'message': 'Scheduler is not running.'})


if __name__ == '__main__':
    app.run(debug=True)
