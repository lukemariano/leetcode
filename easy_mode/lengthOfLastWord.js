// Link para o problema: https://leetcode.com/problems/length-of-last-word/description/
/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLastWord = function (s) {
  // remove espaços da string e cria uma lista em que cada palavra é um item
  let listString = s.trim().split(" ");
  // Encontra a última palavra da lista
  let lastWordLength = listString[listString.length - 1];
  return lastWordLength.length;
};

// o bloco de códigos abaixo é somente para teste local

console.log(lengthOfLastWord("Hello World"));
