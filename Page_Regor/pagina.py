from flask import Flask, render_template, request, redirect, url_for, jsonify, Response
import dataBase as dbase
from ventas import Ventas

db = dbase.dbConnection()

app = Flask(__name__)

#index.html
@app.route('/')
def index():
    return render_template('index.html')

#ventas.html
@app.route('/ventas')
def ventas():
    ventas = db['ventas']
    ventasReceived = ventas.find()
    return render_template('ventas.html', ventas = ventasReceived)

#metodo post
@app.route('/ventas', methods=['POST'])
def addVentas():
    ventas = db['ventas']
    name = request.form['name']
    email = request.form['email']
    phone_number = request.form['phone_number']
    address = request.form['address']
    cp = request.form['cp']

    if name and email and phone_number and address and cp:
        venta = Ventas(name, email, phone_number, address, cp)
        ventas.insert_one(venta.toDBCollection())
        Response = jsonify({
            "name": name,
            "email": email,
            "phone_number": phone_number,
            "address": address,
            "cp": cp
        })
        return redirect(url_for('index'))
    else:
        return notFound()

#metodo delete
@app.route('/delete/<string:ventas_name>')
def delete(ventas_name):
    ventas = db['ventas']
    ventas.delete_one({'name': ventas_name})
    return redirect(url_for('ventas'))

#metodo editar
@app.route('/edit/<string:ventas_name>', methods=['POST'])
def edit(ventas_name):
    ventas = db['ventas']
    name = request.form['name']
    email = request.form['email']
    phone_number = request.form['phone_number']
    address = request.form['address']
    cp = request.form['cp']

    if name and email and phone_number and address and cp:
        ventas.update_one({'name': ventas_name}, {'$set' : {'name': name, 'email': email, 'phone_number': phone_number, 'address': address, 'cp': cp}})
        Response = jsonify({'message': 'ventas' + ventas_name + ' Actualizado correctamente '})
        return redirect(url_for('ventas'))
    else:
        return notFound()
    
@app.errorhandler(404)
def notFound(error=None):
    message ={
        'message': 'Ingrese los datos que se le solicitaron' + request.url
    }
    Response = jsonify(message)
    Response.status_code = 404
    return Response

if __name__ == '__main__':
    app.run(debug=False)