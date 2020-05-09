class UserManager(BaseUserManager):

     def CreateUser(self,username,password):
            if username is None:
                raise TypeError('Tem que ter um usuario')
        user =self.model(nome =nome )   
        user.set_password(password)
        user.save()

        return user