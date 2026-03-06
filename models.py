
from datetime import datetime
from database import db, ma
from marshmallow_sqlalchemy import SQLAlchemySchema, SQLAlchemyAutoSchema 
from typing import List
from email_validator import validate_email, EmailNotValidError


class DatabaseOperations:
    @classmethod
    def get_data(cls, db_table, id):
        return db.session.get(db_table, id)

class Contact(db.Model, DatabaseOperations):
    __tablename__ = 'contacts'
    contact_id = db.Column(db.Integer, primary_key=True)
    contact_name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)

    def user_contacts(self, id):
        return DatabaseOperations.get_data(Contact, id)
        
class MedicationReminder(db.Model, DatabaseOperations):
    reminder_id = db.Column(db.Integer, primary_key=True)
    frequency = db.Column(db.String, nullable=False)
    reminder_time = db.Column(db.DateTime)
    medication_id = db.Column(db.Integer, db.ForeignKey('medications.medication_id'))

    @classmethod
    def user_medication_reminder(cls, medication_reminder: 'MedicationReminder'):
       pass

class History(db.Model, DatabaseOperations):
    history_id = db.Column(db.Integer, primary_key=True)
    medication_id = db.Column(db.Integer, db.ForeignKey('medications.medication_id')) 
    status = db.Column(db.String, nullable=False)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)
    medication_taken = db.Column(db.Integer, default=0)

class Medication(db.Model, DatabaseOperations):
    __tablename__ = 'medications'
    medication_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    dosage = db.Column(db.String, nullable=False)
    note = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    date_prescribed = db.Column(db.DateTime, default=datetime.utcnow)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)
    medication_reminders = db.relationship(
        lambda: MedicationReminder, 
        backref='medication_reminder', 
        lazy='dynamic',
        primaryjoin='Medication.medication_id == MedicationReminder.medication_id',
        foreign_keys="[MedicationReminder.medication_id]"
    )
    medication_history = db.relationship(lambda: History, backref='history', lazy='dynamic')

    def user_medication(self, id):
        return DatabaseOperations.get_data(Medication, id)


class User(db.Model, DatabaseOperations):
    __tablename__ = 'users'
    user_id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String(100))
    date_added = db.Column(db.DateTime, default=datetime.utcnow) 
    last_active = db.Column(db.DateTime, default=datetime.utcnow) 
    contacts = db.relationship(lambda: Contact, backref='contacts', lazy='dynamic')
    medications = db.relationship(lambda: Medication, backref='medications', lazy='dynamic')

    def get_user(self, id):
        return DatabaseOperations.get_data(User, id)

class UserSchema(ma.SQLAlchemySchema):
    class Meta:
        model = User
        include_relationships = True
        load_instance = True
    user_id = ma.auto_field()
    fullname = ma.auto_field()
    email = ma.auto_field()
    contacts = ma.auto_field()
    medications = ma.auto_field()

class ContactSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Contact
        include_fk = True

class MedicationSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Medication
        include_fk = True

user_schema = UserSchema()
contact_schema = ContactSchema(many=True)
medication_schema = MedicationSchema(many=True)
