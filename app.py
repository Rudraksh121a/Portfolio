from flask import Flask, render_template, json

app = Flask(__name__)

@app.route('/')
def portfolio():
    # Load metadata from JSON file
    with open('data.json', 'r') as f:
        data = json.load(f)
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)