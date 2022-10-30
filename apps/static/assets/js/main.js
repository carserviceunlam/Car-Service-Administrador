
$(function () {



    $("#formCliente").submit(function (event) {

        event.preventDefault();
        $.ajax({
            data: $("#formCliente").serialize(),
            url: $("#formCliente").attr('action'),
            type: $("#formCliente").attr('method'),
            success: function (response) {
                $('#agregarUsuarioModal').modal('hide');
                location.reload();
                console.log(response)
            },
            error: function (error) {
                console.log(error)
                errorModal(error)

            }

        })
    });

    $("#editarCliente").submit(function (event) {

        event.preventDefault();
        $.ajax({
            data: $("#editarCliente").serialize(),
            url: $("#editarCliente").attr('action'),
            type: $("#editarCliente").attr('method'),
            success: function (response) {
                $('#registrarCliente').modal('hide');
                location.reload();
                console.log(response)
            },
            error: function (error) {
                console.log(error)
            }

        })
    });
    

    function errorModal(errores) {
        console.log("errorModal");
        $('#errores').html("");
        let error = "";

        for (let item in errores.responseJSON.error) {
            error += '<div class="alert alert-danger" <strong>' + errores.responseJSON.error[item] + '</strong></div>'
        }
        $('#errores').append(error);
    }


});

