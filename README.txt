Employees Application

Document and source code written by Georgi Butev.

1. Installation

Edit development.ini database connection. For example MySQL
(Username - root, Password - aten, existing database - emp):
	sqlalchemy.url = mysql://root:aten@localhost:3306/emp
	sqlalchemy.pool_recycle = 3600

Setup the database model:
	paster setup-app development.ini

Start the Pylons server:
	paster serve development.ini --reload

Navigate your web browser to:
	http://127.0.0.0:5000/

2. App Description

This application requires Python 2.7.6, Pylons 1, and SQLAlchemy 8.
Also python-mysql binding are needed.

The user can add employees to the MySQL database using a form.
The table contains - name, email, password, birthday, wage, and department.
Each form submit is validated against several requirements, such as no empty fields are allowed,
the email should contain @ sign and domain, and password should be 6 chars long.
Inappropriate symbols submitted through the form are avoided in the controller.
The user can also edit (update existing data) and remove (existing record) of an employee.

The JS contains a single function which clears the text field containing an example.

The CSS styling aims at optimal ease of use. Bigger fonts are used when adding an employee but
smaller fonts are used when displaying the records from the database.

This project is using SQLAlchemy which is configured for MySQL server. Setting other
servers (SQLite, PostgreSQL) is also possible by editing the development.ini configuration.
You should use an existing database during installation. However the tables are created
based on the model setup.

3. Files

/build/doc
	Folder containing class documentation generated using pudge.

/emp/config/environment.py
	SQLAlchemy engine ini and config.

/emp/config/routing.py
	Route from base (i.e. http://127.0.0.0:5000/) to application and action (i.e. http://127.0.0.1:5000/app/main).

/emp/controller/app.py
	Application controller which contains the following actions:
		__before__() Start the session object for SQLAlchemy queries.
		main() Display HTML mako template.
		@validate Validate the submitted user form.
		addSingle() Get form submitted values, instantiate mapper, and commit to database with INSERT.
		view() Query the database for all records, order alphabetically, assign to helper array.
		edit() UPDATE or DELETE from the database based on the selected action and received id.

/emp/lib/base.py
	Import and manage the session object.

/emp/lib/base.py
	Import HTML helpers which are used for easier form construct.

/emp/model/__init__.py
	Import Session configure and engine bind and import User model, all at startup.

/emp/model/form.py
	Formencode model used for validation of user submitted forms.

/emp/model/user.py
	Model database mapper for SQLAlchemy. The class contains the table's name as well as table description (e.g. name is string 33 chars long).

/emp/public/script.js
	Script containing single function used to clear the form text fields from the predefined value.

/emp/public/style.css
	Contains general page styling, navigation bar style, and HTML form style.

/emp/templates/edit.mako
	Displays a list of all users in the database. Allows for text data edit followed by update in the database table. Optionally records can also be deleted from the table.
	It is using a form loop to display all data from the query array. Form action leads to edit() which decideds whether to UPDATE or DELETE record.

/emp/templates/main.mako
	Displays a form which allows the user to add a record to the database (i.e. employee). HTML helpers are used to construct the form which is validated before processing. The form action leads to addSingle() which INSERTs the data in to the database table.

/emp/websetup.py
	Important because it loads the environment configuration (i.e. environment.ini) and created/drops the user table in a selected MySQL database.

+------------+-------------+------+-----+---------+----------------+
| Field      | Type        | Null | Key | Default | Extra          |
+------------+-------------+------+-----+---------+----------------+
| id         | int(11)     | NO   | PRI | NULL    | auto_increment |
| name       | varchar(33) | YES  |     | NULL    |                |
| email      | varchar(33) | YES  |     | NULL    |                |
| password   | varchar(25) | YES  |     | NULL    |                |
| birthday   | varchar(33) | YES  |     | NULL    |                |
| wage       | int(11)     | YES  |     | NULL    |                |
| department | varchar(33) | YES  |     | NULL    |                |
+------------+-------------+------+-----+---------+----------------+

/development.ini
	You should use this config file to start the server as there is no production.ini
	You can change the default HTTP server address from http://127.0.0.1:5000/
	You should change the database settings. If you are using MySQL then only alter the username, password, and existing database name which will be used by the application to store tables.
	You can change the logging configuration. The selected level is DEBUG which displays queries and results. You may change this to WARN to avoid all display.