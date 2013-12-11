# Used to validate the user submitted form
# The schema is required in order to determine the requirements

import formencode

class UserForm(formencode.Schema):

	# Other fields that don't require validation, such as select option
	allow_extra_fields = True
	filter_extra_fields = True
	# The username field should not be empty
	name = formencode.validators.NotEmpty()
	# The email field should not be empty and should contain @ sign
	email = formencode.validators.Email()
	# The password length should be at least 6 chars long
	password = formencode.validators.MinLength(6)
	# The birthday field should not be empty
	birthday = formencode.validators.NotEmpty()
	# The wage field should numeric
	wage = formencode.validators.Int()