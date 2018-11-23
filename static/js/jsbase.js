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

//funcion para previsualizar imagenes
document.getElementById("id_fotoSoc").onchange = function (e) {
    let reader = new FileReader();
    reader.readAsDataURL(e.target.files[0]);
    reader.onload = function () {
        let preview = document.getElementById('preview'),
            image = document.createElement('img');
            image.height=200;
        image.src = reader.result;

        preview.innerHTML = '';
        preview.append(image);
    };
}

//llamado al datepicker
$('.datepicker').datepicker();
$('#id_fechaActa').datepicker();

//suma automatica
function sumar() {
    var total = 0;
    $(".monto").each(function () {
      if (isNaN(parseFloat($(this).val()))) {
        total += 0;
      } else {
        total += parseFloat($(this).val());
      }
    });
    //alert(total);
    document.getElementById('spTotal').innerHTML = total;
  }
  