from flask import Flask, request, redirect, url_for, render_template

app = Flask(__name__)

@app.route('/success/<name>')
def success(name):
    return 'welcome %s' % name

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form["nm"]
        return redirect(url_for('success', name=user))
    else:
        return render_template('login.html')

@app.route('/')
def index():
    return " THis is the Homepage \n  We have \n /login, /gtg, /hello/name"

@app.route('/hello/<name>')
def hello_name(name):
    #Anything inside {} is evaluated as Python code and replaced with its value.
    return f"Hello {name}"

@app.route('/code/<int:code_num>')
def code_name(code_num):
    #Anything inside {} is evaluated as Python code and replaced with its value.
    return f"Hi! Your code is {code_num}"

def gfg():
   return "geeksforgeeks"
app.add_url_rule('/gtg','gfg',gfg)

if __name__ == '__main__':
    app.run(debug=True)

print(app.url_map)
