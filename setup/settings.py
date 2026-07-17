"""
Configurações do projeto.

Preparado para funcionar em 2 modos, sem precisar mexer neste arquivo:

1) NO SEU COMPUTADOR (desenvolvimento): não precisa configurar nada.
   Sem nenhuma variável de ambiente definida, ele roda automaticamente
   com DEBUG=True e permite qualquer host — exatamente como já vinha
   funcionando até agora.

2) NO AR (produção, ex: PythonAnywhere): você define 3 variáveis de
   ambiente (explicado no LEIA-ME de deploy) e ele automaticamente
   fica seguro: DEBUG=False, chave secreta própria, e só aceita
   requisições do seu domínio.
"""

import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


def variavel_bool(nome, padrao):
    """Lê uma variável de ambiente tipo 'True'/'False' com um valor padrão."""
    valor = os.environ.get(nome)
    if valor is None:
        return padrao
    return valor.strip().lower() in ('1', 'true', 'sim', 'yes')


# ── SECRET_KEY ──────────────────────────────────────────────────────────
# Em produção, defina a variável de ambiente SECRET_KEY com uma chave só
# sua (o LEIA-ME de deploy explica como gerar uma). Sem essa variável
# definida (ex: no seu computador), usa a chave abaixo — sem problema
# para desenvolvimento local, mas NUNCA suba pro ar sem trocar.
SECRET_KEY = os.environ.get(
    'SECRET_KEY',
    'h$sp7cvz*^q-6djm5c*5s84w=naic7i30wr^b@tr!%!hsm0(z+'  # só para uso local
)

# ── DEBUG ────────────────────────────────────────────────────────────────
# Sem a variável de ambiente DEBUG definida, fica True (jeito de sempre,
# no seu computador). Em produção, defina DEBUG=False.
DEBUG = variavel_bool('DEBUG', padrao=True)

# ── ALLOWED_HOSTS ────────────────────────────────────────────────────────
# Sem a variável de ambiente ALLOWED_HOSTS definida, aceita qualquer host
# (jeito de sempre, para uso local). Em produção, defina algo como:
# ALLOWED_HOSTS=seuusuario.pythonanywhere.com
_allowed_hosts_env = os.environ.get('ALLOWED_HOSTS')
if _allowed_hosts_env:
    ALLOWED_HOSTS = [h.strip() for h in _allowed_hosts_env.split(',') if h.strip()]
else:
    ALLOWED_HOSTS = ['*']


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'setup.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # 'APP_DIRS': True já faz o Django procurar automaticamente dentro de
        # core/templates/ — por isso não precisamos listar nada em 'DIRS'.
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'setup.wsgi.application'


# ── Banco de dados ───────────────────────────────────────────────────────
# Continua SQLite mesmo em produção — no PythonAnywhere o disco é
# permanente (ao contrário de outros serviços gratuitos), então o
# db.sqlite3 não se perde. Simples e funciona bem para o tamanho do
# projeto.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]


# Idioma e fuso horário — ajustado para o Brasil.
LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'
USE_I18N = True
USE_TZ = True


# ── Arquivos estáticos (CSS, imagens de fundo, etc.) ─────────────────────
# STATIC_URL: o endereço usado nos templates (via {% static %}).
# STATIC_ROOT: pasta onde o comando 'collectstatic' vai JUNTAR todos os
# arquivos estáticos num só lugar, pra publicar. Só é usado em produção
# (no seu computador, o Django continua servindo direto de core/static/
# automaticamente, sem precisar rodar collectstatic).
STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'


# ── Segurança extra, só quando DEBUG=False (produção) ───────────────────
# Evita alguns golpes comuns (roubo de cookie de sessão, clickjacking,
# cookies trafegando sem criptografia). O PythonAnywhere já fornece HTTPS
# de graça nos subdomínios .pythonanywhere.com.
#
# OBS: não ativamos aqui o "SECURE_SSL_REDIRECT" (que forçaria redirecionar
# tudo pra HTTPS) de propósito — em alguns provedores isso causa um loop
# infinito de redirecionamento se o servidor não repassar corretamente o
# cabeçalho de origem. Como o PythonAnywhere já serve tudo em HTTPS por
# padrão, isso não costuma ser necessário.
if not DEBUG:
    SECURE_BROWSER_XSS_FILTER = True
    X_FRAME_OPTIONS = 'DENY'
    SESSION_COOKIE_HTTPONLY = True
    CSRF_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
