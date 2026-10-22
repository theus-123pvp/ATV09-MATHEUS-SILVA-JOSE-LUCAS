from django.db import models
from django.utils.text import slugify

class Conteudo(models.Model):
    titulo = models.CharField("Título", max_length=150)
    slug = models.SlugField("Slug", max_length=170, unique=True)
    conteudo_html = models.TextField("Conteúdo HTML", help_text="Informe somente o conteúdo interno da página, sem html, head, body, header, nav ou footer.")
    ativo = models.BooleanField("Ativo", default=True)

    class Meta:
        verbose_name = "Conteúdo"
        verbose_name_plural = "Conteúdos"
        ordering = ["titulo"]

    def __str__(self):
        return self.titulo

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.titulo)
        super().save(*args, **kwargs)

class Menu(models.Model):
    class TipoDestino(models.TextChoices):
        INTERNO = "interno", "Conteúdo interno"
        EXTERNO = "externo", "Link externo"

    titulo = models.CharField("Título", max_length=100)
    tipo_destino = models.CharField("Tipo de destino", max_length=10, choices=TipoDestino.choices, default=TipoDestino.INTERNO)
    ordem = models.PositiveIntegerField("Ordem", default=0)
    ativo = models.BooleanField("Ativo", default=True)
    conteudo = models.ForeignKey(Conteudo, verbose_name="Conteúdo relacionado", on_delete=models.CASCADE, blank=True, null=True, related_name="itens_menu")
    url_externa = models.URLField("URL externa", blank=True)

    class Meta:
        verbose_name = "Item do menu"
        verbose_name_plural = "Itens do menu"
        ordering = ["ordem", "titulo"]

    def __str__(self):
        return self.titulo

    def clean(self):
        from django.core.exceptions import ValidationError
        if self.tipo_destino == self.TipoDestino.INTERNO:
            if not self.conteudo:
                raise ValidationError({"conteudo": "Selecione um conteúdo para links internos."})
            if self.url_externa:
                raise ValidationError({"url_externa": "Links internos não devem ter URL externa."})
        elif self.tipo_destino == self.TipoDestino.EXTERNO:
            if not self.url_externa:
                raise ValidationError({"url_externa": "Informe a URL para links externos."})
            if self.conteudo:
                raise ValidationError({"conteudo": "Links externos não devem ter conteúdo relacionado."})
