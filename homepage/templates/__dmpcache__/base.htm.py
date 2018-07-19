# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1524253334.9293509
_enable_loop = True
_template_filename = '/Users/brand/Desktop/finalexam/homepage/templates/base.htm'
_template_uri = 'base.htm'
_source_encoding = 'utf-8'
import django_mako_plus
_exports = ['content']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def content():
            return render_content(context._locals(__M_locals))
        self = context.get('self', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('<!DOCTYPE html>\n<html>\n    <meta charset="UTF-8">\n    <head>\n\n        <title>Crypto Compare</title>\n\n')
        __M_writer('        <script src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/jquery-3.3.1.js"></script>\n')
        __M_writer('        <script src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/bootstrap-4.0.0/js/bootstrap.bundle.js"></script>\n        <link rel="stylesheet" href="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/bootstrap-4.0.0/css/bootstrap.sandstone-theme.min.css" />\n')
        __M_writer('        <link rel="stylesheet" href="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/jquery-bootstrap-datepicker.css" />\n        <script src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/jquery-bootstrap-datepicker.js"></script>\n\n')
        __M_writer('        <script src="/django_mako_plus/dmp-common.min.js"></script>\n        ')
        __M_writer(str( django_mako_plus.links(self) ))
        __M_writer('\n\n    </head>\n    <body>\n\n        <div id="finalbanner">\n            2018 411/413 Final Exam\n        </div>\n\n\n        <main>\n            ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n        </main>\n\n    </body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\n                Site content goes here in sub-templates.\n            ')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/brand/Desktop/finalexam/homepage/templates/base.htm", "uri": "base.htm", "source_encoding": "utf-8", "line_map": {"17": 0, "26": 2, "27": 10, "28": 10, "29": 10, "30": 12, "31": 12, "32": 12, "33": 13, "34": 13, "35": 15, "36": 15, "37": 15, "38": 16, "39": 16, "40": 19, "41": 20, "42": 20, "47": 33, "53": 31, "59": 31, "65": 59}}
__M_END_METADATA
"""
