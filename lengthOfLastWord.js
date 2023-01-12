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

console.log(lengthOfLastWord("Hello World"));
