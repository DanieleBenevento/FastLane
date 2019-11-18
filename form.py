from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators, SubmitField, ValidationError, IntegerField, SelectField
from wtforms.fields.html5 import EmailField, URLField
from wtforms.validators import DataRequired, Length, Email, InputRequired
from app import PrivateCustomer




class RegistrationFormPrivate(FlaskForm):

    name = StringField('Name', validators=[DataRequired()])
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=4, max=20)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), Length(min=4, max=20)])
    email = EmailField('Email address', validators=[DataRequired(), Email()])
    phone = IntegerField('Phone number', validators=[DataRequired()])
    country = SelectField('Country', choices = COUNTRIES, validators=[InputRequired])
    address = StringField('Address', validators=[DataRequired()])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = PrivateCustomer.query.filter_by(username=self.username.data).first()
        if user:
            raise ValidationError('"%s" already exist, please select new username' % username.data)


class RegistrationFormCompany(FlaskForm):
    name_company = StringField('Name', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=4, max=20)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), Length(min=4, max=20)])
    email = EmailField('Email address', validators=[DataRequired(), Email()])
    email_admin = EmailField('Administrator email address', validators=[DataRequired(), Email()])
    phone = IntegerField('Phone number', validators=[DataRequired()])
    country = SelectField('Country',choices=COUNTRIES, validators=[InputRequired])
    city = StringField('City', validators=[DataRequired()])
    vat_code = StringField('VAT code', validators=[DataRequired()])
    web_site = URLField('Web site', validators=[DataRequired()])
    address = StringField('Address', validators=[DataRequired()])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = PrivateCustomer.query.filter_by(username=self.username.data).first()
        if user:
            raise ValidationError('"%s" already exist, please select new username' % username.data)


class loginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=4,max=20)])
    submit = SubmitField('Login')
