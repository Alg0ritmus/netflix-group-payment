

let getCookie = (cname) => {
    let name = cname + "=";
    let decodedCookie = decodeURIComponent(document.cookie);
    let ca = decodedCookie.split(';');
    for(let i = 0; i <ca.length; i++) {
      let c = ca[i];
      while (c.charAt(0) == ' ') {
        c = c.substring(1);
      }
      if (c.indexOf(name) == 0) {
        return c.substring(name.length, c.length);
      }
    }
    return "";
}

const token = getCookie("csrftoken");

let toggle_hidden_section = (toggle_section) => {
    var toggle_hidden_section = document.getElementById(toggle_section);
    if (toggle_hidden_section.style.display == "block"){
        toggle_hidden_section.style.display = "none";
    }
    else{
        toggle_hidden_section.style.display = "block";
    }
};


let edit_item = (element) => {
    let tooltip = element.children[0];
    if (tooltip.style.visibility == "visible") {
        tooltip.style.visibility = "hidden";
        tooltip.style.opacity = 0;
    }
    else{
        tooltip.style.visibility = "visible";
        tooltip.style.opacity = 1;
    }
    
}

let redirect_to_edit = (url) => {
    let full_url = (window.location.host+url);
    window.location.replace(url);
}

let send_edited = (element,item_id) => {
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "/api/uprav_polozky/"+item_id+"/", true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.setRequestHeader("X-CSRFToken", token);
    xhr.send(JSON.stringify({
        id: item_id
    }));
    
}



let delete_item = (item_id) => {
    var xhr = new XMLHttpRequest();
    xhr.open("DELETE", "/api/vymaz_polozky/"+item_id+"/", true);
    xhr.onreadystatechange = () => {
        if (xhr.readyState == XMLHttpRequest.DONE) {
            window.location.replace(window.location.href)
        }
    } 
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.setRequestHeader("X-CSRFToken", token);
    xhr.send(JSON.stringify({
        id: item_id
    }));
}


/* scrolled grid down */

let scrollGrid = () => {
    var objDiv = document.getElementsByClassName("grid-container")[0];

    objDiv.scrollTop = objDiv.scrollHeight;

}
scrollGrid();


let getDate = () => {
    date = new Date();
    year = date.getFullYear();
    month = date.getMonth() + 1;
    day = date.getDate();
    //document.getElementById("current_date").innerHTML = 
    return (day + "." + month + "." + year);
}


/*  GETTING RESPONSE FROM SERVER
    xhr.open....

    xhr.onreadystatechange = function() {
        if (xhr.readyState == XMLHttpRequest.DONE) {
            fill_data_from_req(element,xhr.responseText);
        }
    } 

*/