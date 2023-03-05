from flask import Flask

app = Flask(__name__)

@app.route("/",methods=['GET']) ### localhost:port_number/home

##localhost:port_number/result_page

def home():
    return "this our first flask application"

if __name__ == "__main__":
    #app.run(debug=True)
    app.run(host = '0.0.0.0',port = 8000)


