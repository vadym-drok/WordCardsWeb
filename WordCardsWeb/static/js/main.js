// Delete Word from dictionary
function delete_w_JS(pk){
    let del_choice = confirm('Do you want to delete this Word'  + '?');
    if (del_choice) {
      window.location.href = (pk + "/delete/");
    }
  }


