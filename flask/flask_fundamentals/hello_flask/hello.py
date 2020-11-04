from flask import Flask  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response

@app.route('/dojo')
def dojo():
  return "Dojo!"    

@app.route('/say/<flask>') # for a route '/hello/____' anything after '/hello/' gets passed as a variable 'name'
def hi(flask):
    print(flask)
    return "Hi, " + flask

@app.route('/users/<username>/') # for a route '/users/____/____', two parameters in the url get passed as username and id
def show_user_profile(username):
    print(username)
    return "username: " + username 

@app.route('/repeat/<number>/<hello>')
def hello(number, hello):    
    number=int(number)
    return hello * number

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.
