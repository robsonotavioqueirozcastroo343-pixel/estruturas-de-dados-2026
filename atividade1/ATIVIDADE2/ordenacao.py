"""
Central de Distribuicao de Pedidos
Experimento comparativo entre algoritmos de ordenacao:
Bubble Sort, Insertion Sort, Selection Sort e Quick Sort

Criterio de contagem adotado:
- COMPARACOES: toda vez que dois elementos do vetor sao comparados entre si
  (ex.: if a[j] > a[j+1]).
- TROCAS / MOVIMENTACOES:
    * Bubble Sort e Selection Sort: cada "swap" (troca de posicao entre dois
      elementos) conta como 1 troca.
    * Insertion Sort: nao ha troca classica (swap), e sim deslocamento de
      elementos uma posicao a frente para abrir espaco. Cada deslocamento
      (movimentacao) conta como 1, e a insercao final do elemento na posicao
      correta tambem conta como 1 movimentacao.
    * Quick Sort: cada troca (swap) realizada durante o particionamento
      conta como 1 movimentacao.
"""

import random
import copy
import sys

# Quick Sort com pivo fixo (ultimo elemento) tem pior caso O(n^2) em vetores
# ja ordenados ou em ordem inversa, gerando recursao de profundidade n.
# Aumentamos o limite de recursao do Python para o desafio adicional nao
# estourar com vetores de 1000 elementos ja ordenados/invertidos.
sys.setrecursionlimit(10000)


# ---------------------------------------------------------------------------
# BUBBLE SORT
# ---------------------------------------------------------------------------
def bubble_sort(vetor):
    a = vetor
    n = len(a)
    comparacoes = 0
    trocas = 0
    for i in range(n - 1):
        trocou = False
        for j in range(n - 1 - i):
            comparacoes += 1
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                trocas += 1
                trocou = True
        if not trocou:
            break
    return comparacoes, trocas


# ---------------------------------------------------------------------------
# INSERTION SORT
# ---------------------------------------------------------------------------
def insertion_sort(vetor):
    a = vetor
    n = len(a)
    comparacoes = 0
    movimentacoes = 0
    for i in range(1, n):
        chave = a[i]
        j = i - 1
        while j >= 0:
            comparacoes += 1
            if a[j] > chave:
                a[j + 1] = a[j]
                movimentacoes += 1
                j -= 1
            else:
                break
        a[j + 1] = chave
        movimentacoes += 1
    return comparacoes, movimentacoes


# ---------------------------------------------------------------------------
# SELECTION SORT
# ---------------------------------------------------------------------------
def selection_sort(vetor):
    a = vetor
    n = len(a)
    comparacoes = 0
    trocas = 0
    for i in range(n - 1):
        menor = i
        for j in range(i + 1, n):
            comparacoes += 1
            if a[j] < a[menor]:
                menor = j
        if menor != i:
            a[i], a[menor] = a[menor], a[i]
            trocas += 1
    return comparacoes, trocas


# ---------------------------------------------------------------------------
# QUICK SORT
# ---------------------------------------------------------------------------
def quick_sort(vetor):
    a = vetor
    contadores = {"comparacoes": 0, "movimentacoes": 0}

    def particiona(baixo, alto):
        pivo = a[alto]
        i = baixo - 1
        for j in range(baixo, alto):
            contadores["comparacoes"] += 1
            if a[j] <= pivo:
                i += 1
                a[i], a[j] = a[j], a[i]
                contadores["movimentacoes"] += 1
        a[i + 1], a[alto] = a[alto], a[i + 1]
        contadores["movimentacoes"] += 1
        return i + 1

    def ordena(baixo, alto):
        if baixo < alto:
            p = particiona(baixo, alto)
            ordena(baixo, p - 1)
            ordena(p + 1, alto)

    ordena(0, len(a) - 1)
    return contadores["comparacoes"], contadores["movimentacoes"]


# ---------------------------------------------------------------------------
# EXPERIMENTO
# ---------------------------------------------------------------------------
def roda_experimento(tamanhos, tipo="aleatorio", semente=42):
    random.seed(semente)
    resultados = []

    for n in tamanhos:
        if tipo == "aleatorio":
            original = [random.randint(1, 100000) for _ in range(n)]
        elif tipo == "ordenado":
            original = list(range(n))
        elif tipo == "inverso":
            original = list(range(n, 0, -1))
        else:
            raise ValueError("tipo invalido")

        v_bubble = original.copy()
        v_insertion = original.copy()
        v_selection = original.copy()
        v_quick = original.copy()

        cb, tb = bubble_sort(v_bubble)
        ci, mi = insertion_sort(v_insertion)
        cs, ts = selection_sort(v_selection)
        cq, mq = quick_sort(v_quick)

        # verificacao de corretude
        assert v_bubble == sorted(original)
        assert v_insertion == sorted(original)
        assert v_selection == sorted(original)
        assert v_quick == sorted(original)

        resultados.append({
            "tamanho": n,
            "bubble_comp": cb, "bubble_troc": tb,
            "insertion_comp": ci, "insertion_mov": mi,
            "selection_comp": cs, "selection_troc": ts,
            "quick_comp": cq, "quick_mov": mq,
        })
    return resultados


def imprime_tabela(resultados, titulo):
    print(f"\n=== {titulo} ===")
    cab = ("Tam", "Bub.Comp", "Bub.Troc", "Ins.Comp", "Ins.Mov",
           "Sel.Comp", "Sel.Troc", "Qck.Comp", "Qck.Mov")
    print("{:>6} {:>10} {:>9} {:>9} {:>8} {:>9} {:>9} {:>9} {:>8}".format(*cab))
    for r in resultados:
        print("{:>6} {:>10} {:>9} {:>9} {:>8} {:>9} {:>9} {:>9} {:>8}".format(
            r["tamanho"], r["bubble_comp"], r["bubble_troc"],
            r["insertion_comp"], r["insertion_mov"],
            r["selection_comp"], r["selection_troc"],
            r["quick_comp"], r["quick_mov"]))


if __name__ == "__main__":
    tamanhos = [10, 20, 1000]

    # Etapa 3: experimento principal com vetores aleatorios
    res_aleatorio = roda_experimento(tamanhos, tipo="aleatorio")
    imprime_tabela(res_aleatorio, "Resultados - Vetores Aleatorios (Etapa 3)")

    # Desafio adicional: mesmo experimento com vetor ordenado e vetor invertido
    res_ordenado = roda_experimento(tamanhos, tipo="ordenado")
    imprime_tabela(res_ordenado, "Resultados - Vetores Ja Ordenados (Desafio)")

    res_inverso = roda_experimento(tamanhos, tipo="inverso")
    imprime_tabela(res_inverso, "Resultados - Vetores em Ordem Inversa (Desafio)")
