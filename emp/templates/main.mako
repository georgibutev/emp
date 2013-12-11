<!DOCTYPE html>
<html>
<head>
<title>Employees Application</title>
${h.stylesheet_link('style.css')}
${h.javascript_link('script.js')}
</head>

<body>
<div id="nav">
${h.ul([h.link_to('Add User', url(controller='app', action='main')),
		h.link_to('Edit', url(controller='app', action='view'))])}
</div>

<h1>Employees Application</h1>

${h.form(c.addUserAction)}
	<table>
		<tr><td><h2>Add Employee</h2></td></tr>
		<th>Description</th>
		<th>Detail</th>
			<tr>
				<td>${h.title('Employee Name: ', True, 'name')}</td>
				<td>${h.text('name', 'Georgi Butev', 'name', onclick="clearTextField(this.id)")}<br/></td>
			</tr>
			<tr>
				<td>${h.title('Employee Email: ', True, 'email')}</td>
				<td>${h.text('email', 'georgibutev@gmail.com', 'email', onclick="clearTextField(this.id)")}<br/></td>
			</tr>
			<tr>
				<td>${h.title('Employee Password: ', True, 'password')}</td>
				<td>${h.password('password', '1234', 'password', onclick="clearTextField(this.id)")}<br/></td>
			</tr>
			<tr>
				<td>${h.title('Birthday: ', True, 'birthday')}</td>
				<td>${h.text('birthday', '01/01/1980', 'birthday', onclick="clearTextField(this.id)")}<br/></td>
			</tr>
			<tr>
				<td>${h.title('Employee Wage: ', False, 'wage')}</td>
				<td>${h.text('wage', 3, 'wage', onclick="clearTextField(this.id)")}<br/></td>
			</tr>
			<tr>
				<td>${h.title('Department: ', False, 'dep')}</td>
				<td>${h.select('dep', 'GP', [ 'Surgeon', 'GP', 'Nurse' ], id='dep')}<br/></td>
			</tr>
			<tr>
				<td>Submit: </td>
				<td>${h.submit('submit', 'Add User', 'submit')}</td>
			</tr>
		</table>
${h.end_form()}

</body>
</html>