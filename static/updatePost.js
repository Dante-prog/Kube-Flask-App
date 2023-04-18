function enableButtons(event,id) {
  var content = event.value;
  var idN = "buttonU-"+id;
  var button = document.getElementById(idN);
   
    if (content) {
      button.removeAttribute("disabled");
    } else {
      button.setAttribute("disabled", true);
    }
   
}



  