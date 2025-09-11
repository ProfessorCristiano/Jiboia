from jiboia import *


x = leia("Digite um valor para número 1: ")

se(inteiro(x) > 10,
   seVerdadeiro(
       lambda: escreva('Valor informado:'),
       lambda: escreva(x),
       lambda: pulalinha(),
       lambda: escreva('é maior que 10')
   ),
   seFalso(
       lambda: escreva(x),
       lambda: escreva('não é maior do que 10')
   )
)
