from flask import Flask,render_template,request

app=Flask(__name__)

@app.route("/")
def home():
    return render_template("reg.html")

@app.route("/register",methods=["POST","GET"])
def register():
    if request.method=="POST":
        username=request.form.get('username')
        email=request.form.get('email')
        phonenumber=request.form.get('phonenumber')
        return render_template("result.html",username=username,email=email,phonenumber=phonenumber)
if __name__ == '__main__':
    app.run(debug=True)