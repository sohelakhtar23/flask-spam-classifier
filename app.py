from flask import Flask, render_template, request
import model
from flask_socketio import SocketIO

app = Flask(__name__)

app.config['SECRET_KEY'] = 'vnkdjnfjknfl1232#'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/predict', methods=["POST"])
def predict():
    # HTML -> .py
    if request.method == "POST":
        email_text = request.form["email_text"]

        predict = model.email_prediction(email_text)
        # predict_category = 'SPAM' if predict==1 else 'HAM'

    # .py -> HTML
    return render_template("index.html", msg = predict)


@app.route('/session', methods=["POST"])
def session():
    if request.method == "POST":
        user_name = request.form["username"]
        print(user_name)
    return render_template('session.html', user = user_name)

def messageReceived(methods=['GET', 'POST']):
    print('message was received!!!')

@socketio.on('my event')
def handle_my_custom_event(json, methods=['GET', 'POST']):
    print('received my event: ' + str(json))
    msg_text = str(json["message"])
    json["category"] = str(model.email_prediction(msg_text))
    print(str(json))
    socketio.emit('my response', json, callback=messageReceived)
    

if __name__ == "__main__":
    socketio.run(app, debug=True)
    # app.run(debug=True)