from django.core.management.base import BaseCommand
from web.models import Hotel, Habitacion, Cliente, TipoEmpleado, Empleado, Pago, Reserva
from datetime import date

class Command(BaseCommand):
    help = "Poblar base de datos con datos de prueba"

    def handle(self, *args, **kwargs):
        # Hoteles
        hotel1 = Hotel.objects.create(nombre_hotel='Hotel Pacific Reef', direccion='Av. Providencia 1234, Santiago', categoria='5 estrellas')

        # Habitaciones
        hab1 = Habitacion.objects.create(hotel=hotel1, tipo_hab='Doble', capacidad=2, precio=75000, disponibilidad='S')
        hab2 = Habitacion.objects.create(hotel=hotel1, tipo_hab='Suite', capacidad=4, precio=150000, disponibilidad='S')

        # Clientes
        cliente1 = Cliente.objects.create(nombre='Carlos', apellido_p='Pérez', apellido_m='Gómez', correo='carlos.perez@gmail.com', telefono='+56911111111', direccion='Santiago')
        cliente2 = Cliente.objects.create(nombre='María', apellido_p='López', apellido_m='Fuentes', correo='maria.lopez@gmail.com', telefono='+56922222222', direccion='Valparaíso')

        # Tipos de Empleado
        tipo1 = TipoEmpleado.objects.create(descripcion='Recepcionista')
        tipo2 = TipoEmpleado.objects.create(descripcion='Mucama')

        # Empleados
        emp1 = Empleado.objects.create(nombre='Juan', apellido_p='Ramírez', apellido_m='Torres', hotel=hotel1, tipo_empleado=tipo1)
        emp2 = Empleado.objects.create(nombre='Ana', apellido_p='González', apellido_m='Vega', hotel=hotel1, tipo_empleado=tipo2)

        # Pagos
        pago1 = Pago.objects.create(tipo_pago='Tarjeta', estado_pago='Pagado', fecha_pago=date(2024,1,15), total_pago=150000)
        pago2 = Pago.objects.create(tipo_pago='Efectivo', estado_pago='Pendiente', fecha_pago=date(2024,1,16), total_pago=75000, abono=30000)

        # Reservas
        Reserva.objects.create(cliente=cliente1, habitacion=hab1, pago=pago2, empleado=emp1, fecha_entrada=date(2024,2,1), fecha_salida=date(2024,2,3), cantidad_personas=2)
        Reserva.objects.create(cliente=cliente2, habitacion=hab2, pago=pago1, empleado=emp2, fecha_entrada=date(2024,3,5), fecha_salida=date(2024,3,10), cantidad_personas=3)

        self.stdout.write(self.style.SUCCESS("Datos de prueba creados exitosamente"))