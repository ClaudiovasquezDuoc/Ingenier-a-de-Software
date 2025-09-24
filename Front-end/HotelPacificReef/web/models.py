from django.db import models

# -------------------
# Tabla Hotel
# -------------------
class Hotel(models.Model):
    nombre_hotel = models.CharField(max_length=100)
    direccion = models.CharField(max_length=150, blank=True, null=True)
    categoria = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.nombre_hotel

# -------------------
# Tabla Habitación
# -------------------
class Habitacion(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    tipo_hab = models.CharField(max_length=50, blank=True, null=True)
    capacidad = models.PositiveSmallIntegerField(blank=True, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    disponibilidad = models.CharField(max_length=1, blank=True, null=True)

    def __str__(self):
        return f"{self.tipo_hab} - {self.hotel.nombre_hotel}"

# -------------------
# Tabla Cliente
# -------------------
class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido_p = models.CharField(max_length=50)
    apellido_m = models.CharField(max_length=50, blank=True, null=True)
    correo = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20)
    direccion = models.CharField(max_length=150, blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido_p}"

# -------------------
# Tabla TipoEmpleado
# -------------------
class TipoEmpleado(models.Model):
    descripcion = models.CharField(max_length=100)

    def __str__(self):
        return self.descripcion

# -------------------
# Tabla Empleado
# -------------------
class Empleado(models.Model):
    nombre = models.CharField(max_length=50)
    apellido_p = models.CharField(max_length=50)
    apellido_m = models.CharField(max_length=50, blank=True, null=True)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    tipo_empleado = models.ForeignKey(TipoEmpleado, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre} {self.apellido_p}"

# -------------------
# Tabla Pago
# -------------------
class Pago(models.Model):
    tipo_pago = models.CharField(max_length=50)
    estado_pago = models.CharField(max_length=30)
    fecha_pago = models.DateField()
    total_pago = models.DecimalField(max_digits=10, decimal_places=2)
    abono = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return f"{self.tipo_pago} - {self.estado_pago}"

# -------------------
# Tabla Reserva
# -------------------
class Reserva(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    habitacion = models.ForeignKey(Habitacion, on_delete=models.CASCADE)
    pago = models.ForeignKey(Pago, on_delete=models.SET_NULL, blank=True, null=True)
    empleado = models.ForeignKey(Empleado, on_delete=models.SET_NULL, blank=True, null=True)
    fecha_entrada = models.DateField()
    fecha_salida = models.DateField()
    cantidad_personas = models.PositiveSmallIntegerField()

    def __str__(self):
        return f"Reserva {self.id} - {self.cliente.nombre}"