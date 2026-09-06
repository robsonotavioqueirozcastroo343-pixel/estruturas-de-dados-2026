
# ATIVIDADE AVALIATIVA – ESTRUTURAS DE DADOS
## Arrays, Matrizes, Algoritmos de Ordenação e Busca

---

## PARTE 1 – PESQUISA: BUBBLE SORT E QUICK SORT

### Bubble Sort

**Como funciona / lógica de ordenação:**

O algoritmo percorre o array repetidamente, comparando pares de elementos adjacentes e trocando-os de posição quando estão fora de ordem. A cada passagem completa, o maior elemento "borbulha" até o final do array (por isso o nome). O processo se repete até que uma passagem inteira não precise fazer nenhuma troca, sinal de que o array está ordenado.

Passo a passo:
1. Compara `array[i]` com `array[i+1]`.
2. Se `array[i] > array[i+1]`, troca os dois.
3. Avança para o próximo par.
4. Ao fim de cada passagem, o maior valor não ordenado já está na posição correta.
5. Repete até não haver mais trocas.

**Complexidade:**
- Melhor caso: **O(n)** — ocorre quando o array já está ordenado (com otimização de flag de parada antecipada).
- Caso médio: **O(n²)**
- Pior caso: **O(n²)** — array em ordem inversa.

**Vantagens:**
- Extremamente simples de entender e implementar.
- Ordenação *in-place* (não precisa de memória extra significativa).
- Estável (mantém a ordem relativa de elementos iguais).
- Detecta rapidamente se o array já está ordenado (com otimização).

**Limitações:**
- Muito ineficiente para grandes volumes de dados.
- Número de comparações e trocas cresce quadraticamente.

**Situações em que seu uso é adequado:**
- Conjuntos de dados pequenos.
- Fins didáticos, para ensinar lógica de ordenação.
- Quando o array já está quase ordenado.

**Situações em que seu uso não é recomendado:**
- Grandes volumes de dados (milhares/milhões de elementos).
- Aplicações que exigem alta performance.

---

### Quick Sort

**Como funciona / lógica de ordenação:**

Usa a estratégia de "dividir para conquistar" (*divide and conquer*). Escolhe um elemento como **pivô**, particiona o array de modo que todos os elementos menores que o pivô fiquem à esquerda e os maiores à direita. Em seguida, aplica recursivamente o mesmo processo às duas partições.

Passo a passo:
1. Escolhe um pivô (pode ser o primeiro, último, do meio ou aleatório).
2. Particiona o array: elementos menores à esquerda do pivô, maiores à direita.
3. Aplica Quick Sort recursivamente na partição esquerda.
4. Aplica Quick Sort recursivamente na partição direita.
5. Quando a partição tem 0 ou 1 elemento, já está ordenada (caso base).

**Complexidade:**
- Melhor caso: **O(n log n)** — partições balanceadas.
- Caso médio: **O(n log n)**
- Pior caso: **O(n²)** — ocorre quando o pivô escolhido é sempre o menor ou maior elemento (ex.: array já ordenado com pivô mal escolhido), gerando partições muito desbalanceadas.

**Vantagens:**
- Muito eficiente na prática para grandes volumes de dados.
- Bom uso de cache (acessos localizados na memória).
- Amplamente usado em bibliotecas de linguagens de programação.

**Limitações:**
- Pior caso quadrático se o pivô for mal escolhido.
- Não é estável por padrão.
- Recursão pode consumir pilha de memória (O(log n) no caso médio, O(n) no pior caso).

**Situações em que seu uso é adequado:**
- Grandes volumes de dados.
- Quando performance é prioridade e a instabilidade não é problema.

**Situações em que seu uso não é recomendado:**
- Quando a estabilidade da ordenação é obrigatória (sem adaptações).
- Em sistemas com restrição severa de memória de pilha (recursão profunda no pior caso).
- Dados já ordenados ou quase ordenados, se a escolha do pivô não for cuidadosa (ex.: pivô sempre o primeiro elemento).

---

### Tabela comparativa

| Característica | Bubble Sort | Quick Sort |
|---|---|---|
| Princípio de funcionamento | Comparação e troca de elementos adjacentes repetidamente | Divisão e conquista via particionamento em torno de um pivô |
| Melhor caso | O(n) | O(n log n) |
| Caso médio | O(n²) | O(n log n) |
| Pior caso | O(n²) | O(n²) |
| Uso de memória | In-place, O(1) extra | In-place, mas O(log n) a O(n) de pilha de recursão |
| Vantagem principal | Simplicidade e estabilidade | Alta eficiência em grandes volumes |
| Limitação principal | Ineficiente para grandes entradas | Pior caso ruim com pivô mal escolhido; instável |
| Aplicação recomendada | Conjuntos pequenos ou quase ordenados; fins didáticos | Conjuntos grandes onde performance é essencial |
