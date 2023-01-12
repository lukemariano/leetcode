# link para o problema em questão: https://leetcode.com/problems/remove-duplicates-from-sorted-list/

"""

Como a linked list está ordenada,
provavelmente as duplicatas estarão lado a lado.
- Exemplo: 1 --> 1 --> 2

Sendo assim, em uma lista linkada conforme: 1 --> 1 --> 2,
em que o número "1" está duplicado, considerarei apenas
o primeiro número 1 (o original) e excluirei a duplicata da sequência:
- Exemplo: 1(original) --> 1[extra a ser deletado] --> 2
           Output: 1 --> 2

Dessa forma evitamos que o head da lista nunca seja deletado.
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # define a mesma instância de uma lista linkada para
        # head e current_node -> alterar um objeto altera o outro também
        current_node = head

        # o primeiro loop define a "head" atual da lista
        while current_node:
            # o segundo loop faz o tratamento de possíveis dados duplicados
            # se o próximo nó for igual ao nó atual(head),
            # mantém o head e deleta o nó duplicado
            while current_node.next and current_node.next.val == current_node.val:
                current_node.next = current_node.next.next
            current_node = current_node.next
        return head


# o bloco de códigos abaixo é somente para teste local

if __name__ == "__main__":
    data_input = [1, 1, 2, 3, 3]  # input teste
    tail = head = ListNode(data_input[0])

    for i in data_input[1:]:
        tail.next = ListNode(i)  # Cria e adiciona outro nó
        tail = tail.next  # Move o ponteiro da calda

    # instancia um objeto da classe Solution para o teste
    solver = Solution()
    output = solver.deleteDuplicates(head)

    # variáveis para gerar o output da lista linkada tratada
    curr = head
    nodes_list = []

    while curr:
        nodes_list.append(curr.val)
        curr = curr.next

    print(nodes_list)  # output
