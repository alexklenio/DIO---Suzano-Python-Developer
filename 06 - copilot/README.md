# DIO-criando-o-primeiro-copiloto-no-microsoft-copilot-studio.
 

Este repositório reúne minhas anotações, capturas de tela e reflexões sobre o curso **Criando seu primeiro Copiloto no Microsoft Copilot Studio**, parte do **Módulo 5 do Bootcamp Suzano Python Developer** da [DIO.me](https://www.dio.me).  

O conteúdo foi estruturado em **seis vídeos** que apresentam, de forma progressiva, como configurar o ambiente, criar e testar um copiloto personalizado utilizando o Microsoft Copilot Studio.

---

## 📺 Conteúdo do Curso  

### 1. Etapas do Desafio  

<details>
<summary> Slide da aula🔻</summary>
<p align="center">
    <img src="images/image.png" alt="" width="840">
</p>
</details>

#### Anotações:

- Criar uma conta gratuita no Microsft 365 através deste [link](https://copilot.microsoft.com/chats/v1Ed4quJJ6RGC3asffb1H#:~:text=Criar%20uma%20conta%20gratuita%20no,.).
- Com ela você terá permissão de criar uma conta no Copilot Studio.
- Acessar o link https://copilotstudio.microsoft.com para criar conta do Copilot Studio.

### 2. Conteúdo Programático

<details>
<summary> Slide da aula🔻</summary>
<p align="center">
    <img src="images/image-2.png" alt="" width="840">
</p>
</details>

### 3. Conexão e Criação de uma conta no Microsoft 365

<details>
<summary> Slides da aula🔻</summary>
<p align="center">
    <img src="images/image-5.png" alt="" width="840">
</p>

<p align="center">
    <img src="images/image-6.png" alt="" width="840">
</p>

<p align="center">
    <img src="images/image-7.png" alt="" width="840">
</p>

<p align="center">
    <img src="images/image-8.png" alt="" width="840">
</p>

<p align="center">
    <img src="images/image-9.png" alt="" width="840">
</p>

</details> 

### 4. Criação um Copilot baseado em modelo  

- O símbolo do avião indica o Agente de Viagens (Safe Travel). É um modelo.

<details>
<summary> Slides da aula🔻</summary>
<p align="center">
    <img src="images/image-11.png" alt="" width="840">
</p>
</details>

- Para testes, vamos considerar qu estamos criando uma AGENTE para uma agência de viagens.
- A descrição é um prompt.
- O prompt funciona como instrução de configuração, orientando a IA a responder conforme os parâmetros definidos e garantindo alinhamento com o objetivo do copiloto.

<details>
<summary> Slides da aula🔻</summary>
<p align="center">
    <img src="images/image-13.png" alt="" width="840">
</p>
</details>

- O AGENTE atua como mecanismo de controle, garantindo que o copiloto mantenha consistência e relevância nas respostas, evitando a geração de informações incorretas ou sem relação com o contexto (‘alucinações’).

<details>
<summary> Slides da aula🔻</summary>
<p align="center">
    <img src="images/image-14.png" alt="" width="840">
</p>
</details>

- A base de conhecimento foi integrada ao US Travel Website, portal oficial de informações de viagens do governo dos Estados Unidos, permitindo que o copiloto acesse dados confiáveis e atualizados diretamente da fonte oficial.

<details>
<summary> Slides da aula🔻</summary>
<p align="center">
    <img src="images/image-15.png" alt="" width="840">
</p>
</details>

- Alterando o idioma.

<details>
<summary> Slides da aula🔻</summary>
<p align="center">
    <img src="images/image-16.png" alt="" width="840">
</p>
</details>

- Após a criação do AGENTE o Copilot disponibiliza um overview.

<details>
<summary> Slides da aula🔻</summary>
<p align="center">
    <img src="images/image-18.png" alt="" width="840">
</p>
</details>

- Posso visualizar todos os tópicos:

<details>
<summary> Slides da aula🔻</summary>
<p align="center">
    <img src="images/image-17.png" alt="" width="840">
</p>
</details>

### 5. Criação de um Copilot em branco

- A criação e administração de copilotos é realizada por meio do portal Microsoft Copilot Studio, que centraliza a orquestração, configuração e gerenciamento de todos os copilotos associados à conta do usuário.

<details>
<summary> Slide da aula🔻</summary>
<p align="center">
<p align="center">
    <img src="images/image-19.png" alt="" width="840">
</p>
</details>

- É possível selecionar o ambiente de desenvolvimento utilizado previamente, assegurando a continuidade da configuração e gerenciamento do copiloto no mesmo contexto criado na etapa anterior. 

<details>
<summary> Slide da aula🔻</summary>
<p align="center">
    <img src="images/image-20.png" alt="" width="840">
</p>
</details>

- Descrição do agente.

<details>
<summary> Slide da aula🔻</summary>
<p align="center">
    <img src="images/image-22.png" alt="" width="840">
</p>
</details>

- Dá-se o nome do agente (pressionar o botão "Criar¨).

<details>
<summary> Slide da aula🔻</summary>
<p align="center">
    <img src="images/image-24.png" alt="" width="840">
</p>  
</details>

### 6. Criação de um Copilot em branco

- Temos um agente já disponível no ambiente que criamos.

<details>
<summary> Slide da aula🔻</summary>
<p align="center">
    <img src="images/image-25.png" alt="" width="840">
</p>
</details>

- O obejtivo, agora, será criar um agente "em branco".
- Recomenda-se criar a estrutura de conhecimento ("Knowledge") depois.

<details>
<summary> Slide da aula🔻</summary>
<p align="center">
    <img src="images/image-27.png" alt="" width="840">
</p>
</details>

- Opções avançadas

<details>
<summary> Slide da aula🔻</summary>
<p align="center">
    <img src="images/image-28.png" alt="" width="840">
</p>
</details>

- Aqui é possível selecionar uma solução já criada.

<details>
<summary> Slide da aula🔻</summary>
<p align="center">
    <img src="images/image-29.png" alt="" width="840">
</p>
</details>

- Em seguida, gerar a arquitetura do nosso copilot (pressionar o botão "Criar¨).
- O sistema irá treinar antes de disponibilizar o agente.

- Teste: "O que é o agente?"

<details>
<summary> Slide da aula🔻</summary>
<p align="center">
    <img src="images/image-31.png" alt="" width="840">
</p>
</details>

---

## 🎯 Principais Aprendizados  

- Entender a **plataforma Microsoft Copilot Studio** e seu papel no ecossistema Microsoft 365.  
- Saber como **criar um copiloto** partindo de modelos prontos.  
- Aprender a **configurar tópicos e fluxos conversacionais**.  
- Publicar e **testar o copiloto em cenários reais**.  
- Realizar **ajustes contínuos e monitoramento de desempenho** para aprimorar a experiência do usuário.  

---

## 🔗 Links relacionados  

- [Microsoft Copilot Studio](https://copilotstudio.microsoft.com/)  
- [Repositório de Estudos - Bootcamp Suzano Python Developer](https://github.com/ahaerdy/DIO-learning/tree/main/Suzano%20-%20Python%20Developer)  

  

