# -*- coding: utf-8 -*-

# Atualiza informações sobre o clima => URL('default', 'home') => form.clima
def atual_est_esc():
    if not request.vars.estado: return 'Pesquise por uma cidade'

    cidade = request.vars.estado.split(' - ')
    cid_escolhida = db(db.cidades.cidade==cidade[0]).select(db.cidades.id_cidade).first()
    
    temp = requests.get('http://servicos.cptec.inpe.br/XML/cidade/%s/previsao.xml' 
                        %cid_escolhida.id_cidade)	# para 4 dias

    dct_temp = xmltodict.parse(temp.text)

    res = DIV(DIV(request.vars.estado, _class="item ui big label", 
                  _style="padding: 0.3em; text-align: center"),_class="ui list")

    for item in dct_temp['cidade']['previsao']:
        data = item['dia'].split('-')
        tempo = siglas.tempo_clima(item['tempo'])
        dia = '%s/%s' %(data[2], data[1])
        tipo = tempo
        minima = item['minima']
        maxima = item['maxima']
        
        res.append(DIV('%s' %dia, ' - ', '%s' %tipo, XML('<br />'),
            'Mín: ', '%s' %minima, ' - ', 'Máx: ', '%s' %maxima, XML('<br />'), _class="item"))
    return res


# Atualiza informações sobre o CEP digitado
def atual_cep():
    resposta = requests.get('http://api.postmon.com.br/v1/cep/%s'%request.vars.cep).json()
    return DIV(
    			DIV(XML('<b>Endereço:</b> '), '%s' %resposta['logradouro'], _class="item"),
    			DIV(XML('<b>Bairro:</b> '), '%s' %resposta['bairro'], _class="item"),
    			DIV(XML('<b>Cidade:</b> '), '%s' %resposta['cidade'], _class="item"),
    			DIV(XML('<b>Estado:</b> '), '%s' %resposta['estado_info']['nome'], _class="item"),
    			DIV(XML('<b>CEP:</b> '), '%s' %resposta['cep'], _class="item"),
    		_class="ui list")


# Atualiza informações sobre o fuso digitado
def atual_fuso():
	cid_escolhida = horario_outra_zona(loc_agora, request.vars.fuso)
	return P('%s' %cid_escolhida[0], XML('<br />'), '%s - %s' %(cid_escolhida[1], cid_escolhida[2]))
