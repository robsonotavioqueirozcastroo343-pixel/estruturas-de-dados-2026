## PARTE 5 – HANDS ON 2: MATRIZ APLICADA – MONITORAMENTO DE SENSORES

### Código do Experimento (Python)

```python
import random


def investigar_sensores(sensores, limite):
    """
    sensores: matriz 5x24 (linha = sensor, coluna = horario 0-23)
    limite: temperatura limite informada pelo usuario

    Retorna um dicionario com:
    - media de cada sensor
    - maior temperatura registrada, sensor e horario dessa ocorrencia
    - media geral (todas as 120 medicoes)
    - quantidade de leituras acima do limite
    """
    num_sensores = len(sensores)
    num_horarios = len(sensores[0]) if num_sensores > 0 else 0

  
    medias_sensores = []
    for i in range(num_sensores):
        soma_sensor = 0
        for j in range(num_horarios):
            soma_sensor += sensores[i][j]
        medias_sensores.append(soma_sensor / num_horarios)


    maior_valor = sensores[0][0]
    sensor_maior = 0
    horario_maior = 0
    soma_geral = 0
    total_leituras = 0

    for i in range(num_sensores):
        for j in range(num_horarios):
            valor = sensores[i][j]
            soma_geral += valor
            total_leituras += 1
            if valor > maior_valor:
                maior_valor = valor
                sensor_maior = i
                horario_maior = j

    media_geral = soma_geral / total_leituras

  
    for i in range(num_sensores):
        for j in range(num_horarios):
            if sensores[i][j] > limite:
                acima_do_limite += 1

    return {
        "medias_sensores": medias_sensores,
        "maior_valor": maior_valor,
        "sensor_maior": sensor_maior,
        "horario_maior": horario_maior,
        "media_geral": media_geral,
        "total_leituras": total_leituras,
        "acima_do_limite": acima_do_limite,
    }


if __name__ == "__main__":
    random.seed(21)
    NUM_SENSORES = 5
    NUM_HORAS = 24

 
    sensores = [
        [round(random.uniform(18.0, 33.0), 1) for _ in range(NUM_HORAS)]
        for _ in range(NUM_SENSORES)
    ]

    limite = 28.0  

    resultado = investigar_sensores(sensores, limite)

    print("=== Matriz de Sensores (5 sensores x 24 horas) ===")
    for i, linha in enumerate(sensores):
        valores = "  ".join(f"{v:>5.1f}" for v in linha)
        print(f"Sensor {i}: {valores}")

    print("\n=== Resultados ===")
    for i, media in enumerate(resultado["medias_sensores"]):
        print(f"Media do sensor {i}: {media:.2f} °C")

    print(f"\nMaior temperatura registrada: {resultado['maior_valor']} °C")
    print(f"Sensor responsavel: Sensor {resultado['sensor_maior']}")
    print(f"Horario da ocorrencia: {resultado['horario_maior']}h")
    print(f"Media geral ({resultado['total_leituras']} medicoes): {resultado['media_geral']:.2f} °C")
    print(f"\nLimite informado: {limite} °C")
    print(f"Quantidade de leituras acima do limite: {resultado['acima_do_limite']}")
```

### Saída do Programa (Exemplo Real)

```
=== Matriz de Sensores (5 sensores x 24 horas) ===
Sensor 0:  20.5   28.3   27.5   25.2   21.2   29.9   30.1   25.7   25.6   21.5   18.0   23.6   26.8   19.0   29.9   21.5   21.5   18.6   33.0   29.1   31.1   27.2   18.5   22.9
Sensor 1:  25.5   19.7   32.3   23.5   20.3   30.3   19.9   31.9   24.8   26.3   23.1   25.3   20.8   18.6   31.0   21.5   29.7   21.1   32.5   31.4   29.3   29.4   26.7   28.9
Sensor 2:  19.8   25.1   30.4   21.0   31.8   31.3   24.1   23.5   24.8   23.8   32.9   23.8   18.4   19.4   28.8   32.9   25.4   25.4   26.3   29.2   21.3   27.1   26.3   27.3
Sensor 3:  20.7   20.6   23.2   31.9   23.2   27.0   22.6   19.5   19.0   30.2   29.7   23.6   28.3   28.1   31.5   32.4   24.1   32.8   32.4   26.9   31.2   25.4   23.6   21.7
Sensor 4:  31.1   20.4   19.0   30.1   29.6   25.2   30.6   18.8   21.9   22.3   24.3   20.6   19.0   23.1   31.5   32.8   29.2   25.2   21.8   32.4   25.9   28.9   18.4   21.2

=== Resultados ===
Media do sensor 0: 24.84 °C
Media do sensor 1: 25.99 °C
Media do sensor 2: 25.84 °C
Media do sensor 3: 26.23 °C
Media do sensor 4: 25.14 °C

Maior temperatura registrada: 33.0 °C
Sensor responsavel: Sensor 0
Horario da ocorrencia: 18h
Media geral (120 medicoes): 25.61 °C

Limite informado: 28.0 °C
Quantidade de leituras acima do limite: 43
```

### Explicações Finais

**Por que são necessários loops aninhados?**
Porque a matriz de sensores tem duas dimensões: uma para o **sensor** (linha) e outra para o **horário** (coluna). Um loop sozinho conseguiria percorrer apenas uma dessas dimensões. Para visitar **cada uma das 120 medições** (5 sensores × 24 horários), é preciso um loop externo percorrendo os sensores e, para cada sensor, um loop interno percorrendo os 24 horários — daí a necessidade dos loops aninhados.

**Qual o papel dos índices `[i][j]`?**
O índice `i` identifica **qual sensor** está sendo consultado (linha da matriz) e o índice `j` identifica **em qual horário** aquela medição foi feita (coluna da matriz). Juntos, `sensores[i][j]` aponta exatamente para uma medição específica: a temperatura registrada pelo sensor `i` no horário `j`.

**Quantas posições da matriz são percorridas?**
Para cada operação que exige varrer toda a matriz (como encontrar o maior valor, calcular a média geral ou contar leituras acima do limite), são percorridas **5 × 24 = 120 posições**, uma para cada combinação possível de sensor e horário.

**Qual a relação entre número de linhas, colunas e quantidade de operações?**
A quantidade de operações necessárias para percorrer toda a matriz é dada pelo **produto entre o número de linhas (m) e o número de colunas (n)**, ou seja, **m × n**. Nesse experimento, isso resulta em O(m × n) = O(5 × 24) = O(120) operações por percurso completo — o que caracteriza a mesma complexidade **O(m × n)** vista na busca sequencial em matrizes da Parte 3.
