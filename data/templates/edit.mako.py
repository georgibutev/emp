# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1386787348.626
_enable_loop = True
_template_filename = 'C:\\Users\\Georgi\\pylons\\projects\\emp\\emp\\templates/edit.mako'
_template_uri = '/edit.mako'
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
        __M_writer(escape(h.stylesheet_link('/style.css')))
        __M_writer(u'\r\n')
        # SOURCE LINE 6
        __M_writer(escape(h.javascript_link('/script.js')))
        __M_writer(u'\r\n</head>\r\n\r\n<body>\r\n<div id="nav">\r\n')
        # SOURCE LINE 11
        __M_writer(escape(h.ul([h.link_to('Add User', url(controller='app', action='main')),
		h.link_to('Edit', url(controller='app', action='view'))])))
        # SOURCE LINE 12
        __M_writer(u'\r\n</div>\r\n\r\n<h1>Employees Application</h1>\r\n\r\n<div class="all">\r\n\r\n<table>\r\n\t<th>Employee</th><th>Email</th><th>Password</th><th>Birthday</th><th>Wage in &euro;</th><th>Department</th><th>Action</th>\r\n')
        # SOURCE LINE 21
        for user in c.user:
            # SOURCE LINE 22
            __M_writer(u'\t\t')
            __M_writer(escape(h.form(c.editUserAction)))
            __M_writer(u'\r\n\t\t<tr>\r\n\t\t\t<td>')
            # SOURCE LINE 24
            __M_writer(escape(h.text('name', user.name, 'name')))
            __M_writer(u'</td>\r\n\t\t\t<td>')
            # SOURCE LINE 25
            __M_writer(escape(h.text('email', user.email, 'email')))
            __M_writer(u'</td>\r\n\t\t\t<td>')
            # SOURCE LINE 26
            __M_writer(escape(h.password('password', user.password, 'password')))
            __M_writer(u'</td>\r\n\t\t\t<td>')
            # SOURCE LINE 27
            __M_writer(escape(h.text('birthday', user.birthday, 'birthday')))
            __M_writer(u'</td>\r\n\t\t\t<td>')
            # SOURCE LINE 28
            __M_writer(escape(h.text('wage', user.wage, 'wage')))
            __M_writer(u'</td>\r\n\t\t\t<td>')
            # SOURCE LINE 29
            __M_writer(escape(h.text('dep', user.department, 'dep')))
            __M_writer(u'</td>\r\n\t\t\t<td>')
            # SOURCE LINE 30
            __M_writer(escape(h.select('edit', 'e', [['e', 'Edit'], ['r', 'Remove']])))
            __M_writer(u'</td>\r\n\t\t\t<td>')
            # SOURCE LINE 31
            __M_writer(escape(h.submit('submit', 'Submit', 'submit')))
            __M_writer(u'</td>\r\n\t\t\t')
            # SOURCE LINE 32
            __M_writer(escape(h.hidden('id', user.id, 'id')))
            __M_writer(u'\r\n\t\t</tr>\r\n\t\t')
            # SOURCE LINE 34
            __M_writer(escape(h.end_form()))
            __M_writer(u'\r\n')
        # SOURCE LINE 36
        __M_writer(u'</table>\r\n</div>\r\n</body>\r\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


