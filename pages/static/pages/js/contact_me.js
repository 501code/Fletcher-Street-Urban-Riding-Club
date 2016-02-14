$(function() {

    $("#contactForm input,#contactForm textarea").jqBootstrapValidation({
        preventSubmit: true,
        submitError: function($form, event, errors) {
            // additional error messages or events
        },
        submitSuccess: function($form, event) {
            event.preventDefault(); // prevent default submit behaviour
            // get values from FORM
            var csrfmiddlewaretoken = $("input[name='csrfmiddlewaretoken']").val();
            var name = $("input#id_name").val();
            var email = $("input#id_email").val();
            var subject = $("input#id_subject").val();
            var message = $("textarea#id_body").val();
            var firstName = name; // For Success/Failure Message
            // Check for white space in name for Success/Fail message
            if (firstName.indexOf(' ') >= 0) {
                firstName = name.split(' ').slice(0, -1).join(' ');
            }
            $.ajax({
                url: "/contact/",
                type: "POST",
                data: {
                    csrfmiddlewaretoken: csrfmiddlewaretoken,
                    name: name,
                    subject: subject,
                    email: email,
                    body: message
                }
            })
            .done(function(html){
                $('#contact_form').html(html)
            });

        },
        filter: function() {
            return $(this).is(":visible");
        },
    });

    $("a[data-toggle=\"tab\"]").click(function(e) {
        e.preventDefault();
        $(this).tab("show");
    });
});


/*When clicking on Full hide fail/success boxes */
$('#name').focus(function() {
    $('#success').html('');
});
