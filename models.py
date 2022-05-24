from uuid import UUID
from matplotlib.pyplot import table
from sqlalchemy import ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy.orm import relationship, backref
from flask import Flask
import uuid
app= Flask(__name__) 

SECRET_KEY='c1b6653f2af3ef38389f562bf8681107'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:123456@localhost:5432/sqlalchemy_doc"
db= SQLAlchemy(app)
migrate=Migrate(app, db)


class Association(db.Model):
    def __init__(self,employers_id, employees_id ):
        self.employers_id=employers_id
        self.employees_id=employees_id
         
association=db.Table('association', 
                    db.Column("employers_id", db.Integer, db.ForeignKey('employers.id')) ,
                    db.Column("employees_id", db.Integer, db.ForeignKey('employees.id'))
                )

# db.Index("associate",association.employers_id, association.employees_id, unique=True )

class Employers(db.Model):
    # _tablename__= "employer"
    id=db.Column(db.Integer, primary_key=True)
    company = db.Column(db.String(255))
    first_name = db.Column(db.String(255)) #employer's
    last_name = db.Column(db.String(255)) #employer's
    email = db.Column(db.String(255)) 
    employee = db.relationship('Employees', secondary= Association, backref=db.backref("employer"), lazy='dynamic')

    def __init__(self, company, first_name, last_name, email):
        self.company=company
        self.first_name=first_name
        self.last_name=last_name
        self.email=email
        
class Employees(db.Model):
    # __tablename__="employee"
    id=db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    email = db.Column(db.String(255))
    worksfor = db.Column(db.String(255))
    # employer_id= db.Column(db.Integer, db.ForeignKey('employer.id'), nullable=True)
    # employees=db.relationship('Employers', backref="employees", lazy=True)

    def __init__(self, worksfor, first_name, last_name, email):
        self.worksfor=worksfor
        self.first_name=first_name
        self.last_name=last_name
        self.email=email
       
# class Associated(db.Model):
#     __tablename__='associations'
#     id=db.Column(db.Integer, primary_key=True)
#     employers_id = db.Column(db.Integer, db.ForeignKey('employers.id'))
#     empolyee_id=db.Column(db.Integer, db.ForeignKey('employers.id'))
    
#     employers=relationship(Employers, backref=backref("associations",cascade="all, delete-orphan"))
#     employee=relationship(Employers, backref=backref("associations", cascade="all,delete-orphan"))
    