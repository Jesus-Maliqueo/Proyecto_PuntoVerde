# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AdminInterfaceTheme(models.Model):
    name = models.CharField(unique=True, max_length=50)
    active = models.IntegerField()
    title = models.CharField(max_length=50)
    title_visible = models.IntegerField()
    logo = models.CharField(max_length=100)
    logo_visible = models.IntegerField()
    css_header_background_color = models.CharField(max_length=10)
    title_color = models.CharField(max_length=10)
    css_header_text_color = models.CharField(max_length=10)
    css_header_link_color = models.CharField(max_length=10)
    css_header_link_hover_color = models.CharField(max_length=10)
    css_module_background_color = models.CharField(max_length=10)
    css_module_text_color = models.CharField(max_length=10)
    css_module_link_color = models.CharField(max_length=10)
    css_module_link_hover_color = models.CharField(max_length=10)
    css_module_rounded_corners = models.IntegerField()
    css_generic_link_color = models.CharField(max_length=10)
    css_generic_link_hover_color = models.CharField(max_length=10)
    css_save_button_background_color = models.CharField(max_length=10)
    css_save_button_background_hover_color = models.CharField(max_length=10)
    css_save_button_text_color = models.CharField(max_length=10)
    css_delete_button_background_color = models.CharField(max_length=10)
    css_delete_button_background_hover_color = models.CharField(max_length=10)
    css_delete_button_text_color = models.CharField(max_length=10)
    list_filter_dropdown = models.IntegerField()
    related_modal_active = models.IntegerField()
    related_modal_background_color = models.CharField(max_length=10)
    related_modal_rounded_corners = models.IntegerField()
    logo_color = models.CharField(max_length=10)
    recent_actions_visible = models.IntegerField()
    favicon = models.CharField(max_length=100)
    related_modal_background_opacity = models.CharField(max_length=5)
    env_name = models.CharField(max_length=50)
    env_visible_in_header = models.IntegerField()
    env_color = models.CharField(max_length=10)
    env_visible_in_favicon = models.IntegerField()
    related_modal_close_button_visible = models.IntegerField()
    language_chooser_active = models.IntegerField()
    language_chooser_display = models.CharField(max_length=10)
    list_filter_sticky = models.IntegerField()
    form_pagination_sticky = models.IntegerField()
    form_submit_sticky = models.IntegerField()
    css_module_background_selected_color = models.CharField(max_length=10)
    css_module_link_selected_color = models.CharField(max_length=10)
    logo_max_height = models.PositiveSmallIntegerField()
    logo_max_width = models.PositiveSmallIntegerField()
    foldable_apps = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'admin_interface_theme'


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
    id_venta = models.OneToOneField('Compra', models.DO_NOTHING, db_column='id_venta', primary_key=True)
    nombre = models.CharField(max_length=100)
    forma_pago = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'boleta'


class Compra(models.Model):
    id_venta = models.IntegerField(primary_key=True)
    monto = models.IntegerField()
    forma_pago = models.CharField(max_length=10)
    fecha_venta = models.DateField()
    reserva_id_reserva = models.OneToOneField('Reserva', models.DO_NOTHING, db_column='reserva_id_reserva')
    retiro_id_retiro = models.ForeignKey('Retiro', models.DO_NOTHING, db_column='retiro_id_retiro')
    emitido_en = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'compra'


class Comprador(models.Model):
    id_comprador = models.CharField(primary_key=True, max_length=20)
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=50)
    telefono = models.IntegerField()
    correo = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'comprador'


class ContenedorLleno(models.Model):
    id_lleno = models.IntegerField(primary_key=True)
    reservado = models.CharField(max_length=1)
    lleno = models.CharField(max_length=1)
    reserva_id_reserva = models.ForeignKey('Reserva', models.DO_NOTHING, db_column='reserva_id_reserva', blank=True, null=True)
    llen_conts_id_llenado = models.OneToOneField('LlenadoContenedores', models.DO_NOTHING, db_column='llen_conts_id_llenado')
    precios_id_precio = models.ForeignKey('Precios', models.DO_NOTHING, db_column='precios_id_precio')

    class Meta:
        managed = False
        db_table = 'contenedor_lleno'


class DetaAsignacion(models.Model):
    contenedor_id_contenedor = models.ForeignKey('LlenadoContenedores', models.DO_NOTHING, db_column='contenedor_id_contenedor')
    receptor_rut_receptor = models.ForeignKey('Receptor', models.DO_NOTHING, db_column='receptor_rut_receptor')

    class Meta:
        managed = False
        db_table = 'deta_asignacion'


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
    id_venta = models.OneToOneField(Compra, models.DO_NOTHING, db_column='id_venta', primary_key=True)
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
    id_contenedor = models.IntegerField()
    invent_conts_id_contenedor = models.OneToOneField('InventarioContenedores', models.DO_NOTHING, db_column='invent_conts_id_contenedor')

    class Meta:
        managed = False
        db_table = 'informe'


class IngresoMaterial(models.Model):
    id_material = models.IntegerField(primary_key=True)
    tipo_producto = models.CharField(max_length=1)
    fecha = models.DateTimeField()
    pesos_material = models.IntegerField()
    llen_conts_id_llenado = models.OneToOneField('LlenadoContenedores', models.DO_NOTHING, db_column='llen_conts_id_llenado', blank=True, null=True)

    def __str__(self):
      fila1 = "ID :" + str(self.id_material) + "Tipo Producto: :" + "Peso Material:" + str(self.pesos_material)  + self.tipo_producto +"Fecha :" +str(self.fecha)
      return fila1

    class Meta:
        managed = False
        db_table = 'ingreso_material'


class InventarioContenedores(models.Model):
    id_contenedor = models.IntegerField(primary_key=True)
    tipo_contenedor = models.CharField(max_length=1)
    peso = models.IntegerField()
    id_llenado = models.IntegerField()

    def __str__(self):
      fila = "ID :" + str(self.id_contenedor) +"Tipo Contenedor:" + str(self.tipo_contenedor)   +"Peso :" +str(self.peso) +"Llenado :" +str(self.id_llenado)
      return fila

    class Meta:
        managed = False
        db_table = 'inventario_contenedores'


class LlenadoContenedores(models.Model):
    id_llenado = models.IntegerField(primary_key=True)
    tipo_contenedor = models.CharField(max_length=1)
    peso = models.IntegerField()
    estado_contenedor = models.CharField(max_length=10)
    precio = models.IntegerField()
    invt_conts_id_contenedor = models.OneToOneField(InventarioContenedores, models.DO_NOTHING, db_column='invt_conts_id_contenedor')
    ingreso_material_id_material = models.OneToOneField(IngresoMaterial, models.DO_NOTHING, db_column='ingreso_material_id_material', blank=True, null=True)

    def __str__(self):
       fila = "ID :" + str(self.id_llenado) + "Tipo Contenedor:" + self.tipo_contenedor +"Peso :" +str(self.peso) + "Estado Contenedor:" + str(self.estado_contenedor) + "Precio:" + str(self.precio) 
       return fila

    class Meta:
        managed = False
        db_table = 'llenado_contenedores'


class Precios(models.Model):
    id_precio = models.IntegerField(primary_key=True)
    tipo_material = models.CharField(max_length=1)
    descripcion = models.CharField(max_length=20)
    precio = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'precios'


class Receptor(models.Model):
    rut_receptor = models.CharField(primary_key=True, max_length=20)
    primer_nombre = models.CharField(max_length=20)
    segundo_nombre = models.CharField(max_length=20)
    primer_apellido = models.CharField(max_length=20)
    segundo_apellido = models.CharField(max_length=20)
    turno = models.DateTimeField()
    ingreso_material_id_material = models.OneToOneField(IngresoMaterial, models.DO_NOTHING, db_column='ingreso_material_id_material')

    class Meta:
        managed = False
        db_table = 'receptor'


class Reserva(models.Model):
    id_reserva = models.IntegerField(primary_key=True)
    fecha = models.DateField()
    fecha_limite = models.DateField()
    venta_id_venta = models.OneToOneField(Compra, models.DO_NOTHING, db_column='venta_id_venta')
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