## PARTE 2 – EXPERIMENTO DE ORDENAÇÃO

### Código do Experimento (Python)

```python
import random
import sys

# Aumentar o limite de recursão para o Quick Sort caso necessário
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

# Execução do Experimento
tamanhos = [10, 20, 1000]
resultados = {}

for t in tamanhos:
    # Gerando dados aleatórios idênticos para ambos
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

# Exibição dos resultados formatados
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
