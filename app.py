from flask import Flask,render_template,request
from HMS_Model import HMS_Model
from Classes import *
import pymysql

app = Flask(__name__)

@app.route('/')
def hello_world():  # put application's code here
    model = HMS_Model("localhost", "root", "", "hms")
    records = model.getAllDoctors()
    nurses = model.getAllNurses()
    return render_template("Admin.html", doctorList=records, nurseList=nurses)
    # return render_template("insertPatient.html")


##################################################Start of DOCTOR UPDATION#################################

@app.route('/updateDoctor',methods=['POST','GET'])
def updateDoctor():
    id = request.args.get("updateButton")
    model = HMS_Model("localhost", "root", "", "hms")
    doc = model.getDoctorbyID(id)
    return render_template("UpdateDoctor.html",doctor=doc)

@app.route('/updateDoctor1',methods = ["POST"])
def doctor_update():
    id = request.form["id"]
    name = request.form["name"]
    contact = request.form["contact"]
    city = request.form["city"]
    qual = request.form["qualification"]
    conhour = request.form["conhours"]
    fee = request.form["fee"]
    doc = Doctor1(id,name, contact, city, qual, conhour, fee)
    model = HMS_Model("localhost", "root", "", "hms")
    update = model.update_doctor(doc)
    if update==True:
        return ("Done")
    else:
        return ("Failed")

##################################End of doctor updation###############################################################



##################################START OF NURSE UPDATION##############################################################

@app.route('/updateNurse',methods=['POST','GET'])
def updateNurse():
    id = request.args.get("updateButton")
    model = HMS_Model("localhost", "root", "", "hms")
    nur = model.getNursebyID(id)
    return render_template("UpdateNurse.html",nurse=nur)

@app.route('/updateNurse1',methods = ["POST"])
def nurse_update():
    id = request.form["id"]
    name = request.form["name"]
    contact = request.form["contact"]
    dept = request.form["dept"]
    nurse = nurse1(id,name,contact,dept)
    model = HMS_Model("localhost", "root", "", "hms")
    update = model.update_Nurse(nurse)
    if update==True:
        return ("Done")
    else:
        return ("Failed")

@app.route('/AddNurse')
def Addnurse():
    return render_template("Add_Nurse.html")

@app.route('/AddNurse',methods=["POST"])
def add_Nurse():
    name=request.form["name"]
    contact = request.form["contact"]
    dept = request.form["dept"]
    n = nurse(name,contact,dept)
    model = HMS_Model("localhost", "root", "", "hms")
    if model.insertNurse(n):
        return ("Nurse Added")
    else:
        return ("failed")


@app.route('/deleteDoctor',methods=['POST','GET'])
def deleteDoctor():
    id = request.args.get("deleteButton")
    model = HMS_Model("localhost", "root", "", "hms")
    nur = model.getDoctorbyID(id)
    #print(id)
    res = model.delete_Doctor(id)
    if res:
        return("Done")
    else:
        return("Failed")


if __name__ == '__main__':
    app.run()

######################################     START OF DELETING NURSE   #################################

@app.route('/deleteNurse',methods=['POST','GET'])
def deleteNurse():
    id = request.args.get("deleteButton")
    model = HMS_Model("localhost", "root", "", "hms")
    nur = model.getNursebyID(id)
    #print(id)
    res = model.delete_Nurse(id)
    if res:
        return("Done")
    else:
        return("Failed")


@app.route('/AddDoctor')
def add_doc():
    return render_template("Add_Doctor.html")

@app.route('/AddDoctor',methods=["POST"])
def add_Doctor():
    name = request.form["name"]
    contact = request.form["contact"]
    city = request.form["city"]
    qual = request.form["qualification"]
    conhour = request.form["conhours"]
    fee = request.form["fee"]
    doc = Doctor(name,contact,city,qual,conhour,fee)
    model = HMS_Model("localhost", "root", "", "hms")
    if model.insertDoctor(doc):
        return ("Doctor Added")
    else:
        return ("failed")

@app.route('/Admin')
def adminview():
    model = HMS_Model("localhost", "root", "", "hms")
    records = model.getAllDoctors()
    nurses = model.getAllNurses()
    return render_template("Admin.html", doctorList=records, nurseList=nurses)

@app.route("/login", methods=["POST"])
def login():
    name = request.form["name"]
    email = request.form["email"]
    password = request.form["pwd"]
    admin = Admin(name,email,password)
    model = HMS_Model("localhost", "root", "", "hms")
    exist = model.signincheckExist(admin)
    if exist:
        return render_template("index.html")
    else:
        return render_template("loginAdmin.html")


# @app.route("/signupform")
# def signupform():
#     return render_template("Signup.html",error=False,errormsg=None)
#
# @app.route("/signup", methods=["POST"])
# def signup():
#     email=request.form["email"]
#     password = request.form["pwd"]
#     user=Admin(email,password)
#     model=HMS_Model("localhost","root","","lab6")
#     exist=model.checkUserExist(user)
#     if not exist:
#         insert=model.insertUser(user)
#         if insert:
#             return render_template("Test.html",name=email)
#         else:
#             return render_template("Signup.html", error=True , errormsg="Some error in signup")
#     else:
#         return render_template("Signup.html",error=True,errormsg="Email already exist")
#
@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/doctors')
def doctors():
    return render_template('doctors.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/blogdetails')
def details():
    return  render_template('blog-details.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run()
