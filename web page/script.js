getAndSet();
setInterval(getAndSet, 1000);
//try using fetch()
function getAndSet(){
	var data;
	fetch("https://cosc365-981cd.firebaseio.com/run.json")
	.then((response) => response.json())
	.then((responseJSON) => {
		data = JSON.stringify(responseJSON["dist"]);
		console.log(responseJSON);
		console.log(data);
		changeClass(data);
	});
}

function changeClass(data){
	num = parseInt(data);
	if(num < 255){
		document.getElementById("1").className = 'on';
		document. getElementById("1").innerHTML = data;
	}else if(num == 8190 ){
		document.getElementById("1").className = 'off';
		document.getElementById("1").innerHTML = 'out of range';
	}else{
		document.getElementById("1").className = 'off';
		document.getElementById("1").innerHTML = data;
	}
}
