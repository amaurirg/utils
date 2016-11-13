$(document).ready(function(){
$(function(){
	$('.ui.accordion').accordion();
	$('#div_clima').hide()
	$('#div_fuso').hide()
	$('#div_cep').hide()
});

$( function() {
{{=ASSIGNJS(siglas = lista_cid_est)}}
$( "#no_table_estado" ).autocomplete({
    source: function( request, response ) {
    var matcher = new RegExp( "^" + $.ui.autocomplete.escapeRegex( request.term ), "i" );
    response( $.grep( siglas, function( item ){
        return matcher.test( item );
    }) );
  }
});
} );

$( function() {
{{=ASSIGNJS(siglas = lista_fuso)}}
$( "#no_table_fuso" ).autocomplete({ source: siglas });
} );


jQuery('#form_clima').submit(function() {
	$('#div_clima').show();
  ajax('{{=URL('funcoes', 'atual_est_esc')}}',
       ['estado'], 'div_clima');
  	$('#content_clima').removeClass("active")
  	$('#title_clima').removeClass("active")
  return false;
});


jQuery('#form_fuso').submit(function() {
	$('#div_fuso').show();
  ajax('{{=URL('funcoes', 'atual_fuso')}}',
       ['fuso'], 'div_fuso');
	$('#content_fuso').removeClass("active")
  	$('#title_fuso').removeClass("active")
  return false;
});


jQuery('#form_cep').submit(function() {
	$('#div_cep').show();
  ajax('{{=URL('funcoes', 'atual_cep')}}',
       ['cep'], 'div_cep');
  	$('#content_cep').removeClass("active")
  	$('#title_cep').removeClass("active")
  return false;
});
});