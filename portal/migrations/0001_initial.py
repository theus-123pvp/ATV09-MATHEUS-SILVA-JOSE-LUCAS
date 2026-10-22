from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):
    initial = True
    dependencies = []
    operations = [
        migrations.CreateModel(name="Conteudo", fields=[
            ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
            ("titulo", models.CharField(max_length=150, verbose_name="Título")),
            ("slug", models.SlugField(max_length=170, unique=True, verbose_name="Slug")),
            ("conteudo_html", models.TextField(help_text="Informe somente o conteúdo interno da página, sem html, head, body, header, nav ou footer.", verbose_name="Conteúdo HTML")),
            ("ativo", models.BooleanField(default=True, verbose_name="Ativo")),
        ], options={"verbose_name": "Conteúdo", "verbose_name_plural": "Conteúdos", "ordering": ["titulo"]}),
        migrations.CreateModel(name="Menu", fields=[
            ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
            ("titulo", models.CharField(max_length=100, verbose_name="Título")),
            ("tipo_destino", models.CharField(choices=[("interno", "Conteúdo interno"), ("externo", "Link externo")], default="interno", max_length=10, verbose_name="Tipo de destino")),
            ("ordem", models.PositiveIntegerField(default=0, verbose_name="Ordem")),
            ("ativo", models.BooleanField(default=True, verbose_name="Ativo")),
            ("url_externa", models.URLField(blank=True, verbose_name="URL externa")),
            ("conteudo", models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name="itens_menu", to="portal.conteudo", verbose_name="Conteúdo relacionado")),
        ], options={"verbose_name": "Item do menu", "verbose_name_plural": "Itens do menu", "ordering": ["ordem", "titulo"]}),
    ]
