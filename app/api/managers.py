from django.contrib.auth.base_user import BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, id, auth_id,first_name, last_name, email, password=None, **extra_fields):
        
        if not id:
            raise ValueError('Users must have an id')
 
        user = self.model(
            id=id,
            auth_id=auth_id,
            first_name=first_name,
            last_name=last_name,
            email=email
        )
 
        user.set_password(password)
        user.save()
        return user
 
    def create_superuser(self, id, auth_id, first_name, last_name, email, password=None, **extra_fields):

        user = self.create_user(
            id,
            auth_id,
            first_name,
            last_name,
            email,
            password=password,
        )
        
        user.save()
        return user