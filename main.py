import boto3
import json

# Criar o cliente SNS
sns_client = boto3.client('sns', region_name='us-east-1')

# Criar a mensagem JSON
message = {
    "nome": "Andrew Lucas",
    "is_Basculho": "True"
}

# Publicar a mensagem no tópico SNS
response = sns_client.publish(
    TopicArn='arn:aws:sns:us-east-1:651706772649:MeuTopicoTeste',
    Message=json.dumps(message)
)

print(response)