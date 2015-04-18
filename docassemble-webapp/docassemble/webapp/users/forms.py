# Copyright 2014 SolidBuilds.com. All rights reserved
#
# Authors: Ling Thio <ling.thio@gmail.com>

from flask_user.forms import RegisterForm
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from docassemble.base.util import word

# Define the User registration form
# It augments the Flask-User RegisterForm with additional fields

def fix_nickname(form, field):
    field.data = form.first_name.data + ' ' + form.last_name.data
    return

class MyRegisterForm(RegisterForm):
    first_name = StringField('First name')
    last_name = StringField('Last name')
    social_id = StringField('Social ID')
    nickname = StringField('Nickname', [fix_nickname])

# Define the User profile form
class UserProfileForm(Form):
    first_name = StringField('First name', validators=[
        DataRequired('First name is required')])
    last_name = StringField('Last name', validators=[
        DataRequired('Last name is required')])
    country = StringField(word('Country Code'), validators=[
        DataRequired(word('Country Code is required'))])
    subdivisionfirst = StringField(word('First Subdivision'), validators=[
        DataRequired(word('First Subdivision is required'))])
    subdivisionsecond = StringField(word('Second Subdivision'), validators=[
        DataRequired(word('Second Subdivision is required'))])
    subdivisionthird = StringField(word('Third Subdivision'), validators=[
        DataRequired(word('Third Subdivision is required'))])
    organization = StringField(word('Organization'), validators=[
        DataRequired(word('Organization is required'))])
    submit = SubmitField('Save')

