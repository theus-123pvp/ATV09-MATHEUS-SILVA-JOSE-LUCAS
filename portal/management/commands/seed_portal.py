from django.core.management.base import BaseCommand
from portal.models import Conteudo, Menu

CONTEUDOS = [
    ("Currículo José Lucas", "curriculo-jose-lucas", """<section class="card"><h2>Informações pessoais</h2><img src="/static/portal/img/IMG-20260616-WA0011.jpg" alt="Foto de perfil de José Lucas" width="180"><p><strong>Nome:</strong> José Lucas Galdino Vieira</p><p><strong>Idade:</strong> 17 anos (conforme o material original)</p><p><strong>Cidade:</strong> Taquarana — AL</p><p><strong>Objetivo:</strong> Fazer um bom trabalho e contribuir para o crescimento da empresa.</p><p><strong>Habilidades:</strong> Comunicação, programação, IA e marketing digital.</p><p><strong>Contato:</strong> Consulte o arquivo original antes de publicar dados pessoais.</p></section>"""),
    ("Currículo Matheus", "curriculo-matheus", """<section class="card"><h2>Matheus da Silva Cordeiro</h2><img src="/static/portal/img/IMG-20260616-WA0013.jpg" alt="Foto de perfil" width="160"><p><strong>Email:</strong> mateus.curriculo@gmail.com</p><p><strong>Telefone:</strong> (81) 99999-0000</p><p><strong>Localização:</strong> Recife — PE</p><p><strong>Escolaridade:</strong> Ensino Médio em andamento.</p><h3>Curso atual</h3><p>Técnico em Desenvolvimento de Sistemas.</p><h3>Objetivo profissional</h3><p>Pretendo crescer profissionalmente, aprender novas tecnologias e ajudar a empresa com dedicação e responsabilidade.</p></section>"""),
    ("Tema livre — Flamengo", "tema-flamengo", """<section class="card"><h2>Jogadores em destaque</h2><img src="/static/portal/img/IMG-20260616-WA0010.jpg" alt="Jogadores do Flamengo" width="260"><article><h3>Pedro</h3><p>Gols, assistências e títulos conforme o material original da atividade.</p></article><article><h3>Arrascaeta</h3><p>Jogador do Flamengo em destaque no trabalho.</p></article><article><h3>Gabigol</h3><p>Jogador apresentado no material original.</p></article><article><h3>Bruno Henrique</h3><p>Jogador apresentado no material original.</p></article><p><a href="https://www.flamengo.com.br/" target="_blank" rel="noopener noreferrer">Site oficial do Flamengo</a></p></section>"""),
    ("Tema livre — Corinthians", "tema-corinthians", """<section class="card"><h2>Corinthians</h2><img src="/static/portal/img/IMG-20260616-WA0012.jpg" alt="Símbolo do Corinthians" width="180"><table><tr><th>Jogador</th><th>Ano</th><th>Títulos (conforme trabalho original)</th></tr><tr><td>Cássio</td><td>2012</td><td>9 títulos</td></tr><tr><td>Sócrates</td><td>1978</td><td>3 títulos</td></tr><tr><td>Marcelinho Carioca</td><td>1994</td><td>10 títulos</td></tr><tr><td>Rivellino</td><td>1965</td><td>5 títulos</td></tr></table><p>O Sport Club Corinthians Paulista é conhecido por sua torcida e por conquistar títulos importantes.</p><p><a href="https://www.corinthians.com.br/" target="_blank" rel="noopener noreferrer">Site oficial do Corinthians</a></p></section>"""),
]
class Command(BaseCommand):
    help = "Cadastra conteúdos e itens de menu de exemplo para demonstrar a ATV09."
    def handle(self, *args, **options):
        for titulo, slug, html in CONTEUDOS:
            obj, created = Conteudo.objects.update_or_create(slug=slug, defaults={"titulo": titulo, "conteudo_html": html, "ativo": True})
            self.stdout.write(f"Conteúdo {'criado' if created else 'atualizado'}: {titulo}")
        menu_items = [
            ("Currículo José Lucas", "interno", 1, "curriculo-jose-lucas", ""),
            ("Currículo Matheus", "interno", 2, "curriculo-matheus", ""),
            ("Tema livre — Flamengo", "interno", 3, "tema-flamengo", ""),
            ("Tema livre — Corinthians", "interno", 4, "tema-corinthians", ""),
            ("Site do Flamengo", "externo", 5, None, "https://www.flamengo.com.br/"),
            ("W3Schools", "externo", 6, None, "https://www.w3schools.com/"),
        ]
        for titulo, tipo, ordem, slug, url in menu_items:
            conteudo = Conteudo.objects.filter(slug=slug).first() if slug else None
            Menu.objects.update_or_create(titulo=titulo, defaults={"tipo_destino": tipo, "ordem": ordem, "ativo": True, "conteudo": conteudo, "url_externa": url})
        self.stdout.write(self.style.SUCCESS("Portal de exemplo pronto. Revise dados e imagens no Django Admin."))
