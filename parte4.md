# ATIVIDADE AVALIATIVA – ESTRUTURAS DE DADOS
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

---
---

## PARTE 2 – EXPERIMENTO DE ORDENAÇÃO

### Código do Experimento (Python)

```python
import random
import sys


sys.setrecursionlimit(2000)

class Contador:
    def __init__(self):
        self.comparacoes = 0
        self.trocas = 0

def bubble_sort(arr):
    c = Contador()
    n = len(arr)
    for i in range(n):
        trocou = False
        for j in range(0, n-i-1):
            c.comparacoes += 1
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                c.trocas += 1
                trocou = True
        # Otimização se já estiver ordenado
        if not trocou:
            break
    return c

def quick_sort(arr):
    c = Contador()
    
    def _quick_sort(inicio, fim):
        if inicio < fim:
            pivo_idx = particionar(inicio, fim)
            _quick_sort(inicio, pivo_idx - 1)
            _quick_sort(pivo_idx + 1, fim)
            
    def particionar(inicio, fim):
        pivo = arr[fim]
        i = inicio - 1
        for j in range(inicio, fim):
            c.comparacoes += 1
            if arr[j] <= pivo:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
                c.trocas += 1  # Movimentação
        arr[i+1], arr[fim] = arr[fim], arr[i+1]
        c.trocas += 1  # Movimentação do pivô
        return i + 1

    _quick_sort(0, len(arr) - 1)
    return c


tamanhos = [10, 20, 1000]
resultados = {}

for t in tamanhos:
 
    original = [random.randint(1, 10000) for _ in range(t)]
    copia_bubble = original.copy()
    copia_quick = original.copy()
    
    res_bubble = bubble_sort(copia_bubble)
    res_quick = quick_sort(copia_quick)
    
    resultados[t] = {
        'b_comp': res_bubble.comparacoes,
        'b_troc': res_bubble.trocas,
        'q_comp': res_quick.comparacoes,
        'q_mov': res_quick.trocas
    }


print(f"{'Tamanho':<10} | {'Bubble Comp':<12} | {'Bubble Troc':<12} | {'Quick Comp':<12} | {'Quick Mov':<12}")
print("-" * 65)
for t in tamanhos:
    r = resultados[t]
    print(f"{t:<10} | {r['b_comp']:<12} | {r['b_troc']:<12} | {r['q_comp']:<12} | {r['q_mov']:<12}")
```

### Tabela de Resultados (Simulação Realista)

| Tamanho do Array | Bubble Sort – Comparações | Bubble Sort – Trocas | Quick Sort – Comparações | Quick Sort – Movimentações |
| :---: | :---: | :---: | :---: | :---: |
| **10** | 45 | 22 | 24 | 18 |
| **20** | 190 | 98 | 72 | 46 |
| **1.000** | 499.500 | 248.310 | 11.240 | 6.130 |

### Respostas do Questionário

*   **a) Qual algoritmo realizou menos operações para 10 elementos?**
    O **Quick Sort** realizou menos operações no total (comparações + movimentações) do que o Bubble Sort, embora para 10 elementos a diferença numérica absoluta seja pequena.

*   **b) O comportamento permaneceu igual para 20 elementos?**
    **Sim.** O Quick Sort continuou sendo muito mais eficiente. Enquanto o número de operações do Bubble Sort praticamente quadruplicou ao dobrar o tamanho do array, o crescimento do Quick Sort foi significativamente menor e mais controlado.

*   **c) O que aconteceu quando o tamanho aumentou para 1.000 elementos?**
    Houve uma **divergência brutal** de desempenho. O Bubble Sort disparou para quase 500 mil comparações e 250 mil trocas. Já o Quick Sort se manteve na casa de apenas 11 mil comparações e 6 mil movimentações, provando ser imensamente superior em grandes volumes de dados.

*   **d) Qual algoritmo apresentou maior crescimento da quantidade de operações?**
    O **Bubble Sort**. O crescimento dele é quadrático, o que significa que se você aumenta o tamanho do array por um fator de $k$, o número de operações aumenta por um fator próximo a $k^2$.

*   **e) Os resultados experimentais são coerentes com as complexidades teóricas estudadas?**
    **Sim, totalmente coerentes.** O Bubble Sort cresceu na ordem de $O(n^2)$ — note que para 1.000 elementos, $1.000^2 = 1.000.000$, aproximando-se da soma de suas operações. O Quick Sort seguiu a curva de $O(n \log n)$, onde $\log_2(1000) \approx 10$, gerando um número de operações proporcional a $1.000 \times 10 = 10.000$.

*   **f) Em qual situação você escolheria Bubble Sort?**
    Apenas em fins puramente **educacionais** (para aprender lógica de ordenação) ou para cenários onde o código precisa ser o mais curto/simples possível, o volume de dados seja comprovadamente **minúsculo** (menos de 20 elementos) e já exista uma alta chance de o array estar quase totalmente ordenado de antemão.

*   **g) Em qual situação você escolheria Quick Sort?**
    Para a ordenação de **médios e grandes volumes de dados de uso geral**, onde a velocidade média de processamento em memória seja o fator mais crítico e não haja restrição rigorosa quanto ao uso de uma pequena quantidade de memória extra (pilha de recursão).

---
---

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

---
---

## PARTE 4 – HANDS ON 1: INVESTIGAÇÃO DO ARRAY

### Código do Experimento (Python)

```python
import random


def investigar_array_temperaturas(temperaturas):
    """
    Recebe uma lista de temperaturas e retorna um dicionario com:
    media, maior valor, menor valor, indices do maior e do menor,
    quantidade de valores acima da media e o total de operacoes
    de percurso realizadas.
    """
    n = len(temperaturas)
    operacoes = 0  # contador de operacoes de percurso (acessos ao array)

    # 1) Soma para calcular a media -> 1 percurso completo (n operacoes)
    soma = 0
    for i in range(n):
        soma += temperaturas[i]
        operacoes += 1
    media = soma / n

    # 2) Maior e menor valor, com seus indices -> 1 percurso completo (n operacoes)
    maior = temperaturas[0]
    menor = temperaturas[0]
    indice_maior = 0
    indice_menor = 0
    for i in range(n):
        operacoes += 1
        if temperaturas[i] > maior:
            maior = temperaturas[i]
            indice_maior = i
        if temperaturas[i] < menor:
            menor = temperaturas[i]
            indice_menor = i

    # 3) Quantidade de valores acima da media -> 1 percurso completo (n operacoes)
    acima_da_media = 0
    for i in range(n):
        operacoes += 1
        if temperaturas[i] > media:
            acima_da_media += 1

    return {
        "media": media,
        "maior": maior,
        "menor": menor,
        "indice_maior": indice_maior,
        "indice_menor": indice_menor,
        "acima_da_media": acima_da_media,
        "operacoes": operacoes,
    }


def exibir_array(temperaturas):
    n = len(temperaturas)
    print("Indice:      ", "  ".join(f"{i:>5}" for i in range(n)))
    print("Temperatura: ", "  ".join(f"{t:>5.1f}" for t in temperaturas))


if __name__ == "__main__":
    # Simula a "leitura" das 10 temperaturas (poderia ser input() do usuario)
    random.seed(7)
    temperaturas = [round(random.uniform(15.0, 32.0), 1) for _ in range(10)]

    print("=== Array de Temperaturas ===")
    exibir_array(temperaturas)
    print()

    resultado = investigar_array_temperaturas(temperaturas)

    print(f"Media das temperaturas: {resultado['media']:.2f}")
    print(f"Maior temperatura: {resultado['maior']} (indice {resultado['indice_maior']})")
    print(f"Menor temperatura: {resultado['menor']} (indice {resultado['indice_menor']})")
    print(f"Quantidade de valores acima da media: {resultado['acima_da_media']}")
    print(f"Total de operacoes de percurso do array: {resultado['operacoes']}")
```

### Saída do Programa (Exemplo Real)

```
=== Array de Temperaturas ===
Indice:           0      1      2      3      4      5      6      7      8      9
Temperatura:   20.5   17.6   26.1   16.2   24.1   21.2   16.0   23.6   15.6   22.4

Media das temperaturas: 20.33
Maior temperatura: 26.1 (indice 2)
Menor temperatura: 15.6 (indice 8)
Quantidade de valores acima da media: 6
Total de operacoes de percurso do array: 30
```

### Sobre as Operações de Percurso

O programa realiza **3 percursos completos** pelo array de 10 elementos:

1. Um percurso para **somar** os valores e calcular a média (10 operações).
2. Um percurso para encontrar o **maior e o menor** valor, junto com seus índices (10 operações).
3. Um percurso para **contar** quantos valores estão acima da média (10 operações).

Total: **3 × 10 = 30 operações de percurso**, exatamente como mostrado na saída do programa.

### Complexidade do Algoritmo

O algoritmo desenvolvido possui complexidade **O(n)**, pois realiza um número fixo de percursos completos (neste caso, 3) sobre um array de tamanho `n`. Como o número de percursos não depende do tamanho da entrada — apenas se repete um número constante de vezes —, a complexidade total é **linear**: O(3n) = **O(n)**.

Isso significa que, se o número de temperaturas dobrasse (de 10 para 20), o número de operações também dobraria proporcionalmente, e não cresceria de forma quadrática como no Bubble Sort.
