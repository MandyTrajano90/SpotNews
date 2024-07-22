# SpotNews 📰

É um projeto para desenvolver minhas habilidades no Django REST Framework (DRF).
Precisa de um CRUD em API REST? O DRF está aí pra ajudar! Precisa criar formulários HTML para modelos do banco de dados? Com pouco esforço eles estarão prontos para uso!

<details>
<summary><strong>🧑‍💻 O que foi desenvolvido</strong></summary>

É uma aplicação que armazena notícias que podem ser categorizadas por um usuário cadastrado.

</details>

<details>
  <summary><strong>:memo: Habilidades desenvolvidas </strong></summary>

Neste projeto, aprendi a:

<ul>
    <li>Escrever aplicações usando Django e Django Rest Framework</li>
    <li>Desenvolver uma aplicação que usa a arquitetura Model-View-Template</li>
    <li>Trabalhar com banco de dados MYSQL</li>
</ul>

</details>



## Instalando o projeto

1. Este projeto usa dependências que não são funcionais em todas as versões do Python. Por isso, recomendo que seu Python esteja na versão `3.10.0` ou superior. 
  
> ⚠️ **ATENÇÃO: NUNCA REMOVA VERSÕES ANTIGAS INSTALADAS DO PYTHON. SEU SISTEMA OPERACIONAL PODE DEPENDER DELAS!** ⚠️

2. Para conseguir instalar a dependência `mysqlclient` você precisa garantir a existência de algumas bibliotecas no seu sistema operacional:

- **Debian/Ubuntu**

```bash
sudo apt-get install python3-dev default-libmysqlclient-dev build-essential pkg-config
```

- **Mac**

```bash
brew install mysql pkg-config
```

3. Clone o repositório

- Use o comando: `git clone git@github.com:MandyTrajano90/SpotNews.git`
- Entre na pasta do repositório que você acabou de clonar:
  - `cd SpotNews`

4. Instale as dependências

    - Siga os passos do tópico [**🏕️ Ambiente Virtual**]

<details>
  <summary><strong>🏕️ Ambiente Virtual</strong></summary>
  O Python oferece um recurso chamado de ambiente virtual, onde permite sua máquina rodar sem conflitos, diferentes tipos de projetos com diferentes versões de bibliotecas.

  1. **criar o ambiente virtual**

  ```bash
  python3 -m venv .venv
  ```

  2. **ativar o ambiente virtual**

  ```bash
  source .venv/bin/activate
  ```

  3. **instalar as dependências no ambiente virtual**

  ```bash
  python3 -m pip install -r dev-requirements.txt
  ```

  Com o seu ambiente virtual ativo, as dependências serão instaladas neste ambiente.
  Quando precisar desativar o ambiente virtual, execute o comando `deactivate`. Lembre-se de ativar novamente quando voltar a trabalhar no projeto.

</details>

<details>
  <summary><strong>🏃🏾 Executando o Projeto</strong></summary>
  As notícias estarão armazenadas no nosso banco de dados.

  <strong>MySQL</strong>

  Para a realização deste projeto, utilizei um banco de dados chamado `spotnews_database`.

  Para rodar o MySQL via Docker execute os seguintes comandos na raiz do projeto:

  ```bash
  docker build -t spotnews-db .
  docker run -d -p 3306:3306 --name=spotnews-mysql-container -e MYSQL_ROOT_PASSWORD=password -e MYSQL_DATABASE=spotnews_database spotnews-db
  ```
  
  Esses comandos irão fazer o build da imagem e subir o container.
  
  Lembre-se de que o MySQL utiliza por padrão a porta 3306. Se já houver outro serviço utilizando esta porta, considere desativá-lo ou mudar a porta no comando acima.

</details>

<details>
<summary><strong>🎛 Linter</strong></summary>

Para garantir a qualidade do código, utilizei nesse projeto o linter `Flake8`. Assim o código fica alinhado com as boas práticas de desenvolvimento, sendo mais legível e de fácil manutenção! Para poder executar o `Flake8`, certifique-se de ter seguido os passos do tópico [**🏕️ Ambiente Virtual**] dentro do repositório.

Para rodá-lo localmente no repositório, execute o comando a seguir:

```bash
python3 -m flake8
```

Se a análise do `Flake8` encontrar problemas no seu código, tais problemas serão mostrados no seu terminal. Se não houver problema no seu código, nada será impresso no seu terminal.

</details>

<details>
  <summary><strong>🛠 Testes</strong></summary>

  👀 Para executar os testes certifique-se de que você está com o ambiente virtual ativado.

  <strong>Executar os testes</strong>

  ```bash
  python3 -m pytest
  ```

  O arquivo `pyproject.toml` já configura corretamente o `pytest`. Entretanto, caso você tenha problemas com isso e queira explicitamente uma saída completa, o comando é:

  ```bash
  python3 -m pytest -s -vv --continue-on-collection-errors
  ```

  O `pytest` possui diversos parâmetros que podem ser utilizados para executar os testes de diferentes formas. Alguns exemplos são:

  ```bash
  python3 -m pytest tests/test_nome_do_arquivo.py  # Executa todos os testes do arquivo de testes especificado
  python3 -m pytest tests/test_nome_do_arquivo.py::test_nome_do_teste  # Executa apenas o teste especificado
  python3 -m pytest -k expressao  # Executa apenas os testes que contém a expressão informada como substring
  python3 -m pytest -x  # Executa os testes até encontrar o primeiro erro
  ```

  Você pode combinar os parâmetros para executar os testes da forma que desejar! Para mais informações, consulte a [documentação do pytest](https://docs.pytest.org/en/7.3.x/contents.html).
  </details>





## 👁️ Dê uma olhada no código







https://github.com/user-attachments/assets/f64efcb0-1689-4624-9e7f-692d2b9fb822



<!-- Olá, Tryber!
Esse é apenas um arquivo inicial para o README do seu projeto.
É essencial que você preencha esse documento por conta própria, ok?
Não deixe de usar nossas dicas de escrita de README de projetos, e deixe sua criatividade brilhar!
:warning: IMPORTANTE: você precisa deixar nítido:
- quais arquivos/pastas foram desenvolvidos por você; 
- quais arquivos/pastas foram desenvolvidos por outra pessoa estudante;
- quais arquivos/pastas foram desenvolvidos pela Trybe.
-->
