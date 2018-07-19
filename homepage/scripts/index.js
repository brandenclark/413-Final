$(function (context) {
    return function () {

        // Just an easter egg for fun.  You can remove it or leave it. :)
        // Congrats on finishing the semester.
        // $('body').prepend('<img id="picolas" src="/static/homepage/media/cage.jpg" alt="Picalas Cage" />')


        // TODO: add the datepicker.
        // The script/css for the control are already in base.htm.
        // You just need to select the control with jquery and initialize
        // the datepicker.  Use the international date format: yyyy-mm-dd
        // See http://www.eyecon.ro/bootstrap-datepicker/ for docs on this control.
        $('#id_start_date').datepicker({format: 'yyyy-mm-dd'})
        $('#id_end_date').datepicker({format: 'yyyy-mm-dd'})



        // TODO: ajax for "Set Starting Date" button (see index.html).
        // When clicked, the button retrieves via ajax: /homepage/lowest/SMBL
        // where SMBL is the currently-selected symbol in the form.
        // On return, it places the returned date in the form control.
        $('#start_date_button').on('click', function(){
          $.ajax({
            url: "/lowest/" + $('#id_symbol').val(),
            success: function(data){
              $('#id_start_date').datepicker('setValue',data)
            }
          })
        })


        // TODO: ajax for "Set Ending Date" button (see index.html).
        // When clicked, the button retrieves via ajax: /homepage/highest/SMBL
        // where SMBL is the currently-selected symbol in the form.
        // On return, it places the returned date in the form control.
        $('#end_date_button').on('click', function(){
          $.ajax({
            url: "/highest/" + $('#id_symbol').val(),
            success: function(data){
              $('#id_end_date').datepicker('setValue',data)
            }
          })
        })

    }
}(DMP_CONTEXT.get()))
