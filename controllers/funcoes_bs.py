# -*- coding: utf-8 -*-

# Atualiza informações sobre o clima => URL('default', 'home') => form.clima
def atual_est_esc():
    if not request.vars.estado: return 'Pesquise por uma cidade'
    # a = UL(LI('teste'))
    # return a
    cidade = request.vars.estado.split(' - ')
    cid_escolhida = db(db.cidades.cidade==cidade[0]).select(db.cidades.id_cidade).first()
    
    temp = requests.get('http://servicos.cptec.inpe.br/XML/cidade/%s/previsao.xml' %cid_escolhida.id_cidade)	# para 4 dias

    dct_temp = xmltodict.parse(temp.text)

    res = UL(LI(request.vars.estado, _class="list-group-item list-group-item-success"),_class="list-group")

    # print dct_temp

    for item in dct_temp['cidade']['previsao']:
        data = item['dia'].split('-')
        tempo = siglas.tempo_clima(item['tempo'])
        dia = '%s/%s' %(data[2], data[1])
        tipo = tempo
        minima = item['minima']
        maxima = item['maxima']
        
        res.append(
            LI('%s' %dia, ' - ', '%s' %tipo, XML('<br />'),
            'Mín: ', '%s' %minima, ' - ', 'Máx: ', '%s' %maxima, _class="list-group-item"))

        # res.append(UL(
        #     LI('%s' %dia, ' - ', '%s' %tipo, _class="list-group-item"), 
        #     LI('Mín: ', '%s' %minima, ' - ', 'Máx: ', '%s' %maxima, _class="list-group-item"), _class="list-group"))
        # res.append(LI('%s' %dia, ' - ', '%s' %tipo, _class="list-group-item"))
        # res.append(LI('Mín: ', '%s' %minima, ' - ', 'Máx: ', '%s' %maxima, _class="list-group-item"))
        # res.append(LI('Máx: ', '%s' %maxima, _class="list-group-item"))
        # return P(request.vars.estado, XML('<br />'), '%s' %dia, ' - ', '%s' %tempo, XML('<br />'), 'Mín: ', '%s' %minima, '° - Máx: ', '%s' %maxima, '°')
    # print res
    return res
		# print dia, tipo, minima, maxima
	# atualizado = dct_temp['cidade']['atualizacao'].split('-')
	# print atualizado[2], atualizado[1], atualizado[0]
	# print atualizado

    # return dct_temp['cidade']['nome']
    # print '%s - %s' %(dct_temp['cidade']['nome'], dct_temp['cidade']['uf'])
    # return '%s - %s' %(dct_temp['cidade']['nome'], dct_temp['cidade']['uf'])
    # return request.vars.estado
    # return 'http://servicos.cptec.inpe.br/XML/cidade/%s/previsao.xml' %cid_escolhida.id_cidade

def atual_cep():
    resp = requests.get('http://api.postmon.com.br/v1/cep/%s'%request.vars.cep)
    resposta = json.loads(resp.text)
    return UL(
    			LI(XML('<b>Endereço:</b> '), '%s' %resposta['logradouro'], _class="list-group-item"),
    			LI(XML('<b>Bairro:</b> '), '%s' %resposta['bairro'], _class="list-group-item"),
    			LI(XML('<b>Cidade:</b> '), '%s' %resposta['cidade'], _class="list-group-item"),
    			LI(XML('<b>Estado:</b> '), '%s' %resposta['estado_info']['nome'], _class="list-group-item"),
    			LI(XML('<b>CEP:</b> '), '%s' %resposta['cep'], _class="list-group-item"),
    		_class="list-group")


def atual_fuso():
	cid_escolhida = horario_outra_zona(loc_agora, request.vars.cidade)
	return P('%s' %cid_escolhida[0], XML('<br />'), '%s - %s' %(cid_escolhida[1], cid_escolhida[2]))

