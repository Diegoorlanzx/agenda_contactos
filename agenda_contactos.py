print('*** Agenda Contactos ***')

agenda= {
    'carlos': {
        'telefono': '55584789',
        'email': 'carlos@gmail.com',
        'direccion': 'calle principal'
    },
    'maria': {
        'telefono': '55585555',
        'email': 'maria@gmail.com',
        'direccion': 'calle secundaria'
    },

    'pedro': {
        'telefono': '55547541256',
        'email': 'pedor@gmail.com',
        'direccion': 'calle tercera'
    }
}

print(agenda)

print(f''' Informacion del contacto maria :
    Telefono: {agenda ['maria']['telefono']}
    Email: {agenda ['maria']['email']}
    Direccion: {agenda ['maria'] ['direccion']}
    
''')

agenda['ana']= {
        'telefono': '555878546369',
        'email': 'ana@gmail.com',
        'direccion': 'calle cuarta'
}

print(agenda)

agenda.pop('pedro')
print(agenda)

for nombre, detalles in agenda.items():
    print('  ')
    print(f'''nombre: {nombre}
        'Telefono': {detalles.get('telefono')},
        'Email': {detalles.get('email')},
        'Direccion': {detalles.get('direccion')}'
''')

personas= [{'nombre' : 'regina', 'apellido' : 'florez', 'edad' : '20'},
           {'nombre' : 'alejandro', 'apellido' : 'reyes', 'edad' : '30'}]

print(f'''
    'nombre': {personas[0].get('nombre')}
    'apellido': {personas[0].get('apellido')}
    'edad':{personas[0].get('edad')}        
''')

for contador,persona in enumerate(personas):
    print(f'{contador} - persona:{persona}')
    print(f'detalle: nombre:{persona.get('nombre')}, apellido:{persona.get('apellido')}')