#!/usr/bin/env python3
# -*-coding:utf-8 -*-

from flask import Blueprint  # 蓝本

main = Blueprint('main', __name__)

from .import views, errors
