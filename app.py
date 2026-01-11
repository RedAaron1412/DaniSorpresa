from flask import Flask, render_template, jsonify
app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template("index.html")

@app.route("/prueba")
def prueba():
    return jsonify({"mensaje": "Hola"})

if __name__ == "__main__":
    app.run(debug=True)
