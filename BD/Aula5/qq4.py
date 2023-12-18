# Uma colisão em tabelas hash ocorre quando dois ou mais elementos têm a mesma posição de índice após a aplicação da função de hash. Como cada posição da tabela hash deve corresponder a uma chave única, a colisão pode levar a conflitos e dificuldades na recuperação eficiente dos valores associados às chaves.

# Existem várias maneiras de resolver o problema das colisões em tabelas hash, e duas das abordagens mais comuns são:

# Encadeamento Separado (Chaining):

# Nessa abordagem, cada posição da tabela hash contém uma lista (ou estrutura de dados similar, como uma árvore) que armazena todos os elementos que mapeiam para essa posição.
# Quando ocorre uma colisão, os elementos são simplesmente adicionados à lista correspondente à posição de índice.
# A busca por um valor associado a uma chave envolve procurar na lista correspondente à posição de índice.
# Endereçamento Aberto (Open Addressing):

# Nesta abordagem, os elementos colidentes são inseridos diretamente em outras posições da tabela hash, seguindo uma estratégia de sondagem até encontrar uma posição vazia.
# Existem várias técnicas de sondagem, como sondagem linear, sondagem quadrática e sondagem dupla, cada uma determinando como a busca por uma posição vazia deve ser feita.
# A busca por um valor associado a uma chave também envolve percorrer a tabela hash, seguindo a estratégia de sondagem até encontrar a chave desejada ou uma posição vazia.
# A escolha entre encadeamento separado e endereçamento aberto depende das características específicas do sistema e dos requisitos da aplicação. Em geral, encadeamento separado é mais flexível e fácil de implementar, enquanto endereçamento aberto pode ser mais eficiente em termos de espaço e acesso direto à tabela. Ambas as abordagens têm vantagens e desvantagens, e a escolha depende do contexto específico.