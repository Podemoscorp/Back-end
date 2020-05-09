from django.db import models
from datetime import datetime 
from  utils.config import tempero
import jwt
 
class Usuario(models.Model):
    nome = models.CharField(db_index=True, max_length=50,unique=True)
    endereço = models.CharField(max_length=50)
    idade = models.IntegerField()
    email = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)
    username = models.CharField(max_length=25, unique=True)
    cpf = models.CharField(max_length=25, unique=True)
    perfil = models.CharField(max_length=25)
    datetime = models.DateTimeField(default=datetime.now,blank=True)

    def __str__(self):
        return self.nome
    
    @property
    def token(self):


        return self._generate_jwt_token()
    
    def get_short_name(self):

        return self.nome

    def _generate_jwt_token(self):
        payload={"nome":self.nome,"senha":self.password}
        key = tempero
        algoritmo='HS256'

        encoded =jwt.encode(payload,key,algoritmo)

        return encoded
    
    


class Aluno(models.Model):
    nome = models.CharField(max_length=50)
    endereço = models.CharField(max_length=50)
    idade = models.IntegerField()
    email = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50)
    username = models.CharField(max_length=25, unique=True)
    cpf = models.CharField(max_length=25, unique=True)
    datetime = models.DateTimeField(default=datetime.now,blank=True)

    def __str__(self):
        return self.nome
    


        

class Noticias(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    imagem = models.CharField(max_length=200)
    datetime = models.DateTimeField(default=datetime.now,blank=True)
    postador = models.ForeignKey(Usuario , on_delete=models.CASCADE)

class Extras(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    imagem = models.CharField(max_length=200)
    conteudo = models.CharField(max_length=200)
    datetime = models.DateTimeField(default=datetime.now,blank=True)
    postador = models.ForeignKey(Usuario , on_delete=models.CASCADE)
    tema = models.CharField(max_length=30)

class Cursos(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField()
    imagem = models.CharField(max_length=200)
    datetime = models.DateTimeField(default=datetime.now,blank=True)
    professor = models.ForeignKey(Usuario , on_delete=models.CASCADE)
    alunos = models.ManyToManyField(Aluno)
    tema = models.CharField(max_length=30)

class Certificados(models.Model):
    titulo = titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    imagem = models.CharField(max_length=200)
    conteudo_certificado = models.CharField(max_length=200)
    aluno = models.ForeignKey(Aluno , on_delete=models.CASCADE)
    datetime = models.DateTimeField(default=datetime.now,blank=True)