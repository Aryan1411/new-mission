from flask import render_template, request, redirect, url_for
from application.model import User
from app import app,db


@app.route('/')
def home():
    return "Welcome to the Home Page"

@app.route('/register', methods=['GET', 'POST'])
def user_register():
    return "register_page"

@app.route('/login', methods=['GET', 'POST'])
def user_login():
    return "User login page"

@app.route("/admin_login", methods=['GET', 'POST'])
def admin_login():
    return "Admin login page"