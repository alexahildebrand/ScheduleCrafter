from crafter import db, login_manager
from crafter import bcrypt
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    __tablename__ = 'Students'
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=30),nullable = False, unique=True)
    email_address = db.Column(db.String(length=50), nullable=False, unique=True)
    password_hash = db.Column(db.String(length=60), nullable=False)
    budget = db.Column(db.Integer(), nullable=False, default=18)
    courses = db.relationship('Course', backref = 'owned_student', lazy = True)

    @property
    def prettier_units(self):
       if len(str(self.budget)) >=4:
           return f'{str(self.budget)[:-3]},{str(self.budget)[-3:]}'
       else:
           return f"{self.budget}"

    @property
    def password(self):
        return self.password

    @password.setter
    def password(self, plain_text_password):
        self.password_hash = bcrypt.generate_password_hash(plain_text_password).decode('utf-8')

    def check_password_correction(self, attempted_password):
        return bcrypt.check_password_hash(self.password_hash, attempted_password)

    def can_enroll(self, class_obj):
        return self.budget >= class_obj.units

    def can_drop(self, class_obj):
        return class_obj in self.courses

class Course(db.Model):
    __tablename__='Courses'
    name = db.Column('name', db.String(length=30), primary_key=True)
    description = db.Column('description', db.String(length=1024), nullable=False)
    units = db.Column('units', db.Integer(), nullable=False)
    student = db.Column(db.Integer(), db.ForeignKey('Students.id'))
    def __repr__(self):
        return f'Course {self.name}'

    def enroll(self, user):
        self.student = user.id
        user.budget -= self.units
        db.session.commit()

    def drop(self, user):
        self.student = None
        user.budget += self.units
        db.session.commit()

class Professor(db.Model):
    __tablename__='Professors'
    name=db.Column('Name', db.String(length=50), primary_key = True, nullable=False, unique=True)
    rating = db.Column('Rating', db.String(), nullable =False)
    review = db.Column('Review', db.String(length=2000))
    class_list = db.Column('ClassList', db.String(length=1000))


class Section(db.Model):
    __tablename__ = "Sections"
    id = db.Column('SectionID', db.String(length=10), primary_key =True)
    course = db.Column('CourseName',db.String(), db.ForeignKey('Course.id'))
    professor = db.Column('ProfessorName',db.String(), db.ForeignKey('Professor.name'))
    time = db.Column('Time',db.String(length=20), nullable=True)



