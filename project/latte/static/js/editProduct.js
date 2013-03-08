$(function(){

    var productId = window.location.pathname.split("/")[3];
    var imagesUrl = "http://127.0.0.1:8000/api/restaurant/" + Global.restaurant_id + "/product/" + productId + "?callback=jsonpCallback";
    var fullUrl = location.protocol + '//' + location.hostname + (location.port ? ':' + location.port : '');

    var spinner = makeAndRunSpin();

    $("#imageGallery div").addClass("autoSizeIm");

    $.ajax({
        url: imagesUrl,
        type: "GET",
        contentType: "application/json",
        dataType: 'jsonp',
        success: function(data){
            var first = true;
            $("#imageContainer").append("<table></table>");
            $.each(data[0].pictures, function(key, picture){
                $("#imageGallery div").removeClass("autoSizeIm");
                $("#imageGallery div").addClass("manualSizeIm");

                var fullImageUrl = fullUrl + picture.relative_path;

                if(first) {
                    $("#imageGallery .carousel-inner").append('<div class="active item"><img src="' + fullImageUrl + '" alt="product"/></div>');
                    first = false;
                }
                else {
                    $("#imageGallery .carousel-inner").append('<div class="item"><img src="' + fullImageUrl + '" alt="product"/></div>');
                }
                $("#imageContainer table").append("<tr class=" + picture.id + "><td><img src='" + fullImageUrl + "' alt='product'/></td><td><i class='icon-remove'></i></td></tr>");

            });
            if(!first) {
                console.log("aha");
                $("#imageGallery").append('<a class="carousel-control left" href="#imageGallery" data-slide="prev">‹</a>');
                $("#imageGallery").append('<a class="carousel-control right" href="#imageGallery" data-slide="next">›</a>');

                $('.carousel').carousel({
                    interval: 3000
                });
            }
            spinner.stop();
        }
    });

    $("#imageContainer").on("click", "table tr td i", function(){

        var imgRow = $(this).closest("tr");
        var imgId = imgRow.attr("class");
        var deleteConfirm = getDeleteConfirmationHtml();
        deleteConfirm.modal("show");

        deleteConfirm.find("#confirmDelete").click(function() {
            $.ajax({
                url: "/home/deletePicture/" + imgId,
                type: "POST",
                success: function(response) {
                    if(response == "Success") {
                        imgRow.hide("fast", function () {
                            $(imgRow).remove();
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

});

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
  +'<p>Are you sure want to delete picture?</p>'
  +'</div>'
  +'<div class="modal-footer">'
  +'<a href="#" id="cancelDelete" class="btn">Cancel</a>'
  +'<a href="#" id="confirmDelete" class="btn btn-primary">Delete</a>'
  +'</div>'
  +'</div>');
}

function makeAndRunSpin(){
    var opts = {
        lines: 10, // The number of lines to draw
        length: 6, // The length of each line
        width: 4, // The line thickness
        radius: 7, // The radius of the inner circle
        corners: 1, // Corner roundness (0..1)
        rotate: 0, // The rotation offset
        color: '#000', // #rgb or #rrggbb
        speed: 1, // Rounds per second
        trail: 60, // Afterglow percentage
        shadow: false, // Whether to render a shadow
        hwaccel: false, // Whether to use hardware acceleration
        className: 'spinner', // The CSS class to assign to the spinner
        zIndex: 2e9, // The z-index (defaults to 2000000000)
        top: 'auto', // Top position relative to parent in px
        left: 'auto' // Left position relative to parent in px
    };
    var target = document.getElementById('imageTd');
    return new Spinner(opts).spin(target);
}