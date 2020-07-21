## Tutorial Criando Uma aplicação python e Django, implementando api rest e deploy.

Tutorial para iniciantes em Python e Django com um Projeto de Sistema para Gestão de estoque com PDV.


1 - Instalar o PIP3

        sudo apt-get install python3-pip

2 - Install virtualenv

    sudo pip3 install virtualenvwrapper

    export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
    source /usr/local/bin/virtualenvwrapper.sh

Se o Virtual env não funcionar vamos tentar outra alternativa:
O virtualenvwrapper não está localizado em / usr / local / bin

    pip3 install virtualenvwrapper
    cd ~/.local/bin/
    vim ~/.bashrc

->> Adicione as seguintes linhas no final do arquivo.

		export WORKON_HOME=$HOME/.virtualenvs
		export PROJECT_HOME=$HOME/Devel
		export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
		export VIRTUALENVWRAPPER_VIRTUALENV=/usr/local/bin/virtualenv
		source ~/.local/bin/virtualenvwrapper.sh


3- Para testar se está tudo funcionando executa o comando abaixo

Uma lista de ambientes vazios é impressa com o comando a seguir.
    
    workon


Um novo ambiente, nome_da_virtualenv é criado e ativado.

    mkvirtualenv nome_da_virtualenv

Desta vez, o ambiente temporário está incluído.

    workon

Caso não ative o comando para ativar uma virutal env é.

    workon nome_da_virtualenv


4-Vamos instalar o Django dentro do env executando o comando abaixo:

    pip3 install django


5 - Vamos criar o projeto Django 

Crie uma pasta com o nome do seu projeto

    mkdir api-rest
    cd api-rest

Dentro da pasta vamos criar o projeto Django com o comando a seguir:

    django-admin startproject pdv . 

Não esqueça do ponto no final, com ele apenas cria o projeto django, sem o ponto ele cria um diretório e coloca o projeto dentro, como já temos o diretório criado então vamos utiliza o ponto para criar apenas o projeto dentro da nossa pasta.


6 - Agora com o comando (tree) vamos ver a estrutura de diretórios.

    sudo apt install tree
    tree

- Todo diretorio com o __init_.py é reconhecido como pacote python.


7 - Para facilitar a chamada do manager.py vamos criar um arquivo texto com o nome Makefile .

    touch Makefile

8 - Dentro do arquivo Makefile vamos colocar os seguintes comandos

    clean:
        find . -name "*.pyc" -exec rm -rf {} \;
    
    run: clean
        python manage.py runserver
    
    migrate: clean
        python manage.py migrate
    
    migrations: clean
        python manage.py makemigrations
    
    exclude_migrations: clean
        rm **/migrations/*[0-9]*.py
    
    superuser: clean
        python manage.py createsuperuser
    
    shell: clean
        python manage.py shell
    
    run_rede: clean
        ./manage.py runserver 0.0.0.0:8000



9 - Uma app é uma biblioteca python que segue algumas convenções do Django.

Para criar uma APP product vamos utilizar o comando

    python manage.py startapp product


10 -Vamos instalar a APPs, sugiro que utilizem o Sublime ou Pycharm, mas podem utilizar outro editor de sua preferência.

No arquivo chamado "settings.py" vamos adicionar no final do bloco "INSTALLED_APPS"
ficando assim    'product' ou 'nomedoprojeto.product' depende de onde está a pasta da product.

    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'product',
    ]


Pronto já foi registrada a APP, vamos rodar o projeto você pode executar qualquer um dos dois comando abaixo:
    
    make run
    python manage.py runserver

11 - Vamos fazer a tradução alterando o arquivo "settings.py"  
  
    LANGUAGE_CODE = 'en-us'
    TIME_ZONE = 'UTC'

substituir por
  
    LANGUAGE_CODE = 'pt-br'
    TIME_ZONE = 'America/Sao_Paulo'

12 - CRIANDO DIRETORIO TEMPLATES

Vamos na app product para criar um diretório com o nome "templates" para armazenar o os arquivos .html,  dentro deste diretório product/templates vamos criar um arquivo html com o nome index.html.

Personalise o arquivo index.html:
    
13 - Vamos criar a View home dentro da app product, no arquivo **views.py**

    def home(request):
        return render(request, 'index.html')


14 - Vamos criar uma rota, para isso vamos no arquivo ( **urls.py** ) , logo dentro do bloco ( **urlpatterns** ) vamos adicionar o seguinte caminho.

    path('', home),

* Temos que importar a view:


    from product.views import home

Ficando assim o arquivo **urls.py**:

    from product.views import home
    
    urlpatterns = [
        path('', home),
        path('admin/', admin.site.urls),
    ]

Executando o comando **make run** já vamos ter acesso a pagina que foi criada.

15 - Criando o arquivo requirements, no terminal execute o comando: 

###### Esse arquivo nada mais é do que um arquivo de texto, contendo uma lista de itens/pacotes instalados.
       
    pip3 freeze > requirements.txt
    
16 - Criar e executar as migrations:

    make migrations
    make migrate

######"As migrações são a maneira do Django de propagar alterações que você faz nos seus modelos (adicionando um campo, excluindo um modelo etc.) no esquema do banco de dados. Eles foram projetados para serem principalmente automáticos, mas você precisará saber quando fazer migrações, quando executá-las e os problemas comuns em que poderá se deparar." https://docs.djangoproject.com/en/3.0/topics/migrations/ 

 17 - Vamos criar um Super User:
 
     make superuser
     ou
     python manage.py createsuperuser
     

*  Execute o projeto e acesse o admin com as credenciais cadastradas 
 http://127.0.0.1:8000/admin/
 

18 - Vamos criar os Models do produto. 

    class Product(models.Model):
        description = models.CharField('Nome do Produto', max_length=150)
        price = models.DecimalField('Preço do produto', decimal_places=2, max_digits=6)
        stock = models.IntegerField('Estoque Disponível')
        stock_min = models.IntegerField('Mínimo estoque aceitável')
    
        def __str__(self):
            return f'Produto ( {self.description} ) - Preço Unt ( {self.price} ) - Qtd em estoque ( {self.stock} ) '

19 - Vamos registrar no admin:

    from .models import Product
    
    admin.site.register(Product)




* ###### Execute o projeto e acesse o admin onde já poderar fazer o cadastro de um produto.




 ###**Em breve atualizações com implementações de acesso via API REST.**
 
 
 
 