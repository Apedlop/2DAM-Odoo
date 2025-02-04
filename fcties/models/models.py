from odoo import models, fields, api

class Alumnos(models.Model):
    _name = 'fcties.alumnos'
    _description = 'Alumnos'

    # Campos obligatorios
    nombre = fields.Char(string="Nombre", required=True)
    apellidos = fields.Char(string="Apellidos", required=True)
    fecha_nacimiento = fields.Date(string="Fecha de Nacimiento", required=True)
    curso_academico = fields.Char(string="Curso Académico", required=True)
    ciclo_formativo = fields.Selection(
        [('DAM', 'Desarrollo de Aplicaciones Multiplataforma'),
         ('DAW', 'Desarrollo de Aplicaciones Web'),
         ('ASIR', 'Administración de Sistemas Informáticos en Red')],
        string="Ciclo Formativo", required=True)
    periodo_practica = fields.Selection(
        [('abril', 'Abril'), ('septiembre', 'Septiembre')],
        string="Periodo de Práctica", required=True)
    nota_media = fields.Float(string="Nota Media", required=True)

    # Campos opcionales
    correo_electronico = fields.Char(string="Correo Electrónico")
    telefono = fields.Char(string="Teléfono")

    # Relación con Empresas donde ha hecho prácticas
    empresas_practicas = fields.Many2many(
        'fcties.empresa',
        string='Empresas donde ha hecho prácticas',
    )

    # Campo calculado para la nota en formato texto
    @api.depends('nota_media')
    def _compute_nota_media_texto(self):
        for alumno in self:
            if 5 <= alumno.nota_media < 7:
                alumno.nota_media_texto = "Aprobado"
            elif 7 <= alumno.nota_media < 9:
                alumno.nota_media_texto = "Notable"
            elif 9 <= alumno.nota_media <= 10:
                alumno.nota_media_texto = "Sobresaliente"
            else:
                alumno.nota_media_texto = "No válida"

    # Campo de nota media en formato texto
    nota_media_texto = fields.Char(string="Nota Media (Texto)", compute='_compute_nota_media_texto', store=True)

    # Filtro para obtener alumnos con nota media > 8
    def alumnos_nota_mayor_8(self):
        return self.search([('nota_media', '>', 8)])

class Empresa(models.Model):
    _name = 'fcties.empresa'
    _description = 'Empresa'

    # Campos obligatorios
    nombre = fields.Char(string="Nombre de la Empresa", required=True)
    persona_contacto = fields.Char(string="Persona de Contacto", required=True)
    telefono_contacto = fields.Char(string="Teléfono de Contacto", required=True)
    correo_electronico = fields.Char(string="Correo Electrónico", required=True)
    direccion = fields.Text(string="Dirección", required=True)

    # Relación con Alumnos que han hecho las prácticas en la empresa
    alumnos_practicas = fields.Many2many(
        'fcties.alumnos',
        string='Alumnos en Prácticas',
        help='Lista de alumnos que han realizado prácticas en esta empresa'
    )
