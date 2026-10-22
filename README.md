Integrantes: Matheus Silva e José Lucas
Turma: 513
# ATV09 — Migração do Portal para Django

Projeto adaptado a partir dos arquivos enviados da atividade anterior. O visual original foi mantido como referência (fundo escuro e menu vermelho), as imagens originais foram preservadas em `portal/static/portal/img/` e a navegação principal foi migrada para URLs e Views do Django.

## Requisitos
- Python 3.10 ou superior (recomendado)
- pip
- Git (para versionamento)

## Ubuntu: instalar e executar
Abra o terminal dentro da pasta do projeto:

```bash
sudo apt update
sudo apt install python3 python3-venv python3-pip git -y
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py seed_portal
python manage.py runserver
```

Acesse o portal em `http://127.0.0.1:8000/` e a área administrativa em `http://127.0.0.1:8000/admin/`.

> Se executar `seed_portal` antes de `createsuperuser`, não há problema. O comando cadastra quatro conteúdos internos e seis itens de menu de exemplo. Revise os dados no Admin antes da entrega. O comando pode ser executado novamente sem duplicar os registros de exemplo.

## Estrutura
- `config/`: configurações e URLs do projeto Django.
- `portal/models.py`: Models `Conteudo` e `Menu`.
- `portal/views.py`: página inicial, conteúdo dinâmico e obtenção do menu.
- `portal/templates/portal/`: templates Django com cabeçalho, navegação, conteúdo e rodapé.
- `portal/static/portal/css/style.css`: estilos responsivos.
- `portal/static/portal/img/`: imagens do ZIP original.
- `portal/management/commands/seed_portal.py`: dados de demonstração para começar rapidamente.

## Funcionalidades implementadas
- Model `Conteudo`: título, slug, conteúdo HTML e ativo.
- Model `Menu`: título, tipo de destino, ordem, ativo, relação opcional com `Conteudo` e URL externa.
- Django Admin para administrar os dois Models.
- Menu dinâmico consultado no banco de dados.
- URLs dinâmicas `/conteudo/<slug>/`.
- Templates Django e arquivos estáticos separados.
- Layout responsivo para telas menores.

## Git e GitHub
Depois de revisar e testar o projeto:

```bash
git init
git add .
git commit -m "Cria projeto Django da ATV09"
```

Crie um repositório no GitHub e siga as instruções do próprio GitHub para conectar o repositório local e enviar os commits. Não envie `.venv/` nem `db.sqlite3`.

## Antes de entregar
- Confirme os nomes da dupla e a turma.
- Revise os dados pessoais e as informações dos jogadores; alguns dados vieram do material original e podem estar desatualizados.
- Verifique se todas as imagens aparecem corretamente.
- Faça testes no portal e no Django Admin.
- Troque a chave `SECRET_KEY` e desative `DEBUG` caso publique em um servidor real. Para a avaliação local, a configuração atual é de desenvolvimento.
