from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/my page/me', methods=['GET'])
def abase():
       return render_template("abase.html")
   

@app.route('/my page/about', methods=['GET'])
def about():
       return render_template("about.html")
  

@app.route('/my page/contact', methods=['POST'])
def display_contact():
    data = request.form
    print(data)
       return redirect("/mypage/contact")