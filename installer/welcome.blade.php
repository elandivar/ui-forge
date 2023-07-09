<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
  <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css">
  <title>Página con Cards</title>
  <style>
    .logo-container {
      display: flex;
      justify-content: center;
      margin-bottom: 20px;
    }

    .center-content {
      display: flex;
      /*flex-direction: column;*/
      align-items: center;
      justify-content: center;
      min-height: 100vh;
    }

    .card-container {
      /*float: left;*/
      margin-bottom: 20px;
      position: relative;
    }

    .card-container::before {
      content: "";
      position: absolute;
      top: 0;
      left: 0;
      width: 4px;
      height: 100%;
      background-color: #4f4f4f;
    }

    .card {
      background-color: #4f4f4f;
      color: #ffffff;
      display: flex;
      /*align-items: center;*/
      padding: 15px;
    }

    .card-title a {
      color: #ffffff;
    }

    .icon-container {
      width: 60px;
      background-color: #4f4f4f;
      display: flex;
      align-items: center;
      justify-content: center;
      margin-right: 10px;
    }

    .icon {
      color: #ffffff;
      font-size: 24px;
    }

    .card-body {
      flex: 1;
    }
  </style>
</head>
<body>
  <div class="container">
    <div class="logo-container">
      <img src="ruta/al/logo.png" alt="Logo" class="img-fluid">
    </div>
    <div class="center-content">
      <div class="row">
        <div class="col-sm-6 col-md-4">
          <div class="card-container">
            <div class="card card-container">
              <div class="icon-container">
                <i class="fas fa-heart icon"></i>
              </div>
              <div class="card-body">
                <h5 class="card-title"><a href="URL_1">Título 1</a></h5>
                <p class="card-text">Mensaje 1</p>
              </div>
            </div>
          </div>
        </div>
        <div class="col-sm-6 col-md-4">
          <div class="card-container">
            <div class="card card-container">
              <div class="icon-container">
                <i class="fas fa-star icon"></i>
              </div>
              <div class="card-body">
                <h5 class="card-title"><a href="URL_2">Título 2</a></h5>
                <p class="card-text">Mensaje 2</p>
              </div>
            </div>
          </div>
        </div>
        <div class="col-sm-6 col-md-4">
          <div class="card-container">
            <div class="card card-container">
              <div class="icon-container">
                <i class="fas fa-check-circle icon"></i>
              </div>
              <div class="card-body">
                <h5 class="card-title"><a href="URL_3">Título 3</a></h5>
                <p class="card-text">Mensaje 3</p>
              </div>
            </div>
          </div>
        </div>
        <div class="col-sm-6 col-md-4">
          <div class="card-container">
            <div class="card card-container">
              <div class="icon-container">
                <i class="fas fa-envelope icon"></i>
              </div>
              <div class="card-body">
                <h5 class="card-title"><a href="URL_4">Título 4</a></h5>
                <p class="card-text">Mensaje 4</p>
              </div>
            </div>
          </div>
        </div>
        <div class="col-sm-6 col-md-4">
          <div class="card-container">
            <div class="card card-container">
              <div class="icon-container">
                <i class="fas fa-globe icon"></i>
              </div>
              <div class="card-body">
                <h5 class="card-title"><a href="URL_5">Título 5</a></h5>
                <p class="card-text">Mensaje 5</p>
              </div>
            </div>
          </div>
        </div>
        <div class="col-sm-6 col-md-4">
          <div class="card-container">
            <div class="card card-container">
              <div class="icon-container">
                <i class="fas fa-user icon"></i>
              </div>
              <div class="card-body">
                <h5 class="card-title"><a href="URL_6">Título 6</a></h5>
                <p class="card-text">Mensaje 6</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>

  <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
</body>
</html>