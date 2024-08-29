Task Mupi - Gerenciador de Tarefas com Django e Django REST Framework

Descrição

Task Mupi é um aplicativo web para gerenciamento de tarefas, construído com Django e Django REST Framework. Ele permite que os usuários criem, editem, marquem como concluídas e excluam suas tarefas. A aplicação também possui uma API RESTful para que você possa integrar com outras aplicações ou serviços.

Funcionalidades

    Autenticação:
        Registro de novos usuários
        Login e logout
        
    Gerenciamento de Tarefas:
        Criar novas tarefas
        Editar tarefas existentes
        Marcar tarefas como concluídas ou pendentes
        Excluir tarefas
        Filtrar tarefas por status (todas, concluídas, pendentes)

    API REST:
        Endpoints para todas as funcionalidades de gerenciamento de tarefas
        Autenticação via token

Tecnologias Utilizadas

    Backend:
        Django
        Django REST Framework
    Frontend:
        HTML
        CSS (com Bootstrap)
    Banco de Dados:
        SQLite (padrão do Django)
        Pode ser facilmente configurado para usar outros bancos de dados (PostgreSQL, MySQL, etc.)

Como executar o projeto

    Clone o repositório:
    Bash

    git clone https://github.com/ThiagoCostaD/task_mupi.git

    Use o código com cuidado.

Crie um ambiente virtual:
Bash

python -m venv venv

Use o código com cuidado.

Ative o ambiente virtual:

    Windows:
    Bash

    venv\Scripts\activate

    Use o código com cuidado.

macOS/Linux:
Bash

source venv/bin/activate

Use o código com cuidado.

Instale as dependências:
Bash

pip install -r requirements.txt

Use o código com cuidado.

Execute as migrações:
Bash

python manage.py migrate

Use o código com cuidado.

6. Crie um superusuário:  

Bash

   python manage.py createsuperuser

Use o código com cuidado.

    Inicie o servidor de desenvolvimento:
    Bash

    python manage.py runserver

    Use o código com cuidado.

Acesse o aplicativo:  

        Abra seu navegador e acesse http://localhost:8000/


Contribuindo

Sinta-se à vontade para contribuir com o projeto! Abra issues para reportar bugs ou sugerir melhorias, ou envie pull requests com suas contribuições de código.

Licença

Este projeto está licenciado sob a licença MIT. Consulte o arquivo LICENSE para obter mais detalhes.

Contato

Em caso de dúvidas ou sugestões, entre em contato pelo e-mail thiagoocdiniz@gmail.com.   