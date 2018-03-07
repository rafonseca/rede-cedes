from django.db import models
from django.contrib.auth.models import User
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
    ('AC','Acre'),
    ('AL','Alagoas'),
    ('AP','Amapá'),
    ('AM','Amazonas'),
    ('BA','Baía'),
    ('CE','Ceará'),
    ('DF','Distrito Federal'),
    ('ES','Espírito Santo'),
    ('GO','Goiás'),
    ('MA','Maranhão'),
    ('MT','Mato Grosso'),
    ('MS','Mato Grosso do Sul'),
    ('MG','MG_atualizar no models.py'),
    ('PA','PA_atualizar no models.py'),
    ('PB','PB_atualizar no models.py'),
    ('PR','PR_atualizar no models.py'),
    ('PE','PE_atualizar no models.py'),
    ('PI','PI_atualizar no models.py'),
    ('RJ','RJ_atualizar no models.py'),
    ('RN','RN_atualizar no models.py'),
    ('RS','RS_atualizar no models.py'),
    ('RO','RO_atualizar no models.py'),
    ('RR','RR_atualizar no models.py'),
    ('SC','SC_atualizar no models.py'),
    ('SP','SP_atualizar no models.py'),
    ('SE','SE_atualizar no models.py'),
    ('TO','TO_atualizar no models.py'),
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

from django.contrib.auth.models import User
class CentroPesquisa(models.Model):
    nome = models.CharField(max_length=200)
    uf = models.CharField(max_length=2,choices=UF_CHOICES,primary_key=True)
    ies = models.CharField(max_length=50,blank=True)
    gestores = models.ManyToManyField(User)
    def nome_estado(self):
        uf_dict={uf:nome for uf,nome in UF_CHOICES}
        return uf_dict[self.uf]

    def __str__(self):
        return "%s" % (self.uf)

### Modelos da meta 1

class EstruturaFisica(models.Model):
    centro = models.OneToOneField(CentroPesquisa,on_delete=models.CASCADE,primary_key=True)
    tem_sede = models.BooleanField(default=False)
    tem_banner = models.BooleanField(default=False)
    tem_internet = models.BooleanField(default=False)
    equip_inf = models.BooleanField(default=False)
    moveis = models.BooleanField(default=False)
    coordenador = models.BooleanField(default=False)
    coord_adj = models.BooleanField(default=False)
    apoio_tecnico = models.BooleanField(default=False)
    bolsistas = models.BooleanField(default=False)
    repr_pesquisadores = models.BooleanField(default=False)
    repr_social = models.BooleanField(default=False)

    #campos não obrigatórios
    telefone = models.CharField(max_length=15,blank=True)
    # def get_absolute_url(self):
    #     return reverse('estrutura-fisica-detail', kwargs={'pk': self.pk})

### Modelos da Meta 2


class Pesquisa(models.Model):
    centro = models.ForeignKey(CentroPesquisa,on_delete=models.CASCADE,null=True)
    nome = models.CharField(max_length=400,)
    linha=models.CharField(max_length=3,choices=LINHA_CHOICES,)

    #campos não obrigatórios
    grupo_pesquisa = models.CharField(max_length=400,blank=True)
    def get_absolute_url(self):
        return reverse('pesquisa-detail', kwargs={'pk': self.pk,'centro': self.centro})
    def linha_human_readable(self):
        linha_dict={k:v for k,v in LINHA_CHOICES}
        return (linha_dict[self.linha])



class Pesquisador(models.Model):
    nome = models.CharField(max_length=200,)
    titulacao =models.CharField(max_length=2,choices=TITULACAO_CHOICES,blank=True)
    #campos não obrigatórios

    centro= models.ForeignKey(CentroPesquisa,on_delete=models.SET_NULL,null=True,blank=True) # centro
    bolsista = models.BooleanField(default=False)
    def __str__(self):
        return self.nome


# ### Modelos da Meta 3
class Evento(models.Model):
    centro = models.ForeignKey(
        CentroPesquisa, on_delete=models.CASCADE, null=True,)
    nome = models.CharField(max_length=200)
    tipo = models.CharField(max_length=2, choices=TIPO_EVENTO_CHOICES,)
    abrangencia = models.CharField(max_length=2, choices=ABRANGENCIA_CHOICES,)
    coordenador_evento = models.ForeignKey(
        Pesquisador, on_delete=models.CASCADE, null=True,)

    # campos não obrigatórios
    tema = models.CharField(max_length=200, blank=True)
    data_inicio = models.DateField(null=True, blank=True)
    data_fim = models.DateField(null=True, blank=True)
    num_participantes = models.IntegerField(null=True, blank=True)
    palestrantes = models.CharField(max_length=1000, blank=True)
    publico_alvo = models.CharField(max_length=1000, blank=True)
    descricao = models.CharField(max_length=2000, blank=True)
    local = models.CharField(max_length=1000, blank=True)
    pesquisadores_envolvidos = models.ManyToManyField(
        Pesquisador, related_name='evento_como_pesquisador', blank=True)
    bolsistas_envolvidos = models.ManyToManyField(
        Pesquisador, related_name='evento_como_bolsista', blank=True)

    def tipo_human_readable(self):
        tipo_dict = {k: v for k, v in TIPO_EVENTO_CHOICES}
        return (tipo_dict[self.tipo])

# ### Modelos de meta 4,5,6,7
class Publicacao(models.Model):
    centro = models.ForeignKey(CentroPesquisa,on_delete=models.CASCADE,null=True)
    titulo= models.CharField(max_length=200,)
    tipo= models.CharField(max_length=2,choices=PUBLICACAO_CHOICES,)
    autor= models.ForeignKey(Pesquisador,on_delete=models.CASCADE,null=True)

    #campos não obrigatórios
    abrangencia= models.CharField(max_length=2,choices=ABRANGENCIA_CHOICES,blank=True)
    referencia_abnt= models.CharField(max_length=200,blank=True)
    localizacao_digital=models.URLField(blank=True)
#Modelos da meta 8
class DifusaoMidiatica(models.Model):
    centro = models.ForeignKey(CentroPesquisa,on_delete=models.CASCADE,null=True)
    titulo= models.CharField(max_length=200,)
    tipo= models.CharField(max_length=2,choices=DIFUSAO_CHOICES,)

    #campos não obrigatórios
    data_inicio=models.DateField(blank=True)
    localizacao_digital=models.URLField(blank=True)
    coordenador= models.ForeignKey(Pesquisador,on_delete=models.CASCADE,null=True,blank=True)
    bolsistas_envolvidos= models.ManyToManyField(Pesquisador,related_name='difusao_como_bolsista',blank=True)
    publico_alvo=  models.CharField(max_length=1000,blank=True)

#Modelos metas 9,10,11
#Meta 9: Realização de atividade de formação de equipe.
class AtividadeFormacao(models.Model):
    centro = models.ForeignKey(CentroPesquisa,on_delete=models.CASCADE,null=True)
    titulo= models.CharField(max_length=200,)
    tipo=models.CharField(max_length=5,choices=FORMACAO_CHOICES,)
    coordenador_formacao= models.ForeignKey(Pesquisador,on_delete=models.CASCADE,null=True)

    #campos não obrigatórios
    tema = models.CharField(max_length=200,blank=True)
    data_inicio=models.DateField(null=True,blank=True)
    data_fim=models.DateField(null=True,blank=True)
    total_horas= models.IntegerField(null=True,blank=True)
    num_participantes= models.IntegerField(null=True,blank=True)
    palestrantes= models.CharField(max_length=1000,blank=True)
    publico_alvo=  models.CharField(max_length=1000,blank=True)
    descricao= models.CharField(max_length=2000,blank=True)
    local= models.CharField(max_length=1000,blank=True)
    pesquisadores_envolvidos= models.ManyToManyField(Pesquisador,related_name='at_formacao_como_pesquisador',blank=True)
    bolsistas_envolvidos= models.ManyToManyField(Pesquisador,related_name='at_formacao_como_bolsista',blank=True)
#Modelos meta 12
class Orientacao(models.Model):
    centro = models.ForeignKey(CentroPesquisa,on_delete=models.CASCADE,null=True,)
    titulo= models.CharField(max_length=200,)
    tipo= models.CharField(max_length=3,choices=ORIENTACAO_CHOICES,)

    #campos não obrigatórios
    data_inicio=models.DateField(null=True,blank=True)
    data_fim=models.DateField(null=True,blank=True)
    orientador= models.ForeignKey(Pesquisador,on_delete=models.CASCADE,null=True,related_name='orientacao_como_orientador',blank=True)
    autor= models.ForeignKey(Pesquisador,on_delete=models.CASCADE,null=True,related_name='orientacao_como_autor',blank=True)
    descricao= models.CharField(max_length=2000,blank=True)
#Modelos meta 13
#intercambio
class Intercambio(models.Model):
    centro = models.ForeignKey(CentroPesquisa,on_delete=models.CASCADE,null=True)
    coordenador= models.ForeignKey(Pesquisador,on_delete=models.CASCADE,null=True,related_name='intercambio_como_coordenador')
    estudante_bolsista= models.ForeignKey(Pesquisador,on_delete=models.CASCADE,null=True,related_name='intercambio_como_bolsista')
    data_inicio=models.DateField(null=True,blank=True)
    data_fim=models.DateField(null=True,blank=True)
    local= models.CharField(max_length=200,)
    ambito=models.CharField(max_length=2,choices=AMBITO_CHOICES,)

    #campos não obrigatórios
    grupos_estudo= models.CharField(max_length=500,blank=True)
    descricao= models.CharField(max_length=2000,blank=True)

#Modelos meta 14
#intervencao politica
class IntervencaoPolitica(models.Model):
    centro = models.ForeignKey(CentroPesquisa,on_delete=models.CASCADE,null=True)
    coordenador= models.ForeignKey(Pesquisador,on_delete=models.CASCADE,null=True,related_name='in_politica_como_coordenador')
    nivel_governo=models.CharField(max_length=2,choices=NIVEL_GOVERNO_CHOICES,)
    ambito=models.CharField(max_length=2,choices=AMBITO_CHOICES,)

    #campos não obrigatórios
    data_inicio=models.DateField(null=True,blank=True)
    data_fim=models.DateField(null=True,blank=True)
    local= models.CharField(max_length=200,blank=True)
    descricao= models.CharField(max_length=2000,blank=True)
    publico_alvo=  models.CharField(max_length=1000,blank=True)
    pesquisadores_envolvidos= models.ManyToManyField(Pesquisador,related_name='in_politica_como_pesquisador',blank=True)
    bolsistas_envolvidos= models.ManyToManyField(Pesquisador,related_name='in_politica_como_bolsista',blank=True)

#objetivo 5, meta 15
#centro de memoria
class CentroMemoria(models.Model):
    centro = models.OneToOneField(CentroPesquisa,on_delete=models.CASCADE,primary_key=True)
    coordenador= models.ForeignKey(Pesquisador,on_delete=models.CASCADE,null=True,related_name='in_memoria_como_coordenador')
    situacao_implementacao=models.CharField(max_length=2,choices=SIT_MEMORIA_CHOICES,)
    situacao_acervo_fisico=models.CharField(max_length=2,choices=SIT_ACERVO_CHOICES,)

    #campos não obrigatórios
    tema= models.CharField(max_length=2000,blank=True)
    pesquisadores_envolvidos= models.ManyToManyField(Pesquisador,related_name='in_memoria_como_pesquisador',blank=True)
    bolsistas_envolvidos= models.ManyToManyField(Pesquisador,related_name='in_memoria_como_bolsista',blank=True)
    localizacao_digital=models.URLField(blank=True)
    num_titulos= models.IntegerField(null=True,blank=True)
