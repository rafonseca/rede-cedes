from django.db import models
from django.urls import reverse
# Create your models here.
NIVEL_GOVERNO_CHOICES=[
    ('mu','Municipal'),
    ('es','Estadual'),
    ('fe','Federal'),
]
AMBITO_CHOICES=[
    ('le','Legislativo'),
    ('ex','Executivo'),
]
ABRANGENCIA_CHOICES=[
    ('lo','Local'),
    ('na','Nacional'),
    ('in','Internacional'),
    ]
UF_CHOICES=[
    ('AC','AC'),
    ('AL','AL'),
    ('AP','AP'),
    ('AM','AM'),
    ('BA','BA'),
    ('CE','CE'),
    ('DF','DF'),
    ('ES','ES'),
    ('GO','GO'),
    ('MA','MA'),
    ('MT','MT'),
    ('MS','MS'),
    ('MG','MG'),
    ('PA','PA'),
    ('PB','PB'),
    ('PR','PR'),
    ('PE','PE'),
    ('PI','PI'),
    ('RJ','RJ'),
    ('RN','RN'),
    ('RS','RS'),
    ('RO','RO'),
    ('RR','RR'),
    ('SC','SC'),
    ('SP','SP'),
    ('SE','SE'),
    ('TO','TO'),
]
LINHA_CHOICES=[
    ('mel','Memória do esporte e do lazer'),
    ('pel','Perfil do esporte e do lazer'),
    ('ppa','Políticas, programas e ações integradas de esporte e do lazer'),
    ('gne','Grupos com necessidades específicas'),
    ('oea','Observatório do esporte e da atividade física'),
    ('gel','Gestão do esporte e do lazer'),
    ('aps','Avaliação de políticas, programas e projetos sociais de esporte e lazer'),
    ('iel','Infraestrutura e espaços de esporte e lazer'),
    ('pps','Processos políticos'),
    ('ele','Esporte, lazer, escola e formação'),
]
TITULACAO_CHOICES=[
    ('dr','Doutor(a)'),
    ('mr','Mestre(a)'),
    ('es','Especialista'),
    ('gr','Graduado(a)'),
    ('ou','Outros'),
]
PUBLICACAO_CHOICES=[
    ('li','Livro ou Capítulo de Livro'),
    ('ar','Artigo Científico em Revista'),
    ('an','Publicação em Anais de Congresso'),
    ('ca','Publicação de cartilha, DVD, material didático e/ou informativo'),
]
TIPO_EVENTO_CHOICES=[
    ('Co','Congresso ou Encontro'),
    ('Jo','Jornada'),
    ('Cu','Curso/Workshop'),
    ('Of','Oficina, Palestra, Colóquio'),
    ('Se','Seminário'),
    ('Ou','Outro'),
]
DIFUSAO_CHOICES=[
    ('in','Internet'),
    ('tv','TV'),
    ('ra','Rádio'),
    ('re','Revista'),
    ('jo','Jornal'),
]
FORMACAO_CHOICES=[
    ('posls','Curso de Pós Graduação Lato Senso (360h ou mais)'),
    ('dogpg','Disciplina Optativa no âmbito da Graduação e/ou Pós Graduação sobre políticas de esporte e lazer'),
    ('capel','Curso de Aperfeiçoamento sobre políticas públicas de esporte e lazer (100h ou mais)'),
    ('expel','Curso de Extensão presencial e/ou à distância sobre políticas de esporte e lazer (até 80h)'),
]
ORIENTACAO_CHOICES=[
    ('Mog','Monografia de graduação'),
    ('TCC','TCC – Trabalho Final de Curso de graduação'),
    ('Ini','Iniciação científica'),
    ('Moe','Monografia de especialização'),
    ('Dis','Dissertação de mestrado'),
    ('Tes','Tese de doutorado'),
    ('Est','Estudo de pós-doutorado'),
]
SIT_MEMORIA_CHOICES=[
    ( 'na','não estruturado'),
    ( 'ei','em implementação'),
    ( 'im','implementado'),
    ]
SIT_ACERVO_CHOICES=[
    ( 'nc','Não catalogado;'),
    ( 'ca','Catalogado, mas não disponível;'),
    ( 'dm','Disponível, controle manual;'),
    ( 'di','Disponível, controle informatizado.'),
    ]
class CentroPesquisa(models.Model):
    nome = models.CharField(max_length=200)
    uf = models.CharField(max_length=2,choices=UF_CHOICES,primary_key=True)
    ies = models.CharField(max_length=50,null=True)
    def __str__(self):
        return "%s" % (self.uf)

### Modelos da meta 1

class EstruturaFisica(models.Model):
    centro = models.OneToOneField(CentroPesquisa,on_delete=models.CASCADE,primary_key=True)
    tem_sede = models.BooleanField(default=False)
    tem_banner = models.BooleanField(default=False)
    telefone = models.CharField(max_length=15,blank=True)
    tem_internet = models.BooleanField(default=False)
    equip_inf = models.BooleanField(default=False)
    moveis = models.BooleanField(default=False)
    coordenador = models.BooleanField(default=False)
    coord_adj = models.BooleanField(default=False)
    apoio_tecnico = models.BooleanField(default=False)
    bolsistas = models.BooleanField(default=False)
    repr_pesquisadores = models.BooleanField(default=False)
    repr_social = models.BooleanField(default=False)
    def __str__(self):
        return "Estrutura Física: %s" % (self.centro.nome)
    def get_absolute_url(self):
        return reverse('estrutura-fisica-detail', kwargs={'pk': self.pk})

### Modelos da Meta 2
#
# class Meta2(models.Model):
#     centro = models.OneToOneField(CentroPesquisa,on_delete=models.CASCADE,primary_key=True)
#     def __str__(self):
#         return "Relatório (Meta 2): %s" % (self.centro.nome)

class Pesquisa(models.Model):
    nome = models.CharField(max_length=400,null=False)
    grupo_pesquisa = models.CharField(max_length=400,null=True)
    centro = models.ForeignKey(CentroPesquisa,on_delete=models.CASCADE,null=False)

    linha=models.CharField(max_length=3,choices=LINHA_CHOICES,null=False)
    def __str__(self):
        return "%s" % (self.nome)
    def get_absolute_url(self):
        return reverse('pesquisa-detail', kwargs={'pk': self.pk})


class Pesquisador(models.Model):
    nome = models.CharField(max_length=200)
    centro_local = models.ForeignKey(CentroPesquisa,related_name='pesquisador_local',on_delete=models.SET_NULL,null=True)
    centro_colaborador = models.ForeignKey(CentroPesquisa,related_name='pesquisador_colaborador',on_delete=models.SET_NULL,null=True)
    titulacao =models.CharField(max_length=2,choices=TITULACAO_CHOICES,null=True)
    def __str__(self):
        return "%s" % (self.nome)

# ### Modelos da Meta 3

class Evento(models.Model):
    nome = models.CharField(max_length=200)
    tipo=models.CharField(max_length=2,choices=TIPO_EVENTO_CHOICES)
    abrangencia =models.CharField(max_length=2,choices=ABRANGENCIA_CHOICES)
    tema = models.CharField(max_length=200,null=True)
    data_inicio=models.DateField(null=True)
    data_fim=models.DateField(null=True)
    num_participantes= models.IntegerField(null=True)
    palestrantes= models.CharField(max_length=1000,null=True)
    publico_alvo=  models.CharField(max_length=1000,null=True)
    descricao= models.CharField(max_length=2000,null=True)
    local= models.CharField(max_length=1000,null=True)
    coordenador_evento= models.ForeignKey(Pesquisador,on_delete=models.CASCADE,null=False)
    pesquisadores_envolvidos= models.ManyToManyField(Pesquisador,related_name='evento_como_pesquisador')
    bolsistas_envolvidos= models.ManyToManyField(Pesquisador,related_name='evento_como_bolsista')

# ### Modelos de meta 4,5,6,7
class Publicacao(models.Model):

    titulo= models.CharField(max_length=200)
    abrangencia= models.CharField(max_length=2,choices=ABRANGENCIA_CHOICES,null=True)
    tipo= models.CharField(max_length=2,choices=PUBLICACAO_CHOICES,null=False)
    autor= models.ForeignKey(Pesquisador,on_delete=models.CASCADE,null=False)
    referencia_abnt= models.CharField(max_length=200,null=True)
    localizacao_digital=models.URLField(null=True)
#Modelos da meta 8
class DifusaoMidiatica(models.Model):

    titulo= models.CharField(max_length=200)
    tipo= models.CharField(max_length=2,choices=DIFUSAO_CHOICES)
    data_inicio=models.DateField(null=True)
    localizacao_digital=models.URLField(null=True)
    coordenador= models.ForeignKey(Pesquisador,on_delete=models.CASCADE,null=False)
    bolsistas_envolvidos= models.ManyToManyField(Pesquisador,related_name='difusao_como_bolsista')
    publico_alvo=  models.CharField(max_length=1000,null=True)
#Modelos metas 9,10,11
#Meta 9: Realização de atividade de formação de equipe.

class AtividadeFormacao(models.Model):

    titulo= models.CharField(max_length=200)
    tipo=models.CharField(max_length=5,choices=FORMACAO_CHOICES)
    tema = models.CharField(max_length=200,null=True)
    data_inicio=models.DateField(null=True)
    data_fim=models.DateField(null=True)
    total_horas= models.IntegerField(null=True)
    num_participantes= models.IntegerField(null=True)
    palestrantes= models.CharField(max_length=1000,null=True)
    publico_alvo=  models.CharField(max_length=1000,null=True)
    descricao= models.CharField(max_length=2000,null=True)
    local= models.CharField(max_length=1000,null=True)
    coordenador_formacao= models.ForeignKey(Pesquisador,on_delete=models.CASCADE,null=False)
    pesquisadores_envolvidos= models.ManyToManyField(Pesquisador,related_name='at_formacao_como_pesquisador')
    bolsistas_envolvidos= models.ManyToManyField(Pesquisador,related_name='at_formacao_como_bolsista')
#Modelos meta 12
class Orientacao(models.Model):

    titulo= models.CharField(max_length=200,null=False)
    tipo= models.CharField(max_length=3,choices=ORIENTACAO_CHOICES,null=False)
    data_inicio=models.DateField(null=True)
    data_fim=models.DateField(null=True)
    orientador= models.ForeignKey(Pesquisador,on_delete=models.CASCADE,null=False,related_name='orientacao_como_orientador')
    autor= models.ForeignKey(Pesquisador,on_delete=models.CASCADE,null=False,related_name='orientacao_como_autor')
    descricao= models.CharField(max_length=2000,null=True)
#Modelos meta 13
#intercambio
class Intercambio(models.Model):
    grupos_estudo= models.CharField(max_length=500,null=True)
    descricao= models.CharField(max_length=2000,null=True)
    coordenador= models.ForeignKey(Pesquisador,on_delete=models.CASCADE,null=False,related_name='intercambio_como_coordenador')
    estudante_bolsista= models.ForeignKey(Pesquisador,on_delete=models.CASCADE,null=False,related_name='intercambio_como_bolsista')
    data_inicio=models.DateField(null=True)
    data_fim=models.DateField(null=True)
    local= models.CharField(max_length=200,null=True)

    ambito=models.CharField(max_length=2,choices=AMBITO_CHOICES)

#Modelos meta 14
#intervencao politica
class IntervencaoPolitica(models.Model):
        descricao= models.CharField(max_length=2000,null=True)
        coordenador= models.ForeignKey(Pesquisador,on_delete=models.CASCADE,null=False,related_name='in_politica_como_coordenador')
        data_inicio=models.DateField(null=True)
        data_fim=models.DateField(null=True)
        local= models.CharField(max_length=200,null=True)

        nivel_governo=models.CharField(max_length=2,choices=NIVEL_GOVERNO_CHOICES)
        ambito=models.CharField(max_length=2,choices=AMBITO_CHOICES)
        publico_alvo=  models.CharField(max_length=1000,null=True)
        pesquisadores_envolvidos= models.ManyToManyField(Pesquisador,related_name='in_politica_como_pesquisador')
        bolsistas_envolvidos= models.ManyToManyField(Pesquisador,related_name='in_politica_como_bolsista')
#objetivo 5, meta 15
#centro de memoria

class CentroMemoria(models.Model):
        tema= models.CharField(max_length=2000,null=True)
        coordenador= models.ForeignKey(Pesquisador,on_delete=models.CASCADE,null=False,related_name='in_memoria_como_coordenador')
        pesquisadores_envolvidos= models.ManyToManyField(Pesquisador,related_name='in_memoria_como_pesquisador')
        bolsistas_envolvidos= models.ManyToManyField(Pesquisador,related_name='in_memoria_como_bolsista')
        situacao_implementacao=models.CharField(max_length=2,choices=SIT_MEMORIA_CHOICES)
        localizacao_digital=models.URLField(null=True)
        num_titulos= models.IntegerField(null=True)
        situacao_acervo_fisico=models.CharField(max_length=2,choices=SIT_ACERVO_CHOICES)
