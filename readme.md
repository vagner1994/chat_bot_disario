# Passo a Passo: Números "Disários" em Python

## Passo 1: Compreendendo o Conceito

### O que é um número "disário"?

Um número "disário" é um número especial que atende a uma regra matemática específica. A regra é a seguinte: você deve dividir o número em seus dígitos e elevar cada dígito à posição que ele ocupa no número (começando a contar a partir da esquerda). Em seguida, some todos esses resultados. Se a soma desses resultados for igual ao número original, o número é considerado "disário". Caso contrário, não é "disário".

#### Exemplo:

Vamos usar o número 89 como exemplo:

- Dividimos o número em seus dígitos: 8 e 9.
- Elevamos 8 à primeira potência (8^1), o que resulta em 8.
- Elevamos 9 à segunda potência (9^2), o que resulta em 81.
- Somamos os resultados: 8 + 81 = 89.

Como a soma dos resultados é igual ao número original (89), o número 89 é "disário".

## Passo 2: Compreendendo o Código

### O que é um código em Python?

Python é uma linguagem de programação que permite escrever programas de computador. No código que fornecemos, criamos um programa que funciona como um "robô" capaz de se comunicar com você por meio do aplicativo de mensagens Telegram.

#### Como funciona o código?

O código é composto por várias partes:

- Primeiro, importamos a biblioteca `telepot`, que nos permite criar um bot de Telegram.

- Em seguida, definimos uma função chamada `verificar_disario`. Esta função implementa a regra matemática para verificar se um número é "disário" ou não, como explicado anteriormente.

- A função `principal` é a parte principal do código que lida com as mensagens dos usuários. Quando um usuário envia uma mensagem, o código verifica se a mensagem é um número e, em seguida, usa a função `verificar_disario` para determinar se o número é "disário". O código responde ao usuário com uma mensagem apropriada.

- O bot é criado usando a chave de API (token) fornecida pelo Telegram.

- O programa entra em um loop e fica "ouvindo" mensagens continuamente. Quando um usuário envia uma mensagem, o código responde de acordo com a lógica definida.

## Passo 3: Como o Robô Foi Construído

Para criar o robô, você precisa seguir esses passos:

1. **Criar um bot no Telegram**: Você deve criar um bot no Telegram e obter um token para acessá-lo. Para fazer isso, você pode conversar com o BotFather no Telegram e seguir as instruções.

2. **Instalar a biblioteca Telepot**: Use o comando `pip install telepot` para instalar a biblioteca Telepot em seu ambiente Python.

3. **Escrever o código**: Você deve escrever o código Python, como o fornecido anteriormente, que usa o token do seu bot e implementa a lógica para verificar se um número é "disário".

4. **Executar o código**: Execute o código Python e mantenha-o em execução. Isso fará com que o robô esteja sempre disponível para receber mensagens e responder de acordo.

5. **Interagir com o robô**: Agora, você pode interagir com o robô enviando números para ele, e ele responderá se o número é "disário" ou não.

Lembre-se de que o código pode ser personalizado para atender às suas necessidades e incluir funcionalidades adicionais, se desejado.

Espero que este guia tenha ajudado a entender o conceito de números "disários" e como o robô foi construído. Se tiver mais perguntas ou precisar de esclarecimentos adicionais, sinta-se à vontade para perguntar.
