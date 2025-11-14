from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return "Bienvenido a mi aplicación de Flask 🐍"

@app.route('/html')
def html():
    return "<button>Dame click</button>"

@app.route('/json')
def json():
    return {"ok": True}

@app.route('/user/<name>')
def user(name):
    return f"Hola {name}"

@app.route('/post/<int:post_id>')
def post(post_id):
    return f"Post {post_id * 2}"

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    return data

@app.post('/document')
def document():
    form = request.form['type']
    file = request.files['file']
    print(form, file)
    return "Documento"

@app.get('/hello')
def hello():
    return render_template('hello.html')

@app.get('/search')
def search():
    page = request.args.get('page')
    perPage = request.args.get('perPage')
    print(page, perPage)
    return "Search"

if __name__ == '__main__':
    app.run(debug=True)