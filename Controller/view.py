from flask import Blueprint, Flask, render_template

viewController = Blueprint("/", __name__, url_prefix="/view")


@viewController.route("/")
def main():
    return render_template("/main.html")

