# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Boleta(models.Model):
    id_venta = models.OneToOneField('Venta', models.DO_NOTHING, db_column='id_venta', primary_key=True)
    nombre = models.CharField(max_length=100)
    forma_pago = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'boleta'


class Comprador(models.Model):
    id_comprador = models.CharField(primary_key=True, max_length=20)
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=50)
    telefono = models.IntegerField()
    correo = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'comprador'


class Contenedor(models.Model):
    id_contenedor = models.IntegerField(primary_key=True)
    tipo_contenedor = models.CharField(max_length=1)
    peso = models.IntegerField()
    estado_contenedor = models.CharField(max_length=1)
    precio = models.IntegerField()
    contenedor_lleno_id_cont = models.ForeignKey('ContenedorLleno', models.DO_NOTHING, db_column='contenedor_lleno_id_cont', blank=True,null=True)
    

    def __str__(self):
     fila = "ID :" + str(self.id_contenedor) + "Tipo Contenedor:" + self.tipo_contenedor +"Peso :" +str(self.peso) + "Estado Contenedor:" + str(self.estado_contenedor) + "Precio:" + str(self.precio) 
     return fila


    class Meta:
        managed = False
        db_table = 'contenedor'


    


class ContenedorLleno(models.Model):
    id_cont = models.IntegerField(primary_key=True)
    reservado = models.CharField(max_length=1)
    lleno = models.CharField(max_length=1)
    reserva_id_reserva = models.ForeignKey('Reserva', models.DO_NOTHING, db_column='reserva_id_reserva')

    class Meta:
        managed = False
        db_table = 'contenedor_lleno'


class DetaAsignacion(models.Model):
    receptor_rut_receptor = models.ForeignKey('Receptor', models.DO_NOTHING, db_column='receptor_rut_receptor')
    contenedor_id_contenedor = models.ForeignKey(Contenedor, models.DO_NOTHING, db_column='contenedor_id_contenedor')

    class Meta:
        managed = False
        db_table = 'deta_asignacion'


class DetalleConte(models.Model):
    informe_id_infome = models.ForeignKey('Informe', models.DO_NOTHING, db_column='informe_id_infome')
    contenedor_id_contenedor = models.ForeignKey(Contenedor, models.DO_NOTHING, db_column='contenedor_id_contenedor')

    class Meta:
        managed = False
        db_table = 'detalle_conte'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Empleado(models.Model):
    rut_empleado = models.CharField(primary_key=True, max_length=20)
    primer_nombre = models.CharField(max_length=20)
    segundo_nombre = models.CharField(max_length=20)
    primer_apellido = models.CharField(max_length=20)
    segundo_apellido = models.CharField(max_length=20)
    direccion = models.CharField(max_length=20)
    telefono = models.IntegerField()
    ocupacion = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'empleado'


class Factura(models.Model):
    id_venta = models.OneToOneField('Venta', models.DO_NOTHING, db_column='id_venta', primary_key=True)
    nombre_empresa = models.CharField(max_length=100)
    giro_industria = models.CharField(max_length=100)
    region = models.CharField(max_length=50)
    comuna = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'factura'


class Informe(models.Model):
    id_infome = models.IntegerField(primary_key=True)
    fecha_informe = models.DateField()
    empleado_rut_empleado = models.ForeignKey(Empleado, models.DO_NOTHING, db_column='empleado_rut_empleado')

    class Meta:
        managed = False
        db_table = 'informe'


class IngresoMaterial(models.Model):
    id_material = models.IntegerField(primary_key=True)
    tipo_producto = models.CharField(max_length=1)
    fecha = models.DateField()
    pesos_material = models.IntegerField()
    receptor_rut_receptor = models.ForeignKey('Receptor', models.DO_NOTHING, db_column='receptor_rut_receptor')
    contenedor_id_contenedor = models.ForeignKey(Contenedor, models.DO_NOTHING, db_column='contenedor_id_contenedor')

    class Meta:
        managed = False
        db_table = 'ingreso_material'


class Receptor(models.Model):
    rut_receptor = models.CharField(primary_key=True, max_length=20)
    primer_nombre = models.CharField(max_length=20)
    segundo_nombre = models.CharField(max_length=20)
    primer_apellido = models.CharField(max_length=20)
    segundo_apellido = models.CharField(max_length=20)
    turno = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'receptor'


class Reserva(models.Model):
    id_reserva = models.IntegerField(primary_key=True)
    fecha = models.DateField()
    fecha_limite = models.DateField()
    venta_id_venta = models.OneToOneField('Venta', models.DO_NOTHING, db_column='venta_id_venta')
    comprador_id_comprador = models.ForeignKey(Comprador, models.DO_NOTHING, db_column='comprador_id_comprador')

    class Meta:
        managed = False
        db_table = 'reserva'


class Retiro(models.Model):
    id_retiro = models.IntegerField(primary_key=True)
    primer_nombre = models.CharField(max_length=20)
    segundo_nombre = models.CharField(max_length=20)
    primer_apellido = models.CharField(max_length=20)
    segundo_apellido = models.CharField(max_length=20)
    fecha_retiro = models.DateField()
    contacto = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'retiro'


class Venta(models.Model):
    id_venta = models.IntegerField(primary_key=True)
    monto = models.IntegerField()
    forma_pago = models.CharField(max_length=10)
    fecha_venta = models.DateField()
    reserva_id_reserva = models.OneToOneField(Reserva, models.DO_NOTHING, db_column='reserva_id_reserva')
    retiro_id_retiro = models.ForeignKey(Retiro, models.DO_NOTHING, db_column='retiro_id_retiro')
    emitido_en = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'venta'