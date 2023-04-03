class Admin:
    def __init__(self,name,email,pwd):
        self.admin_name = name
        self.admin_email = email
        self.admin_password = pwd

class Doctor:
    def __init__(self,name,contact,city,qual,conHours,fee):
        self.doctor_name = name
        self.doctor_contact = contact
        self.doctor_city = city
        self.doctor_qualification = qual
        self.doctor_consulting_hours = conHours
        self.doctor_consulting_fee = fee
    def printDoc(self):
        print("Name="+self.doctor_name)
        print("city="+self.doctor_city)

class Doctor1:
    def __init__(self,id,name,contact,city,qual,conHours,fee):
        self.ID = id
        self.doctor_name = name
        self.doctor_contact = contact
        self.doctor_city = city
        self.doctor_qualification = qual
        self.doctor_consulting_hours = conHours
        self.doctor_consulting_fee = fee

class nurse:
    def __init__(self,name,contact,dept):
        self.nurse_name=name
        self.nurse_contact = contact
        self.nurse_department = dept

class nurse1:
    def __init__(self,id,name,contact,dept):
        self.ID = id
        self.nurse_name=name
        self.nurse_contact = contact
        self.nurse_department = dept

class patient:
    def __init__(self,name,cnic,age,dob,contact,city,email,pwd,bdgroup,gender,disease):
        self.patient_name = name
        self.patient_cnic = cnic
        self.patient_age = age
        self.patient_dob = dob
        self.patient_contact = contact
        self.patient_city = city
        self.patient_email = email
        self.patient_password = pwd
        self.patient_blood_group = bdgroup
        self.patient_gender = gender
        self.patient_disease = disease


