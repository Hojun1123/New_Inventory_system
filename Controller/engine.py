from flask import Blueprint, Flask, render_template, request
from Service.Engine import addEngines
engineController = Blueprint("engine", __name__, url_prefix="/engine")


@engineController.route("/addEngine", methods=['GET', 'POST'])
def addEngine():
    if request.method == 'POST':
        data = request.form.get("barcode")
        a = addEngines.inputEngine(data)
        print(a)

        return render_template("/readBarcode.html")
    else:
        return render_template("/readBarcode.html")

