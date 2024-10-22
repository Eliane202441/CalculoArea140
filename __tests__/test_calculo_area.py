# 2 - Crie os testes de unidade para essas três funções que criou na questão 1

import pytest
from calculoarea import area_quadrado, area_retangulo, area_triangulo
from utils.utils import ler_csv


def test_area_quadrado():
    assert area_quadrado(4) == 16
    assert area_quadrado(0) == 0
    assert area_quadrado(5.5) == 30.25  # Teste com número decimal

def test_area_retangulo():
    assert area_retangulo(5, 10) == 50
    assert area_retangulo(0, 10) == 0
    assert area_retangulo(7.5, 4) == 30  # Teste com número decimal

def test_area_triangulo():
    assert area_triangulo(6, 4) == 12
    assert area_triangulo(10, 0) == 0
    assert area_triangulo(7.5, 8) == 30  # Teste com número decimal


# 3 - Altere um desses testes de unidade para que leia uma massa de teste a partir de uma lista de valores

massa_teste_area_quadrado = [
    (4, 16),   # Teste com número inteiro
    (0, 0),    # Teste com lado zero
    (5.5, 30.25),  # Teste com número decimal
    (10, 100),  # Teste com número maior
]

@pytest.mark.parametrize("lado, resultado_esperado", massa_teste_area_quadrado)

def test_area_quadrado(lado, resultado_esperado):
    assert area_quadrado(lado) == resultado_esperado

# 4 - Altere outro desses testes de unidade para que leia uma massa de teste a partir de um arquivo csv


@pytest.mark.parametrize("base, altura, resultado_esperado",
                          ler_csv('./fixtures/massa_calculo_area.cs]')
                          )
def test_area_retangular_csv(base, altura, resultado_esperado):
    # Converte base e altura para float antes de chamar a função
    
    resultado_obtido = area_retangulo(float(base), float(altura))

    assert float(resultado_esperado) == resultado_esperado

   

   
