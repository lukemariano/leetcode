// link para o problema em questão: https://leetcode.com/problems/first-missing-positive/description/

/**
 * @param {number[]} nums
 * @return {number}
 */
var firstMissingPositive = function (nums) {
  const sortArray = nums.sort((a, b) => a - b); // ordena o array
  let min = 1;

  // para cada numero no array, verifica se o número mínimo está no array
  // se estiver, acrescenta + 1 a variável 'min'
  // se não for igual, e se num > min então encontramos o número mínimo
  sortArray.forEach((num) => {
    if (num == min) min++;
    if (num > min) return min;
  });

  return min;
};

// o bloco de códigos abaixo é somente para teste local

console.log(firstMissingPositive([1, 2, 0]));
