$(document).ready(function() {

    // SIGNUP for a meetup
    //
    $('.meetup-submit-btn').on('click', function(){

        var meetup_id = $(this).attr('meetup-id');
        var form = $('#meetup_form_' + meetup_id).serialize();

        $.ajax({
            data: form,
            type:"POST",
            url: window.URLS['registerURL'],
            success: function(result) {
                alert('you have successfully registered to this meetup. goodluck!');
                $('#meetup_modal_' + meetup_id).modal('hide');
            }
        });

    });

});
