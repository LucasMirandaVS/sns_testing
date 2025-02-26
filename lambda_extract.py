import json

def lambda_handler(event, context):
    # Extrair a mensagem do evento SNS
    message = event['Records'][0]['Sns']['Message']
    
    # Parsear a mensagem para JSON
    parsed_message = json.loads(message)
    
    # Extrair informações da mensagem
    nome = parsed_message.get('nome')
    is_Basculho =  parsed_message.get('is_Basculho')
    
    # Imprimir as informações
    print(f"Nome: {nome}, is_Basculho: {is_Basculho}")
    
    # Retornar a resposta
    return {
        'statusCode': 200,
        'body': json.dumps({'nome': nome, 'is_Basculho': is_Basculho})
    }