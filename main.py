import os
from flask import Flask, render_template, url_for, flash, redirect, request, session
from forms import FillData, LoginForm, SectorSelection, Team, Employee, DeleteEmployee
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from combine_docx import combine_resumes_and_other_stuff,combine_all_docx

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mytestkey'

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
    os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app, db)


@app.route("/testing", methods=['GET', 'POST'])
def testing():
    emp = Database_IT.query.all()
    sector = session['sector']
    selection_status, employee_position, position_number, employement_status = team_characteristics(
        sector)
    selection_status = request.args.getlist(selection_status)
    employee_position = request.args.getlist(employee_position)
    position_number = request.args.getlist(position_number)
    employement_status = request.args.getlist(employement_status)

    selected_employee_resumes = []
    selected_employees = {}

    for i in range(len(selection_status)):
        if selection_status[i] == "yes":
            selected_employees[emp[i]] = position_number[i]

    number_of_selected_employees = len(selected_employees) + 1

    for i in range(1, number_of_selected_employees):
        for e, pos in selected_employees.items():
            if i == int(pos):
                selected_employee_resumes.append(e.resume)

    combine_resumes_and_other_stuff(selected_employee_resumes)

    return render_template('testing.html', emp=emp, selected_employees=selected_employees, selected_employee_resumes=selected_employee_resumes, sector=sector, position_number=position_number, employement_status=employement_status, selection_status=selection_status, employee_position=employee_position)

@app.route("/checkbox", methods=['GET', 'POST'])
def checkbox():
    doc_selected = request.form.getlist('mycheckbox')
    print(doc_selected)
    doc_position = request.form.getlist('fname')
    print(doc_position)
    doc_dic={}
    

    for i in range(0,len(doc_selected)):
        doc_dic[doc_selected[i]] = doc_position[i]
    print(doc_dic)
    doc_list=[]
    for n in range(0, len(doc_selected)+1):
        for v, pos in doc_dic.items():
            if n == int(pos):
                doc_list.append(v)

    print(doc_list)
    
    combine_all_docx(filename_master = 'static/TENDER_DOCS/BLANK.docx',files_list=doc_list)
    return render_template('checkbox.html')
    #,emp=emp,selected_doc=selected_doc, doc_list=doc_list,doc_selected=doc_selected,doc_position=doc_position


# class Team(db.Model):
#     __tablename__ = 'IT Services & Solutions'
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.Text)
#     resume = db.Column(db.Text)
#     signature = db.Column(db.Text)

#     def __init__(self, name, resume, signature):
#         self.name = name
#         self.resume = resume
#         self.signature = signature

#     def __repr__(self):
#         return f"{self.name}"


class Database_IT(db.Model):
    __tablename__ = 'IT Services & Solutions'
    name = db.Column(db.Text, primary_key=True)
    title = db.Column(db.Text)
    resume = db.Column(db.Text)
    signature = db.Column(db.Text)

    def __init__(self, name, title, resume, signature):
        self.name = name
        self.title = title
        self.resume = resume
        self.signature = signature

    def __repr__(self):
        return f"{self.name}"


class Database_Consulting(db.Model):
    __tablename__ = 'Consulting'
    name = db.Column(db.Text, primary_key=True)
    title = db.Column(db.Text)
    resume = db.Column(db.Text)
    signature = db.Column(db.Text)

    def __init__(self, name, title, resume, signature):
        self.name = name
        self.title = title
        self.resume = resume
        self.signature = signature

    def __repr__(self):
        return f"{self.name}"

    def __repr__(self):
        return f"{self.name}"


class Database_Cluster(db.Model):
    __tablename__ = 'Cluster'
    name = db.Column(db.Text, primary_key=True)
    title = db.Column(db.Text)
    resume = db.Column(db.Text)
    signature = db.Column(db.Text)

    def __init__(self, name, title, resume, signature):
        self.name = name
        self.title = title
        self.resume = resume
        self.signature = signature

    def __repr__(self):
        return f"{self.name}"

    def __repr__(self):
        return f"{self.name}"


class Database_Survey(db.Model):
    __tablename__ = 'Survey'
    name = db.Column(db.Text, primary_key=True)
    title = db.Column(db.Text)
    resume = db.Column(db.Text)
    signature = db.Column(db.Text)

    def __init__(self, name, title, resume, signature):
        self.name = name
        self.title = title
        self.resume = resume
        self.signature = signature

    def __repr__(self):
        return f"{self.name}"

    def __repr__(self):
        return f"{self.name}"


class Database_Agro(db.Model):
    __tablename__ = 'Agro'
    name = db.Column(db.Text, primary_key=True)
    title = db.Column(db.Text)
    resume = db.Column(db.Text)
    signature = db.Column(db.Text)

    def __init__(self, name, title, resume, signature):
        self.name = name
        self.title = title
        self.resume = resume
        self.signature = signature

    def __repr__(self):
        return f"{self.name}"

    def __repr__(self):
        return f"{self.name}"


class Database_Startup(db.Model):
    __tablename__ = 'Startup'
    name = db.Column(db.Text, primary_key=True)
    title = db.Column(db.Text)
    resume = db.Column(db.Text)
    signature = db.Column(db.Text)

    def __init__(self, name, title, resume, signature):
        self.name = name
        self.title = title
        self.resume = resume
        self.signature = signature

    def __repr__(self):
        return f"{self.name}"

    def __repr__(self):
        return f"{self.name}"


class Database_DigitalAdvertising(db.Model):
    __tablename__ = 'DigitalAdvertising'
    name = db.Column(db.Text, primary_key=True)
    title = db.Column(db.Text)
    resume = db.Column(db.Text)
    signature = db.Column(db.Text)

    def __init__(self, name, title, resume, signature):
        self.name = name
        self.title = title
        self.resume = resume
        self.signature = signature

    def __repr__(self):
        return f"{self.name}"

    def __repr__(self):
        return f"{self.name}"


class Database_Mobile(db.Model):
    __tablename__ = 'Mobile'
    name = db.Column(db.Text, primary_key=True)
    title = db.Column(db.Text)
    resume = db.Column(db.Text)
    signature = db.Column(db.Text)

    def __init__(self, name, title, resume, signature):
        self.name = name
        self.title = title
        self.resume = resume
        self.signature = signature

    def __repr__(self):
        return f"{self.name}"

    def __repr__(self):
        return f"{self.name}"


class Database_Web(db.Model):
    __tablename__ = 'Web'
    name = db.Column(db.Text, primary_key=True)
    title = db.Column(db.Text)
    resume = db.Column(db.Text)
    signature = db.Column(db.Text)

    def __init__(self, name, title, resume, signature):
        self.name = name
        self.title = title
        self.resume = resume
        self.signature = signature

    def __repr__(self):
        return f"{self.name}"

    def __repr__(self):
        return f"{self.name}"


class Database_Training(db.Model):
    __tablename__ = 'Training'
    name = db.Column(db.Text, primary_key=True)
    title = db.Column(db.Text)
    resume = db.Column(db.Text)
    signature = db.Column(db.Text)

    def __init__(self, name, title, resume, signature):
        self.name = name
        self.title = title
        self.resume = resume
        self.signature = signature

    def __repr__(self):
        return f"{self.name}"

    def __repr__(self):
        return f"{self.name}"


@app.route("/", methods=['GET', 'POST'])
def home():
    return render_template('home.html')


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/sector", methods=['GET', 'POST'])
def sector():
    form = SectorSelection()
    if form.validate_on_submit():
        session['sector_choice'] = form.sector.data

        if session['sector_choice'] == "IT Services & Solutions":
            return redirect(url_for('teamIT'))

        elif session['sector_choice'] == 'Consultancy':
            return redirect(url_for("teamConsulting"))

        elif session['sector_choice'] == 'Cluster Development':
            return redirect(url_for("teamCluster"))

        elif session['sector_choice'] == "Digital Advertising":
            return redirect(url_for("teamDigitalAdvertising"))

        elif session['sector_choice'] == 'Mobile & Web App':
            return redirect(url_for("teamMobile"))

        elif session['sector_choice'] == 'Web Portals':
            return redirect(url_for("teamWeb"))

        elif session['sector_choice'] == 'Surveys & Studies':
            return redirect(url_for("teamSurvey"))

        elif session['sector_choice'] == 'Agro & Food Processing':
            return redirect(url_for("teamAgro"))

        elif session['sector_choice'] == 'Startup & Incubation':
            return redirect(url_for("teamStartup"))

        elif session['sector_choice'] == 'Training & Skill Development':
            return redirect(url_for("teamTraining"))

    return render_template('sector.html', title='Sector Selection', form=form)


@app.route("/manage_employee", methods=['GET', 'POST'])
def manage_employee():
    return render_template('manage_employee.html', title='Manage Employee')


@app.route("/employee_added")
def employee_added():
    return render_template("employee_added.html")


@app.route("/add_employee", methods=['GET', 'POST'])
def addEmployee():
    form = Employee()
    signature = ""
    resume = ""
    if form.validate_on_submit():
        if form.emp_signature.data:
            signature = save_signature(
                form.emp_signature.data, form.emp_name.data)
        if form.emp_resume.data:
            resume = save_resume(form.emp_resume.data, form.emp_name.data)

        sector = form.emp_sector.data

        name = form.emp_name.data
        title = form.emp_title.data

        if sector == "IT Services & Solutions":
            emp = Database_IT(name=name, title=title,
                              resume=resume, signature=signature)

        elif sector == 'Consultancy':
            emp = Database_Consulting(name, title, resume, signature)

        elif sector == 'Cluster Development':
            emp = Database_Cluster(name, title, resume, signature)

        elif sector == "Digital Advertising":
            emp = Database_DigitalAdvertising(
                name, title, resume, signature)

        elif sector == 'Mobile & Web App':
            emp = Database_Mobile(name, title, resume, signature)

        elif sector == 'Web Portals':
            emp = Database_Web(name, title, resume, signature)

        elif sector == 'Surveys & Studies':
            emp = Database_Survey(name, title, resume, signature)

        elif sector == 'Agro & Food Processing':
            emp = Database_Agro(name, title, resume, signature)

        elif sector == 'Startup & Incubation':
            emp = Database_Startup(name, title, resume, signature)

        elif sector == 'Training & Skill Development':
            emp = Database_Training(name, title, resume, signature)

        db.session.add(emp)
        db.session.commit()

        return redirect(url_for("employee_added"))

    return render_template("add_employee.html", title='Add Employee', form=form)


@app.route('/delete_sector_selection', methods=['GET', 'POST'])
def delete_sector_selection():
    form = SectorSelection()
    if form.validate_on_submit():
        session['delete_sector'] = form.sector.data
        return redirect(url_for("delete_member"))

    return render_template('sector.html', title='Sector Selection', form=form)


@app.route("/delete_member", methods=['GET', 'POST'])
def delete_member():
    sector = session['delete_sector']
    if sector == "IT Services & Solutions":
        emp = Database_IT.query.all()
    elif sector == 'Consultancy':
        emp = Database_Consulting.query.all()
    elif sector == 'Cluster Development':
        emp = Database_Cluster.query.all()
    elif sector == "Digital Advertising":
        emp = Database_DigitalAdvertising.query.all()
    elif sector == 'Mobile & Web App':
        emp = Database_Mobile.query.all()
    elif sector == 'Web Portals':
        emp = Database_Web.query.all()
    elif sector == 'Surveys & Studies':
        emp = Database_IT.query.all()
    elif sector == 'Agro & Food Processing':
        emp = Database_Agro.query.all()
    elif sector == 'Startup & Incubation':
        emp = Database_Startup.query.all()
    elif sector == 'Training & Skill Development':
        emp = Database_Training.query.all()
    return render_template('delete_employee.html', emp=emp)


@app.route('/deletion_completed', methods=['GET', 'POST'])
def deletion_completed():
    sector = session['delete_sector']
    deleted_employee = []

    if sector == "IT Services & Solutions":
        emp = Database_IT.query.all()
        deletion_status = request.args.getlist('deletion_status')
        for i in range(len(deletion_status)):
            if deletion_status[i] == 'yes':
                ename = emp[i].name
                deleted_employee.append(ename)
                del_emp = Database_IT.query.get(ename)
                del_resume = del_emp.resume
                del_signature = del_emp.signature
                db.session.delete(del_emp)
                db.session.commit()
                try:
                    os.remove(del_resume)
                    os.remove(del_signature)
                except:
                    print("File Not Found")

    elif sector == 'Consultancy':
        emp = Database_Consulting.query.all()
        deletion_status = request.args.getlist('deletion_status')
        for i in range(len(deletion_status)):
            if deletion_status[i] == 'yes':
                ename = emp[i].name
                deleted_employee.append(ename)
                del_emp = Database_Consulting.query.get(ename)
                del_resume = del_emp.resume
                del_signature = del_emp.signature
                db.session.delete(del_emp)
                db.session.commit()
                try:
                    os.remove(del_resume)
                    os.remove(del_signature)
                except:
                    print("File Not Found")

    elif sector == 'Cluster Development':
        emp = Database_Cluster.query.all()
        deletion_status = request.args.getlist('deletion_status')
        for i in range(len(deletion_status)):
            if deletion_status[i] == 'yes':
                ename = emp[i].name
                deleted_employee.append(ename)
                del_emp = Database_Cluster.query.get(ename)
                del_resume = del_emp.resume
                del_signature = del_emp.signature
                db.session.delete(del_emp)
                db.session.commit()
                try:
                    os.remove(del_resume)
                    os.remove(del_signature)
                except:
                    print("File Not Found")

    elif sector == "Digital Advertising":
        emp = Database_DigitalAdvertising.query.all()
        deletion_status = request.args.getlist('deletion_status')
        for i in range(len(deletion_status)):
            if deletion_status[i] == 'yes':
                ename = emp[i].name
                deleted_employee.append(ename)
                del_emp = Database_DigitalAdvertising.query.get(ename)
                del_resume = del_emp.resume
                del_signature = del_emp.signature
                db.session.delete(del_emp)
                db.session.commit()
                try:
                    os.remove(del_resume)
                    os.remove(del_signature)
                except:
                    print("File Not Found")

    elif sector == 'Mobile & Web App':
        emp = Database_Mobile.query.all()
        deletion_status = request.args.getlist('deletion_status')
        for i in range(len(deletion_status)):
            if deletion_status[i] == 'yes':
                ename = emp[i].name
                deleted_employee.append(ename)
                del_emp = Database_Mobile.query.get(ename)
                del_resume = del_emp.resume
                del_signature = del_emp.signature
                db.session.delete(del_emp)
                db.session.commit()
                try:
                    os.remove(del_resume)
                    os.remove(del_signature)
                except:
                    print("File Not Found")

    elif sector == 'Web Portals':
        emp = Database_Web.query.all()
        deletion_status = request.args.getlist('deletion_status')
        for i in range(len(deletion_status)):
            if deletion_status[i] == 'yes':
                ename = emp[i].name
                deleted_employee.append(ename)
                del_emp = Database_Web.query.get(ename)
                del_resume = del_emp.resume
                del_signature = del_emp.signature
                db.session.delete(del_emp)
                db.session.commit()
                try:
                    os.remove(del_resume)
                    os.remove(del_signature)
                except:
                    print("File Not Found")

    elif sector == 'Surveys & Studies':
        emp = Database_IT.query.all()
        deletion_status = request.args.getlist('deletion_status')
        for i in range(len(deletion_status)):
            if deletion_status[i] == 'yes':
                ename = emp[i].name
                deleted_employee.append(ename)
                del_emp = Database_Survey.query.get(ename)
                del_resume = del_emp.resume
                del_signature = del_emp.signature
                db.session.delete(del_emp)
                db.session.commit()
                try:
                    os.remove(del_resume)
                    os.remove(del_signature)
                except:
                    print("File Not Found")

    elif sector == 'Agro & Food Processing':
        emp = Database_Agro.query.all()
        deletion_status = request.args.getlist('deletion_status')
        for i in range(len(deletion_status)):
            if deletion_status[i] == 'yes':
                ename = emp[i].name
                deleted_employee.append(ename)
                del_emp = Database_Agro.query.get(ename)
                del_resume = del_emp.resume
                del_signature = del_emp.signature
                db.session.delete(del_emp)
                db.session.commit()
                try:
                    os.remove(del_resume)
                    os.remove(del_signature)
                except:
                    print("File Not Found")

    elif sector == 'Startup & Incubation':
        emp = Database_Startup.query.all()
        deletion_status = request.args.getlist('deletion_status')
        for i in range(len(deletion_status)):
            if deletion_status[i] == 'yes':
                ename = emp[i].name
                deleted_employee.append(ename)
                del_emp = Database_Startup.query.get(ename)
                del_resume = del_emp.resume
                del_signature = del_emp.signature
                db.session.delete(del_emp)
                db.session.commit()
                try:
                    os.remove(del_resume)
                    os.remove(del_signature)
                except:
                    print("File Not Found")

    elif sector == 'Training & Skill Development':
        emp = Database_Training.query.all()
        deletion_status = request.args.getlist('deletion_status')
        for i in range(len(deletion_status)):
            if deletion_status[i] == 'yes':
                ename = emp[i].name
                deleted_employee.append(ename)
                del_emp = Database_Training.query.get(ename)
                del_resume = del_emp.resume
                del_signature = del_emp.signature
                db.session.delete(del_emp)
                db.session.commit()
                try:
                    os.remove(del_resume)
                    os.remove(del_signature)
                except:
                    print("File Not Found")

    return render_template('employee_deleted.html', deleted_employee=deleted_employee)


@app.route("/Team_IT", methods=['GET', 'POST'])
def teamIT():
    emp = Database_IT.query.all()
    session['sector'] = 'IT'
    return render_template('team_IT.html', emp=emp)


@app.route("/Team_Cluster", methods=['GET', 'POST'])
def teamCluster():
    emp = Database_Cluster.query.all()
    session['sector'] = 'Cluster'
    return render_template('team_cluster.html', emp=emp)


@ app.route("/Team_Web", methods=['GET', 'POST'])
def teamWeb():
    emp = Database_Web.query.all()
    session['sector'] = 'Web'
    return render_template('team_web.html', emp=emp)


@ app.route("/Team_Survey", methods=['GET', 'POST'])
def teamSurvey():
    emp = Database_Survey.query.all()
    session['sector'] = 'Survey'
    return render_template('team_survey.html', emp=emp)


@ app.route("/Team_Agro", methods=['GET', 'POST'])
def teamAgro():
    emp = Database_Agro.query.all()
    session['sector'] = 'Agro'
    return render_template('team_agro.html', emp=emp)


@ app.route("/Team_Startup", methods=['GET', 'POST'])
def teamStartup():
    emp = Database_Startup.query.all()
    session['sector'] = 'Startup'
    return render_template('team_startup.html', emp=emp)


@ app.route("/Team_Training", methods=['GET', 'POST'])
def teamTraining():
    emp = Database_Training.query.all()
    session['sector'] = 'Training'
    return render_template('team_training.html', emp=emp)


@ app.route("/Team_Consulting", methods=['GET', 'POST'])
def teamConsulting():
    emp = Database_Consulting.query.all()
    session['sector'] = 'Consulting'
    return render_template('team_consulting.html', emp=emp)


@ app.route("/Team_Digital_Advertising", methods=['GET', 'POST'])
def teamDigitalAdvertising():
    emp = Database_DigitalAdvertising.query.all()
    session['sector'] = 'DigitalAdvertising'
    return render_template('team_digital_advertising.html', emp=emp)


@ app.route("/register", methods=['GET', 'POST'])
def register():
    text= request.form.getlist('replace')
    print(text)
    var_list=['title','dated','rfp','location','email_id']


    var_dic={}
    

    for i in range(0,len(text)):
        var_dic[var_list[i]] = text[i]
    print(var_dic)
    



    return render_template('register.html')


@ app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('sector'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)


def save_signature(image, name):
    _, f_extension = os.path.splitext(image.filename)
    file_name = name + '_signature' + f_extension
    image_path = os.path.join(
        basedir, 'static', 'data', 'employee_data', 'signature', file_name)
    image.save(image_path)
    return image_path


def save_resume(resume_file, name):
    _, f_extension = os.path.splitext(resume_file.filename)
    file_name = name + '_resume' + f_extension
    resume_path = os.path.join(
        basedir, 'static', 'data', 'employee_data', 'resume', file_name)
    resume_file.save(resume_path)
    return resume_path


def team_characteristics(sector):
    selection_status = sector + "-selection_status"
    employee_position = sector + "-employee_position"
    position_number = sector + "-position_number"
    employement_status = sector + "-employement_status"
    return selection_status, employee_position, position_number, employement_status


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
