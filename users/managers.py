from django.contrib.auth.base_user import BaseUserManager

class CustomuserManager(BaseUserManager):
    def create_user(self,email,password=None,**extra_fileds):
        if not email:
            raise ValueError("This Email Field must be set")
        email  =self.normalize_email(email)
        user = self.model(email=email , **extra_fileds)
        user.set_password(password)
        user.save(using = self._db)
        return user
    
    def create_superuser(self,email,password  =None,**extra_fileds):
        extra_fileds.setdefault("is_staff" , True)

        extra_fileds.setdefault("is_superuser" , True)

        if not extra_fileds.get('is_staff'):
            raise ValueError("Superuser must have is_staff = True")
        if not extra_fileds.get('is_superuser'):
            raise ValueError("Superuser must have is_superuser = True")

        return self.create_user(email,password,**extra_fileds)