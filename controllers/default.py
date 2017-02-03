# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

# -------------------------------------------------------------------------
# This is a sample controller
# - index is the default action of any application
# - user is required for authentication and authorization
# - download is for downloading files uploaded in the db (does streaming)
# -------------------------------------------------------------------------


def index():
    return dict()


def home():     
    est_esc = db(db.cidades).select(db.cidades.cidade, db.cidades.estado)
    lista_cid_est = ['{0} - {1}'.format(i.cidade,i.estado) for i in est_esc]

    return dict(lista_fuso=common_timezones, lista_cid_est=lista_cid_est)

def home_bs():     
    est_esc = db(db.cidades).select(db.cidades.cidade, db.cidades.estado)
    lista_cid_est = ['{0} - {1}'.format(i.cidade,i.estado) for i in est_esc]

    return dict(lista_fuso=common_timezones, lista_cid_est=lista_cid_est)

def jquery_autocomplete():
    lista_cid_est = ['AC', 'AL', 'AM', 'AP', 'BA', 'CE', 'DF', 'ES', 'GO', 
                   'MA', 'MG', 'MS', 'MT', 'PA', 'PB', 'PE', 'PI', 'PR', 
                   'RJ', 'RN', 'RO', 'RR', 'RS', 'SC', 'SE', 'SP', 'TO']
    return dict(lista_cid_est=lista_cid_est)

def select_ui():
    return dict(lista_fuso=common_timezones)

def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/bulk_register
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    also notice there is http://..../[app]/appadmin/manage/auth to allow administrator to manage users
    """
    return dict(form=auth())


@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()


