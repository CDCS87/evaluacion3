from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    promedio = None
    estado = None
    if request.method == 'POST':
        nota1 = float(request.form.get('nota1', 0))
        nota2 = float(request.form.get('nota2', 0))
        nota3 = float(request.form.get('nota3', 0))
        asistencia = int(request.form.get('asistencia', 0))

        # Acciones con los datos ingresados
        promedio = round((nota1 + nota2 + nota3) / 3, 1)
        estado = 'APROBADO' if promedio >= 40 and asistencia >= 75 else 'REPROBADO'

    return render_template('ejercicio1.html', promedio=promedio, estado=estado)


@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    nombre_mayor = None
    caracteres = None

    if request.method == 'POST':
        nombre1 = request.form.get('nombre1', '')
        nombre2 = request.form.get('nombre2', '')
        nombre3 = request.form.get('nombre3', '')

        nombres = [nombre1, nombre2, nombre3]
        nombre_mayor = max(nombres, key=len)
        caracteres = len(nombre_mayor)

    return render_template('ejercicio2.html', nombre_mayor=nombre_mayor, caracteres=caracteres)


if __name__ == '__main__':
    app.run(debug=True)
