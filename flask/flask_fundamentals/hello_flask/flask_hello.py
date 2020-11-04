from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    print("in the hello function")
    return "Hello!!"

@app.route("/<name>")
def hello_person(name):
    print("*"*80)
    print("in hello_person function")
    print(name)
    return f"Hello {name}!"

if __name__ == "__main__":
    app.run(debug=True)
