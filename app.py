from distutils.command.build_scripts import first_line_re
from flask import Flask, jsonify, redirect, request, make_response
from werkzeug.utils import secure_filename
import urllib.request
import os
import jwt
import uuid
import psycopg2
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from models import app, db, SECRET_KEY, Employers, Employees, association, Association
# app= Flask(__name__) 
# db= SQLAlchemy(app)

@app.route('/employerinfo', methods=['POST', 'GET'])
def upload_get_all():
    if request.method == 'POST':
        body=request.json
        # body= request.form.get()
        print(body)
        company = body['company']
        first_name = body['first_name']
        last_name = body['last_name']
        email = body['email']
        data=Employers(company, first_name, last_name, email)
        db.session.add(data)
        db.session.commit()
        return jsonify({
                       
                        "company": company,
                        "first_name": first_name, 
                        "last_name":last_name,
                        "email":email
        })

    if request.method == 'GET':
        allinfo=Employers.query.all()
        output= []
        if allinfo:
            for info in allinfo:
                data= {}
                data["id"]= info.id
                data["company"]=info.company
                data["first_name"]=info.first_name
                data["last_name"]=info.last_name
                data["email"]=info.email
                output.append(data)
                # print(info)
            return jsonify({"data": output})
        
        else:
            return jsonify({'message': "No data present"})

@app.route('/employer_info/<id>', methods=['GET','DELETE', 'PUT'])
def info_per_id(id):
    if request.method== 'GET':
        allinfo=Employers.query.get(id)
        if allinfo:
            info={ 
                    "company": allinfo.company,
                    "first_name": allinfo.first_name, 
                    "last_name":allinfo.last_name,
                    "email":allinfo.email

            }
            return jsonify({"data": info})

        else:
            return jsonify({"message":f"the id {id} does not exist."})    
    
    if request.method=='DELETE':
        allinfo= Employers.query.get(id)
        db.session.delete(allinfo)
        db.session.commit()
        return jsonify({"message": f"The id {id} is deleted" })
    
    
    if request.method=='PUT':
        body=request.json
        newcompany = body['company']
        newfirst_name= body['first_name']
        newlast_name=body['last_name']
        newemail= body['email']

        allinfo=Employers.query.filter_by(id=id).first()
        
        allinfo.company=newcompany
        allinfo.first_name=newfirst_name
        allinfo.last_name=newlast_name
        allinfo.email=newemail
        db.session.add(allinfo)
        db.session.commit()
        return jsonify({"message": "The data has been updated"})
    else:
        return jsonify({"message": f"id {id} does not exist."})

        

        
#***************************Employee's Data**************************************************


# @app.route('/employeeinfo', methods=['POST', 'GET'])
# def upload_empdata_all():
#     if request.method == 'POST':
#         body=request.json
#         worksfor = body['worksfor']
#         first_name = body['first_name']
#         last_name = body['last_name']
#         email = body['email']
#         data=Employees(worksfor, first_name, last_name, email)
#         db.session.add(data)
#         db.session.commit()
#         return jsonify({
#                         "worksfor": worksfor,
#                         "first_name": first_name, 
#                         "last_name":last_name,
#                         "email":email
#         })



#     if request.method == 'GET':
#         allinfo=Employees.query.all()
#         output= []
#         if allinfo:
#             for info in allinfo:
#                 data= {}
#                 data["id"]= info.id
#                 data["worksfor"]=info.worksfor
#                 data["first_name"]=info.first_name
#                 data["last_name"]=info.last_name
#                 data["email"]=info.email
#                 output.append(data)
#                 # print(info)
#             return jsonify({"data": output})
        
#         else:
#             return jsonify({'message': "No data present"})

# @app.route('/employee_info/<id>', methods=['GET','DELETE', 'PUT'])
# def info_per_id1(id):
#     if request.method=='GET':
#         allinfo=Employees.query.get(id)
        
#         if allinfo:
#             info={ 
#                     "worksfor": allinfo.worksfor,
#                     "first_name": allinfo.first_name, 
#                     "last_name":allinfo.last_name,
#                     "email":allinfo.email

#             }
#             return jsonify({"data": info})

#         else:
#             return jsonify({"message":f"the id {id} does not exist."})  


#     if request.method=='DELETE':
#         allinfo= Employees.query.get(id)
#         if allinfo:
#             db.session.delete(allinfo)
#             db.session.commit()
#             return jsonify({"message": f"The id {id} is deleted" })
#         else:
#             return jsonify({"message": f"the id {id} does not exist."})

#     if request.method=='PUT':
#         body=request.json
#         newworksfor = body['worksfor']
#         newfirst_name= body['first_name']
#         newlast_name=body['last_name']
#         newemail= body['email']

#         allinfo=Employees.query.filter_by(id=id).first()

#         allinfo.worksfor=newworksfor
#         allinfo.first_name=newfirst_name
#         allinfo.last_name=newlast_name
#         allinfo.email=newemail
#         db.session.add(allinfo)
#         db.session.commit()
#         return jsonify({"message": "The data has been updated"})


# **************************************************Association***************************************************

# @app.route("/association/<int:employers_id>/<int:employees_id>")
# def associate(employers_id,employees_id ):
#     try:
#         associate= Association(employers_id, employees_id)
#         # print(associate.employers_id)
#         # print(associate.employees_id)
#         db.session.add(associate)
#         db.session.commit()
#         return jsonify({"message":"ok"} )

        
#     except Exception as error:
#         return(str(error))
        
# @app.route("/")



@app.route('/employeeinfo', methods=['POST', 'GET'])
def upload_empdata_all():
    if request.method == 'POST':
        body=request.json
        worksfor = body['worksfor']
        first_name = body['first_name']
        last_name = body['last_name']
        email = body['email']
        data=Employees(worksfor, first_name, last_name, email)
        db.session.add(data)
        db.session.commit()
        return jsonify({
                        "worksfor": worksfor,
                        "first_name": first_name, 
                        "last_name":last_name,
                        "email":email
        })



    if request.method == 'GET':
        allinfo=Employees.query.all()
        output= []
        if allinfo:
            for info in allinfo:
                data= {}
                data["id"]= info.id
                data["worksfor"]=info.worksfor
                data["first_name"]=info.first_name
                data["last_name"]=info.last_name
                data["email"]=info.email
                output.append(data)
                # print(info)
            return jsonify({"data": output})
        
        else:
            return jsonify({'message': "No data present"})

@app.route('/employee_info/<id>', methods=['GET','DELETE', 'PUT'])
def info_per_id1(id):
    if request.method=='GET':
        allinfo=Employees.query.get(id)
        
        linked = Association.query.filter_by(id).first()
        print(linked)
        print("______________________________________")
        
        
        if allinfo:
            info={ 
                                      
                    "worksfor": allinfo.worksfor,
                    "first_name": allinfo.first_name, 
                    "last_name":allinfo.last_name,
                    "email":allinfo.email

            }
            return jsonify({"data": info})

        else:
            return jsonify({"message":f"the id {id} does not exist."})  


    if request.method=='DELETE':
        allinfo= Employees.query.get(id)
        if allinfo:
            db.session.delete(allinfo)
            db.session.commit()
            return jsonify({"message": f"The id {id} is deleted" })
        else:
            return jsonify({"message": f"the id {id} does not exist."})

    if request.method=='PUT':
        body=request.json
        newworksfor = body['worksfor']
        newfirst_name= body['first_name']
        newlast_name=body['last_name']
        newemail= body['email']

        allinfo=Employees.query.filter_by(id=id).first()

        allinfo.worksfor=newworksfor
        allinfo.first_name=newfirst_name
        allinfo.last_name=newlast_name
        allinfo.email=newemail
        db.session.add(allinfo)
        db.session.commit()
        return jsonify({"message": "The data has been updated"})





if __name__ == "__main__":
    # db.mapper(Association, association)
    app.run(port=8000, debug=True)