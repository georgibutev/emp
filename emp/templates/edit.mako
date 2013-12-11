<!DOCTYPE html>
<html>
<head>
<title>Employees Application</title>
${h.stylesheet_link('/style.css')}
${h.javascript_link('/script.js')}
</head>

<body>
<div id="nav">
${h.ul([h.link_to('Add User', url(controller='app', action='main')),
		h.link_to('Edit', url(controller='app', action='view'))])}
</div>

<h1>Employees Application</h1>

<div class="all">

<table>
	<th>Employee</th><th>Email</th><th>Password</th><th>Birthday</th><th>Wage in &euro;</th><th>Department</th><th>Action</th>
		%for user in c.user:
		${h.form(c.editUserAction)}
		<tr>
			<td>${h.text('name', user.name, 'name')}</td>
			<td>${h.text('email', user.email, 'email')}</td>
			<td>${h.password('password', user.password, 'password')}</td>
			<td>${h.text('birthday', user.birthday, 'birthday')}</td>
			<td>${h.text('wage', user.wage, 'wage')}</td>
			<td>${h.text('dep', user.department, 'dep')}</td>
			<td>${h.select('edit', 'e', [['e', 'Edit'], ['r', 'Remove']])}</td>
			<td>${h.submit('submit', 'Submit', 'submit')}</td>
			${h.hidden('id', user.id, 'id')}
		</tr>
		${h.end_form()}
		%endfor
</table>
</div>
</body>
</html>