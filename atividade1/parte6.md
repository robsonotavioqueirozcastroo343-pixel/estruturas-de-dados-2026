## PARTE 6 – ANÁLISE E CONCLUSÃO

### Conclusão Comparando os Experimentos Realizados

Ao longo desta atividade, foi possível observar na prática como o **tamanho da entrada** influencia diretamente o **número de operações** realizadas por diferentes algoritmos, independentemente de todos produzirem resultados corretos ao final.

No experimento de ordenação (Parte 2), o Bubble Sort e o Quick Sort produziram exatamente o mesmo array ordenado, mas com quantidades de operações completamente diferentes: para 1.000 elementos, o Bubble Sort precisou de quase 500 mil comparações, enquanto o Quick Sort resolveu o problema com pouco mais de 11 mil. Essa diferença ilustra na prática a distinção entre complexidade **O(n²)** e **O(n log n)**.

No experimento de busca em matrizes (Parte 3), ficou evidente que o número de comparações depende diretamente de **onde** o valor procurado está localizado: buscas no início custam pouquíssimas operações, enquanto buscas no final ou por valores inexistentes exigem percorrer a matriz inteira — o que caracteriza o comportamento O(m × n).

Os Hands On (Partes 4 e 5) reforçaram esse raciocínio em contextos aplicados: o array de temperaturas (O(n)) e a matriz de sensores (O(m × n)) mostraram que, mesmo em problemas do cotidiano — como monitorar sensores por 24 horas —, a estrutura de dados escolhida e a forma como ela é percorrida têm impacto direto na eficiência do programa.

### Respostas às Questões

**1. O aumento do tamanho da estrutura de dados influencia a quantidade de operações?**

Sim, e de forma decisiva. Em todos os experimentos realizados — ordenação, busca em matrizes, array de temperaturas e matriz de sensores —, o aumento do tamanho da entrada resultou em um aumento proporcional (ou mais que proporcional) no número de operações. A única diferença entre os algoritmos foi a **taxa** desse crescimento: linear (O(n)), quadrática (O(n²)) ou log-linear (O(n log n)), mas em nenhum caso o número de operações permaneceu constante conforme os dados cresciam.

**2. Bubble Sort e Quick Sort crescem da mesma maneira quando o número de elementos aumenta?**

Não. O Bubble Sort cresce de forma **quadrática** (O(n²)): ao multiplicar o tamanho da entrada por um fator k, o número de operações cresce aproximadamente por k². Já o Quick Sort cresce de forma **log-linear** (O(n log n)), muito mais lenta: multiplicar o tamanho da entrada por k faz o número de operações crescer por aproximadamente k × log(k). Essa diferença de comportamento assintótico é exatamente o que foi observado experimentalmente na Parte 2, onde a distância entre os dois algoritmos aumentou drasticamente conforme o array cresceu de 10 para 1.000 elementos.

**3. Por que analisar somente o resultado final da ordenação não é suficiente para comparar algoritmos?**

Porque **dois algoritmos podem chegar exatamente ao mesmo resultado final e, ainda assim, gastar quantidades completamente diferentes de recursos computacionais** para chegar lá. Se a comparação fosse feita apenas observando se o array ficou ordenado corretamente, Bubble Sort e Quick Sort pareceriam equivalentes — afinal, ambos produzem a mesma saída. Só ao contabilizar o número de comparações e trocas/movimentações é que a real diferença de eficiência entre os algoritmos se torna visível. Essa é, inclusive, a ideia central de toda a atividade: **o "como" um algoritmo chega ao resultado é tão importante quanto o resultado em si**, especialmente quando o volume de dados cresce e a eficiência passa a impactar diretamente o tempo e os recursos necessários para a execução do programa.
