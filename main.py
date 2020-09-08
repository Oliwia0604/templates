from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/mypage/contact', methods=['GET'])
def contact():
    return render_template("contact.html")
   

@app.route('/mypage/about', methods=['GET'])
def about():
    return render_template("about.html")
  

@app.route('/mypage/contact', methods=['POST'])
def display_contact():
    data = request.form
    print(data)
    return redirect("/mypage/contact")