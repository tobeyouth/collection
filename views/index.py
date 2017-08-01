# -*- coding: utf-8 -*

from flask import render_template


def index():
    context = {}
    return render_template('/index.html', **context)
