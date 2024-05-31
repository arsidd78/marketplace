function previewImages(event) {
    var files = event.target.files;
    var previewContainer = document.getElementById('imagePreview');
    previewContainer.innerHTML = ''; // Clear existing images

    if (files) {
        for (var i = 0; i < files.length; i++) {
            var file = files[i];

            var reader = new FileReader();
            reader.onload = function(e) {
                var imgElement = document.createElement('img');
                imgElement.src = e.target.result;
                previewContainer.appendChild(imgElement);
            }
            reader.readAsDataURL(file);
        }
    }
}
