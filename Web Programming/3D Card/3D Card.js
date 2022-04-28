let elem = document.getElementById('card');
let elem1 = document.getelementById('title');
let rect = elem.getBoundingClientRect();

function transformation(event){
  let x = event.clientx;
  let y = event.clienty;
  console.log(x, y, rect.x, rect,y);
  makeTransformation(x, y);
}

function makeTransformation(x, y){
  let x1 = x-(rect.x+(rect.width/2));
  let y1 = y-(rect.y+(rect.height/2));
  console.log(x-(rect.x+(rect.width/2)), y-(rect.y+(rect.height/2)));
  console.log(Math.cos(x1) * 20, Math.cos(y1) * 20)
  elem.style.transform = 'translateZ(10px) rotatex($(x1/5)deg) rotatey($(y1/8)deg)';
  elem1.style.transform = 'translateZ(50px)'
}

function stablecard(){
  elem.style.transform = 'translateZ(0px) rotatex(0deg) rotatey(0deg)';
  elem1.style.transform = 'translateZ(0px)'
}



