# Pré-Processamento de Dados

Para preparar os dados para o LP-BERT, é necessário realizar um pré-processamento dos dados originais. Um script foi desenvolvido para filtrar os dados essenciais, que incluem o id do usuário, datetime e coordenadas de localização. Esses dados são processados e filtrados para gerar o uid (código de identificação do usuário), d e t (dia e tempo passado desde a última coleta) e as coordenadas x e y.

Durante o processamento dos dados, é importante atentar para três detalhes:

1. Informar o nome da base de dados original.
2. Garantir que a base de dados contenha pelo menos 15 dias de dados disponíveis.
3. Informar o tamanho da grade que será utilizada para projetar as coordenadas de localização, configurada atualmente para 200 células de largura.

Após o processamento, serão gerados dois arquivos: um de teste e um de treino, já no formato aceito pelo LP-BERT.

Antes de executar o programa, é necessário realizar algumas configurações no LP-BERT para adaptá-lo aos dados fornecidos:

- Verifique o valor máximo de dias na base de treino, configurado para 15 dias. Ajuste o `DayEmbedding` no arquivo `model.py` se sua base de dados tiver um valor diferente.
- Conheça o valor máximo de `t` e ajuste o `TimeEmbedding` em `model.py` para esse valor específico.
- Informe as coordenadas máximas, verificando os valores máximos de `x` e `y`. Ajuste o `LocationXEmbeddingModel` e o `LocationYEmbeddingModel`, bem como a variável `max_x` em `train_task1.py`, para corresponder ao valor máximo de `x` na sua base de dados de entrada.

Com essas configurações, o LP-BERT estará pronto para ser executado de forma adequada com seus dados.