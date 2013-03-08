$(function(){

    $("#addButton").click(function(){
        window.location = "addProduct";
    });

    $(".btnEdit").click(function(){
        var attrs = $(this).attr("id").split("|");
        window.location = "editProduct/" + attrs[1];

        return false;
    });

    $(".btnDelete").click(function(){
        var attrs = $(this).attr("id").split("|");
        var clickedButton = $(this);
        var deleteConfirm = getDeleteConfirmationHtml();
        deleteConfirm.modal("show");

        deleteConfirm.find("#confirmDelete").click(function() {
            $.ajax({
                type: "POST",
                url: "deleteProduct/" + attrs[1],
                success: function(response) {
                    if(response == "Success") {
                        clickedButton.closest("tr").hide("fast", function () {
                            $(clickedButton.closest("tr")).remove();
                        });
                    }
                    else {
                        alert("Error!");
                    }
                    deleteConfirm.modal("hide");
                }
            });
            return false;
        });

        deleteConfirm.find("#cancelDelete").click(function() {
            deleteConfirm.modal("hide");
            return false;
        });
    });
})

/*
 * Function for getting HTML for modal dialog for confirmation of delete contact action
 */
function getDeleteConfirmationHtml() {

    return $('<div class="modal hide fade" id="deleteContactDialog">'
  +'<div class="modal-header">'
  +'<button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>'
  +'<h3 id="confirmDeleteContact"></h3>'
  +'</div>'
  +'<div class="modal-body">'
  +'<p>Are you sure want to delete product?</p>'
  +'</div>'
  +'<div class="modal-footer">'
  +'<a href="#" id="cancelDelete" class="btn">Cancel</a>'
  +'<a href="#" id="confirmDelete" class="btn btn-primary">Delete</a>'
  +'</div>'
  +'</div>');
}