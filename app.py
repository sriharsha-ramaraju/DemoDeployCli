from flask import Flask
app= Flask(__name__)

@app.route('/') # / is for home page , if you say /sriharsha then it will navigate to sriharhsa page inside home page
def home():
    return "<center><h1> app which i deployed using azure web servcie using azureCLI-to see <h1>" # for home page to dislay the heading (h1) at the center of the page
if __name__ == '__main__':
    app.run(debug=True)