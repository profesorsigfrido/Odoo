#importo librerias del modulo odoo
from odoo import models,fields

# creamos clase y heredamos model de la clase models
class TodoTask(models.Model):
       #nombre del modelo y descipcion
	_name = 'todo.task'
	_description = 'Todo Task'
       #3 campos que ponemos en el modelo
	name = fields.Char('Descripcion',required=True)
	is_done = fields.Boolean('Hecho?')
	active = fields.Boolean('Activo?',default=True)
