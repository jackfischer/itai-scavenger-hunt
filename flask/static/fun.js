function runCommand(command){
	httpOut("/fun/" + "/");
}

function httpOut(url){
	var xmlHttp = new XMLHttpRequest();
    	xmlHttp.open( "GET", theUrl, false ); // false for synchronous request
    	xmlHttp.send( null );
    	var response = xmlHttp.responseText;
}
