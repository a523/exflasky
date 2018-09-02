import os
from flask import Flask, render_template, session, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from flask_moment import Moment







@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)

if __name__ == "__main__":
    manager.run()

