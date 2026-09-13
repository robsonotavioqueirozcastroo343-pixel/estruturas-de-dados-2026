# Central de Distribuição de Pedidos — Comparação de Algoritmos de Ordenação

## Objetivo
Comparar experimentalmente o número de **comparações** e **trocas/movimentações**
realizadas por quatro algoritmos de ordenação (Bubble Sort, Insertion Sort,
Selection Sort e Quick Sort) ao ordenar códigos de prioridade de pedidos, para
vetores de 10, 20 e 1.000 elementos.

O código completo está em [`ordenacao.py`](ordenacao.py).

## Critério de contagem utilizado

- **Comparações**: toda vez que dois elementos do vetor são comparados entre
  si (ex.: `if a[j] > a[j+1]`).
- **Trocas / Movimentações**:
  - *Bubble Sort* e *Selection Sort*: cada troca de posição (`swap`) entre
    dois elementos conta como **1 troca**.
  - *Insertion Sort*: não há `swap` clássico — os elementos maiores são
    deslocados uma posição à frente para abrir espaço para o elemento sendo
    inserido. Cada deslocamento conta como **1 movimentação**, e a inserção
    final do elemento na posição correta também conta como **1
    movimentação**.
  - *Quick Sort*: cada troca (`swap`) realizada durante o particionamento
    conta como **1 movimentação**.

Todos os quatro algoritmos recebem, em cada experimento, uma cópia do
**mesmo** vetor gerado aleatoriamente, garantindo comparação justa.

---

## Etapa 3 — Resultados (vetor aleatório)

| Tamanho | Bubble Comp. | Bubble Trocas | Insertion Comp. | Insertion Mov. | Selection Comp. | Selection Trocas | Quick Comp. | Quick Mov. |
|:-------:|:------------:|:-------------:|:----------------:|:----------------:|:-----------------:|:------------------:|:------------:|:-----------:|
| 10      | 45           | 26            | 33               | 35               | 45                | 6                   | 29           | 15          |
| 20      | 175          | 87            | 101              | 106              | 190               | 15                  | 65           | 41          |
| 1.000   | 498.324      | 243.438       | 244.432          | 244.437          | 499.500           | 990                 | 10.218       | 6.231       |

*(valores gerados com `random.seed(42)`; execuções são reprodutíveis rodando `ordenacao.py`)*

---

## Etapa 4 — Análise dos resultados

**a) Qual algoritmo realizou o menor número de comparações para 10 elementos?**
O Quick Sort, com 29 comparações, contra 45 do Bubble Sort, 33 do Insertion
Sort e 45 do Selection Sort.

**b) Qual algoritmo realizou menos trocas ou movimentações?**
O Selection Sort, com apenas 6 trocas. Isso é esperado: o Selection Sort faz
no máximo uma troca por passagem (ele só troca depois de já ter encontrado o
menor elemento do restante do vetor), enquanto Bubble, Insertion e Quick
podem mover elementos várias vezes por passagem.

**c) O comportamento observado para 10 elementos permaneceu semelhante
quando o tamanho aumentou para 20?**
Sim, a ordem relativa entre os algoritmos se manteve: Selection Sort continua
com o menor número de trocas (15) e Quick Sort continua com o menor número de
comparações (65). O crescimento também já mostra o padrão esperado — Bubble e
Selection quase quadruplicam suas comparações (dobrar o tamanho → ~4x mais
operações, característica de O(n²)), enquanto o Quick Sort cresce de forma
bem mais modesta.

**d) O que aconteceu com a quantidade de operações quando o vetor passou
para 1.000 elementos?**
A diferença entre os algoritmos ficou muito mais evidente. Bubble Sort e
Selection Sort chegaram a praticamente 500.000 comparações cada (≈ n²/2), e o
Insertion Sort teve um número semelhante de comparações e movimentações no
caso médio aleatório. Já o Quick Sort precisou de apenas 10.218 comparações e
6.231 movimentações — uma diferença de quase 50x em relação aos algoritmos
O(n²). Isso confirma experimentalmente a diferença entre um crescimento
quadrático (n²) e um crescimento quasilinear (n log n).

**e) Bubble Sort, Insertion Sort e Selection Sort apresentam complexidade
O(n²) em situações típicas estudadas. Eles apresentaram exatamente a mesma
quantidade de operações? Explique utilizando seus resultados.**
Não. Apesar de os três serem O(n²) assintoticamente, os valores absolutos são
diferentes porque cada algoritmo compara/move os elementos de formas
distintas:
- Para 1.000 elementos, Bubble Sort fez 498.324 comparações e 243.438 trocas;
- Insertion Sort fez 244.432 comparações e 244.437 movimentações;
- Selection Sort fez 499.500 comparações (sempre o pior caso, pois percorre
  todo o restante do vetor mesmo se já estiver ordenado) e apenas 990 trocas.

O Selection Sort sempre faz ~n²/2 comparações, independente da ordem inicial
dos dados, pois sempre varre o restante do vetor em busca do mínimo. Já
Bubble e Insertion podem ter seu número de comparações reduzido quando o
vetor já está parcialmente ordenado (o Bubble Sort implementado tem
otimização de parada antecipada, e o Insertion Sort para de comparar assim
que encontra a posição correta). Por isso, mesmo pertencendo à mesma classe
de complexidade O(n²), os números absolutos de operações diferem
consideravelmente.

**f) Qual algoritmo apresentou maior crescimento no número de operações?**
O Selection Sort e o Bubble Sort, que se aproximam de n²/2 comparações,
tiveram o maior crescimento em termos absolutos ao passar de 20 para 1.000
elementos (crescimento de ordem quadrática). O Selection Sort, em particular,
apresentou sempre exatamente n(n-1)/2 comparações (190 → 499.500),
confirmando visualmente o comportamento O(n²) mais "puro" entre os quatro.

**g) Como o comportamento experimental do Quick Sort se diferenciou dos
demais algoritmos?**
O Quick Sort cresceu de forma muito mais lenta que os demais à medida que o
tamanho do vetor aumentou — passando de 65 comparações (n=20) para apenas
10.218 (n=1.000), um crescimento muito abaixo do quadrático, coerente com sua
complexidade média O(n log n). Ele "paga" um pouco mais em movimentações
relativas por conta do particionamento, mas ainda assim fica muito abaixo dos
algoritmos O(n²) para vetores grandes.

**h) Os resultados encontrados são coerentes com as complexidades teóricas
estudadas?**
Sim. Bubble, Insertion e Selection mostraram crescimento compatível com O(n²)
— ao multiplicar o tamanho do vetor por ~50 (de 20 para 1.000), o número de
comparações cresceu por um fator próximo de 2.500 (50²), como esperado para
uma função quadrática. O Quick Sort, por sua vez, cresceu de forma muito mais
suave, compatível com O(n log n), confirmando a teoria.

**i) Se você fosse responsável pelo sistema da central de distribuição e
precisasse ordenar milhares de pedidos, qual dos quatro algoritmos
escolheria? Justifique utilizando os resultados do experimento.**
Escolheria o **Quick Sort**. Para 1.000 elementos ele realizou cerca de 50
vezes menos comparações que Bubble e Selection Sort, mantendo desempenho
ótimo mesmo com o aumento do volume de pedidos — algo essencial em uma
central de distribuição, onde o número de pedidos diários pode crescer
rapidamente. Os algoritmos O(n²) seriam inviáveis em produção a partir de
alguns milhares de itens, pois o tempo de execução cresceria de forma
proibitiva.

---

## Desafio adicional — Influência da organização inicial dos dados

Foi repetido o experimento (mesmos tamanhos) usando três organizações
iniciais diferentes para o vetor: **aleatório**, **já ordenado** e **em
ordem inversa**.

### Vetor já ordenado

| Tamanho | Bubble Comp. | Bubble Trocas | Insertion Comp. | Insertion Mov. | Selection Comp. | Selection Trocas | Quick Comp. | Quick Mov. |
|:-------:|:------------:|:-------------:|:----------------:|:----------------:|:-----------------:|:------------------:|:------------:|:-----------:|
| 10      | 9            | 0             | 9                | 9                 | 45                 | 0                   | 45           | 54          |
| 20      | 19           | 0             | 19               | 19                | 190                | 0                   | 190          | 209         |
| 1.000   | 999          | 0             | 999              | 999               | 499.500            | 0                   | 499.500      | 500.499     |

### Vetor em ordem inversa (pior caso)

| Tamanho | Bubble Comp. | Bubble Trocas | Insertion Comp. | Insertion Mov. | Selection Comp. | Selection Trocas | Quick Comp. | Quick Mov. |
|:-------:|:------------:|:-------------:|:----------------:|:----------------:|:-----------------:|:------------------:|:------------:|:-----------:|
| 10      | 45           | 45            | 45               | 54                | 45                 | 5                   | 45           | 29          |
| 20      | 190          | 190           | 190              | 209               | 190                | 10                  | 190          | 109         |
| 1.000   | 499.500      | 499.500       | 499.500          | 500.499           | 499.500            | 500                 | 499.500      | 250.499     |

### Análise

**A organização inicial dos dados interfere na quantidade de operações
realizadas por todos os algoritmos da mesma maneira?** Não, cada algoritmo
reage de forma diferente:

- **Bubble Sort**: é o que mais se beneficia de dados já ordenados — com o
  vetor ordenado, faz apenas O(n) comparações (999 para n=1.000) e **zero**
  trocas, graças à otimização de parada antecipada (`if not trocou: break`).
  Já com o vetor invertido, é o pior caso possível: todas as comparações
  resultam em troca (499.500 comparações e 499.500 trocas).
- **Insertion Sort**: apresenta o mesmo padrão do Bubble Sort — melhor caso
  O(n) quando já ordenado (cada elemento é comparado só uma vez com o
  anterior e não precisa se mover), e pior caso O(n²) quando invertido (cada
  novo elemento precisa "descer" até o início do vetor).
- **Selection Sort**: **não é sensível** à ordem inicial dos dados em termos
  de comparações — sempre faz exatamente n(n−1)/2 comparações (499.500 nos
  três cenários para n=1.000), pois sempre varre o vetor inteiro em busca do
  mínimo. O que muda é apenas o número de trocas: 0 quando já está ordenado,
  até n/2 no pior caso (vetor invertido).
- **Quick Sort (pivô = último elemento)**: é o único que se comporta de
  forma **contraintuitiva** — funciona muito bem com dados aleatórios (apenas
  10.218 comparações para n=1.000), mas atinge seu **pior caso O(n²)**
  exatamente quando o vetor já está ordenado ou totalmente invertido
  (499.500 comparações, igual a Bubble/Selection!). Isso acontece porque o
  pivô escolhido (o último elemento) sempre gera uma partição extremamente
  desbalanceada nesses casos, fazendo a recursão degenerar para
  profundidade n (na prática, isso até exigiu aumentar o limite de recursão
  do Python no experimento, `sys.setrecursionlimit`, para vetores de 1.000
  elementos ordenados/invertidos).

**Conclusão do desafio**: a organização inicial dos dados **não afeta
igualmente** os quatro algoritmos. Bubble e Insertion Sort melhoram muito com
dados já ordenados; o Selection Sort é praticamente imune à ordem inicial (em
comparações); e o Quick Sort, justamente o mais eficiente no caso médio, é o
que mais sofre com entradas já ordenadas ou invertidas quando o pivô é
escolhido de forma ingênua (último elemento). Na prática, implementações
profissionais de Quick Sort usam estratégias como pivô aleatório ou
"mediana de três" exatamente para evitar esse pior caso.
