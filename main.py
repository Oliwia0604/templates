from flask import render_template

@app.route('/abase', methods=['GET'])
def abase():
   if request.method == 'GET':
       print("We received GET")
       return render_template("abase.html")
   

@app.route('/about', methods=['GET'])
def about():
   if request.method == 'GET':
       print("We received GET")
       return render_template("about.html")
  

@app.route('/contact', methods=['GET', 'POST'])
def contact():
   if request.method == 'GET':
       print("We received GET")
       return render_template("contact.html")
   elif request.method == 'POST':
       print("We received POST")
       print(request.form)
       return redirect("/")