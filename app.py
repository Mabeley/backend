from flask import Flask, render_template

app =Flask(__name__)

@app.route('/')
def inicio():
    #render_template> renderiza un archivo .html o .jinja para q flask lo pueda leer e interpretar al cliente
    return render_template('inicio.jinja',nombre ='Mabel', dia='Jueves', integrantes=[
        'Integrante1', 
        'Integrante2', 
        'Integrante3'
    ],usuario={
        'nombre':'Juan',
        'direccion':'La piedritas 105',
        'edad':'40'
    }, selecciones =[{
        'nombre':'Bolivia',
        'clasificado':False
    },{
        'nombre':'Brazil',
        'clasificado':True
    },{
        'nombre':'Chile',
        'clasificado':False
    },{
        'nombre':'Peru',
        'timado': True
    }] )
if(__name__=='__main__'):
    app.run(debug=True)