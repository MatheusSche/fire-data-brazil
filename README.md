# fire-data-brazil

Atividades a realizar
1) Definição do contexto a ser explorado: escolha um dos contextos a seguir:
- eleições municipais 2020
- queimadas no Brasil
2) Montagem do arquivo de dados
A primeira atividade do trabalho envolve a construção do arquivo de dados. Para tanto,
cada equipe deve escolher o contexto que será considerado, e para esse contexto
definir uma ou mais hipóteses (perguntas) a serem testadas em uma rede social.
Assim, as seguintes tarefas deverão ser realizadas:
● Definir uma ou mais hipóteses (serão as consultas que serão realizadas nos dados);
● Escolher a rede social a ser utilizada, e pesquisar como é possível extrair os dados
dela (e se há restrições para a extração, como por exemplo se há uma quantidade
máxima de dados que podem ser extraídos por dia);
● Extrair os dados, fazer uma limpeza e preparar a carga dos dados, definindo a
estrutura da base de dados para, no mínimo, 10 mil linhas com conteúdo válido.
Para a extração dos dados de uma rede social, cada equipe poderá desenvolver o seu
próprio código ou poderá utilizar um código disponível na internet para a extração de dados
da rede social. Sugere-se o uso da rede social Twitter, pela facilidade de uso das APIs, mas
pode ser outra.
2.1) Registros do Arquivo de Dados:
Twitter: a estrutura do registro a ser utilizado para os dados extraídos da rede social Twitter
é composta pelos campos id_twitter (inteiro, chave primária), usuário (caractere de 20
posições), mensagem (caractere de 280 posições), data (caractere de 8 posições), país
(caractere de 20 posições) e hashtags (caractere de 200 posições).
Para a implementação dessa funcionalidade deve-se criar um registro de tamanho fixo
com o caractere ‘\n’ de final de linha (opcional) e sem separador entre os campos
(obrigatório) em uma linguagem de programação (C, C#, C++, Python, PHP, Java ...) que
possua o comando seek.
Se outra rede social for a escolhida, estes campos podem ser adequados aos dados
extraídos, assim como as demais orientações apresentadas nas demais explicações do
trabalho.
Organização de Arquivo de Dados:
● Criar o registro de dados descrito acima para a organização de arquivo do tipo
sequencial usando registro de tamanho fixo com o caractere ‘\n’ de final de linha
(opcional) e sem separador entre os campos (obrigatório).
● Implementar:
○ 1) um procedimento para inserir as, no mínimo, 10 mil linhas de dados,
○ 2) um procedimento para mostrar os dados,
○ 3) um procedimento para realizar a pesquisa binária e
○ 4) um procedimento para consultar dados a partir da pesquisa binária.
Os dados devem ser coletados ao longo do mês de outubro de 2020 (podem ser coletados
dados anteriores se for possível).
2.2) Índices em arquivo:
● Implemente um arquivo de índice para o campo id_twitter de acordo com a
descrição do índice de arquivo da organização sequencial-indexado. Implemente
um procedimento de consulta a partir deste índice usando a pesquisa binária
para pesquisar no arquivo de índice e, depois o comando seek para pesquisar no
arquivo de dados.
● Implemente um arquivo de índice para o campo hashtags de acordo com a
descrição do índice de arquivo da organização sequencial-indexado. Implemente
um procedimento de consulta a partir deste índice usando a pesquisa binária
para pesquisar no arquivo de índice e, depois o comando seek para pesquisar no
arquivo de dados.
Índices em memória:
● Implemente uma estrutura de hash em memória para o campo data. Implemente
um procedimento de consulta a partir deste índice e, depois o comando seek para
pesquisar no arquivo de dados.
● Implemente uma estrutura de árvore binária para o campo hashtags. Implemente
um procedimento de consulta a partir deste índice e, depois o comando seek para
pesquisar no arquivo de dados.
3) Resposta à(s) hipótese(s):
Implemente um procedimento para responder a hipótese (ou as hipóteses) definida no início
do trabalho.
