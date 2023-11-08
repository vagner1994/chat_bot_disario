import telepot
import time

def verificar_disario(numero):
    # Converte o número em uma string para processar os dígitos individualmente
    numero_str = str(numero)
    
    # Inicializa a soma
    soma = 0
    
    for i, digito in enumerate(numero_str):
        potencia = i + 1  # Calcula a potência com base na posição do dígito
        soma += int(digito) ** potencia  # Eleva o dígito à potência e adiciona à soma
    
    return soma == numero  # Retorna True se for "disário", False caso contrário

def principal(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
 
    if content_type == 'text':
        try:
            numero = int(msg['text'])  # Tenta converter a mensagem em um número
            if verificar_disario(numero):
                resposta = 'O número {} é disário!'.format(numero)
            else:
                resposta = 'O número {} não é disário.'.format(numero)
            bot.sendMessage(chat_id, resposta)
        except ValueError:
            bot.sendMessage(chat_id, 'Por favor, digite um número válido.')
 
bot = telepot.Bot('6557010890:AAG1X5OCyP2wMHRnbbN_lQEvtPErZvr5u6g')  # Substitua 'SEU_TOKEN_DO_BOT' pelo token do seu bot
 
bot.message_loop(principal)
 
while True:
    time.sleep(5)
