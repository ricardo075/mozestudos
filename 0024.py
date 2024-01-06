import streamlit as st

# Função para calcular o delta
def calcular_delta(a, b, c):
    delta = b**2 - 4*a*c
    return delta

# Função para calcular x1 e x2
def calcular_raizes(a, b, c):
    delta = calcular_delta(a, b, c)
    if delta < 0:
        return "Delta negativo, não existem raízes reais"
    else:
        x1 = (-b - delta**0.5) / (2*a)
        x2 = (-b + delta**0.5) / (2*a)
        return x1, x2

# Interface com Streamlit
st.title('Cálculo de raízes de uma equação do segundo grau')
a = st.number_input('Digite o valor de a:', value=1.0)
b = st.number_input('Digite o valor de b:', value=0.0)
c = st.number_input('Digite o valor de c:', value=0.0)

if st.button('Calcular'):
    resultado = calcular_raizes(a, b, c)
    st.write('Delta:', calcular_delta(a, b, c))
    if isinstance(resultado, tuple):
        st.write('x1:', resultado[0])
        st.write('x2:', resultado[1])
    else:
        st.write(resultado)


