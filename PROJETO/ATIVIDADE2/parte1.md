# ATIVIDADE AVALIATIVA – ESTRUTURAS DE DOS
## Arrays, Matrizes, Algoritmos de Ordenação e Busca

---

## PARTE 1 – PESQUISA: BUBBLE SORT E QUICK SORT

### 1. Bubble Sort

#### Como funciona / lógica de ordenação:
O algoritmo percorre o array repetidamente, comparando pares de elementos adjacentes e trocando-os de posição quando estão fora de ordem. A cada passagem completa, o maior elemento "borbulha" até o final do array. O processo se repete até que uma passagem inteira ocorra sem nenhuma troca, indicando que o array está ordenado.

#### Complexidade de Tempo:
*   **Melhor caso:** $O(n)$ – Ocorre quando o array já está ordenado (necessita de uma otimização com flag de parada antecipada).
*   **Caso médio:** $O(n^2)$ – Comparações e trocas crescem quadraticamente.
*   **Pior caso:** $O(n^2)$ – Ocorre quando o array está em ordem inversamente ordenada.

#### Vantagens:
*   Extremamente simples de entender e implementar.
*   Algoritmo *in-place* (não exige memória extra significativa).
*   Algoritmo estável (mantém a ordem relativa de elementos iguais).

#### Limitações:
*   Altamente ineficiente para grandes volumes de dados.
*   O número de trocas e comparações cresce muito rápido conforme $n$ aumenta.

#### Situações de uso adequado:
*   Fins educacionais para introduzir o conceito de ordenação.
*   Arrays pequenos onde a simplicidade do código importa mais do que a performance.
*   Arrays que já estão quase totalmente ordenados.

#### Situações não recomendadas:
*   Aplicações comerciais ou sistemas de produção.
*   Conjuntos de dados de médio a grande porte.

---

### 2. Quick Sort

#### Como funciona / lógica de ordenação:
Baseia-se na estratégia de **Divisão e Conquista**. O algoritmo escolhe um elemento como **pivô** e particiona o array de modo que todos os elementos menores que o pivô fiquem à sua esquerda e os maiores à sua direita. O processo é aplicado recursivamente nas subpartições esquerda e direita até que todo o array esteja ordenado.

#### Complexidade de Tempo:
*   **Melhor caso:** $O(n \log n)$ – Ocorre quando o pivô divide o array sempre em duas metades balanceadas.
*   **Caso médio:** $O(n \log n)$ – Na grande maioria dos cenários reais com distribuições aleatórias.
*   **Pior caso:** $O(n^2)$ – Ocorre quando o pivô escolhido é repetidamente o maior ou o menor elemento (ex: array já ordenado usando o primeiro elemento como pivô).

#### Vantagens:
*   Extremamente veloz no caso médio.
*   Possui excelente localidade de referência (aproveita bem o cache do processador).
*   Ordenação eficiente diretamente no array original (*in-place* para os dados, embora gaste memória com a pilha de recursão).

#### Limitações:
*   Algoritmo instável (pode alterar a ordem relativa de elementos de mesmo valor).
*   A performance degrada fortemente para $O(n^2)$ se a escolha do pivô for ruim.
*   Implementação recursiva pode causar estouro de pilha (*stack overflow*) se não for controlada.

#### Situações de uso adequado:
*   Ordenação de grandes volumes de dados de uso geral.
*   Sistemas onde a velocidade média de execução é o fator crítico.

#### Situações não recomendadas:
*   Sistemas críticos de tempo real onde o pior caso ($O(n^2)$) nunca pode acontecer de forma alguma.
*   Aplicações que exigem estritamente uma ordenação estável.

---

### Tabela Comparativa

| Característica | Bubble Sort | Quick Sort |
| :--- | :--- | :--- |
| **Princípio de funcionamento** | Comparação e troca consecutiva de elementos adjacentes. | Divisão e conquista através do particionamento por um pivô. |
| **Melhor caso** | $O(n)$ (com otimização de flag) | $O(n \log n)$ |
| **Caso médio** | $O(n^2)$ | $O(n \log n)$ |
| **Pior caso** | $O(n^2)$ | $O(n^2)$ (se o pivô for ruim) |
| **Uso de memória** | $O(1)$ – Não consome memória extra. | $O(\log n)$ – Consumo devido à pilha de recursão. |
| **Vantagem principal** | Simplicidade extrema e estabilidade dos dados. | Altíssima velocidade no cenário prático e do dia a dia. |
| **Limitação principal** | Lentidão extrema para conjuntos médios ou grandes. | Instabilidade e queda de rendimento no pior caso. |
| **Aplicação recomendada** | Listas minúsculas ou quase totalmente ordenadas. | Grandes arrays e bancos de dados generalistas. |
