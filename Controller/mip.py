from flask import Blueprint, Flask, render_template

mipController = Blueprint("mip", __name__, url_prefix="/mip")


@mipController.route("/addMIP")
def addMip():
    return render_template("/addMIP.html")