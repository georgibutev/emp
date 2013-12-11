# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1386787045.455
_enable_loop = True
_template_filename = 'C:\\Users\\Georgi\\pylons\\projects\\emp\\emp\\templates/main.mako'
_template_uri = '/main.mako'
_source_encoding = 'utf-8'
from markupsafe import escape
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        url = context.get('url', UNDEFINED)
        h = context.get('h', UNDEFINED)
        c = context.get('c', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'<!DOCTYPE html>\r\n<html>\r\n<head>\r\n<title>Employees Application</title>\r\n')
        # SOURCE LINE 5
        __M_writer(escape(h.stylesheet_link('style.css')))
        __M_writer(u'\r\n')
        # SOURCE LINE 6
        __M_writer(escape(h.javascript_link('script.js')))
        __M_writer(u'\r\n</head>\r\n\r\n<body>\r\n<div id="nav">\r\n')
        # SOURCE LINE 11
        __M_writer(escape(h.ul([h.link_to('Add User', url(controller='app', action='main')),
		h.link_to('Edit', url(controller='app', action='view'))])))
        # SOURCE LINE 12
        __M_writer(u'\r\n</div>\r\n\r\n<h1>Employees Application</h1>\r\n\r\n')
        # SOURCE LINE 17
        __M_writer(escape(h.form(c.addUserAction)))
        __M_writer(u'\r\n\t<table>\r\n\t\t<tr><td><h2>Add Employee</h2></td></tr>\r\n\t\t<th>Description</th>\r\n\t\t<th>Detail</th>\r\n\t\t\t<tr>\r\n\t\t\t\t<td>')
        # SOURCE LINE 23
        __M_writer(escape(h.title('Employee Name: ', True, 'name')))
        __M_writer(u'</td>\r\n\t\t\t\t<td>')
        # SOURCE LINE 24
        __M_writer(escape(h.text('name', 'Georgi Butev', 'name', onclick="clearTextField(this.id)")))
        __M_writer(u'<br/></td>\r\n\t\t\t</tr>\r\n\t\t\t<tr>\r\n\t\t\t\t<td>')
        # SOURCE LINE 27
        __M_writer(escape(h.title('Employee Email: ', True, 'email')))
        __M_writer(u'</td>\r\n\t\t\t\t<td>')
        # SOURCE LINE 28
        __M_writer(escape(h.text('email', 'georgibutev@gmail.com', 'email', onclick="clearTextField(this.id)")))
        __M_writer(u'<br/></td>\r\n\t\t\t</tr>\r\n\t\t\t<tr>\r\n\t\t\t\t<td>')
        # SOURCE LINE 31
        __M_writer(escape(h.title('Employee Password: ', True, 'password')))
        __M_writer(u'</td>\r\n\t\t\t\t<td>')
        # SOURCE LINE 32
        __M_writer(escape(h.password('password', '1234', 'password', onclick="clearTextField(this.id)")))
        __M_writer(u'<br/></td>\r\n\t\t\t</tr>\r\n\t\t\t<tr>\r\n\t\t\t\t<td>')
        # SOURCE LINE 35
        __M_writer(escape(h.title('Birthday: ', True, 'birthday')))
        __M_writer(u'</td>\r\n\t\t\t\t<td>')
        # SOURCE LINE 36
        __M_writer(escape(h.text('birthday', '01/01/1980', 'birthday', onclick="clearTextField(this.id)")))
        __M_writer(u'<br/></td>\r\n\t\t\t</tr>\r\n\t\t\t<tr>\r\n\t\t\t\t<td>')
        # SOURCE LINE 39
        __M_writer(escape(h.title('Employee Wage: ', False, 'wage')))
        __M_writer(u'</td>\r\n\t\t\t\t<td>')
        # SOURCE LINE 40
        __M_writer(escape(h.text('wage', 3, 'wage', onclick="clearTextField(this.id)")))
        __M_writer(u'<br/></td>\r\n\t\t\t</tr>\r\n\t\t\t<tr>\r\n\t\t\t\t<td>')
        # SOURCE LINE 43
        __M_writer(escape(h.title('Department: ', False, 'dep')))
        __M_writer(u'</td>\r\n\t\t\t\t<td>')
        # SOURCE LINE 44
        __M_writer(escape(h.select('dep', 'GP', [ 'Surgeon', 'GP', 'Nurse' ], id='dep')))
        __M_writer(u'<br/></td>\r\n\t\t\t</tr>\r\n\t\t\t<tr>\r\n\t\t\t\t<td>Submit: </td>\r\n\t\t\t\t<td>')
        # SOURCE LINE 48
        __M_writer(escape(h.submit('submit', 'Add User', 'submit')))
        __M_writer(u'</td>\r\n\t\t\t</tr>\r\n\t\t</table>\r\n')
        # SOURCE LINE 51
        __M_writer(escape(h.end_form()))
        __M_writer(u'\r\n\r\n</body>\r\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


