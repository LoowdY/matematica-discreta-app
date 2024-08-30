# Aplicativo de Indução Matemática

Este aplicativo foi desenvolvido utilizando o Streamlit para ajudar na compreensão e aplicação de diferentes métodos de indução matemática. O objetivo principal é fornecer uma plataforma interativa onde os usuários possam aprender sobre indução matemática, realizar exercícios e verificar suas respostas.

## Objetivo

O objetivo do aplicativo é ensinar e ilustrar os seguintes métodos de indução matemática:

1. **Indução Padrão**: Prova que uma propriedade é verdadeira para todos os números naturais, começando de um caso base e usando o passo indutivo.
2. **Indução Forte**: Prova que uma propriedade é verdadeira para todos os números naturais usando todos os casos anteriores.
3. **Indução Estrutural**: Aplica indução a estruturas definidas recursivamente, como árvores e sequências complexas.

## Funcionalidades

O aplicativo oferece as seguintes seções:

### Introdução

Fornece uma explicação sobre o conceito de indução matemática, incluindo exemplos clássicos e a fórmula para a soma dos primeiros \( n \) números naturais, bem como a Conjectura de Goldbach.

### Indução Padrão

Permite ao usuário:
- Escolher um valor inicial para a base da indução.
- Calcular e simplificar uma soma básica.
- Verificar a fórmula da soma dos primeiros \( n \) números naturais.

### Indução Forte

Permite ao usuário:
- Escolher um valor de \( n \) para verificar a fórmula da soma de uma série geométrica.
- Adivinhar o valor da soma incluindo o próximo termo.
- Visualizar a soma acumulada dos termos da sequência em um gráfico.

### Indução Estrutural

Permite ao usuário:
- Escolher entre diferentes estruturas (sequência ou árvore).
- Para sequências, calcular e visualizar a soma dos quadrados dos primeiros elementos.
- Para árvores, calcular o número total de nós em uma árvore binária completa e visualizar a árvore.

### Questionário

Um quiz para testar o conhecimento do usuário sobre indução matemática, com perguntas sobre indução padrão, forte e estrutural.

### Dúvidas Comuns

Responde a perguntas frequentes sobre indução matemática, incluindo:
- O que fazer se a base da indução não for verdadeira.
- Aplicação da indução em conjuntos não naturais.
- Diferença entre indução forte e padrão.

## Como Executar o Aplicativo

1. Certifique-se de que você tem o Python instalado em seu ambiente.
2. Instale as dependências necessárias usando o comando:
   ```bash
   pip install --user -r requirements.txt
   streamlit run app.py
## Contato

E-mail: jrenanlopes@gmail.com  
LinkedIn: [João Renan](https://www.linkedin.com/in/joao-renan/)

## Agradecimentos

Agradeço ao Professor Pedro Henrique Sales Girotto por suas valiosas contribuições e orientações no desenvolvimento deste projeto. Seu conhecimento e experiência foram fundamentais para a realização deste trabalho.


