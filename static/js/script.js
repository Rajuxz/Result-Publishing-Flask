$(document).ready(function(){
    $('form').on('submit',function(event){
      $.ajax({
        data:{
          email:$('#email_add').val(),
          password: $('#password').val()
        },
        type: 'POST',
        url: '/sign_in'
      })
      .done(function(data){
        if(data.error){
          $('#failure-alert').text(data.error).show();
          $('#success-alert').hide()

            //$('p').show()
        }else{
          $('#success-alert').text(data.email).show();
          $('#failure-alert').hide()
        }
      });
      event.preventDefault();
    });
    $('#add_student').on('click',function(event){
      console.log("Button clicked !");
      ``
    });
  });