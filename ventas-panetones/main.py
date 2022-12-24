from persona import Persona
from producto import Producto
from factura import Factura
from factura_detalle import FacturaDetalle
from contador import Contador
personas: Persona = []
productos: Producto = []
facturas: Factura = []


def crear_persona():
    dni: str = str(input("Ingrese DNI: "))
    nombres: str = str(input("Ingrese Nombres: "))
    apellidos: str = str(input("Ingrese Apellidos: "))
    direccion: str = str(input("Ingrese Direccion: "))
    telefono: str = str(input("Ingrese Telefono: "))
    persona: Persona = Persona(dni, nombres, apellidos, direccion, telefono)
    personas.append(persona)


lista_personas:list=[{"dni":"47259697","nombres":"roy","apellidos":"Tipo Mamani","direccion":"UPeU","telefono":"997124032"},
                     {"dni":"47259698","nombres":"juan","apellidos":" Mamani","direccion":"UPeU","telefono":"997124032"},
                     {"dni":"47259699","nombres":"pedro","apellidos":"Tipo","direccion":"UPeU","telefono":"997124032"},
                     {"dni":"47259610","nombres":"jose","apellidos":"Ayamamani","direccion":"UPeU","telefono":"997124032"},
                     {"dni":"71128207","nombres":"max","apellidos":"Ito Apaza","direccion":"UPeU","telefono":"928817188"}]

lista_productos:list=[{"codigo":"01","nombre":"paneton","precio":10.20,"marca":"pan con pasas"},
                      {"codigo":"02","nombre":"paneton","precio":10.00,"marca":"bells"},
                      {"codigo":"03","nombre":"Paneton","precio":25.00,"marca":"donofrio"},
                      {"codigo":"04","nombre":"paneton","precio":25.50,"marca":"todino"},
                      {"codigo":"05","nombre":"paneton","precio":30.50,"marca":"union"},
                      {"codigo":"06","nombre":"paneton","precio":30.50,"marca":"putina"},
                      {"codigo":"07","nombre":"paneton","precio":180.50,"marca":"gloria"}]


def cargar_datos():
    for persona in lista_personas:
        persona:Persona=Persona(persona["dni"],persona["nombres"],persona["apellidos"],persona["direccion"],persona["telefono"])
        personas.append(persona)
    for producto in lista_productos:
        producto:Producto=Producto(producto["codigo"],producto["nombre"],producto["precio"],producto["marca"])
        productos.append(producto)

def listar_personas():
    i = 0
    while i < len(personas):
        Persona.convertir_a_string(personas[i])
        i = i + 1


def buscar_persona():
    dni: str = str(input("Ingrese DNI para buscar: "))
    for persona in personas:
        if persona.dni == dni:
            Persona.convertir_a_string(persona)
            return persona


def editar_persona():
    dni: str = str(input("Ingrese DNI para Editar: "))
    for persona in personas:
        if persona.dni == dni:
            persona.nombres = str(input("Ingrese un nuevo nombre: "))


def eliminar_persona():
    dni: str = str(input("Ingrese DNI para Eliminar: "))
    for index, persona in enumerate(personas):
        if persona.dni == dni:
            personas.pop(index)


def crear_producto():
    codigo: str = str(input("Ingtrese Codigo Del Producto: "))
    nombre: str = str(input("Ingtrese Nombre Del Producto: "))
    precio: float = float(input("Ingtrese Precio Del Producto: "))
    marca: str = str(input("Ingtrese Marca Del Producto: "))
    producto: Producto = Producto(codigo, nombre, precio, marca)
    productos.append(producto)


def listar_productos():
    i = 0
    while i < len(productos):
        Producto.convertir_a_string(productos[i])
        i +=1


def buscar_producto():
    codigo: str = str(input("Ingtrese Codigo para buscar  Producto: "))
    for producto in productos:
        if producto.codigo == codigo:
            Producto.convertir_a_string(producto)
            return producto


def editar_producto():
    codigo: str = str(input("Ingtrese Codigo para editar  Producto: "))
    for producto in productos:
        if producto.codigo == codigo:
            Producto.convertir_a_string(producto)
            nombre: str = str(input("Ingrese Nuevo nombre de producto: "))
            producto.nombre = nombre
            Producto.convertir_a_string(producto)


def eliminar_producto():
    codigo: str = str(input("Ingtrese Codigo para eliminar  Producto: "))
    for index, producto in enumerate(productos):
        if producto.codigo == codigo:
            Producto.convertir_a_string(producto)
            productos.pop(index)


def crear_factura():
    print("Para crear la factura debe buscar un cliente")
    cliente: Persona = buscar_persona()
    factura: factura = Factura(len(facturas)+1, cliente)
    factura.convertir_a_string()
    contuar: bool = True
    while contuar:
        producto: Producto = buscar_producto()
        cantidad: float = float(input("Ingrese la cantidad del producto: "))
        factura.detalle.append(FacturaDetalle(
            producto.codigo, producto.nombre, cantidad, producto.precio))
        condicion: str = str(input("Escriba SI para seguir agregando producto: "))
        if condicion == "SI":
            contuar = True
        else:
            contuar = False
            factura.calcular_totales()
            facturas.append(factura)


def listar_facturas():
    print("| SERIE | NUMERO | DNI CLIENTE | NOMBRE CLIENTE | BASE IMPONIBLE | IGV   | TOTAL |")
    for factura in facturas:
        Factura.convertir_a_string(factura)


def buscar_factura():
    numero: int = int(input("Ingrese numero de factura para buscar: "))
    for factura in facturas:
        if factura.numero == numero:
            Factura.convertir_a_string(factura)
            print("**************************")
            print("| CODIGO | PRODUCTO | CANTIDAD |BASE-IMPONIBLE | IGV   | TOTAL |")
            for detalle in factura.detalle:
                FacturaDetalle.convertir_a_string(detalle)


def main():
    """from reportlab.lib.pagesizes import letter
    from reportlab.pdfgen import canvas

    canvas = canvas.Canvas("form.pdf", pagesize=letter)
    canvas.setLineWidth(.3)
    canvas.setFont('Helvetica', 12)

    canvas.drawString(30,750,'OFFICIAL COMMUNIQUE')
    canvas.drawString(30,735,'OF ACME INDUSTRIES')
    canvas.drawString(500,750,"12/12/2010")
    canvas.line(480,747,580,747)

    canvas.drawString(275,725,'AMOUNT OWED:')
    canvas.drawString(500,725,"$1,000.00")
    canvas.line(378,723,580,723)

    canvas.drawString(30,703,'RECEIVED BY:')
    canvas.line(120,700,580,700)
    canvas.drawString(120,703,"JOHN DOE")

    canvas.save()"""
    continuar: bool = True
    while continuar:

        print("*****************************************")
        print("*********** LA DOÑA MAX *************")
        print("         ESTA A TU DISPOCION           ")
        print("===================MENÚ==================")
        print("**************INGRESE OPCIONES***********")
        print("       1: PARA AGREGAR PERSONA")
        print("       2: PARA LISTAR PERSONAS")
        print("       3: PARA BUSCAR PERSONA")
        print("       4: PARA EDITAR PERSONA")
        print("       5: PARA ELIMINAR PERSONA")

        print("       6: PARA AGREGAR PRODUCTO")
        print("       7: PARA LISTAR PRODUCTOS")
        print("       8: PARA BUSCAR PRODUCTO")
        print("       9: PARA EDITAR PRODUCTO")
        print("       10: PARA ELIMINAR PRODUCTO")

        print("       15: PARA GENERAR FACTURA")
        print("       16: PARA LISTAR FACTURA")
        print("       17: PARA BUSCAR FACTURA")
        print("       20: PARA SALIR")
        caso: str = str(input("INGRESE OPCIÓN: "))
        match caso:
            case "1":
                crear_persona()
            case "2":
                listar_personas()
            case "3":
                buscar_persona()
            case "4":
                editar_persona()
            case "5":
                eliminar_persona()

            case "6":
                crear_producto()
            case "7":
                listar_productos()
            case "8":
                buscar_producto()
            case "9":
                editar_producto()
            case "10":
                eliminar_producto()
            case "15":
                crear_factura()
            case "16":
                listar_facturas()
            case "17":
                buscar_factura()
            case "20":
                continuar = False


if __name__ == '__main__':
    main()
