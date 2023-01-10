# link para o problema: https://leetcode.com/problems/search-insert-position/submissions/

from typing import List


def searchInsert(nums: List[int], target: int) -> int:
    if target in nums:  # verifica se o target está na lista
        return nums.index(target)  # se ja estiver pega o indice do target
    else:
        nums.append(target)  # se não estiver adiciona o target na lista
        nums.sort()  # ordena a lista
        return nums.index(target)  # retorna o indice do target


output = searchInsert(nums=[1, 3, 5, 6], target=2)
print(output)
