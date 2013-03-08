$(function(){

    $("#addButton").click(function(){
        window.location = "addProduct";
    });

    $("button").click(function(){
        var attrs = $(this).attr("id").split("|");

        // If user click button for edit product
        if(attrs[0] == "edit"){
            window.location = "editProduct/" + attrs[1];
        }

        // If user click button for delete product
        if(attrs[0] == "delete"){
            window.location = "deleteProduct/" + attrs[1];
        }

    });

})