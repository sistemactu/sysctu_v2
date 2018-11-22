/*
document.getElementById("id_fotoSoc").onchange = function (e) {
    if (document.images) {
        document.images.logo.width = 200;
        document.images.logo.height = 200;
    } else {
        logo = document.getElementById("logo");
        logo.width = 200;
        logo.height = 200;
    }
}*/

document.getElementById("id_fotoSoc").onchange = function (e) {
    // Creamos el objeto de la clase FileReader
    let reader = new FileReader();

    // Leemos el archivo subido y se lo pasamos a nuestro fileReader
    reader.readAsDataURL(e.target.files[0]);

    // Le decimos que cuando este listo ejecute el código interno
    reader.onload = function () {
        let preview = document.getElementById('preview'),
            image = document.createElement('img');
            image.height=200;
        image.src = reader.result;

        preview.innerHTML = '';
        preview.append(image);
    };
}