from flask import Flask, render_template, url_for, jsonify

app = Flask(__name__)

@app.route('/home')
def home():
    url_for('static', filename='francisco.css')
    return render_template('index.html')

@app.route('/augment', methods=['GET'])
def augment():
    data = {
        "before_augmentation": "This augmentation service is great.",
        "after_augmentation": [
            "This augmentation service is excellent.",
            "This is a great augmentation service.",
            "This service for augmentation is superb.",
            "This augmentation service is fantastic."
        ]
    }
    response = jsonify(data)
    return response

if __name__ == "__main__":
    app.run()
