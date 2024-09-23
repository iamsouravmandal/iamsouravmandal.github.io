import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Get the port from the environment or use 5000 by default
    app.run(host="0.0.0.0", port=port)  # Bind to the $PORT environment variable and allow external connections

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/products')
def products():
    return render_template('products.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
