# Generated by Django 4.0.5 on 2023-02-27 17:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cobro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Ahorro', models.IntegerField()),
                ('Cliente', models.CharField(max_length=120)),
                ('Fecha', models.DateField()),
                ('Intereses', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Compras',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Cliente', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Detalle_Factura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_producto', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Detalle_producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Marca', models.CharField(max_length=70)),
                ('Modelo', models.CharField(max_length=90)),
                ('Nombre_producto', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Comercial', models.CharField(max_length=110)),
                ('Razon_zocial', models.CharField(max_length=250)),
                ('Ruc', models.CharField(max_length=13)),
                ('Estado', models.IntegerField()),
                ('Contabilidad', models.BooleanField(verbose_name=1)),
            ],
        ),
        migrations.CreateModel(
            name='Grupo_clientes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=40)),
                ('Descripcion', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Grupo_producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_producto', models.CharField(max_length=80)),
                ('id_proveedor', models.CharField(max_length=90)),
                ('Nombre', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(max_length=20)),
                ('contrase??a', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Permisos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Descripcion', models.CharField(max_length=10)),
                ('Estado', models.IntegerField()),
                ('Fecha', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Proforma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Dias_emision', models.DateField()),
                ('Dias_vencimiento', models.DateField()),
                ('Total_neto', models.IntegerField()),
                ('id_cliente', models.IntegerField()),
                ('id_grupo_de_cliente', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Promociones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=40)),
                ('Descripcion', models.CharField(max_length=120)),
                ('Fecha_de_nacimiento', models.DateField()),
                ('Fecha_de_fin', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Proveedores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('proveedor', models.CharField(max_length=200)),
                ('Compa??ia', models.CharField(max_length=200)),
                ('Direccion', models.CharField(max_length=500)),
                ('Telefono', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Descripcion', models.CharField(max_length=10)),
                ('Estado', models.IntegerField()),
                ('Fecha', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Trabajador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ci', models.CharField(max_length=10)),
                ('Nombre', models.CharField(max_length=50)),
                ('Apelllido', models.CharField(max_length=50)),
                ('F_Nacimiento', models.DateField()),
                ('Email', models.EmailField(max_length=254)),
                ('Estado', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('Descuento', models.IntegerField()),
                ('Impuesto', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Ventas_proformas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_ventas', models.IntegerField()),
                ('id_proforma', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Usuario', models.CharField(max_length=10)),
                ('Clave', models.CharField(max_length=30)),
                ('imagen', models.ImageField(upload_to='')),
                ('Estado', models.IntegerField()),
                ('id_Rol', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.rol')),
                ('id_Trabajador', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.trabajador')),
            ],
        ),
        migrations.CreateModel(
            name='Sucursales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sucursal', models.CharField(max_length=3)),
                ('Nombre', models.CharField(max_length=100)),
                ('Direccion', models.CharField(max_length=200)),
                ('Estado', models.IntegerField()),
                ('id_empresa', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.empresa')),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Stock', models.CharField(max_length=10)),
                ('Precio_unitario', models.IntegerField()),
                ('Descripcion', models.CharField(max_length=100)),
                ('id_proveedor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.proveedores')),
            ],
        ),
        migrations.CreateModel(
            name='Permiso_Sucursales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_permiso', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.permisos')),
                ('id_usuario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Inventario',
            fields=[
                ('id_articulo', models.CharField(max_length=10, primary_key=30, serialize=False)),
                ('Movimiento', models.IntegerField()),
                ('Cantidad', models.BooleanField(max_length=100)),
                ('Valor', models.BooleanField()),
                ('Fecha', models.DateTimeField()),
                ('Stock', models.BooleanField()),
                ('Costo', models.BooleanField()),
                ('Descripcion', models.CharField(max_length=250)),
                ('id_movimiento', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.detalle_factura')),
                ('id_surcursal', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.proveedores')),
                ('id_usuario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Elin_venta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_cliente', models.CharField(max_length=80)),
                ('Usuario', models.CharField(max_length=90)),
                ('Monto', models.IntegerField()),
                ('Fecha', models.DateField()),
                ('id_venta', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.venta')),
            ],
        ),
        migrations.CreateModel(
            name='Elim_comra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Num_factura', models.CharField(max_length=300)),
                ('Nombre_factura', models.CharField(max_length=10)),
                ('id_cliente', models.IntegerField()),
                ('id_compra', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.compras')),
            ],
        ),
        migrations.AddField(
            model_name='detalle_factura',
            name='id_compras',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.proveedores'),
        ),
        migrations.AddField(
            model_name='compras',
            name='id_proveedor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.proveedores'),
        ),
        migrations.AddField(
            model_name='compras',
            name='id_trabajador',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.trabajador'),
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.IntegerField()),
                ('Direcion', models.CharField(max_length=3)),
                ('Telefono', models.CharField(max_length=100)),
                ('Correo', models.CharField(max_length=200)),
                ('Fecha_de_registro', models.IntegerField()),
                ('Estado', models.IntegerField()),
                ('Apellido', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.empresa')),
            ],
        ),
        migrations.CreateModel(
            name='Amortizacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Estado', models.CharField(max_length=10)),
                ('Valor', models.IntegerField()),
                ('Cuota', models.CharField(max_length=100)),
                ('Saldo', models.CharField(max_length=50)),
                ('Fecha', models.CharField(max_length=50)),
                ('Vencimiento', models.CharField(max_length=40)),
                ('Ventas', models.CharField(max_length=200)),
                ('n_cuenta', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.proveedores')),
            ],
        ),
    ]
