export const handler = async (event) => {
    // Extrair a mensagem do evento SNS
    const message = event.Records[0].Sns.Message;
    
    // Parsear a mensagem para JSON
    let parsedMessage;
    try {
        parsedMessage = JSON.parse(message);
    } catch (error) {
        console.error("Erro ao parsear a mensagem:", error);
        return {
            statusCode: 500,
            body: JSON.stringify({ error: "Erro ao processar a mensagem" })
        };
    }
    
    // Extrair informações da mensagem
    const nome = parsedMessage.nome;
    const is_Basculho = parsedMessage.is_Basculho;
    
    // Imprimir as informações
    console.log(`Nome: ${nome}, is_Basculho: ${is_Basculho}`);
    
    // Retornar a resposta
    return {
        statusCode: 200,
        body: JSON.stringify({ nome: nome, is_Basculho: is_Basculho })
    };
  };