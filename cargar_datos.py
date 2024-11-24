import pandas as pd
import mysql.connector
from mysql.connector import Error   

# Ruta del archivo Excel
file_path = 'gestion-carteras-web.xlsx'


# Cargar los datos del archivo Excel
df = pd.read_excel(file_path)

# Renombrar las columnas para que coincidan con los nombres de las tablas en la base de datos
df = df.rename(columns={
    'NroFactura': 'numero_factura',
    'NitAseguradora': 'nit',
    'Entidad': 'entidad', 
    'dFechaFactura': 'fecha_factura',
    'dFechaIngreso': 'fecha_ingreso',
    'dFechaEgreso': 'fecha_egreso',
    'VALOR TOTAL FACTURA': 'valor_total_factura',
    'Valor Copago DESCUENTO': 'valor_copago',
    'VALOR_TOTAL A COBRAR': 'valor_total_cobrar',
    'vEstado': 'estado',
    'FechaRadicado': 'fecha_radicado',
    'NroRadicado': 'numero_radicado',
    'vTipoIdentificacion': 'tipo_identificacion',
    'vIdentificacion': 'identificacion',
    'vNombrePaciente': 'nombre_paciente',
    'dFechaNacimiento': 'fecha_nacimiento',
    'Afiliacion': 'afiliacion',
    'NivelRango': 'nivel_rango',
    'CONTRATO': 'contrato',
    'SEDE': 'sede'
})

# Conectar a la base de datos MySQL
try:
    connection = mysql.connector.connect(
        host='localhost',
        user='usuario',
        password='root',
        database='gestion_carteras'  # Nombre de tu base de datos
    )

    if connection.is_connected():
        print("Conexión a la base de datos exitosa.")

        # Insertar entidades
        entidad = df[['entidad', 'nit']].drop_duplicates().reset_index(drop=True)
        entidad['id'] = range(1, len(entidad) + 1)

        cursor = connection.cursor()
        for _, row in entidad.iterrows():
            cursor.execute(
                "INSERT INTO Entidad (id, nombre, nit) VALUES (%s, %s, %s)",
                (row['id'], row['entidad'], row['nit'])
            )
        connection.commit()

        print("Datos de entidades insertados correctamente.")

        # Insertar pacientes
        pacientes = df[['tipo_identificacion', 'identificacion', 'nombre_paciente', 
                        'fecha_nacimiento', 'afiliacion', 'nivel_rango']].drop_duplicates().reset_index(drop=True)
        pacientes['id'] = range(1, len(pacientes) + 1)

        for _, row in pacientes.iterrows():
            cursor.execute(
                "INSERT INTO Pacientes (id, tipo_identificacion, identificacion, nombre, fecha_nacimiento, afiliacion, nivel_rango) "
                "VALUES (%s, %s, %s, %s, %s, %s, %s)",
                (row['id'], row['tipo_identificacion'], row['identificacion'], row['nombre_paciente'],
                 row['fecha_nacimiento'], row['afiliacion'], row['nivel_rango'])
            )
        connection.commit()

        print("Datos de pacientes insertados correctamente.")

        # Insertar contratos
        contratos = df[['contrato', 'sede', 'entidad']].drop_duplicates().reset_index(drop=True)
        contratos['id'] = range(1, len(contratos) + 1)

        for _, row in contratos.iterrows():
            cursor.execute(
                "INSERT INTO Contratos (id, contrato, sede, entidad_id) "
                "VALUES (%s, %s, %s, %s)",
                (row['id'], row['contrato'], row['sede'], row['entidad'])
            )
        connection.commit()

        print("Datos de contratos insertados correctamente.")

        # Insertar facturas
        facturas = df[['numero_factura', 'entidad', 'nit', 'fecha_factura', 'fecha_ingreso', 'fecha_egreso',
                       'valor_total_factura', 'valor_copago', 'valor_total_cobrar', 'estado', 
                       'fecha_radicado', 'numero_radicado', 'contrato', 'sede']].drop_duplicates().reset_index(drop=True)
        for _, row in facturas.iterrows():
            cursor.execute(
                "INSERT INTO Facturas (numero_factura, entidad_id, paciente_id, fecha_factura, fecha_ingreso, fecha_egreso, "
                "valor_total_factura, valor_copago, valor_total_cobrar, estado, fecha_radicado, numero_radicado, contrato_id) "
                "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                (row['numero_factura'], row['entidad_id'], row['paciente_id'], row['fecha_factura'],
                 row['fecha_ingreso'], row['fecha_egreso'], row['valor_total_factura'], row['valor_copago'],
                 row['valor_total_cobrar'], row['estado'], row['fecha_radicado'], row['numero_radicado'],
                 row['contrato_id'])
            )
        connection.commit()

        print("Datos de facturas insertados correctamente.")

        cursor.close()

except Error as e:
    print("Error al conectar con MySQL", e)

finally:
    if connection.is_connected():
        connection.close()
        print("Conexión a la base de datos cerrada.")
    