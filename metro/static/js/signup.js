$(document).ready(function(){
    $('#sign').click(function(){
      var fname=$('#inputFname4')
      var Lname=$('#inputLname4')
      var email=$('#inputEmail4')
      var passvalue=$('#inputPassword4')
      var cpassvalue=$('#inputcPassword4')
      var pattern=" /^([a-zA-Z0-9_.+-])+\@@(([a-zA-Z0-9-])+\.)+([a-zA-Z0-9]{2,4})+$/"

      if(fname.val()==""){
        $('#p2').show()
        $('#inputFname4').css({'border':'solid 2px red'})
        return false
      }
      else{
        $('#inputFname4').css({'border':' solid 1px black'})
        $('#p2').hide()
      }    
      if(Lname.val()==""){
        $('#p3').show()
        $('#inputLname4').css({'border':'solid 2px red'})
        return false
      }
      else{
        $('#inputLname4').css({'border':' solid 1px black'}) 
        $('#p3').hide()
      }

      if(email.val()==""){
        $('#p4').show()
        $('#inputEmail4').css({'border':'solid 2px red'})
        return false
      }
      else{
        $('#inputEmail4').css({'border':' solid 1px black'}) 
        $('#p4').hide()
      }
      if(pattern.match(email.val())==null){
        $('#p4').html("**Please enter email in proper manner")
        $('#p4').show()
        $('#inputEmail4').css({'border':'solid 2px red'})   
        return false 
      }
      else{
        $('inputEmail4').css({'border':'solid 1px black'})
        $('#p4').hide()
      }

      if(passvalue.val()==""){
        $('#p1').show()
        $('#inputPassword4').css({'border':'solid 2px red'})
        return false
      }
      else{
        $('inputPassword4').css({'border':'solid 1px black'})
        $('#p1').hide()
      }
      if(passvalue.length<8){
        $('#p1').html("**must contain 8 character")
        $('#p1').show()
        $('#inputPassword4').css({'border':'solid 2px red'})   
        return false
      }
      else if(passvalue.length>8){
        $('inputPassword4').css({'border':'solid 1px black'})
        $('#p1').hide()
      }
      if(cpassvalue.val()==""){
        $('#p5').show()
        $('#inputcPassword4').css({'border':'solid 2px red'})
        return false
      }
      else{
        $('inputcPassword4').css({'border':'solid 1px black'})
        $('#p5').hide()
      }
      if(cpassvalue.val()!=passvalue.val()){
          $('#p5').html("**password did not match")
          $('#p5').show()
          return false
      }
    
     




      

    })
  })