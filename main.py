# from flask import Flask, jsonify, render_template
# import flask_monitoringdashboard as dashboard
# import time
# from random import randint
# import threading
# from apscheduler.schedulers.background import BackgroundScheduler
# import random
#
# app = Flask(__name__)
#
# # dashboard.config.init_from(envvar='FLASK_MONITORING_DASHBOARD_CONFIG')
# dashboard.config.init_from(file=r'C:\Users\shiva\PycharmProjects\pythonProject\config.cfg')
#
#
# def numberOfNewCustomers():
#     return float(randint(1, 5))
#
#
# numberOfNewCustomers_schedule = {'seconds': 10}
# midnight_schedule = {'month': "*",
#                      'day': "*",
#                      'hour': 23,
#                      'minute': 59,
#                      'second': 00}
# dashboard.add_graph("Every 10 Seconds",
#                     numberOfNewCustomers,
#                     "interval",
#                     **numberOfNewCustomers_schedule)
#
# # Make sure to call config.init_from() before bind()
# #dashboard.bind(app)
#
#
# @app.route('/')
# def login_to_flask():
#     return render_template('index.html')
#
#
# @app.route('/home')
# def home():
#     return render_template('home.html')
#
# #def print_message():
# #    while True:
# #        print("Hello, welcome to the Flask app!")
# #        time.sleep(60)  # 60 seconds = 1 minutes
#
#
# #@app.route('/')
# #def index():
# #    return print_message()
#
#
# @app.route('/endpoint1')
# def endpoint1():
#     time.sleep(0.20)
#     return 'Endpoint1', 400
#
#
# @app.route('/endpoint2')
# def endpoint2():
#     time.sleep(5)
#     return 'Endpoint2'
#
#
# @app.route('/monitor')
# def monitor():
#     while True:
#         print("Hello")
#         time.sleep(120)  # Sleep for 2 minutes (120 seconds)
#
#
# # Example data
# #data = {'message': 'Hello, world!'}
#
#
# # Function to save data to a text file
# #def save_data():
# #    with open('output.txt', 'w') as file:
# #        file.write(str(data))
# #    print("Data saved to output.txt")
#
#
# # Route to handle requests
# #@app.route('/api', methods=['GET'])
# #def get_data():
#     # Return data as JSON
# #    return jsonify(data)
#
#
# #def check_output_file():
# #    try:
# #        with open('output.txt', 'r') as file:
# #            data = file.read()
# #            print("Contents of output.txt:")
# #            print(data)
# #    except FileNotFoundError:
# #        print("output.txt file not found.")
# #    except Exception as e:
# #        print("An error occurred while reading output.txt:", str(e))
#
#
# # Call the function to check the output.txt file
# #check_output_file()
#
#
# # Initialize scheduler
# #scheduler = BackgroundScheduler()
#
#
# # Function to generate and store data
# #def generate_and_store_data():
#     # Generate random data
# #    data = {'random_number': random.randint(1, 100)}
#
#     # Store data in text file
# #    with open('output.txt', 'w') as file:
# #        file.write(str(data))
#
#
# # Route to get data
# #@app.route('/get_data', methods=['GET'])
# #def get_data():
# #    try:
#         # Read data from file
# #        with open('output.txt', 'r') as file:
# #            data = eval(file.read())  # Convert string to dictionary
# #        return jsonify(data)
# #    except FileNotFoundError:
# #        return jsonify({'error': 'Data file not found.'})
# #    except Exception as e:
# #        return jsonify({'error': str(e)})
#
#
# #if __name__ == '__main__':
#     # Schedule the generate_and_store_data function to run every 10 seconds
# #    scheduler.add_job(generate_and_store_data, 'interval', seconds=10)
# #    scheduler.start()
#
#     # Run Flask app
# #    dashboard.bind(app)
# #    app.run(debug=True)
#
#
# # Initialize scheduler
# scheduler = BackgroundScheduler()
#
# # Variable to track if scheduler is running
# scheduler_running = False
#
#
# # Function to generate and store data
# def generate_and_store_data():
#     # Generate random data
#     data = {'random_number': random.randint(1, 100)}
#
#     # Store data in text file
#     with open('output.txt', 'w') as file:
#         file.write(str(data))
#
#
# # Route to get data
# @app.route('/get_data', methods=['GET'])
# def get_data():
#     try:
#         # Read data from file
#         with open('output.txt', 'r') as file:
#             data = eval(file.read())  # Convert string to dictionary
#         return jsonify(data)
#     except FileNotFoundError:
#         return jsonify({'error': 'Data file not found.'})
#     except Exception as e:
#         return jsonify({'error': str(e)})
#
#
# # Route to render template with buttons
# @app.route('/')
# def index():
#     return render_template('index.html')
#
#
# # Route to start scheduler
# @app.route('/start', methods=['POST'])
# def start_scheduler():
#     global scheduler_running, scheduler
#     if not scheduler_running:
#         # Reinitialize scheduler
#         scheduler = BackgroundScheduler()
#         scheduler.add_job(generate_and_store_data, 'interval', seconds=1)
#         scheduler.start()
#         scheduler_running = True
#         return jsonify({'message': 'Scheduler started.'})
#     else:
#         return jsonify({'message': 'Scheduler is already running.'})
#
#
# # Route to stop scheduler
# @app.route('/stop', methods=['POST'])
# def stop_scheduler():
#     global scheduler_running, scheduler
#     if scheduler_running:
#         scheduler.shutdown()
#         scheduler_running = False
#         return jsonify({'message': 'Scheduler stopped.'})
#     else:
#         return jsonify({'message': 'Scheduler is not running.'})
#
#
# if __name__ == '__main__':
#     dashboard.bind(app)
#     app.run(debug=True)
#
# from flask import Flask, jsonify, render_template
# import flask_monitoringdashboard as dashboard
# from apscheduler.schedulers.background import BackgroundScheduler
# import random
# import time
# app = Flask(__name__)
#
# # Initialize the Flask Monitoring Dashboard with the config file
# dashboard.config.init_from(file=r'C:\Users\shiva\PycharmProjects\pythonProject\config.cfg')
#
# # Function to generate and store data
# def generate_and_store_data():
#     data = {'random_number': random.randint(1, 100)}
#     with open('output.txt', 'w') as file:
#         file.write(str(data))
#
# # Route to get data
# @app.route('/get_data', methods=['GET'])
# def get_data():
#     try:
#         with open('output.txt', 'r') as file:
#             data = eval(file.read())  # Convert string to dictionary
#         return jsonify(data)
#     except FileNotFoundError:
#         return jsonify({'error': 'Data file not found.'})
#     except Exception as e:
#         return jsonify({'error': str(e)})
#
# # Route to render the index template with buttons
# @app.route('/')
# def index():
#     return render_template('index.html')
#
# @app.route('/home')
# def home():
#     return render_template('home.html')
#
# # Initialize scheduler
# scheduler = BackgroundScheduler()
# scheduler_running = False
#
# # Route to start the scheduler
# @app.route('/start', methods=['POST'])
# def start_scheduler():
#     global scheduler_running, scheduler
#     if not scheduler_running:
#         scheduler = BackgroundScheduler()
#         scheduler.add_job(generate_and_store_data, 'interval', seconds=10)  # Schedule every 10 seconds
#         scheduler.start()
#         scheduler_running = True
#         return jsonify({'message': 'Scheduler started.'})
#     else:
#         return jsonify({'message': 'Scheduler is already running.'})
#
# # Route to stop the scheduler
# @app.route('/stop', methods=['POST'])
# def stop_scheduler():
#     global scheduler_running, scheduler
#     if scheduler_running:
#         scheduler.shutdown()
#         scheduler_running = False
#         return jsonify({'message': 'Scheduler stopped.'})
#     else:
#         return jsonify({'message': 'Scheduler is not running.'})
#
# # Route to simulate endpoint1 with delay and error
# @app.route('/endpoint1')
# def endpoint1():
#     time.sleep(0.20)
#     return 'Endpoint1', 400
#
# # Route to simulate endpoint2 with delay
# @app.route('/endpoint2')
# def endpoint2():
#     time.sleep(5)
#     return 'Endpoint2'
#
# # Route to get all available routes
# @app.route('/routes', methods=['GET'])
# def get_routes():
#     route_list = []
#     for rule in app.url_map.iter_rules():
#         if rule.endpoint != 'static':
#             route_list.append({
#                 'endpoint': rule.endpoint,
#                 'url': str(rule)
#             })
#     return jsonify(route_list)
#
# if __name__ == '__main__':
#     dashboard.bind(app)
#     app.run(debug=True)





from flask import Flask, jsonify, render_template, request
import flask_monitoringdashboard as dashboard
from apscheduler.schedulers.background import BackgroundScheduler
import random
import time

app = Flask(__name__)

# Initialize the Flask Monitoring Dashboard with the config file
dashboard.config.init_from(file=r'C:\Users\shiva\PycharmProjects\pythonProject\config.cfg')

# Initialize scheduler
scheduler = BackgroundScheduler()
scheduler_running = False
endpoint1_running = False
endpoint2_running = False
get_data_running = False  # Global variable to track /get_data status


# Function to generate and store data
def generate_and_store_data():
    data = {'random_number': random.randint(1, 100)}
    with open('output.txt', 'w') as file:
        file.write(str(data))




# Route to render the index template with buttons
@app.route('/')
def home():
    return render_template('home.html')


@app.route('/index')
def index():
    return render_template('index.html')


# Route to start the scheduler
@app.route('/start_scheduler', methods=['POST'])
def start_scheduler():
    global scheduler_running, scheduler
    if not scheduler_running:
        scheduler = BackgroundScheduler()
        scheduler.add_job(generate_and_store_data, 'interval', seconds=10)  # Schedule every 10 seconds
        scheduler.start()
        scheduler_running = True
        return jsonify({'message': 'Scheduler started.'})
    else:
        return jsonify({'message': 'Scheduler is already running.'})


# Route to stop the scheduler
@app.route('/stop_scheduler', methods=['POST'])
def stop_scheduler():
    global scheduler_running, scheduler
    if scheduler_running:
        scheduler.shutdown()
        scheduler_running = False
        return jsonify({'message': 'Scheduler stopped.'})
    else:
        return jsonify({'message': 'Scheduler is not running.'})


# Route to simulate endpoint1 with delay and error
@app.route('/endpoint1', methods=['GET', 'POST'])
def endpoint1():
    global endpoint1_running
    if request.method == 'POST':
        action = request.json.get('action')
        if action == 'start':
            endpoint1_running = True
            return jsonify({'message': 'Endpoint1 started.'})
        elif action == 'stop':
            endpoint1_running = False
            return jsonify({'message': 'Endpoint1 stopped.'})
    if endpoint1_running:
        time.sleep(0.20)
        return 'Endpoint1', 400
    return 'Endpoint1 is stopped', 200


# Route to simulate endpoint2 with delay
@app.route('/endpoint2', methods=['GET', 'POST'])
def endpoint2():
    global endpoint2_running
    if request.method == 'POST':
        action = request.json.get('action')
        if action == 'start':
            endpoint2_running = True
            return jsonify({'message': 'Endpoint2 started.'})
        elif action == 'stop':
            endpoint2_running = False
            return jsonify({'message': 'Endpoint2 stopped.'})
    if endpoint2_running:
        time.sleep(5)
        return 'Endpoint2'
    return 'Endpoint2 is stopped', 200


# VSDS APIS


@app.route('/vsds')
def vsds():
    return render_template('vsds.html')

@app.route('/Send_Data_vsds')
def Send_Data_vsds():
    return render_template('VSDS_Send_Data.html')


@app.route('/Send_Image_vsds')
def Send_Image_vsds():
    return render_template('VSDS_Send_Image.html')


@app.route('/Fetch_Coords_vsds')
def Fetch_Coords_vsds():
    return render_template('VSDS_Fetch_Coords.html')


@app.route('/First_Frame_vsds')
def First_Frame_vsds():
    return render_template('VSDS_First_Frame.html')


@app.route('/Vehicle_Selection_vsds')
def Vehicle_Selection_vsds():
    return render_template('VSDS_Vehicle_Selection.html')


@app.route('/Operation_Selection_vsds')
def Operation_Selection_vsds():
    return render_template('VSDS_Operation_Selection.html')


# VIDS APIS


@app.route('/vids')
def vids():
    return render_template('vids.html')


@app.route('/Send_Data_vids')
def Send_Data_vids():
    return render_template('VIDS_Send_Data.html')


@app.route('/Send_Image_vids')
def Send_Image_vids():
    return render_template('VIDS_Send_Image.html')


@app.route('/Fetch_Coords_vids')
def Fetch_Coords_vids():
    return render_template('VIDS_Fetch_Coords.html')


@app.route('/First_Frame_vids')
def First_Frame_vids():
    return render_template('VIDS_First_Frame.html')


@app.route('/Vehicle_Selection_vids')
def Vehicle_Selection_vids():
    return render_template('VIDS_Vehicle_Selection.html')


@app.route('/Event_Selection_vids')
def Event_Selection_vids():
    return render_template('VIDS_Event_Selection.html')


# Route to get all available routes
@app.route('/routes', methods=['GET'])
def get_routes():
    route_list = []
    for rule in app.url_map.iter_rules():
        if rule.endpoint != 'static':
            route_list.append({
                'endpoint': rule.endpoint,
                'url': str(rule)
            })
    return jsonify(route_list)


if __name__ == '__main__':
    dashboard.bind(app)
    app.run(debug=True)
