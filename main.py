from flask import Flask,render_template

# instanciando p Flask na variavel padrão
app = Flask(__name__)

# route = url do site
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ola")
def ola():
    return "ola boi"

if __name__ == "__main__":
    app.run(debug=False)