/*
* Allows in-page filtering based on tags
* https://www.w3schools.com/howto/howto_js_filter_elements.asp
*/

$(function() {
  //select all by default - needs a small timeout to properly work (jQuery bug)
  setTimeout(function(){
    $("#filter-button-all").click();
  },1);

  // Add active class to the current control button (highlight it)
  var btns = $("#filter-container").find(".filter-button")
  for (var i = 0; i < btns.length; i++) {
    btns[i].addEventListener("click", function() {
      var current = document.getElementsByClassName("active");
      current[0].className = current[0].className.replace(" active", "");
      this.className += " active";
    });
  }
});

function filterSelection(filter) {
  var items = $(".filter-item")
  // Add the "hidden" class (display:none) to the filtered elements, and remove the "hidden" class from the elements that are not selected
  for (var i = 0; i < items.length; i++) {
    var filters = items[i].getAttribute("data-filters").split(',');
    var show = false;

    for (var j = 0; j < filters.length; j++) {
      if(filters[j] == filter || filter == "all") { 
        show = true; 
        break;
      }
    }

    // Hide elements that are not selected
    AddClass(items[i], "hidden");

    // Show filtered elements
    if (show) RemoveClass(items[i], "hidden");
  }
}

// Allows adding classes to elements
function AddClass(element, name) {
  var arr1 = element.className.split(" ");
  var classNames = name.split(" ");
  for (var i = 0; i < classNames.length; i++) {
    if (arr1.indexOf(classNames[i]) == -1) {
      element.className += " " + classNames[i];
    }
  }
}

// Allows removing classes from elements
function RemoveClass(element, name) {
  var arr1 = element.className.split(" ");
  var classNames = name.split(" ");
  for (var i = 0; i < classNames.length; i++) {
    while (arr1.indexOf(classNames[i]) > -1) {
      arr1.splice(arr1.indexOf(classNames[i]), 1);
    }
  }
  element.className = arr1.join(" ");
}

