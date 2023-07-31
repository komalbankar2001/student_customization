from odoo import fields, models, api


class Student(models.Model):
    _name = 'students'
    _description = 'Students'

    name = fields.Char(string='Name', required=False)
    age = fields.Integer(string='Age', required=False)
    std_class = fields.Char(string='Std_class', required=False)
