// link para o problema: https://leetcode.com/problems/reverse-integer/description/

/**
 * @param {number} x
 * @return {number}
 */
var reverseIntegers = function (x) {
  let lista_numeros = [];

  for (let n of x.toString()) {
    lista_numeros.push(n);
  }

  // inverte a ordem dos números na lista
  lista_numeros.reverse();

  // Validações para garantir que o número invertido é válido
  stringNumber = "";

  // adiciona os números em uma string para validação
  for (let n of lista_numeros) {
    stringNumber += n.toString();
  }

  // valida se o número começa com 0. Ex: 021 --> 21
  if (stringNumber.startsWith(0)) {
    stringNumber.replace("0", "");
  }

  // a inversão de um número negativo resulta em -123 --> 321-
  // sendo assim, se o último caracter for '-', faço o replace para negativar corretamente
  if (stringNumber.endsWith("-")) {
    stringNumber.replace("-", "");
    let numberParser = parseInt(stringNumber);
    // garante que o número resultante tem 32-bits
    if (numberParser > 0x7fffffff) {
      return 0;
    } else {
      return -numberParser;
    }
  }

  // garante que o número resultante tem 32-bits
  if (parseInt(stringNumber) > 0x7fffffff) {
    return 0;
  } else {
    return parseInt(stringNumber);
  }
};

let inputTest = -123;

console.log(reverseIntegers(inputTest));
