# -*- coding: utf-8 -*-

db.define_table('cidades',
    Field('id_cidade','string'),
    Field('cidade','string'),
    Field('estado','string'),
    format = '%(cidade)s  -  %(estado)s',
    migrate=False)

# db.cidades.cidade.widget = SQLFORM.widgets.autocomplete(request, db.cidades.cidade, limitby=(0,1), min_length=1)

db.define_table('aeroportos',
    Field('estado','string'),
    Field('sigla','string'),
    Field('cidade','string'),
    migrate=False)