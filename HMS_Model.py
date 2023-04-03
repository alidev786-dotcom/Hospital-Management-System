import pymysql
from Classes import *

class HMS_Model:
    def __init__(self,host,user,password,database):
        self.host=host
        self.user=user
        self.password=password
        self.database=database
        self.connection=None
        self.id=None
        try:
            self.connection=pymysql.connect(host=self.host,
                                            user=self.user,
                                            password=self.password,
                                            database=self.database)
        except Exception as e:
            print("There is error in connection",str(e))

    def __del__(self):
        if self.connection!=None:
            self.connection.close()

    def checkAdminExist(self,admin):
        try:
            if self.connection!=None:
                cursor = self.connection.cursor()

                cursor.execute("select email from admin ;")
                records=cursor.fetchall()
                for record in records:
                    # print(record[0])
                    if admin.email==record[7]:
                        # print("here")
                        return True
                return False
        except Exception as e:
             print("Exception in checkAdminExist",str(e))
        finally:
            if cursor!=None:
                cursor.close()

    def signincheckExist(self,admin):
        try:
            if self.connection!=None:
                cursor=self.connection.cursor()
                cursor.execute("select * from admin")
                emailList=cursor.fetchall()
                for e in emailList:
                    if admin.admin_email==e[2] and admin.admin_password==e[3]:
                        return True
                return False
        except Exception as e:
            print("Exception in checkAdminExist",str(e))
        finally:
            if cursor!=None:
                cursor.close()

    def insertAdmin(self,admin):
        try:
            if self.connection!=None:
                cursor=self.connection.cursor()
                query="insert into admin (admin_name,admin_email,admin_password) values (%s,%s,%s)"
                args=(admin.admin_name,admin.admin_email,admin.admin_password)
                cursor.execute(query,args)
                self.connection.commit()
                return True
            else:
                return False
        except Exception as e:
            print("Exception in insertAdmin",str(e))
            return False
        finally:
            if cursor!=None:
                cursor.close()

    def insertDoctor(self,doc):
        try:
            if self.connection != None:
                cursor = self.connection.cursor()
                query = "insert into doctors(doctor_name,doctor_contact,doctor_city,doctor_qualification,doctor_consultingHours,doctor_consultingFee) values (%s,%s,%s,%s,%s,%s)"
                args = (doc.doctor_name,doc.doctor_contact,doc.doctor_city,doc.doctor_qualification,doc.doctor_consulting_hours,doc.doctor_consulting_fee)
                cursor.execute(query, args)
                self.connection.commit()
                return True
            else:
                return False
        except Exception as e:
            print("Exception in insertDoctor", str(e))
            return False
        finally:
            if cursor != None:
                cursor.close()

    def loginAdmin(self, admin):
        try:
            if self.connection != None:
                cursor = self.connection.cursor()
                query = "SELECT admin_name,admin_email,admin_password FROM admin WHERE admin_name=%s AND admin_email=%s AND admin_password=%s"

                args = (admin.admin_name,
                        admin.admin_email,
                        admin.admin_password)

                cursor.execute(query, args)
                record = cursor.fetchone()
                if record[2] == admin.admin_email:
                     return True
                else:
                     return False
            else:
                return False
        except Exception as e:
            return False
            print("Exception in loginUser", str(e))
        finally:
            if cursor != None:
                cursor.close()

    def insertNurse(self,nurse):
        try:
            if self.connection!=None:
                cursor=self.connection.cursor()
                query="insert into nurse(nurse_name,nurse_contact,department) values (%s,%s,%s)"
                args = (nurse.nurse_name,
                        nurse.nurse_contact,
                        nurse.nurse_department)
                cursor.execute(query,args)
                self.connection.commit()
                return True
            else:
                return False
        except Exception as e:
            print("Erron in insertNurse",e)
        finally:
            if cursor!=None:
                cursor.close()

    def getDoctorbyID(self,id):
        try:
            if self.connection != None:
                cursor = self.connection.cursor()
                query = ("select doctor_id, doctor_name,doctor_contact,doctor_city,doctor_qualification,doctor_consultingHours,doctor_consultingFee from doctors where doctor_id=%s")
                args = (id)
                cursor.execute(query,args)
                res = cursor.fetchone()

                doc = Doctor1(res[0],res[1],res[2],res[3],res[4],res[5],res[6])
                # doc.printDoc()
                return doc

        except Exception as e:
            print("Failed")
            print(e)
        finally:
            if cursor != None:
                cursor.close()
#########################   Displaying Doctors    ####################################################

    def getAllDoctors(self):
        try:
            if self.connection != None:
                cursor = self.connection.cursor()
                cursor.execute("select * from doctors")
                records = cursor.fetchall()
                doctorList = []
                for r in records:
                    doctorList.append(Doctor1(r[0], r[1],r[2], r[3],r[4], r[5],r[6]))

                return doctorList
        except Exception as e:
            print("Exception in getAllUsers", str(e))
        finally:
            if cursor != None:
                cursor.close()

    #########################   Displaying NURSES    ####################################################

    def getAllNurses(self):
        try:
            if self.connection != None:
                cursor = self.connection.cursor()
                cursor.execute("select * from nurse")
                records = cursor.fetchall()
                nurseList = []
                for r in records:
                    nurseList.append(nurse1(r[0],r[1], r[2], r[3]))

                return nurseList
        except Exception as e:
            print("Exception in getAllUsers", str(e))
        finally:
            if cursor != None:
                cursor.close()


    def update_doctor(self,doctor):
        try:
            if self.connection != None:
                cursor = self.connection.cursor()
                query = "update doctors set doctor_name=%s,doctor_contact =%s,doctor_city=%s,doctor_qualification=%s,doctor_consultingHours=%s,doctor_consultingFee=%s where doctor_id=%s"
                args = (doctor.doctor_name,doctor.doctor_contact,doctor.doctor_city,doctor.doctor_qualification,doctor.doctor_consulting_hours,doctor.doctor_consulting_fee,doctor.ID)
                cursor.execute(query, args)
                self.connection.commit()
                return True
            else:
                return False
        except Exception as e:
            print("DATABASE ERROR!" + str(e))
            return False
        finally:
            cursor.close()

    def getNursebyID(self,id):
        try:
            if self.connection != None:
                cursor = self.connection.cursor()
                query = ("select nurse_id, nurse_name,nurse_contact,department from nurse where nurse_id=%s")
                args = (id)
                cursor.execute(query,args)
                res = cursor.fetchone()

                nur = nurse1(res[0],res[1],res[2],res[3])
                # doc.printDoc()
                return nur

        except Exception as e:
            print("Failed")
            print(e)
        finally:
            if cursor != None:
                cursor.close()

    def update_Nurse(self, nurse):
        try:
            if self.connection != None:
                cursor = self.connection.cursor()
                query = "update nurse set nurse_name=%s,nurse_contact =%s,department=%s where nurse_id=%s"
                args = (nurse.nurse_name,nurse.nurse_contact,nurse.department,nurse.ID)
                cursor.execute(query, args)
                self.connection.commit()
                return True
            else:
                return False
        except Exception as e:
            print("DATABASE ERROR!" + str(e))
            return False
        finally:
            cursor.close()

    def delete_Nurse(self,nurse_i):
        try:
            if self.connection != None:
                print(nurse_i)
                cursor = self.connection.cursor()
                query = "delete from nurse where nurse_id=%s"
                args = (nurse_i)
                cursor.execute(query, args)
                self.connection.commit()
                cursor.close()
                return True
            else:
                return False
        except Exception as e:
            print("ERROR in Delete Nurse!" + str(e))
            return  False

    def delete_Doctor(self,doc_i):
        try:
            if self.connection != None:
                cursor = self.connection.cursor()
                query = "delete from doctors where doctor_id=%s"
                args = (doc_i)
                cursor.execute(query, args)
                self.connection.commit()
                cursor.close()
                return True
            else:
                return False
        except Exception as e:
            print("ERROR in Delete Doctor!" + str(e))
            return  False




    def insertPatient(self,pat):
        try:
            if self.connection!=None:
                cursor=self.connection.cursor()
                query="INSERT INTO patient(patient_name,patient_cnic,patient_age,patient_dob,patient_contact,patient_city,patient_email,patient_password,patient_bloodGroup,patient_gender,patient_disease) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
                args=(pat.patient_name,
                      pat.patient_cnic,
                      pat.patient_age,
                      pat.patient_dob,
                      pat.patient_contact,
                      pat.patient_city,
                      pat.patient_email,
                      pat.patient_password,
                      pat.patient_blood_group,
                      pat.patient_gender,
                      pat.patient_disease)
                cursor.execute(query,args)
                self.connection.commit()
                return True
            else:
                return False
        except Exception as e:
            print("Exception in checkAdminExist",str(e))
            return False
        finally:
            if cursor!=None:
                cursor.close()