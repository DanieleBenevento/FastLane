from flask import Flask, render_template, redirect, session, flash, url_for
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_utils import database_exists
from flask_bcrypt import Bcrypt

app = Flask(__name__)
db = SQLAlchemy(app)

app.config['SECRET_KEY'] = 'ldjashfjahef;jhasef;jhase;jfhae;'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///fastlane.db'

Bootstrap(app)
bcrypt = Bcrypt(app)

COUNTRIES = ['Afghanistan',
             'Albania',
             'Algeria',
             'American Samoa',
             'Andorra',
             'Angola',
             'Anguilla',
             'Antigua & Barbuda',
             'Argentina',
             'Armenia',
             'Aruba',
             'Australia',
             'Austria',
             'Azerbaijan',
             'Bahamas',
             'Bahrain',
             'Bangladesh',
             'Barbados',
             'Belarus',
             'Belgium',
             'Belize',
             'Benin',
             'Bermuda',
             'Bhutan',
             'Bolivia',
             'Bosnia & Herzegovina',
             'Botswana',
             'Brazil',
             'British Virgin Is.',
             'Brunei',
             'Bulgaria',
             'Burkina Faso',
             'Burma',
             'Burundi',
             'Cambodia',
             'Cameroon',
             'Canada',
             'Cape Verde',
             'Cayman Islands',
             'Central African Rep.',
             'Chad',
             'Chile',
             'China',
             'Colombia',
             'Comoros',
             'Congo Dem.Rep.',
             'Cook Islands',
             'Costa Rica',
             'Cote d''Ivoire',
             'Croatia',
             'Cuba',
             'Cyprus',
             'Czech Republic',
             'Denmark',
             'Djibouti',
             'Dominica',
             'Dominican Republic',
             'East Timor',
             'Ecuador',
             'Egypt',
             'El Salvador',
             'Equatorial Guinea',
             'Eritrea',
             'Estonia',
             'Ethiopia',
             'Faroe Islands',
             'Fiji',
             'Finland',
             'France',
             'French Guiana',
             'French Polynesia',
             'Gabon',
             'Gambia',
             'Gaza Strip',
             'Georgia',
             'Germany',
             'Ghana',
             'Gibraltar',
             'Greece',
             'Greenland',
             'Grenada',
             'Guadeloupe',
             'Guam',
             'Guatemala',
             'Guernsey',
             'Guinea',
             'Guinea-Bissau',
             'Guyana',
             'Haiti',
             'Honduras',
             'HongKong',
             'Hungary',
             'Iceland',
             'India',
             'Indonesia',
             'Iran',
             'Iraq',
             'Ireland',
             'Isle of Man',
             'Israel',
             'Italy',
             'Jamaica',
             'Japan',
             'Jersey',
             'Jordan',
             'Kazakhstan',
             'Kenya',
             'Kiribati',
             'Korea North',
             'Korea South',
             'Kuwait',
             'Kyrgyzstan',
             'Laos',
             'Latvia',
             'Lebanon',
             'Lesotho',
             'Liberia',
             'Libya',
             'Liechtenstein',
             'Lithuania',
             'Luxembourg',
             'Macau',
             'Macedonia',
             'Madagascar',
             'Malawi',
             'Malaysia',
             'Maldives',
             'Mali',
             'Malta',
             'Marshall Islands',
             'Martinique',
             'Mauritania',
             'Mauritius',
             'Mayotte',
             'Mexico',
             'Micronesia Fed. St.',
             'Moldova',
             'Monaco',
             'Mongolia',
             'Montserrat',
             'Morocco',
             'Mozambique',
             'Namibia',
             'Nauru',
             'Nepal',
             'Netherlands',
             'Netherlands Antilles',
             'New Caledonia',
             'New Zealand',
             'Nicaragua',
             'Niger',
             'Nigeria',
             'N. Mariana Islands',
             'Norway',
             'Oman',
             'Pakistan',
             'Palau',
             'Panama',
             'Papua New Guinea',
             'Paraguay',
             'Peru',
             'Philippines',
             'Poland',
             'Portugal',
             'Puerto Rico',
             'Qatar',
             'Reunion',
             'Romania',
             'Russia',
             'Rwanda',
             'Saint Helena',
             'Saint Kitts & Nevis',
             'Saint Lucia',
             'St Pierre & Miquelon',
             'Saint Vincent and the Grenadines',
             'Samoa',
             'San Marino',
             'Sao Tome & Principe',
             'Saudi Arabia',
             'Senegal',
             'Serbia',
             'Seychelles',
             'Sierra Leone',
             'Singapore',
             'Slovakia',
             'Slovenia',
             'Solomon Islands',
             'Somalia',
             'South Africa',
             'Spain',
             'Sri Lanka',
             'Sudan',
             'Suriname',
             'Swaziland',
             'Sweden',
             'Switzerland',
             'Syria',
             'Taiwan',
             'Tajikistan',
             'Tanzania',
             'Thailand',
             'Togo',
             'Tonga',
             'Trinidad & Tobago',
             'Tunisia',
             'Turkey',
             'Turkmenistan',
             'Turks & Caicos Is',
             'Tuvalu',
             'Uganda',
             'Ukraine',
             'United Arab Emirates',
             'United Kingdom',
             'United States',
             'Uruguay',
             'Uzbekistan',
             'Vanuatu',
             'Venezuela',
             'Vietnam',
             'Virgin Islands',
             'Wallis and Futuna',
             'West Bank',
             'Western Sahara',
             'Yemen',
             'Zambia',
             'Zimbabwe'

             ]


class PrivateCustomer(db.Model):
    __tablename__ = 'private_costumer'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(64), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    phone_num = db.Column(db.Integer, nullable=False, unique=True)
    country = db.Column(db.String(64), nullable=False)
    address = db.Column(db.String(64), nullable=False)
    type = db.Column(db.String(64), nullable=False)

    def __repr__(self):
        return '<Customer %s>' % self.username


class CompanyCustomer(db.Model):
    __tablename__ = 'company_customer'
    id_company = db.Column(db.Integer, primary_key=True)
    name_company = db.Column(db.String(64), nullable=True)

    country = db.Column(db.String(64), nullable=False)
    city = db.Column(db.String(64), nullable=False)
    address = db.Column(db.String(128), nullable=False)
    vat_code = db.Column(db.String(64), index=True, unique=True)
    web_site = db.Column(db.String(64), unique=True)
    phone_num = db.Column(db.Integer, unique=True)
    email = db.Column(db.String(64), unique=True)
    email_amm = db.Column(db.String(64), unique=True)
    password = db.Column(db.String(128), nullable=False)
    type = db.Column(db.String(64), nullable=False)

    def __repr__(self):
        return '<Customer %s>' % self.username_company


from form import RegistrationFormPrivate, loginForm, RegistrationFormCompany


@app.before_first_request
def create_all():
    if not database_exists('sqlite:///fastlane.db'):
        db.create_all()
        db.session.commit()


@app.route('/register_private', methods=['POST', 'GET'])
def register():
    form_private = RegistrationFormPrivate()
    if form_private.validate_on_submit():
        hashed_pwd = bcrypt.generate_password_hash(form_private.password.data)
        new_customer = PrivateCustomer(name=form_private.name.data, username=form_private.username.data,
                                       password=hashed_pwd, email=form_private.email.data,
                                       phone_num=form_private.phone.data,
                                       country=form_private.country.data, address=form_private.address.data,
                                       type='Private')
        db.session.add(new_customer)
        db.session.commit()
        return redirect('login')
    return render_template('reg_private.html', formReg=form_private, countries_list=COUNTRIES)


@app.route('/register_company', methods=['POST', 'GET'])
def register_company():
    form_company = RegistrationFormCompany()
    if form_company.validate_on_submit():
        hashed_pwd = bcrypt.generate_password_hash(form_company.password.data)
        new_customer = PrivateCustomer(name_company=form_company.name_company.data, password=hashed_pwd,
                                       email=form_company.email.data, phone_num=form_company.phone.data,
                                       country=form_company.country.data, city=form_company.city.data,
                                       address=form_company.address.data, vat_code=form_company.vat_code.data,
                                       web_site=form_company.web_site.data, email_amm=form_company.email_amm.data,
                                       type='Company')
        db.session.add(new_customer)
        db.session.commit()
        return redirect('login')
    return render_template('reg_company.html', formReg=form_company, countries_list=COUNTRIES)


@app.route('/login', methods=['POST', 'GET'])
def login():
    if session.get('username'):
        return redirect('profile')
    else:
        formRed = loginForm()
        if formRed.validate_on_submit():
            customer_selected = PrivateCustomer.query.filter_by(username=formRed.username.data).first()
            if bcrypt.check_password_hash(customer_selected.password, formRed.password.data):
                session['username'] = customer_selected.username
                return redirect('home')
        return render_template('login.html', formReg=formRed)


@app.route('/profile')
def profile():
    return render_template('profile.html')


@app.route('/')
@app.route('/home')
def home():
    return render_template('layout.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run()
