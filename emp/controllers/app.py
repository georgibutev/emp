import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons import config
from pylons.controllers.util import abort, redirect

from emp.lib.base import BaseController, render, validate
from emp.lib.base import Session
from emp.model import User
from emp.model.form import UserForm

log = logging.getLogger(__name__)

class AppController(BaseController):

    def index(self):
        pass

    def __before__(self):
        # Initialize session for the database
        self.query = Session.query(User)

    def main(self):
    	# Render main page template

        # Link for action
    	c.addUserAction = url(controller='app', action='addSingle')
        return render('/main.mako')

    # Validate the user submitted form
    @validate(schema=UserForm(), form='main')
    def addSingle(self):
    	# Add single user to the database

        # Link for action
        c.addUserAction = url(controller='app', action='addSingle')
        # Get user submitted values
        name = self.form_result.get('name')
        email = self.form_result.get('email')
        password = self.form_result.get('password')
        birthday = self.form_result.get('birthday')
        wage = self.form_result.get('wage')
        department = request.params['dep']
        # User object that corresponds to the mapper for the database
        user = User(name, email, password, birthday, int(wage), department)
        # Similar to INSERT SQL syntax
        Session.add(user)
        # Apply permanent changes
        Session.commit()
        # Notify the user upon success
    	return '%s was successfully stored in the database.' % (name.upper())

    def view(self):
    	# View all users

        # Link to action
        c.editUserAction = url(controller='app', action='edit')
        # Query the database for all records in the user table
        # Sort alphabetically
        # User helper for the template
        c.user = [user for user in self.query.order_by(User.name).all()]
        # Display the template
    	return render('/edit.mako')

    # Validate the user submitted form
    @validate(schema=UserForm(), form='main')
    def edit(self):
    	# Edit a user

        # Decide whether to update or remove record in the database
        if (request.params['edit'] == 'e'):
            # Update record
            # Query the database for user identified by id
            update = self.query.filter_by(id=int(request.params['id'])).first()
            update.name = self.form_result.get('name')
            update.email = self.form_result.get('email')
            update.password = self.form_result.get('password')
            update.birthday = self.form_result.get('birthday')
            update.wage = self.form_result.get('wage')
            update.department = request.params['dep']
            # Similar to UPDATE SQL syntax
            Session.add(update)
            # Apply permanent changes
            Session.commit()
        else:
            # Remove record
            # Query the database for user identified by id
            delete = self.query.filter_by(id=int(request.params['id'])).first()
            # Similar to DELETE SQL syntax
            Session.delete(delete)
            # Apply permanent changes
            Session.commit()
        # Regardless of operation failure or success redirect the user
    	redirect(url(controller='app', action='view'))

    def submit(self):
        pass