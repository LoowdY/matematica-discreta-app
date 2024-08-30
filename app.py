import streamlit as st
import sympy as sp
import random
import matplotlib.pyplot as plt
import numpy as np
import networkx as nx
import os

st.set_page_config(
    page_title="Indução Matemática - CC2TA",
    page_icon="📚",
    layout="centered",
    initial_sidebar_state="expanded"
)


def main():
    st.title('Aprendendo Indução Matemática')

    
    st.sidebar.title('Navegação')
    options = ["Introdução", "Indução Padrão", "Indução Forte", "Indução Estrutural", "Questionário", "Exercícios Extras", "Dúvidas Comuns"]
    choice = st.sidebar.radio("Escolha uma seção", options)

    if choice == "Introdução":
        st.subheader("O que é Indução Matemática?")
        st.write("""
        A indução matemática é uma técnica poderosa usada para provar que uma afirmação é verdadeira para todos os números inteiros a partir de um certo ponto. O método é particularmente útil para teoremas que envolvem números naturais e é aplicado em dois passos principais:
        1. **Base da Indução**: Verificar a validade da proposição para um caso inicial específico.
        2. **Passo Indutivo**: Demonstrar que, se a proposição é verdadeira para um número arbitrário \( k \), então ela deve ser verdadeira para o próximo número \( k+1 \).

        Vamos explorar isso com um exemplo clássico.
        """)

        st.subheader("Exemplo 1: Soma dos Primeiros \( n \) Números Naturais")

        st.write("""
        Queremos provar que a soma dos primeiros \( n \) números naturais é dada pela fórmula:
        """)

        st.latex(r'''
        S_n = \frac{n(n + 1)}{2}
        ''')

        st.write("""
        **Base da Indução**:
        Vamos verificar a fórmula para \( n = 1 \):
        """)

        st.latex(r'''
        S_1 = \frac{1(1 + 1)}{2} = 1
        ''')

        st.write("""
        A soma dos primeiros 1 número natural é realmente 1, então a base da indução está correta.

        **Passo Indutivo**:
        Suponha que a fórmula seja verdadeira para um número arbitrário \( k \). Ou seja, assumimos que:
        """)

        st.latex(r'''
        S_k = \frac{k(k + 1)}{2}
        ''')

        st.write("""
        Devemos mostrar que a fórmula é verdadeira para \( k + 1 \). A soma dos primeiros \( k + 1 \) números naturais é:
        """)

        st.latex(r'''
        S_{k+1} = S_k + (k + 1)
        ''')

        st.write("""
        Substituindo a fórmula assumida para \( S_k \):
        """)

        st.latex(r'''
        S_{k+1} = \frac{k(k + 1)}{2} + (k + 1)
        ''')

        st.write("""
        Simplificando:
        """)

        st.latex(r'''
        S_{k+1} = \frac{k(k + 1) + 2(k + 1)}{2} = \frac{(k + 1)(k + 2)}{2}
        ''')

        st.write("""
        Portanto, a fórmula também se aplica para \( k + 1 \), e a indução está completa.

        Assim, a fórmula para a soma dos primeiros \( n \) números naturais está comprovada por indução matemática.
        """)

        st.subheader("Exemplo 2: Propriedade dos Números Pares")

        st.write("""
        Vamos provar que todo número par positivo pode ser expresso como a soma de dois números primos. Isto é conhecido como a Conjectura de Goldbach.

        **Base da Indução**:
        Para \( n = 2 \), o número 2 é par e pode ser expresso como a soma de 1 + 1 (note que, tradicionalmente, consideramos números primos começando de 2, então esse exemplo não é ideal, mas demonstra a ideia). Para \( n = 4 \):
        """)

        st.latex(r'''
        4 = 2 + 2
        ''')

        st.write("""
        **Passo Indutivo**:
        Suponha que todo número par menor que um certo número \( k \) pode ser expresso como a soma de dois números primos. Devemos mostrar que o número \( k + 2 \) também pode ser expresso desta forma.

        Se \( k + 2 \) é um número par maior que 2, então pode ser expresso como a soma de dois números primos conforme a hipótese de indução. Por exemplo, se \( k = 6 \):
        """)

        st.latex(r'''
        6 = 3 + 3
        ''')

        st.write("""
        Então para \( k + 2 = 8 \):
        """)

        st.latex(r'''
        8 = 3 + 5
        ''')

        st.write("""
        Continuamos a verificar para outros números, e se todos os números pares menores que \( k + 2 \) seguem a conjectura, então \( k + 2 \) também o faz.

        **Nota**: A Conjectura de Goldbach ainda não foi provada formalmente para todos os números, mas é um exemplo de como a indução matemática é aplicada para verificar propriedades conjecturais.
        """)

    elif choice == "Indução Padrão":
        
        run_standard_induction()

    elif choice == "Indução Forte":
        
        run_strong_induction()

    elif choice == "Indução Estrutural":
        
        run_structural_induction()

    elif choice == "Questionário":
        
        run_quiz()

    elif choice == "Exercícios Extras":
        
        run_exercises_2()

    elif choice == "Dúvidas Comuns":
        
        run_faq()
def run_standard_induction():
    st.write("""
    ### Indução Padrão
    A indução padrão é uma técnica fundamental em matemática para provar que uma propriedade é válida para todos os números naturais.
    """)

    # Interatividade 1: Definir a base da indução
    base = st.number_input("Escolha um valor inicial para a base da indução (n=1)", min_value=1, step=1, value=1)
    st.write(f"Você escolheu n={base} como base da indução.")

    # Interatividade 2: Calcular uma soma básica
    n = sp.symbols('n')
    expr = sp.Sum(n, (n, 1, base))
    simplified_expr = sp.simplify(expr.doit())
    st.latex(sp.latex(simplified_expr))

    # Interatividade 3: Verificar se a fórmula da soma está correta
    st.write("Vamos verificar a fórmula para a soma dos primeiros n números.")
    formula = st.text_input("Digite a fórmula que você acha que representa a soma dos primeiros n números:")
    if formula:
        st.write("Sua fórmula é:", formula)
        st.latex(r"\text{Fórmula padrão: } \frac{n(n+1)}{2}")
        if formula == r"n(n+1)/2":
            st.success("Correto!")
        else:
            st.error("Tente novamente!")

def run_strong_induction():
    st.write("""
    ### Indução Forte
    A indução forte é utilizada quando a validade de uma afirmação para um número depende da validade para todos os números menores que ele.
    """)

    # Interatividade 1: Escolha um número n para o qual você quer verificar a fórmula
    n_value = st.number_input("Escolha um valor de n para verificar a fórmula", min_value=1, step=1, value=2)
    st.write(f"Você escolheu n={n_value}")

    # Definir n como uma variável simbólica
    n = sp.symbols('n')

    # Interatividade 2: Mostrar a soma de uma série geométrica até n
    expr = sum([2**i for i in range(1, n_value + 1)])
    st.write(f"A soma dos termos até n={n_value} é:")
    st.latex(sp.latex(expr))

    # Interatividade 3: Pedir ao usuário para adivinhar a soma incluindo o próximo termo
    next_term_value = 2**(n_value + 1)
    correct_next_sum = expr + next_term_value
    
    st.write(f"Vamos adicionar o próximo termo, $2^{{{n_value + 1}}}$, à soma anterior.")
    guess = st.number_input(f"Tente adivinhar o valor da soma até n={n_value + 1}:", value=0)
    
    if st.button("Verificar"):
        if guess == correct_next_sum:
            st.success(f"Correto! A soma até n={n_value + 1} é realmente {correct_next_sum}.")
        else:
            st.error(f"Incorreto. A soma correta até n={n_value + 1} é {correct_next_sum}.")

    # Plotar a soma dos termos da sequência até n_value
    n_values = np.arange(1, n_value + 2)
    sums = [sum([2**i for i in range(1, int(n) + 1)]) for n in n_values]
    
    plt.figure(figsize=(10, 6))
    plt.plot(n_values, sums, marker='o', linestyle='-', color='b', label='Soma dos termos da sequência')
    plt.axhline(y=correct_next_sum, color='r', linestyle='--', label=f'Soma até n={n_value + 1}')
    plt.title('Soma dos Termos de uma Sequência Geométrica (2^n)')
    plt.xlabel('n')
    plt.ylabel('Soma acumulada')
    plt.legend()
    plt.grid(True)
    
    st.pyplot(plt)

def plot_tree(height):
    """Função para plotar uma árvore binária completa com nós numerados"""
    G = nx.Graph()
    
    # Adiciona nós e arestas para uma árvore binária completa
    for i in range(2**height - 1):
        G.add_node(i+1)
        left_child = 2 * (i + 1)
        right_child = left_child + 1
        if left_child <= 2**height - 1:
            G.add_edge(i + 1, left_child)
        if right_child <= 2**height - 1:
            G.add_edge(i + 1, right_child)

    # Utilizando o layout do spring layout
    pos = nx.spring_layout(G, seed=42)  # Usando o seed para resultados consistentes
    
    plt.figure(figsize=(8, 8))
    nx.draw(G, pos, with_labels=True, node_size=700, node_color="skyblue", font_size=15, font_weight="bold")
    st.pyplot(plt)

def run_structural_induction():
    st.write("""
    ### Indução Estrutural
    Usada para estruturas definidas recursivamente, como árvores ou sequências complexas.
    """)

    # Interatividade 1: Escolher uma estrutura simples (ex: sequência ou árvore)
    structure = st.selectbox("Escolha uma estrutura para aplicar a indução estrutural:", ["Sequência", "Árvore"])
    st.write(f"Você escolheu: {structure}")

    # Interatividade 2: Inserir o tamanho da estrutura
    size = st.number_input(f"Escolha o tamanho da {structure.lower()} (ex: número de elementos ou altura)", min_value=1, step=1, value=3)
    st.write(f"Tamanho escolhido: {size}")

    # Definir n como uma variável simbólica
    n = sp.symbols('n')

    if structure == "Sequência":
        st.write("Vamos calcular a soma dos quadrados dos primeiros elementos da sequência.")
        
        # Calculando a soma dos quadrados até o tamanho escolhido
        expr = sp.Sum(n**2, (n, 1, size))
        sum_sequence = expr.doit()
        st.latex(sp.latex(sum_sequence))
        
        # Gerando os valores da sequência para o gráfico
        n_values = np.arange(1, size + 1)
        sums = [sum([i**2 for i in range(1, int(n) + 1)]) for n in n_values]
        
        # Plotando o gráfico da sequência
        plt.figure(figsize=(10, 6))
        plt.plot(n_values, sums, marker='o', linestyle='-', color='g', label='Soma dos quadrados da sequência')
        plt.title('Soma dos Quadrados de uma Sequência')
        plt.xlabel('n')
        plt.ylabel('Soma acumulada')
        plt.legend()
        plt.grid(True)
        
        st.pyplot(plt)
    
    elif structure == "Árvore":
        st.write("Vamos calcular o número total de nós em uma árvore binária completa.")
        
        # Calculando o número de nós em uma árvore binária completa de altura 'size'
        num_nodes = 2**size - 1
        st.latex(f"O número total de nós em uma árvore binária de altura {size} é {num_nodes}.")
        
        # Plotando a árvore binária completa
        plot_tree(size)


def run_quiz():
    questions = {
        "Indução Padrão": [
            ("Qual é o primeiro passo em uma prova por indução padrão?", [
                "Verificar a proposição para n=1",
                "Aplicar o passo indutivo",
                "Generalizar para todos os números",
                "Nenhuma das anteriores"], "Verificar a proposição para n=1"),
            ("O que é necessário para concluir uma prova por indução padrão?", [
                "Um passo indutivo bem definido",
                "Apenas a base da indução",
                "Um contraexemplo",
                "Generalização imediata"], "Um passo indutivo bem definido"),
        ],
        "Indução Forte": [
            ("Como a indução forte difere da indução padrão?", [
                "Usa todos os casos anteriores",
                "Usa apenas o caso n-1",
                "Não requer um caso base",
                "Sempre resulta em uma prova mais curta"], "Usa todos os casos anteriores"),
            ("Quando é mais adequado usar a indução forte?", [
                "Quando cada caso depende de todos os anteriores",
                "Quando apenas o primeiro caso é relevante",
                "Em problemas de contagem simples",
                "Para demonstrar falsidade"], "Quando cada caso depende de todos os anteriores"),
        ],
        "Indução Estrutural": [
            ("Qual é um exemplo de uso de indução estrutural?", [
                "Provar propriedades sobre árvores binárias",
                "Somas de séries numéricas",
                "Calculando derivadas",
                "Resolvendo equações lineares"], "Provar propriedades sobre árvores binárias"),
            ("O que diferencia a indução estrutural das outras formas de indução?", [
                "Foca em estruturas definidas recursivamente",
                "Foca apenas em números inteiros",
                "Não usa um caso base",
                "Usa diferenciação para provar"], "Foca em estruturas definidas recursivamente"),
        ]
    }

    for key, value in questions.items():
        st.write(f"### Perguntas sobre {key}")
        for question, options, correct_answer in value:
            answer = st.radio(question, options)
            if st.button(f'Verificar resposta - {question}'):
                if answer == correct_answer:
                    st.success("Correto!")
                else:
                    st.error("Incorreto. Tente novamente.")

def run_faq():
    st.write("### Respostas para Dúvidas Comuns")
    
    questions = [
        "O que acontece se a base da indução não for verdadeira?",
        "É possível usar indução matemática em conjuntos que não são números naturais?",
        "Como diferenciar quando usar indução forte ou padrão?",
        "Como a indução matemática se aplica a sequências definidas recursivamente?",
        "Qual é a importância da base da indução em provas com múltiplas bases?",
        "Pode-se usar indução para provar desigualdades? Como?"
    ]

    for i, question in enumerate(questions):
        st.write(f"**{i + 1}. {question}**")
    
    if st.button("Mostrar Respostas"):
        # Resposta 1
        st.write("#### 1. O que acontece se a base da indução não for verdadeira?")
        st.write("Se a base da indução não for verdadeira, a prova por indução falha. Sem uma base verdadeira, não podemos garantir que a proposição é verdadeira para todos os casos subsequentes.")
        st.write("**Prova Matemática:**")
        n = sp.symbols('n')
        P_n = n**2 >= n
        st.write("Considere a proposição P(n): n² ≥ n.")
        st.write("A prova por indução segue dois passos:")
        st.write("1. **Base da Indução:** Verifique P(1). Se P(1) for falsa, então a proposição falha para n = 1, e não há como garantir a validade de P(n) para qualquer n ≥ 1.")
        st.write("2. **Passo Indutivo:** Suponha que P(k) é verdadeira para algum k ≥ 1, e mostre que isso implica P(k+1). Se a base for falsa, a cadeia de implicações não começa.")
        P_k1 = (n + 1)**2 >= (n + 1)
        st.write("Exemplo para o caso k+1:")
        st.latex(sp.latex(P_k1))

        # Resposta 2
        st.write("#### 2. É possível usar indução matemática em conjuntos que não são números naturais?")
        st.write("Sim, é possível usar indução matemática em conjuntos que não são números naturais, desde que o conjunto tenha uma estrutura semelhante aos números naturais.")
        st.write("**Prova Matemática:**")
        st.write("A indução pode ser aplicada em qualquer conjunto que satisfaça o princípio do bom ordenamento.")
        st.write("**Exemplo:**")
        k = sp.symbols('k')
        expr = 2*k
        st.write("Considere o conjunto dos números pares positivos:")
        st.latex(sp.latex(expr))
        P_2k = 2*k >= 2
        st.write("A proposição para os números pares pode ser representada como:")
        st.latex(sp.latex(P_2k))
        st.write("Esse conjunto se comporta de forma semelhante ao conjunto dos números naturais, permitindo que a indução seja aplicada.")

        # Resposta 3
        st.write("#### 3. Como diferenciar quando usar indução forte ou padrão?")
        st.write("A indução forte é utilizada quando o caso n+1 depende de vários casos anteriores, não apenas do caso n.")
        st.write("**Prova Matemática:**")
        P_n = sp.symbols('P_n')
        st.write("- **Indução Padrão:** Prova-se P(n) assumindo que P(k) é verdadeira para k = n.")
        st.latex(sp.latex(P_n))
        st.write("- **Indução Forte:** Prova-se P(n) assumindo que P(k) é verdadeira para todos os k ≤ n.")
        st.write("**Exemplo:** Vamos provar que todo número n ≥ 2 pode ser fatorado em números primos.")
        st.write("- **Indução Padrão:** Assumimos que n pode ser fatorado e, então, mostramos que n+1 também pode.")
        st.write("- **Indução Forte:** Assumimos que todos os k ≤ n podem ser fatorados em primos e, então, usamos essa informação para provar que n+1 também pode.")

        # Resposta 4
        st.write("#### 4. Como a indução matemática se aplica a sequências definidas recursivamente?")
        st.write("A indução matemática pode ser aplicada para provar propriedades de sequências definidas recursivamente.")
        st.write("**Prova Matemática:**")
        a_n = sp.symbols('a_n')
        a_n_formula = 2**sp.symbols('n') - 1
        st.write("Suponha uma sequência a_n definida por a_1 = 1 e a_{n+1} = 2a_n + 1. Queremos provar que:")
        st.latex(sp.latex(a_n_formula))
        st.write("para todos os n ≥ 1.")
        st.write("**Passo Indutivo:**")
        k = sp.symbols('k')
        a_k = 2**k - 1
        st.write(f"a_{{k+1}} = 2 * ({a_k}) + 1")
        st.latex(sp.latex(2*(2**k - 1) + 1))

        # Resposta 5
        st.write("#### 5. Qual é a importância da base da indução em provas com múltiplas bases?")
        st.write("Em provas por indução com múltiplas bases, cada base da indução estabelece a veracidade da proposição em diferentes pontos iniciais.")
        st.write("**Prova Matemática:**")
        P_n = sp.symbols('P_n')
        st.write("Considere uma proposição P(n) verdadeira para todos os n ≥ 1, dependendo de P(n) para n = 1 e n = 2.")
        st.latex(sp.latex(P_n))
        st.write("No passo indutivo, mostramos que P(k) para k ≥ 2 implica P(k+1). Ambas as bases são necessárias para garantir que a proposição seja válida para todo n ≥ 1.")

        # Resposta 6
        st.write("#### 6. Pode-se usar indução para provar desigualdades? Como?")
        st.write("Sim, a indução matemática é uma técnica poderosa para provar desigualdades.")
        st.write("**Prova Matemática:**")
        n = sp.symbols('n')
        inequality = 2**n >= n**2
        st.write("Vamos provar que:")
        st.latex(sp.latex(inequality))
        st.write("para todos os n ≥ 4.")
        st.write("**Base da Indução:**")
        st.write("2^4 = 16 ≥ 4^2 = 16")
        st.write("**Passo Indutivo:**")
        step = 2**(n+1) >= (n+1)**2
        st.write("Suponha que 2^k ≥ k^2 para algum k ≥ 4. Queremos provar que:")
        st.latex(sp.latex(step))


def run_exercises_2():
    st.title("Exercícios de Matemática Discreta")

    # Definindo os símbolos
    n, k, i = sp.symbols('n k i')

    # Exercício 1
    st.latex(r"Exercício\ 1:\ Divisibilidade\ de\ n^3 - n\ por\ 6")
    st.latex(r"Queremos\ provar\ que\ a\ expressão\ n^3 - n\ é\ divisível\ por\ 6\ para\ todo\ n \geq 1.")
    
    if st.button("Mostrar Respostas Exercício 1"):
        st.latex(r'''
        \textbf{Divisibilidade por 2:}
        \text{Observamos que entre } n-1, n, \text{ e } n+1, \text{ pelo menos um deles é par.}
        \text{Portanto, o produto } n(n-1)(n+1) \text{ é divisível por 2.}
        ''')

        st.latex(r'''
        \textbf{Divisibilidade por 3:}
        \text{Agora, analisemos a divisibilidade por 3 considerando os casos:}
        ''')

        st.latex(r'''
        \begin{cases}
        n \equiv 0 \pmod{3} & \text{então } n^3 - n \equiv 0 \pmod{3} \\
        n \equiv 1 \pmod{3} & \text{então } n^3 - n \equiv 0 \pmod{3} \\
        n \equiv 2 \pmod{3} & \text{então } n^3 - n \equiv 0 \pmod{3}
        \end{cases}
        ''')

        st.latex(r'''
        \text{Portanto, como } n^3 - n \text{ é divisível tanto por 2 quanto por 3, ele é divisível por 6.}
        ''')

    # Exercício 2
    st.latex(r"Exercício\ 2:\ Soma\ dos\ Primeiros\ n\ Números\ Ímpares")
    st.latex(r"Prove\ que\ a\ soma\ dos\ primeiros\ n\ números\ ímpares\ é\ igual\ a\ n^2.")

    if st.button("Mostrar Respostas Exercício 2"):
        st.latex(r'''
        \textbf{Base da Indução:}
        \text{Para } n = 1, \text{ a soma dos primeiros 1 número ímpar é 1, que é igual a } 1^2.
        ''')

        st.latex(r'''
        1 = 1^2
        ''')

        st.latex(r'''
        \textbf{Passo Indutivo:}
        \text{Suponha que a soma dos primeiros } k \text{ números ímpares seja } k^2.
        \text{Queremos mostrar que a soma dos primeiros } k+1 \text{ números ímpares é } (k+1)^2.
        ''')

        sum_odd_k = sp.Sum(2*i - 1, (i, 1, k))
        sum_odd_k_plus_1 = sum_odd_k.doit() + (2*(k + 1) - 1)
        st.latex(sp.latex(sum_odd_k_plus_1))
        st.latex(r'''
        \text{Compare com } (k+1)^2:
        ''')
        st.latex(sp.latex((k + 1)**2))
        st.latex(r"Portanto,\ a\ soma\ dos\ primeiros\ k+1\ números\ ímpares\ é\ igual\ a\ (k+1)^2.")

    # Exercício 3
    st.latex(r"Exercício\ 3:\ Divisibilidade\ de\ 5^n - 1\ por\ 4")
    st.latex(r"Prove\ que\ 5^n - 1\ é\ divisível\ por\ 4\ para\ todo\ n \geq 1.")

    if st.button("Mostrar Respostas Exercício 3"):
        st.latex(r'''
        \textbf{Base da Indução:}
        \text{Para } n = 1: 5^1 - 1 = 4, \text{ que é divisível por 4.}
        ''')

        st.latex(r'''
        \textbf{Passo Indutivo:}
        \text{Suponha que } 5^k - 1 \text{ seja divisível por 4.}
        \text{Queremos mostrar que } 5^{k+1} - 1 \text{ também é divisível por 4.}
        ''')

        expression = 5**(k+1) - 1
        prev_expression = 5**k - 1
        diff = expression - 5 * prev_expression
        st.latex(sp.latex(diff.simplify()))
        st.latex(r"Como\ a\ diferença\ é\ divisível\ por\ 4,\ a\ proposição\ é\ verdadeira\ para\ n = k+1.")

    # Exercício 4
    st.latex(r"Exercício\ 4:\ Divisibilidade\ de\ n^2 + n\ por\ 2")
    st.latex(r"Prove\ que\ para\ todo\ n \geq 1,\ n^2 + n\ é\ divisível\ por\ 2.")

    if st.button("Mostrar Respostas Exercício 4"):
        st.latex(r'''
        \textbf{Base da Indução:}
        \text{Para } n = 1: 1^2 + 1 = 2, \text{ que é divisível por 2.}
        ''')

        st.latex(r'''
        \textbf{Passo Indutivo:}
        \text{Suponha que para } n = k, \text{ a expressão } k^2 + k \text{ seja divisível por 2.}
        \text{Queremos mostrar que para } n = k+1, \text{ a expressão } (k+1)^2 + (k+1) \text{ também é divisível por 2.}
        ''')

        next_case = (k + 1)**2 + (k + 1)
        st.latex(sp.latex(next_case))
        st.latex(r'''
        \text{Compare com a expressão para } n = k:
        ''')
        st.latex(sp.latex(k**2 + k))
        st.latex(r"Como\ a\ diferença\ é\ divisível\ por\ 2,\ a\ proposição\ é\ verdadeira\ para\ n = k+1.")

if __name__ == "__main__":
    
    main()

    st.write("Autores: João Renan Lopes e Pedro Herique Girotto")
