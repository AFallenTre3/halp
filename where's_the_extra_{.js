function start() {
    var player = playerrpors();
    var computer = rpors();
    var result = beat(player, computer);
    var v = winner(player, computer, result);
}

/*
This program will pit a 
physical player against a simple cpu in Rock, Paper, Scissors 
to see who comes out on top 
it was inspired by my group traditionally playing rock paper scissors 
who determined who would put the laptops away at the end of class
*/

// cpu randomly picks either rock, paper, or scissors
function rpors(){
    var cpu = Randomizer.nextInt(1, 3);
    var random = "R";
    if(cpu == 2){
        random = "P";
    }else if(cpu == 3){
        random = "S";
    }
    return random;
}

// asks what you want to pick (rock, paper, scissors)
function playerrpors(){
    var num = readLine("What will you choose? R/P/S ");
    return num;
}

// recognizes if your pick beats the cpus pick
function beat(num, random){
   var t = ("");
   if( num == "R" && random == "S"){
        t = true;
   } 
   if( num == "R" && random == "P"){
       t = false;   
   } 
   if( num == "P" && random == "R"){
       t = true; 
   } 
   if( num == "P" && random == "S"){
       t = false;
   } 
   if( num == "S" && random == "R"){
       t = true;
   } 
   if( num == "S" && random == "P") {
       t = false;
   } 
   if( num == random){
       t = "ITS A TIE! Play again!";
   }
   return t;
}


function winner(num, random, t){
    if(t = true){
        println("YOU WON! You picked " + num + " they picked " + random);
    }else if{
        println("YOU LOST. You picked " + num + " they picked " + random);
    }
}
