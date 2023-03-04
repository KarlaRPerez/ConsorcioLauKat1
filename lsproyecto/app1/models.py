from django.db import models

# Create your models here.
class Empresa (models.Model):
    Comercial =models.CharField(max_length=110)
    Razon_zocial=models.CharField(max_length=250)
    Ruc = models.CharField(max_length=13)
    Estado= models.IntegerField ()
    Contabilidad=models.BooleanField(1)
    
class Sucursales (models.Model):
    id_empresa=models.ForeignKey(Empresa,null=True,on_delete=models.CASCADE)
    sucursal=models.CharField(max_length=3)
    Nombre = models.CharField(max_length=100)
    Direccion=models.CharField(max_length=200)
    Estado=models.IntegerField()

class Trabajador (models.Model):
    ci=models.CharField(max_length=10)
    Nombre =models.CharField(max_length=50)
    Apelllido=models.CharField(max_length=50)
    F_Nacimiento=models.DateField()
    Email=models.EmailField()
    Estado=models.IntegerField()   
 
    
class Rol (models.Model):
    Descripcion =models.CharField(max_length=10)
    Estado=models.IntegerField()
    Fecha = models.TimeField()
 
class Permisos (models.Model):
    Descripcion =models.CharField(max_length=10)
    Estado=models.IntegerField()
    Fecha = models.TimeField()

class Usuario (models.Model):
    id_Trabajador=models.ForeignKey(Trabajador,null=True,on_delete=models.CASCADE) 
    Usuario =models.CharField(max_length=10)
    Clave =models.CharField(max_length=30)
    imagen=models.ImageField()
    Estado = models.IntegerField()
    id_Rol=models.ForeignKey(Rol,null=True,on_delete=models.CASCADE)
    
class Permiso_Sucursales(models.Model):
      id_Sucursales=models.F
      id_usuario=models.ForeignKey(Usuario,null=True,on_delete=models.CASCADE)
      id_permiso=models.ForeignKey(Permisos,null=True,on_delete=models.CASCADE)
      
class Proveedores (models.Model):
      proveedor =models.CharField(max_length=200)
      Compañia=models.CharField(max_length=200)
      Direccion=models.CharField(max_length=500)
      Telefono = models.CharField(max_length=200)
      
class Compras (models.Model):
    Cliente =models.CharField(max_length=10)
    id_trabajador=models.ForeignKey(Trabajador,null=True,on_delete=models.CASCADE)
    id_proveedor= models.ForeignKey(Proveedores,null=True,on_delete=models.CASCADE)
          
class Elim_comra (models.Model):
    Num_factura=models.CharField (max_length=300)
    Nombre_factura=models.CharField(max_length=10)
    id_cliente = models.IntegerField()  
    id_compra=models.ForeignKey(Compras,null=True,on_delete=models.CASCADE)

class Producto (models.Model):
    id_proveedor=models.ForeignKey(Proveedores,null=True,on_delete=models.CASCADE)
    Stock=models.CharField(max_length=10)
    Precio_unitario= models.IntegerField()  
    Descripcion=models.CharField(max_length=100)
    
class Detalle_Factura (models.Model):
    id_compras=models.ForeignKey(Proveedores,null=True,on_delete=models.CASCADE)
    id_producto=models.CharField(max_length=10)
    
class Proforma (models.Model):
    Dias_emision=models.DateField()
    Dias_vencimiento=models.DateField()
    Estado:models.IntegerField()
    Total_neto=models.IntegerField()
    id_cliente=models.IntegerField()
    id_grupo_de_cliente=models.IntegerField()
    
class Inventario (models.Model):
    id_surcursal=models.ForeignKey(Proveedores,null=True,on_delete=models.CASCADE)
    id_articulo=models.CharField(primary_key=30,max_length=10)
    Movimiento= models.IntegerField()  
    Cantidad=models.BooleanField(max_length=100)
    Valor=models.BooleanField()
    Fecha=models.DateTimeField()
    id_usuario=models.ForeignKey(Usuario,null=True,on_delete=models.CASCADE)
    Stock=models.BooleanField()
    Costo=models.BooleanField()
    id_movimiento=models.ForeignKey(Detalle_Factura,null=True,on_delete=models.CASCADE)
    Descripcion=models.CharField(max_length=250)

class Ventas_proformas (models.Model):
    id_ventas=models.IntegerField()
    id_proforma=models.IntegerField()
 
class Promociones (models.Model):
    Nombre=models.CharField(max_length=40)
    Descripcion=models.CharField(max_length=120)
    Fecha_de_nacimiento= models.DateField()  
    Fecha_de_fin=models.DateField()
    
class Grupo_clientes (models.Model):
    Nombre=models.CharField(max_length=40)
    Descripcion=models.CharField(max_length=120)
    
class Venta (models.Model):
    fecha=models.DateField()
    Descuento=models.IntegerField()
    Impuesto= models.FloatField()  

class Elin_venta (models.Model):
    id_cliente=models.CharField(max_length=80)
    Usuario=models.CharField(max_length=90)
    Monto= models.IntegerField()  
    Fecha=models.DateField()
    id_venta=models.ForeignKey(Venta,null=True,on_delete=models.CASCADE)
    
class Amortizacion (models.Model):
    n_cuenta=models.ForeignKey(Proveedores,null=True,on_delete=models.CASCADE)
    Estado=models.CharField(max_length=10)
    Valor= models.IntegerField()  
    Cuota=models.CharField(max_length=100)
    Saldo=models.CharField(max_length=50)
    Fecha=models.CharField(max_length=50)
    Vencimiento=models.CharField(max_length=40)
    Ventas=models.CharField(max_length=200)
    
class Cobro (models.Model):
    Ahorro=models.IntegerField()
    Cliente=models.CharField(max_length=120)
    Fecha= models.DateField()  
    Intereses=models.FloatField()
    
class Detalle_producto (models.Model):
    Marca=models.CharField(max_length=70)
    Modelo=models.CharField(max_length=90)
    Nombre_producto= models.CharField(max_length=80)  
    
class Grupo_producto (models.Model):
    id_producto=models.CharField(max_length=80)
    id_proveedor=models.CharField(max_length=90)
    Nombre= models.CharField(max_length=80)  
  
class Cliente (models.Model):
    Nombre=models.IntegerField()
    Apellido=models.ForeignKey(Empresa,null=True,on_delete=models.CASCADE)
    Direcion=models.CharField(max_length=3)
    Telefono= models.CharField(max_length=100)
    Correo=models.CharField(max_length=200)
    Fecha_de_registro=models.IntegerField()
    Estado=models.IntegerField()

class Login (models.Model):
    usuario=models.CharField(max_length=20)
    contraseña=models.CharField(max_length=20)
    
class Registro (models.Model):
   Nombre =models.CharField(max_length=30)
   Correo=models.EmailField(max_length=50)
   Usuari=models.ForeignKey(Login,null=True,on_delete=models.CASCADE)
   #Contraseñ=models.ForeignKey(Login,null=True,on_delete=models.CASCADE)
   
class Rol_Usuario (models.Model):
    id_rol=models.ForeignKey(Rol,null=True,on_delete=models.CASCADE)
    id_usuario=models.ForeignKey(Usuario,null=True,on_delete=models.CASCADE)