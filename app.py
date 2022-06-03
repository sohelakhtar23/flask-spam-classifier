from flask import Flask, render_template, request
import model

app = Flask(__name__)

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





if __name__ == "__main__":
    app.run(debug=True)