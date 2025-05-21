# 📝 Blog Gabrielle Fernandes

Blog pessoal desenvolvido para a cliente **Gabrielle Fernandes**, com o objetivo de proporcionar um espaço simples, elegante e funcional para publicação de textos e ideias. O foco do projeto é oferecer uma ótima experiência de leitura em uma interface minimalista e com personalidade.

## 🔍 Visão Geral

O blog foi criado utilizando o framework **Django**, com estilização feita em **Tailwind CSS** e funcionalidades interativas com **JavaScript**. A proposta era construir uma plataforma limpa, moderna e com boa usabilidade, atendendo ao desejo da cliente de ter um blog com identidade visual leve e organizada.

## 🚀 Tecnologias Utilizadas

- **[Django](https://www.djangoproject.com/)** – Backend robusto e ágil para criação das páginas dinâmicas
- **[Tailwind CSS](https://tailwindcss.com/)** – Utilizado para construir um design responsivo e limpo com facilidade
- **JavaScript** – Responsável pelas interações e pequenos comportamentos dinâmicos
- **Figma** – Criação do layout e protótipo visual
- **Git & GitHub** – Controle de versão e hospedagem do código

## 📌 Funcionalidades

- Página inicial com listagem de postagens mais recentes
- Sistema de cadastro e exibição de posts
- Layout 100% responsivo (mobile first)
- Tipografia otimizada para leitura
- Estilo visual limpo, elegante e com identidade

## 🎨 Layout

O layout foi pensado para refletir a personalidade da autora: leveza, clareza e um toque de elegância. Criado inicialmente no Figma e fielmente implementado com o auxílio do Tailwind CSS.

## 🚧 Status do Projeto

> 🛠️ **Em desenvolvimento** – Algumas melhorias visuais e funcionais ainda estão sendo aplicadas.


## ⚙️ Como executar localmente

> Certifique-se de ter Python e Node.js instalados na máquina.

1. Clone o repositório:
git clone https://github.com/andersondv5/blog-gabrielle-fernandes.git
cd blog-gabrielle-fernandes


2. Crie e ative um ambiente virtual:
python -m venv venv
source venv/bin/activate # Linux/macOS
venv\Scripts\activate # Windows


3. Instale as dependências:
pip install -r requirements.txt
npm install


4. Compile o Tailwind CSS:
npx tailwindcss -i ./static/src/input.css -o ./static/css/style.css --watch


5. Execute o servidor Django:
python manage.py runserver

yaml
Copiar
Editar

6. Acesse em: `http://127.0.0.1:8000/`

## 📫 Contato

Desenvolvido por **Anderson Silva**  
📧 anderson.silvadev5@gmail.com  
🔗 [LinkedIn](https://www.linkedin.com/in/anderson-silvadev/)  
🐙 [GitHub](https://github.com/andersondv5)

---

> Este projeto é mais do que um blog — é uma forma de transformar ideias em experiências digitais com propósito, beleza e usabilidade.
