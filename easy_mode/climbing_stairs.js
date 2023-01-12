// link para o problema em questão: https://leetcode.com/problems/climbing-stairs/description/

/**
 * @param {number} n
 * @return {number}
 */
var climbStairs = function (n) {
  // pela sequência de fibonacci, o número posterior é
  // a soma dos dois números anteriores a ele

  // dada que a restrição do problema é: 1 <= n <= 45
  // comecei a sequencia de fibonacci pelo número 1:
  n1 = 1;
  n2 = 1;

  if (n == 1) {
    return n;
  } else if (n == 2) {
    return n1 + n2;
  } else {
    // defino contador = 2 porque na primeira vez o
    // último termo é: (n1 + n2) -> 2
    contador = 2;
    while (contador < n) {
      // o ultimo termo é a soma dos dois últimos
      ultimo_termo = n1 + n2;
      // atualiza último termo e penúltimo termo
      n1 = n2;
      n2 = ultimo_termo;
      contador++;
    }
    return n1 + n2; // combinações possíveis são a soma do último termo com o penúltimo
  }
};

// o bloco de códigos abaixo é somente para teste local

console.log(climbStairs(4));
