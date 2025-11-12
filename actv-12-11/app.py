from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    # Si el usuario envía el formulario
    if request.method == "POST":
        nombre = request.form.get("nombre")
        mensaje = request.form.get("mensaje")
        return f"""
        <html>
            <head>
                <title>Contacto</title>
                <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css">
            </head>
            <body class="container mt-5">
                <h1 class="text-success">¡Gracias por tu mensaje!</h1>
                <p><strong>Nombre:</strong> {nombre}</p>
                <p><strong>Mensaje:</strong> {mensaje}</p>
                <a href="/" class="btn btn-primary">Volver</a>
            </body>
        </html>
        """
    # Si es GET, mostramos el formulario
    return """
    <html>
        <head>
            <title>Formulario de contacto</title>
            <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css">
        </head>
        <body class="container mt-5">
            <h1 class="text-primary">Formulario de contacto</h1>
            <form method="POST">
                <div class="mb-3">
                    <label for="nombre" class="form-label">Nombre:</label>
                    <input type="text" name="nombre" class="form-control" required>
                </div>
                <div class="mb-3">
                    <label for="mensaje" class="form-label">Mensaje:</label>
                    <textarea name="mensaje" class="form-control" rows="4" required></textarea>
                </div>
                <button type="submit" class="btn btn-success">Enviar</button>
            </form>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
