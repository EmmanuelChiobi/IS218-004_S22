from flask import render_template
#don't change this import or it can't find the module controller
from  . controller import ControllerBase


class IndexController(ControllerBase):
    @staticmethod
    def get():
        name = "THIS IS NOT MY NAME"
        return render_template('index.html', name=name)
