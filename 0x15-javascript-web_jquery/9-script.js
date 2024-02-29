$(document).ready(function(){
    $('#btn_translate').click(function(){
        var langCode = $('#language_code').val();
        $.get('https://hellosalut.stefanbohacek.dev/?lang=' + langCode, function(data){
            $('#hello').text(data.hello);
        });
    });
});
