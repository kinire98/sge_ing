# -*- coding: utf-8 -*-

from odoo import models, fields, api #type: ignore

class Libros(models.Model):
    _name = "library_ing.libros"
    _description = "Libros de la biblioteca"

    title = fields.Char(string = "Título")
    authors = fields.Many2many(
            comodel_name = "library_ing.autores",
            relation = "book_authors",
            column1 = "libros_id",
            column2 = "autores_id",
            string = "Autores"
            )
    revisors = fields.Many2many(
            comodel_name = "library_ing.autores",
            relation = "book_revisors",
            column1 = "libros_id",
            column2 = "autores_id",
            string = "Revisores"
            )
    genre = fields.Many2one(
            comodel_name = "library_ing.generos",
            string = "Géneros"
            )
    lent = fields.Many2many(
            comodel_name = "library_ing.socios",
            string = "Prestado a:"
            )

