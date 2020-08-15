   passlength = prompt("How long would you like your password to be? (Integers only)", "5")
	 
	 charset = "ABCDEFGHIJKLMNOPQRSTUVWXYZ123456789"
	 
	 function getRandomInt(min, max) {
        min = Math.ceil(min);
        max = Math.floor(max);
        return Math.floor(Math.random() * (max - min)) + min; 
    }
    

	 function generatePass(){
	     var password = ""
	     for (let i = 0; i<passlength; i++)
         {
            password += charset.charAt(getRandomInt(0,charset.length)) //Add on new chars to pass

         }
         return password
	     
	 }
	
     var pass = generatePass()
     alert(pass)
