# Generated by Django 2.0 on 2018-02-19 15:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AtividadeFormacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('tipo', models.CharField(choices=[('posls', 'Curso de Pós Graduação Lato Senso (360h ou mais)'), ('dogpg', 'Disciplina Optativa no âmbito da Graduação e/ou Pós Graduação sobre políticas de esporte e lazer'), ('capel', 'Curso de Aperfeiçoamento sobre políticas públicas de esporte e lazer (100h ou mais)'), ('expel', 'Curso de Extensão presencial e/ou à distância sobre políticas de esporte e lazer (até 80h)')], max_length=5)),
                ('tema', models.CharField(blank=True, max_length=200)),
                ('data_inicio', models.DateField(blank=True)),
                ('data_fim', models.DateField(blank=True)),
                ('total_horas', models.IntegerField(blank=True)),
                ('num_participantes', models.IntegerField(blank=True)),
                ('palestrantes', models.CharField(blank=True, max_length=1000)),
                ('publico_alvo', models.CharField(blank=True, max_length=1000)),
                ('descricao', models.CharField(blank=True, max_length=2000)),
                ('local', models.CharField(blank=True, max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='CentroPesquisa',
            fields=[
                ('nome', models.CharField(max_length=200)),
                ('uf', models.CharField(choices=[('AC', 'AC'), ('AL', 'AL'), ('AP', 'AP'), ('AM', 'AM'), ('BA', 'BA'), ('CE', 'CE'), ('DF', 'DF'), ('ES', 'ES'), ('GO', 'GO'), ('MA', 'MA'), ('MT', 'MT'), ('MS', 'MS'), ('MG', 'MG'), ('PA', 'PA'), ('PB', 'PB'), ('PR', 'PR'), ('PE', 'PE'), ('PI', 'PI'), ('RJ', 'RJ'), ('RN', 'RN'), ('RS', 'RS'), ('RO', 'RO'), ('RR', 'RR'), ('SC', 'SC'), ('SP', 'SP'), ('SE', 'SE'), ('TO', 'TO')], max_length=2, primary_key=True, serialize=False)),
                ('ies', models.CharField(blank=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='DifusaoMidiatica',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('tipo', models.CharField(choices=[('in', 'Internet'), ('tv', 'TV'), ('ra', 'Rádio'), ('re', 'Revista'), ('jo', 'Jornal')], max_length=2)),
                ('data_inicio', models.DateField(blank=True)),
                ('localizacao_digital', models.URLField(blank=True)),
                ('publico_alvo', models.CharField(blank=True, max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('tipo', models.CharField(choices=[('Co', 'Congresso ou Encontro'), ('Jo', 'Jornada'), ('Cu', 'Curso/Workshop'), ('Of', 'Oficina, Palestra, Colóquio'), ('Se', 'Seminário'), ('Ou', 'Outro')], max_length=2)),
                ('abrangencia', models.CharField(choices=[('lo', 'Local'), ('na', 'Nacional'), ('in', 'Internacional')], max_length=2)),
                ('tema', models.CharField(blank=True, max_length=200)),
                ('data_inicio', models.DateField(blank=True)),
                ('data_fim', models.DateField(blank=True)),
                ('num_participantes', models.IntegerField(blank=True)),
                ('palestrantes', models.CharField(blank=True, max_length=1000)),
                ('publico_alvo', models.CharField(blank=True, max_length=1000)),
                ('descricao', models.CharField(blank=True, max_length=2000)),
                ('local', models.CharField(blank=True, max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Intercambio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_inicio', models.DateField()),
                ('data_fim', models.DateField()),
                ('local', models.CharField(max_length=200)),
                ('ambito', models.CharField(choices=[('le', 'Legislativo'), ('ex', 'Executivo')], max_length=2)),
                ('grupos_estudo', models.CharField(blank=True, max_length=500)),
                ('descricao', models.CharField(blank=True, max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='IntervencaoPolitica',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nivel_governo', models.CharField(choices=[('mu', 'Municipal'), ('es', 'Estadual'), ('fe', 'Federal')], max_length=2)),
                ('ambito', models.CharField(choices=[('le', 'Legislativo'), ('ex', 'Executivo')], max_length=2)),
                ('data_inicio', models.DateField(blank=True)),
                ('data_fim', models.DateField(blank=True)),
                ('local', models.CharField(blank=True, max_length=200)),
                ('descricao', models.CharField(blank=True, max_length=2000)),
                ('publico_alvo', models.CharField(blank=True, max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Orientacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('tipo', models.CharField(choices=[('Mog', 'Monografia de graduação'), ('TCC', 'TCC – Trabalho Final de Curso de graduação'), ('Ini', 'Iniciação científica'), ('Moe', 'Monografia de especialização'), ('Dis', 'Dissertação de mestrado'), ('Tes', 'Tese de doutorado'), ('Est', 'Estudo de pós-doutorado')], max_length=3)),
                ('data_inicio', models.DateField(blank=True)),
                ('data_fim', models.DateField(blank=True)),
                ('descricao', models.CharField(blank=True, max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='Pesquisa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=400)),
                ('linha', models.CharField(choices=[('mel', 'Memória do esporte e do lazer'), ('pel', 'Perfil do esporte e do lazer'), ('ppa', 'Políticas, programas e ações integradas de esporte e do lazer'), ('gne', 'Grupos com necessidades específicas'), ('oea', 'Observatório do esporte e da atividade física'), ('gel', 'Gestão do esporte e do lazer'), ('aps', 'Avaliação de políticas, programas e projetos sociais de esporte e lazer'), ('iel', 'Infraestrutura e espaços de esporte e lazer'), ('pps', 'Processos políticos'), ('ele', 'Esporte, lazer, escola e formação')], max_length=3)),
                ('grupo_pesquisa', models.CharField(blank=True, max_length=400)),
            ],
        ),
        migrations.CreateModel(
            name='Pesquisador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('titulacao', models.CharField(choices=[('dr', 'Doutor(a)'), ('mr', 'Mestre(a)'), ('es', 'Especialista'), ('gr', 'Graduado(a)'), ('ou', 'Outros')], max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Publicacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('tipo', models.CharField(choices=[('li', 'Livro ou Capítulo de Livro'), ('ar', 'Artigo Científico em Revista'), ('an', 'Publicação em Anais de Congresso'), ('ca', 'Publicação de cartilha, DVD, material didático e/ou informativo')], max_length=2)),
                ('abrangencia', models.CharField(blank=True, choices=[('lo', 'Local'), ('na', 'Nacional'), ('in', 'Internacional')], max_length=2)),
                ('referencia_abnt', models.CharField(blank=True, max_length=200)),
                ('localizacao_digital', models.URLField(blank=True)),
                ('autor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='coleta.Pesquisador')),
            ],
        ),
        migrations.CreateModel(
            name='CentroMemoria',
            fields=[
                ('centro', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='coleta.CentroPesquisa')),
                ('situacao_implementacao', models.CharField(choices=[('na', 'não estruturado'), ('ei', 'em implementação'), ('im', 'implementado')], max_length=2)),
                ('situacao_acervo_fisico', models.CharField(choices=[('nc', 'Não catalogado;'), ('ca', 'Catalogado, mas não disponível;'), ('dm', 'Disponível, controle manual;'), ('di', 'Disponível, controle informatizado.')], max_length=2)),
                ('tema', models.CharField(blank=True, max_length=2000)),
                ('localizacao_digital', models.URLField(blank=True)),
                ('num_titulos', models.IntegerField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='EstruturaFisica',
            fields=[
                ('centro', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='coleta.CentroPesquisa')),
                ('tem_sede', models.BooleanField(default=False)),
                ('tem_banner', models.BooleanField(default=False)),
                ('tem_internet', models.BooleanField(default=False)),
                ('equip_inf', models.BooleanField(default=False)),
                ('moveis', models.BooleanField(default=False)),
                ('coordenador', models.BooleanField(default=False)),
                ('coord_adj', models.BooleanField(default=False)),
                ('apoio_tecnico', models.BooleanField(default=False)),
                ('bolsistas', models.BooleanField(default=False)),
                ('repr_pesquisadores', models.BooleanField(default=False)),
                ('repr_social', models.BooleanField(default=False)),
                ('telefone', models.CharField(blank=True, max_length=15)),
            ],
        ),
        migrations.AddField(
            model_name='publicacao',
            name='centro',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='coleta.CentroPesquisa'),
        ),
        migrations.AddField(
            model_name='pesquisador',
            name='centro_colaborador',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='pesquisador_colaborador', to='coleta.CentroPesquisa'),
        ),
        migrations.AddField(
            model_name='pesquisador',
            name='centro_local',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='pesquisador_local', to='coleta.CentroPesquisa'),
        ),
        migrations.AddField(
            model_name='pesquisa',
            name='centro',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='coleta.CentroPesquisa'),
        ),
        migrations.AddField(
            model_name='orientacao',
            name='autor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='orientacao_como_autor', to='coleta.Pesquisador'),
        ),
        migrations.AddField(
            model_name='orientacao',
            name='centro',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='coleta.CentroPesquisa'),
        ),
        migrations.AddField(
            model_name='orientacao',
            name='orientador',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='orientacao_como_orientador', to='coleta.Pesquisador'),
        ),
        migrations.AddField(
            model_name='intervencaopolitica',
            name='bolsistas_envolvidos',
            field=models.ManyToManyField(blank=True, related_name='in_politica_como_bolsista', to='coleta.Pesquisador'),
        ),
        migrations.AddField(
            model_name='intervencaopolitica',
            name='centro',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='coleta.CentroPesquisa'),
        ),
        migrations.AddField(
            model_name='intervencaopolitica',
            name='coordenador',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='in_politica_como_coordenador', to='coleta.Pesquisador'),
        ),
        migrations.AddField(
            model_name='intervencaopolitica',
            name='pesquisadores_envolvidos',
            field=models.ManyToManyField(blank=True, related_name='in_politica_como_pesquisador', to='coleta.Pesquisador'),
        ),
        migrations.AddField(
            model_name='intercambio',
            name='centro',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='coleta.CentroPesquisa'),
        ),
        migrations.AddField(
            model_name='intercambio',
            name='coordenador',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='intercambio_como_coordenador', to='coleta.Pesquisador'),
        ),
        migrations.AddField(
            model_name='intercambio',
            name='estudante_bolsista',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='intercambio_como_bolsista', to='coleta.Pesquisador'),
        ),
        migrations.AddField(
            model_name='evento',
            name='bolsistas_envolvidos',
            field=models.ManyToManyField(blank=True, related_name='evento_como_bolsista', to='coleta.Pesquisador'),
        ),
        migrations.AddField(
            model_name='evento',
            name='centro',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='coleta.CentroPesquisa'),
        ),
        migrations.AddField(
            model_name='evento',
            name='coordenador_evento',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='coleta.Pesquisador'),
        ),
        migrations.AddField(
            model_name='evento',
            name='pesquisadores_envolvidos',
            field=models.ManyToManyField(blank=True, related_name='evento_como_pesquisador', to='coleta.Pesquisador'),
        ),
        migrations.AddField(
            model_name='difusaomidiatica',
            name='bolsistas_envolvidos',
            field=models.ManyToManyField(blank=True, related_name='difusao_como_bolsista', to='coleta.Pesquisador'),
        ),
        migrations.AddField(
            model_name='difusaomidiatica',
            name='centro',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='coleta.CentroPesquisa'),
        ),
        migrations.AddField(
            model_name='difusaomidiatica',
            name='coordenador',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='coleta.Pesquisador'),
        ),
        migrations.AddField(
            model_name='centropesquisa',
            name='gestores',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='atividadeformacao',
            name='bolsistas_envolvidos',
            field=models.ManyToManyField(blank=True, related_name='at_formacao_como_bolsista', to='coleta.Pesquisador'),
        ),
        migrations.AddField(
            model_name='atividadeformacao',
            name='centro',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='coleta.CentroPesquisa'),
        ),
        migrations.AddField(
            model_name='atividadeformacao',
            name='coordenador_formacao',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='coleta.Pesquisador'),
        ),
        migrations.AddField(
            model_name='atividadeformacao',
            name='pesquisadores_envolvidos',
            field=models.ManyToManyField(blank=True, related_name='at_formacao_como_pesquisador', to='coleta.Pesquisador'),
        ),
        migrations.AddField(
            model_name='centromemoria',
            name='bolsistas_envolvidos',
            field=models.ManyToManyField(blank=True, related_name='in_memoria_como_bolsista', to='coleta.Pesquisador'),
        ),
        migrations.AddField(
            model_name='centromemoria',
            name='coordenador',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='in_memoria_como_coordenador', to='coleta.Pesquisador'),
        ),
        migrations.AddField(
            model_name='centromemoria',
            name='pesquisadores_envolvidos',
            field=models.ManyToManyField(blank=True, related_name='in_memoria_como_pesquisador', to='coleta.Pesquisador'),
        ),
    ]
