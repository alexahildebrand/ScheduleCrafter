from crafter import app
from flask import render_template, redirect, url_for, flash
from crafter.models import Course, User, Professor, Section
from crafter.forms import RegisterForm, LoginForm
from crafter import db
from flask_login import login_user, logout_user, login_required


@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/courses')
@login_required
def schedule_page():
    courses = Course.query.all()
    return render_template('courses.html', courses=courses)

@app.route('/register', methods=['GET', 'POST'])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = User(username = form.username.data,
                              email_address=form.email_address.data,
                              password=form.password1.data)
        db.session.add(user_to_create)
        db.session.commit()
        login_user(user_to_create)
        flash(f'Account created successfully! You are now logged in as {user_to_create.username}', category='success')
        return redirect(url_for('schedule_page'))
    if form.errors != {}:  # if there are not errors from the validation
        for err_msg in form.errors.values():
            flash(f'There was an error while creating an account: {err_msg}', category='danger')

    return render_template('register.html', form=form)

@app.route('/professor')
@login_required
def professor_list():
    professors = Professor.query.all()
    return render_template('professor.html', professors=professors)

@app.route('/NealKing')
def NealKing():
    professors = Professor.query.filter_by(name="Neal King")
    return render_template('professor.html', professors=professors)

@app.route('/YongchengZhan')
def YongchengZhan():
    professors = Professor.query.filter_by(name = "Yongcheng Zhan")
    return render_template('professor.html', professors=professors)

@app.route('/JimBurleson')
def JimBurleson():
    professors = Professor.query.filter_by(name = "Jim Burleson")
    return render_template('professor.html', professors=professors)

@app.route('/KevinLertwachara')
def KevinLertwachara():
    professors = Professor.query.filter_by(name = "Kevin Lertwachara")
    return render_template('professor.html', professors=professors)

@app.route('/LeidaChan')
def LeidaChan():
    professors = Professor.query.filter_by(name = "Leida Chan")
    return render_template('professor.html', professors=professors)

@app.route('/ShaimaaEwais')
def ShaimaaEwais():
    professors = Professor.query.filter_by(name = "Shaimaa Ewais")
    return render_template('professor.html', professors=professors)


@app.route('/section')
def section_list():
    sections = Section.query.all()
    return render_template('sections.html', sections=sections)

@app.route('/BUS392')
def BUS392():
    sections = Section.query.filter_by(course='BUS392')
    return render_template('sections.html', sections=sections)

@app.route('/BUS393')
def BUS393():
    sections = Section.query.filter_by(course='BUS393')
    return render_template('sections.html', sections=sections)

@app.route('/BUS394')
def BUS394():
    sections = Section.query.filter_by(course='BUS394')
    return render_template('sections.html', sections=sections)

@app.route('/BUS497')
def BUS497():
    sections = Section.query.filter_by(course='BUS497')
    return render_template('sections.html', sections=sections)

@app.route('/BUS499')
def BUS499():
    sections = Section.query.filter_by(course='BUS499')
    return render_template('sections.html', sections=sections)

@app.route('/login', methods = ['GET', 'POST'])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        attempted_user = User.query.filter_by(username=form.username.data).first()
        if attempted_user and attempted_user.check_password_correction(
                attempted_password=form.password.data
        ):
            login_user(attempted_user)
            flash(f'Success! You are logged in as: {attempted_user.username}', category='success')
            return redirect(url_for('schedule_page'))
        else:
            flash('Username and password are not match! Please try again', category='danger')

    return render_template('login.html', form=form)

@app.route('/logout')
def logout_page():
    logout_user()
    flash('You have been logged out', category='info')
    return redirect(url_for('home_page'))

