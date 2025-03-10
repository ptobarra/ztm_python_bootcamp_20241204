from flask import Flask, render_template, send_from_directory, url_for

# from dotenv import load_dotenv
# load_dotenv()

app = Flask(__name__)
# print(__name__)


@app.route("/")
def my_home():
    # print(url_for("static", filename="favicon.ico"))  # jinja python templating engine - '/static/favicon.ico'
    return render_template("./index.html")
    # return "<p>Hello !!!!!!!!!!!</p>"


@app.route("/<string:page_name>")
def html_page(page_name):    
    return render_template(page_name)


@app.route("/submit_form", methods=["POST", "GET"])
def submit_form():
    return 'form submitted hooorayyy!'


# @app.route("/index.html")
# def my_index():
#     return render_template("./index.html")


# @app.route("/works.html")
# def works():
#     return render_template("./works.html")


# @app.route("/about.html")
# def about():
#     return render_template("./about.html")
#     # return "<p>Hello !!!!!!!!!!!</p>"


# @app.route("/contact.html")
# def contact():
#     return render_template("./contact.html")


# @app.route("/components.html")
# def components():
#     return render_template("./components.html")


# @app.route("/thankyou.html")
# def thankyou():
#     return render_template("./thankyou.html")


# @app.route("/work.html")
# def work():
#     return render_template("./work.html")


# @app.route("/blog")
# def blog():
#     return "These are my thoughts on blogs!"


# @app.route("/favicon.ico")
# def favicon():
#     return send_from_directory("static", "favicon.ico")


# @app.route("/blog/2020/dogs")
# # @app.route("/blog")
# def blog2():
#     return "This is my dog!"


# On Windows (PowerShell)
# $env:FLASK_APP = 'C:\Users\TobarrP\ztm_python_bootcamp_20241204\web_development\web server\server.py'
# $env:FLASK_ENV = "development"
# python -m flask run
# python -m flask --app '.\web_development\web server\server.py' run
# http://127.0.0.1:5000/

# On Windows (Command Prompt)
# set FLASK_APP=C:\Users\TobarrP\ztm_python_bootcamp_20241204\web_development\web_server\server.py
# set FLASK_ENV=development

# python -m flask run --debug
