# Eventex

Sistema de Eventos encomendado pela Morena.

[![Build Status](https://travis-ci.org/jasielserra/Event.svg?branch=master)](https://travis-ci.org/jasielserra/Event)
[![Code Climate](https://codeclimate.com/github/jasielserra/Event/badges/gpa.svg)](https://codeclimate.com/github/jasielserra/Event)


## Como desenvolver?

1. Clone repositório.
2. Crie um virtualenv com Python 3.5.
3. Ative o virtualenv.
4. Instale as dependências.
5. Configure a instância com o .env.
6. Execute os testes.

``` console
git clone git@github.com:jasielserra/Event.git wttd
cd wttd
python -m venv .wttd
source .wttd/bin/activate
pip install -r requirements.txt
cp contrib/env-sample .env
python manage.py test
```

## Como fazer o deploy?

1. Crie uma instância no heroku.
2. Envie as configurações para o heroku.
3. Define uma SECRET_KEY segura para instância.
4. Defina DEBUG=False.
5. Configure o serviço de email.
6. Envie o código para o heroku.

``` console
heroku create minhainstancia
heroku config:push
heroku config:set SECRET_KEY=`python contrib/secret_gen.py`
heroku config:set DEBUG=False
#   configura o email
git push heroku master --force
```


