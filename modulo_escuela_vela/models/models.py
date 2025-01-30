# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Escuela(models.Model):
    _name = "modulo_escuela_vela.escuela"  
    _description = "Escuela de Vela"  

    name = fields.Char(string='Denominación', required=True)
    logo = fields.Image(string='Logotipo', max_width=1024, max_height=1024)
    direccion = fields.Char(string='Dirección', required=True)
    telefono = fields.Char(string='Teléfono', required=True)
    email = fields.Char(string='Correo Electrónico', required=True)

class Curso(models.Model):
    _name = 'modulo_escuela_vela.curso'
    _description = 'Curso de Escuela Vela'

    titulo = fields.Char(string='Título', required=True)
    duracion_dias = fields.Integer(string='Duración en días')
    duracion_horas = fields.Integer(string='Duración en horas')
    precio = fields.Float(string='Precio', required=True)
    escuela_id = fields.Many2one('modulo_escuela_vela.escuela', string='Escuela')
    
class Monitor(models.Model):
    _name = "modulo_escuela_vela.monitor"  
    _description = "Monitor de Vela"  

    name = fields.Char(string='Nombre', required=True)
    code = fields.Char(string='Código de Identificación', required=True, unique=True)
    telefono = fields.Char(string='Teléfono')
    email = fields.Char(string='Correo Electrónico')
    escuelas_ids = fields.Many2many('modulo_escuela_vela.escuela', string='Escuelas')

class Alumno(models.Model):
    _name = "modulo_escuela_vela.alumno"  
    _description = "Alumno de Vela"  

    name = fields.Char(string='Nombre', required=True)
    telefono = fields.Char(string='Teléfono')
    email = fields.Char(string='Correo Electrónico')
    matricula = fields.Char(string='Número de Matrícula', required=True, unique=True)
    escuela_id = fields.Many2one('modulo_escuela_vela.escuela', string='Escuela', required=True)


# class mimodulo(models.Model):
#     _name = 'mimodulo.mimodulo'
#     _description = 'mimodulo.mimodulo'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()

#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

