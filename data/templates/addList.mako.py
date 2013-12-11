# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1386667096.264
_enable_loop = True
_template_filename = 'C:\\Users\\Georgi\\pylons\\projects\\emp\\emp\\templates/addList.mako'
_template_uri = '/addList.mako'
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
		h.link_to('Add List', url(controller='app', action='addList')),
		h.link_to('Edit', url(controller='app', action='view'))])))
        # SOURCE LINE 13
        __M_writer(u'\r\n</div>\r\n\r\n<h1>Employees Application</h1>\r\n\r\n')
        # SOURCE LINE 18
        __M_writer(escape(h.form(c.addListAction)))
        __M_writer(u'\r\n\t\t<h2>Add List of Employees</h2>\r\n\t\t<p>Use the specified format, seperate with commas.</p>\r\n\t\t')
        # SOURCE LINE 21
        __M_writer(escape(h.textarea('list', 'Georgi Butev, georgibutev@gmail.com, pass, 01/01/1980, 3, General Practitioner', 'list', cols=100, rows=5)))
        __M_writer(u'\r\n\t\t')
        # SOURCE LINE 22
        __M_writer(escape(h.submit('submit', 'Submit List', 'submit')))
        __M_writer(u'\r\n')
        # SOURCE LINE 23
        __M_writer(escape(h.end_form()))
        __M_writer(u'\r\n</body>\r\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


