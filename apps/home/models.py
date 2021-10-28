# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Carreras(models.Model):
    codigo_carrera = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=255)
    mostrar_correlativas = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'carreras'


class Categorias(models.Model):
    codigo_categoria = models.AutoField(primary_key=True)
    nombre = models.CharField(unique=True, max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'categorias'


class Competencias(models.Model):
    codigo_competencia = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=100)
    codigo_carrera = models.ForeignKey('Planes', models.DO_NOTHING, db_column='codigo_carrera', blank=True, null=True)
    codigo_plan = models.CharField(max_length=6, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'competencias'


class Correlativas(models.Model):
    codigo_materiaxorientacion = models.OneToOneField('Materiasxorientaciones', models.DO_NOTHING, db_column='codigo_materiaxorientacion', primary_key=True)
    codigo_correlativa = models.ForeignKey('Materias', models.DO_NOTHING, db_column='codigo_correlativa')
    condicion = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'correlativas'
        unique_together = (('codigo_materiaxorientacion', 'codigo_correlativa'),)


class Correlativasxcantidad(models.Model):
    codigo_correlativaxcantidad = models.AutoField(primary_key=True)
    codigo_materiaxorientacion = models.ForeignKey('Materiasxorientaciones', models.DO_NOTHING, db_column='codigo_materiaxorientacion')
    codigo_categoria = models.ForeignKey(Categorias, models.DO_NOTHING, db_column='codigo_categoria', blank=True, null=True)
    condicion = models.IntegerField()
    cantidad = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'correlativasxcantidad'


class Correlativasxcompetencia(models.Model):
    codigo_materiaxorientacion = models.OneToOneField('Materiasxorientaciones', models.DO_NOTHING, db_column='codigo_materiaxorientacion', primary_key=True)
    codigo_competencia = models.ForeignKey(Competencias, models.DO_NOTHING, db_column='codigo_competencia')

    class Meta:
        managed = False
        db_table = 'correlativasxcompetencia'
        unique_together = (('codigo_materiaxorientacion', 'codigo_competencia'),)


class Correlativasxtitulo(models.Model):
    codigo_materiaxorientacion = models.OneToOneField('Materiasxorientaciones', models.DO_NOTHING, db_column='codigo_materiaxorientacion', primary_key=True)
    codigo_titulo = models.ForeignKey('Titulos', models.DO_NOTHING, db_column='codigo_titulo')

    class Meta:
        managed = False
        db_table = 'correlativasxtitulo'
        unique_together = (('codigo_materiaxorientacion', 'codigo_titulo'),)


class LogSimulacion(models.Model):
    ts = models.DateTimeField(blank=True, null=True)
    ip = models.CharField(max_length=39)
    session = models.BigIntegerField()
    carrera = models.SmallIntegerField()
    plan = models.CharField(max_length=5)
    orientacion = models.SmallIntegerField()
    ultimo_cuatrimestre_cursado = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'log_simulacion'


class Materias(models.Model):
    codigo_materia = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=255)
    carga_semanal = models.IntegerField(blank=True, null=True)
    carga_total = models.IntegerField(blank=True, null=True)
    anual = models.BooleanField(blank=True, null=True)
    abreviatura = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'materias'


class Materiasxcategorias(models.Model):
    codigo_materiaxorientacion = models.OneToOneField('Materiasxorientaciones', models.DO_NOTHING, db_column='codigo_materiaxorientacion', primary_key=True)
    codigo_categoria = models.ForeignKey(Categorias, models.DO_NOTHING, db_column='codigo_categoria')

    class Meta:
        managed = False
        db_table = 'materiasxcategorias'
        unique_together = (('codigo_materiaxorientacion', 'codigo_categoria'),)


class Materiasxcompetencia(models.Model):
    codigo_competencia = models.OneToOneField(Competencias, models.DO_NOTHING, db_column='codigo_competencia', primary_key=True)
    codigo_materia = models.ForeignKey(Materias, models.DO_NOTHING, db_column='codigo_materia')

    class Meta:
        managed = False
        db_table = 'materiasxcompetencia'
        unique_together = (('codigo_competencia', 'codigo_materia'),)


class Materiasxorientaciones(models.Model):
    codigo_materiaxorientacion = models.AutoField(primary_key=True)
    codigo_materia = models.ForeignKey(Materias, models.DO_NOTHING, db_column='codigo_materia')
    codigo_carrera = models.ForeignKey('Planes', models.DO_NOTHING, db_column='codigo_carrera')
    codigo_plan = models.CharField(max_length=6)
    codigo_orientacion = models.IntegerField(blank=True, null=True)
    dictado = models.IntegerField(blank=True, null=True)
    cuatrimestre = models.IntegerField(blank=True, null=True)
    contracursada = models.BooleanField(blank=True, null=True)
    excep_contrac = models.CharField(max_length=7, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'materiasxorientaciones'


class Materiasxtitulo(models.Model):
    codigo_titulo = models.OneToOneField('Titulos', models.DO_NOTHING, db_column='codigo_titulo', primary_key=True)
    codigo_materia = models.ForeignKey(Materias, models.DO_NOTHING, db_column='codigo_materia')

    class Meta:
        managed = False
        db_table = 'materiasxtitulo'
        unique_together = (('codigo_titulo', 'codigo_materia'),)


class Optativas(models.Model):
    codigo_optativa = models.IntegerField(primary_key=True)
    codigo_carrera = models.ForeignKey('Planes', models.DO_NOTHING, db_column='codigo_carrera')
    codigo_plan = models.CharField(max_length=6)
    codigo_orientacion = models.IntegerField(blank=True, null=True)
    nombre = models.CharField(max_length=255)
    tipo = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'optativas'


class Orientaciones(models.Model):
    codigo_carrera = models.OneToOneField('Planes', models.DO_NOTHING, db_column='codigo_carrera', primary_key=True)
    codigo_plan = models.CharField(max_length=6)
    codigo_orientacion = models.IntegerField()
    nombre = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'orientaciones'
        unique_together = (('codigo_carrera', 'codigo_plan', 'codigo_orientacion'),)


class Planes(models.Model):
    codigo_carrera = models.OneToOneField(Carreras, models.DO_NOTHING, db_column='codigo_carrera', primary_key=True)
    codigo_plan = models.CharField(max_length=6)
    resolucion = models.CharField(max_length=255, blank=True, null=True)
    ultima_actualizacion = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'planes'
        unique_together = (('codigo_carrera', 'codigo_plan'),)


class Titulos(models.Model):
    codigo_titulo = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=100)
    codigo_carrera = models.ForeignKey(Planes, models.DO_NOTHING, db_column='codigo_carrera')
    codigo_plan = models.CharField(max_length=6)

    class Meta:
        managed = False
        db_table = 'titulos'
