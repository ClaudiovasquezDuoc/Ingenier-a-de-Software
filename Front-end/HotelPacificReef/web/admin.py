from django.contrib import admin
from .models import Hotel, Habitacion, Cliente, TipoEmpleado, Empleado, Pago, Reserva

admin.site.register(Hotel)
admin.site.register(Habitacion)
admin.site.register(Cliente)
admin.site.register(TipoEmpleado)
admin.site.register(Empleado)
admin.site.register(Pago)
admin.site.register(Reserva)