document.addEventListener('DOMContentLoaded', function () {
    function previewImage(event, previewElementId) {
        var files = event.target.files;
        var previewContainer = document.getElementById(previewElementId);
        previewContainer.innerHTML = ''; // Clear existing images

        if (files) {
            for (var i = 0; i < files.length; i++) {
                var file = files[i];

                var reader = new FileReader();
                reader.onload = function(e) {
                    var imgElement = document.createElement('img');
                    imgElement.src = e.target.result;
                    imgElement.width = 100
                    imgElement.height = 100
                    previewContainer.appendChild(imgElement);
                }
                reader.readAsDataURL(file);
            }
        }
    }

    var imageFields = [
        'id_product_images',
        'id_product_images2',
        'id_product_images3',
        'id_product_images4',
        'id_product_images5'
    ];

    var previewContainers = [
        'product_images_preview',
        'product_images2_preview',
        'product_images3_preview',
        'product_images4_preview',
        'product_images5_preview'
    ];

    imageFields.forEach(function(fieldId, index) {
        document.getElementById(fieldId).addEventListener('change', function(event) {
            previewImage(event, previewContainers[index]);
        });
    });
});
