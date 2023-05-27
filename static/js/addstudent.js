$(document).ready(function(){
    $('#addStudent').on('click',function(event){
        event.preventDefault();
        // console.log($('#password').val());
        $.ajax({
            data:{
                name:$('#fullname').val(),
                number:$('#number').val(),
                email:$('#email').val(),
                password:$('#password').val()
            },
            type:'POST',
            url:'addstudent/'
        })
        .done(function(data){
            if(data.error){
                // If case
            }else{
                // Else case
            }

        });
    });
});