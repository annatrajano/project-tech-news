Este projeto contém os requisitos realizados por _[Anna Beatriz Garcia Trajano de Sá](www.linkedin.com/in/anna-beatriz-trajano-de-sá)_ enquanto estudava na [Trybe](https://www.betrybe.com/) :rocket:

# Project Tech News

Neste projeto o objetivo principal era fazer consultas em notícias sobre tecnologia!

As notícias foram obtidas através da raspagem do _Blog da Trybe_: https://blog.betrybe.com.

Além disso, as  notícias foram salvas no banco de dados (MongoDB) utilizando funções em python.

## Python + Flask

 Job Insights - Homepage       
:-------------------------:|
![Screeshot](./img/job_1.png)  |

Job Insights - Filters       
:-------------------------:|
![Screeshot](./img/job_2.png)  |

---

## Demo

![Demo](img/video.gif)

---

## Instalação do projeto localmente:
 
Após cada um dos passos, haverá um exemplo do comando a ser digitado para fazer o que está sendo pedido, caso tenha dificuldades e o exemplo não seja suficiente, não hesite em me contatar em _annagarcia@id.uff.br_ 

1. Abra o terminal e crie um diretório no local de sua preferência com o comando **mkdir**:
```javascript
  mkdir projetos
```

2. Entre no diretório que acabou de criar e depois clone o projeto:
```javascript
  cd projetos
  git clone git@github.com:annatrajano/project-tech-news.git
```

3. Acesse o diretório do projeto e depois crie um ambiente virtual para instalar todas as dependências necessárias:
```javascript
  cd project-tech-news
```

4. O Python oferece um recurso chamado de ambiente virtual, onde permite sua máquina rodar sem conflitos, diferentes tipos de projetos com diferentes versões de bibliotecas.

  1. **criar o ambiente virtual**

  ```bash
  $ python3 -m venv .venv
  ```

  2. **ativar o ambiente virtual**

  ```bash
  $ source .venv/bin/activate
  ```

  3. **instalar as dependências no ambiente virtual**

  ```bash
  $ python3 -m pip install -r dev-requirements.txt
  ```

  Com o seu ambiente virtual ativo, as dependências serão instaladas neste ambiente.
  Quando precisar desativar o ambiente virtual, execute o comando "deactivate". Lembre-se de ativar novamente quando voltar a trabalhar no projeto.


## Habilidades Desenvolvidas

Neste projeto, desenvolvi as seguintes habilidades:
 <ul>
   <li>Utilizar o terminal interativo do Python</li>
   <li>Escrever seus próprios módulos e importá-los em outros códigos</li>
   <li>Aplicar técnicas de raspagem de dados</li>
   <li>Extrair dados de conteúdo HTML</li>
   <li>Armazenar os dados obtidos em um banco de dados (MongoDB) </li>
 </ul>



 
 ## Referências
 [Documentação Oficial - Python](https://docs.python.org/3/)<br>
 [Working With Files in Python](https://realpython.com/working-with-files-in-python/)<br>
 [Pytest](https://docs.pytest.org/en/7.1.x/contents.html)<br>
 [Conventional Commits](https://gist.github.com/qoomon/5dfcdf8eec66a051ecd85625518cfd13)<br>

 ## Escopo do Projeto
 
 ### 1 - Crie a função `fetch`
 ### 2 - Crie a função `scrape_novidades`
 ### 3 - Crie a função `scrape_next_page_link`
 ### 4 - Crie a função `scrape_noticia`
 ### 5 - Crie a função `get_tech_news` para obter as notícias!
 ### 6 - Crie a função `search_by_title`
 ### 7 - Crie a função `search_by_date`
 ### 8 - Crie a função `search_by_tag`
 ### 9 - Crie a função `search_by_category`
