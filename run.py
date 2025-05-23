from flask import Flask, render_template

app = Flask(__name__, template_folder='app/templates')

@app.route('/')
def index():
    return render_template('views/index.html') 

if __name__ == '__main__':
    app.run(debug=True)
