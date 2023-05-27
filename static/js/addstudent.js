$(document).ready(function(){

    /**
     * Sometimes, working with $('#something').on('eventname',function(e){}) sends multiple Post request
     * to endpoint. Adding unbind().bind('',function(){}) worked well. :) 
     */
    $('#addStudentForm').unbind().bind('submit',function(event){
        $.ajax({
            data:{
                name:$('#fullname').val(),
                number:$('#number').val(),
                email:$('#email').val(),
                password:$('#password').val()
            },
            type:'POST',
            url:'/addstudent'
        })
        .done(function(data){
            if(data.error){
                $('#failure-alert').text("Error").show();
                $('#success-alert').hide();
            }else{
                $('#success-alert').text("Success").show();
                $('#failure-alert').hide()
            }
            
        });
        event.preventDefault();
    });
});