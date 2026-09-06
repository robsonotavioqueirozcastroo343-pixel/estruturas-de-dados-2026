# PARTE 2 – EXPERIMENTO DE ORDENAÇÃO

Comparação experimental entre **Bubble Sort** e **Quick Sort**, contabilizando o número de operações (comparações e trocas/movimentações) realizadas durante a ordenação de arrays de 10, 20 e 1.000 elementos.

Os dois algoritmos recebem exatamente os mesmos dados de entrada (mesma semente aleatória, cópias independentes do array original), conforme pede o enunciado.

## Código

Veja [`parte2_ordenacao.py`](./parte2_ordenacao.py).

- **`bubble_sort`**: implementação clássica, com flag de parada antecipada (se uma passagem não faz trocas, o array já está ordenado). Conta cada comparação e cada troca.
- **`quick_sort`**: particionamento estilo Lomuto (pivô = último elemento). Conta cada comparação com o pivô e cada movimentação feita durante o particionamento.

Para rodar:
```bash
python3 parte2_ordenacao.py
```

## Tabela de resultados

| Tamanho do Array | Bubble Sort – Comparações | Bubble Sort – Trocas | Quick Sort – Comparações | Quick Sort – Movimentações |
|---|---|---|---|---|
| 10 | 45 | 26 | 29 | 15 |
| 20 | 187 | 114 | 62 | 44 |
| 1.000 | 499.329 | 241.624 | 10.695 | 6.335 |

**Tempos de execução (informação adicional, em segundos):**

| Tamanho | Bubble Sort | Quick Sort |
|---|---|---|
| 10 | 0,000007s | 0,000034s |
| 20 | 0,000014s | 0,000020s |
| 1.000 | 0,034976s | 0,001196s |

## Respostas

**a) Qual algoritmo realizou menos operações para 10 elementos?**

O Quick Sort (29 comparações + 15 movimentações = 44 operações) contra o Bubble Sort (45 comparações + 26 trocas = 71 operações). Para arrays muito pequenos a diferença já aparece, mas não é dramática.

**b) O comportamento permaneceu igual para 20 elementos?**

Não. A diferença já cresce: o Bubble Sort quase dobrou o número de comparações (187 contra 45), enquanto o Quick Sort cresceu de forma bem mais discreta (62 contra 29). A vantagem do Quick Sort começa a ficar mais evidente.

**c) O que aconteceu quando o tamanho aumentou para 1.000?**

A diferença se tornou brutal: o Bubble Sort precisou de quase 500 mil comparações, enquanto o Quick Sort precisou de pouco mais de 10 mil — quase **50 vezes menos**.

**d) Qual algoritmo apresentou maior crescimento da quantidade de operações?**

O Bubble Sort. Seu crescimento é quadrático (O(n²)): ao multiplicar o tamanho por 50 (de 20 para 1.000), o número de operações cresceu por um fator muito maior que 50. O Quick Sort, por ser O(n log n), cresce de forma bem mais suave.

**e) Os resultados experimentais são coerentes com as complexidades teóricas estudadas?**

Sim. Bubble Sort O(n²) e Quick Sort O(n log n) no caso médio batem exatamente com o padrão observado: a distância entre os dois aumenta conforme n cresce, como a teoria prevê.

**f) Em qual situação você escolheria Bubble Sort?**

Para arrays pequenos, quase ordenados, ou em contextos didáticos onde a simplicidade de implementação importa mais que performance.

**g) Em qual situação você escolheria Quick Sort?**

Para qualquer array de tamanho médio/grande, onde performance é relevante e há cuidado na escolha do pivô (evitando o pior caso O(n²)).
