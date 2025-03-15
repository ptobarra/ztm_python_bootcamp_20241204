from flask import Flask, render_template, url_for

app = Flask(__name__)
print(__name__)

@app.route("/<username>/<int:post_id>")
def hello_world(username=None, post_id=None):
    # return "<p>Hello, World!</p>"
    # return "Hello, PEDRO!"
    # print(url_for('static', filename='bolt.ico'))
    return render_template("remember_index.html", name=username, post_id=post_id)

# @app.route("/blog")
# def blog():    
#     return "These are my thoughts on blogs!"

# @app.route("/favicon.ico")
# def blog():    
#     return "These are my thoughts on blogs!"

@app.route("/blog/2020/dogs")
def blog2():    
    return "This is my dog!"

@app.route("/about.html")
def about():    
    return render_template("remember_about.html")

# set FLASK_APP=remember_server.py
# set FLASK_ENV=development  # to enable debug mode
# flask run

# flask --app remember_server.py run
# set FLASK_APP='C:\Users\ptoba\OneDrive\zero to mastery 20221030\ztm_python_bootcamp_20241204\web_development\web_server\remember_server.py'
# set FLASK_APP='.\web_development\web_server\remember_server.py'
# flask --app 'C:\Users\ptoba\OneDrive\zero to mastery 20221030\ztm_python_bootcamp_20241204\web_development\web_server\remember_server.py' run

# flask --app 'C:\Users\ptoba\OneDrive\zero to mastery 20221030\ztm_python_bootcamp_20241204\web_development\web_server\remember_server.py' run --debug