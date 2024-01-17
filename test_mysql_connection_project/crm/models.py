from django.db import models

"""
La tarea es crear el modelo de un usuario que quede registrado en nuestra BBDD.
El usuario tendrá definido los siguientes atributos:
- Username
- Email
- Password
- User_is_connected (Boolean en dafault=false): nos servirá para manejar la conexión de los usuarios y modificará el last update.
- Created_at (timestamp)
- Last_update (timestamp)
- User_is_deleted(default=false)"""

class User(models.Model):
    """
    User -> modelo de usuario para la bbdd con los atributos definidos arriba
    """
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=25, verbose_name="Nombre de usuario")
    email = models.CharField(max_length=50, verbose_name="Email")
    password = models.CharField(max_length=50, verbose_name="Contraseña")
    user_is_connected = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Última modificación")
    user_is_deleted = models.BooleanField(default=False)


    def __str__(self):
        return "id: {}, username: {}, email: {}".format(self.id, self.username, self.email)

    
