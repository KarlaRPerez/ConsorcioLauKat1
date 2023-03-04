from django.contrib import admin

# Register your models here.

from app1.models import Rol
from app1.models import Trabajador
from app1.models import Usuario
from app1.models import Permisos
from app1.models import Empresa
from app1.models import Permiso_Sucursales
from app1.models import Cliente
from app1.models import Promociones
from app1.models import Detalle_producto
from app1.models import Proveedores
from app1.models import Compras
from app1.models import Producto
from app1.models import Detalle_Factura
from app1.models import Proforma
from app1.models import Inventario
from app1.models import Cobro
from app1.models import Amortizacion
from app1.models import Venta
from app1.models import Elin_venta
from app1.models import Elim_comra
from app1.models import Grupo_clientes
from app1.models import Ventas_proformas
from app1.models import Grupo_producto
from app1.models import Sucursales
from app1.models import Login
from app1.models import Registro
from app1.models import Rol_Usuario


admin.site.register(Rol)
admin.site.register(Trabajador)
admin.site.register(Usuario)
admin.site.register(Permisos)
admin.site.register(Empresa)
admin.site.register(Permiso_Sucursales)
admin.site.register(Cliente)
admin.site.register(Promociones)
admin.site.register(Detalle_producto)
admin.site.register(Proveedores)
admin.site.register(Compras)
admin.site.register(Producto)
admin.site.register(Detalle_Factura)
admin.site.register(Proforma)
admin.site.register(Inventario)
admin.site.register(Cobro)
admin.site.register(Amortizacion)
admin.site.register(Venta)
admin.site.register(Elin_venta)
admin.site.register(Elim_comra)
admin.site.register(Grupo_clientes)
admin.site.register(Ventas_proformas)
admin.site.register(Grupo_producto)
admin.site.register(Sucursales)
admin.site.register(Login)
admin.site.register(Registro)
admin.site.register(Rol_Usuario)