## PARTE 3 – INVESTIGAÇÃO DE BUSCA EM MATRIZES

### Código do Experimento (Python)

```python
def busca_sequencial_matriz(matriz, valor_procurado):
    comparacoes = 0
    linhas = len(matriz)
    colunas = len(matriz[0]) if linhas > 0 else 0
    
    for i in range(linhas):
        for j in range(colunas):
            comparacoes += 1
            if matriz[i][j] == valor_procurado:
                return {
                    "encontrado": True,
                    "linha": i,
                    "coluna": j,
                    "comparacoes": comparacoes
                }
                
    return {
        "encontrado": False,
        "linha": -1,
        "coluna": -1,
        "comparacoes": comparacoes
    }

# Exemplo de uso para testes:
# matriz_exemplo = [[1, 2], [3, 4]]
# resultado = busca_sequencial_matriz(matriz_exemplo, 4)
# print(resultado)
```

### Tabela de Resultados (Quantidade de Comparações)

Os números abaixo representam a quantidade exata de comparações realizadas em cada cenário:

| Matriz | Nº de elementos | Busca no início | Busca no final | Valor inexistente |
| :---: | :---: | :---: | :---: | :---: |
| **2 × 2** | 4 | 1 | 4 | 4 |
| **10 × 10** | 100 | 1 | 100 | 100 |
| **100 × 100** | 10.000 | 1 | 10.000 | 10.000 |

### Respostas do Questionário

*   **a) Por que encontrar um elemento no início exige menos operações?**
    Porque a busca sequencial utiliza uma estrutura de interrupção imediata (`break` ou `return`). Assim que o valor procurado coincide com o elemento atual da matriz, o algoritmo encerra a execução e não precisa varrer o restante da estrutura. No melhor caso (primeira posição), apenas **1 comparação** é necessária.

*   **b) O que acontece quando o elemento procurado não existe?**
    O algoritmo é obrigado a percorrer **todas as posições possíveis** da matriz (todas as linhas e colunas) para garantir com certeza absoluta que o número não está lá. Isso resulta no número máximo de comparações permitido pelo tamanho da estrutura.

*   **c) Qual é o pior caso da busca sequencial?**
    O pior caso ocorre em duas situações equivalentes em esforço computacional: quando o elemento está localizado na **última posição da matriz** (última linha, última coluna) ou quando o elemento **não existe** na matriz.

*   **d) Como o aumento das dimensões da matriz influencia a quantidade de operações?**
    O aumento influencia de forma **quadrática** (caso a matriz seja quadrada, $n \times n$). Se multiplicarmos o tamanho da lateral da matriz por 10 (de 10 para 100), o número de operações máximas aumenta 100 vezes (de 100 para 10.000), demonstrando que o esforço cresce muito rápido conforme a estrutura expande.

*   **e) Qual a complexidade da busca sequencial em uma matriz com $m$ linhas e $n$ colunas?**
    A complexidade no pior caso é **$O(m \times n)$**, onde o algoritmo precisa realizar um número de operações proporcional ao produto total de linhas e colunas. Caso a matriz seja quadrada ($n \times n$), a complexidade pode ser simplificada como **$O(n^2)$**.
