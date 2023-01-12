# link para o problema em questão: https://leetcode.com/problems/add-two-numbers/description/

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head1 = l1
        head2 = l2

        lista1 = []
        lista2 = []

        # appenda valores da primeira lista
        while head1:
            lista1.append(head1.val)
            head1 = head1.next

        # appenda valores da segunda lista
        while head2:
            lista2.append(head2.val)
            head2 = head2.next

        # inverte listas
        lista1.reverse()
        lista2.reverse()

        # valor da lista1
        valor1 = ''
        for n in lista1:
            valor1 += str(n)
        valor1 = int(valor1)

        # valor da lista2
        valor2 = ''
        for n in lista2:
            valor2 += str(n)
        valor2 = int(valor2)

        # soma dos nós
        soma_nodes = valor1 + valor2
        soma_nodes_str = str(soma_nodes)

        # recria novo nó com soma das listas linkadas
        nova_lista_encadeada = []
        for n in soma_nodes_str:
            nova_lista_encadeada.append(int(n))

        # inverte a nova lista encadeada
        nova_lista_encadeada.reverse()

        # define a head e tail para criação da nova lista encadeada
        tail = head = ListNode(nova_lista_encadeada[0])

        for i in nova_lista_encadeada[1:]:
            tail.next = ListNode(i)  # Cria e adiciona outro nó
            tail = tail.next  # Move o ponteiro da calda
        return head


if __name__ == "__main__":
    data_input = [[2, 4, 3], [5, 6, 4]]  # input teste --> 2 listas

    # declarando head e tail das listas encadeadas de input
    tail1 = head1 = ListNode(data_input[0][0])
    tail2 = head2 = ListNode(data_input[1][0])

    # criando listas encadeadas a partir dos inputs
    for i in data_input[0][1:]:
        tail1.next = ListNode(i)  # Cria e adiciona outro nó
        tail1 = tail1.next  # Move o ponteiro da calda

    for i in data_input[1][1:]:
        tail2.next = ListNode(i)  # Cria e adiciona outro nó
        tail2 = tail2.next  # Move o ponteiro da calda

    # instancia um objeto da classe Solution para o teste
    solver = Solution()
    output = solver.addTwoNumbers(head1, head2)

    # iterando sobre a lista encadeada para visualizar o output
    curr = output
    nodes_list = []

    while curr:
        nodes_list.append(curr.val)
        curr = curr.next

    print(nodes_list)  # output
