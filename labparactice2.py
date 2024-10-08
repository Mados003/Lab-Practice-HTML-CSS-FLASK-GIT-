from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        age = request.form['age']
        
        if not name or not email or not age:
            error = "All fields are required."
            return render_template('lab2practice.html', error=error)
        
        return render_template('result.html', name=name, email=email, age=age)
    
    return render_template('lab2practice.html')

if __name__ == '__main__':
    app.run(debug=True)
