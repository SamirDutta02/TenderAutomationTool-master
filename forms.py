"""Imports :- 
            1. We are importing FlaskForm class from flask_wtf to create custom forms
            2. We are importing FileFiled to upload file and FileAllowed to put a validation condition on types of file allowed to be uploaded from flask_wtf.file
            3. We are importing 
    """


from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField, DateField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class FillData(FlaskForm):
    Topic = StringField('Topic',
                        validators=[DataRequired()])

    Contact_Person_Email = StringField('Email',
                                       validators=[DataRequired(), Email()])
    Dated = DateField('Dated', format='%d-%m-%y')
    Location = StringField('Location')
    Contact_Person_Name = StringField('Contact Person Name')
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])

    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    #submit = SubmitField('Next')


class SectorSelection(FlaskForm):

    sector = SelectField("Please select the sector: ",
                         choices=[('Consultancy', 'Consultancy'), ('IT Services & Solutions', 'IT Services & Solutions'),
                                  ('Mobile & Web App', 'Mobile & Web App'), ('Web Portals',
                                                                             'Web Portals'), ('Surveys & Studies', 'Surveys & Studies'),
                                  ('Agro & Food Processing', 'Agro & Food Processing'), (
                             'Startup & Incubation', 'Startup & Incubation'), ('Cluster Development', 'Cluster Development'),
                             ('Digital Advertising', 'Digital Advertising'), ('Training & Skill Development', 'Training & Skill Development')])

    submit = SubmitField('Confirm Sector Selection')


class Team(FlaskForm):
    person_selected = BooleanField('Selection')
    position = StringField("Position in Team")
    emp_status = SelectField("Full Time / Part Time Expert: ",
                             choices=[('Full Time Employee', 'Full Time Employee'), ('Part Time Expert', 'Part Time Expert')])
    submit = SubmitField('Please Confirm the Team')


class Employee(FlaskForm):
    emp_name = StringField("Employee Name : ")
    emp_title = StringField("Employee Title : ")
    emp_sector = SelectField("Sector of the Employee : ",
                             choices=[('Consultancy', 'Consultancy'), ('IT Services & Solutions', 'IT Services & Solutions'),
                                      ('Mobile & Web App', 'Mobile & Web App'), ('Web Portals',
                                                                                 'Web Portals'), ('Surveys & Studies', 'Surveys & Studies'),
                                      ('Agro & Food Processing', 'Agro & Food Processing'), (
                                 'Startup & Incubation', 'Startup & Incubation'), ('Cluster Development', 'Cluster Development'),
                                 ('Digital Advertising', 'Digital Advertising'), ('Training & Skill Development', 'Training & Skill Development')])

    emp_resume = FileField("Upload Employee Resume (in .doc format) : ", validators=[
                           FileAllowed(['docx'])])
    emp_signature = FileField("Upload image of Employee Sign :", validators=[
                              FileAllowed(['png'])])
    submit = SubmitField('Please Confirm the Employee details : ')


class DeleteEmployee(FlaskForm):
    delete_status = BooleanField('Delete')
    submit = SubmitField('Please Confirm')
