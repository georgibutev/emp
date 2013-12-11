from sqlalchemy import Column
from sqlalchemy.types import Integer, String

from emp.model.meta import Base

class User(Base):
	# Mapper used for SQLalchemy operations

	# The name of the table
	__tablename__ = "user"

	# Table description
	# Auto incrementing numeric key to identify the emplyees.
	id = Column(Integer, primary_key=True)
	name = Column(String(33))
	email = Column(String(33))
	password = Column(String(25))
	birthday = Column(String(33))
	# Numeric value
	wage = Column(Integer)
	department = Column(String(33))

	def __init__(self, name, email, password, birthday, wage, department):
	# Initialize the variables so that they are available in the class
		self.name = name
		self.email = email
		self.password = password
		self.birthday = birthday
		self.wage = wage
		self.department = department


	def __repr__(self):
	# Returs a string and digit that describes the User object
		return "<User('%s', '%s', '%s', '%s', %d, '%s')>" % (self.name, self.email, self.password, self.birthday, self.wage, self.department)