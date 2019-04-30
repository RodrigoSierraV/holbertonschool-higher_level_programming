#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
int find(listint_t *head, listint_t *current, listint_t *fast);
/**
 * check_cycle - checks for cycles in a listint_t list
 * @list: pointer to head of list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *current = (listint_t *)list, *fast = (listint_t *)list;

	if (find((listint_t *)list, current, fast))
		return (1);
	return (0);
}
/**
 * find - finds a loop in a linked list.
 * @head: pointer to the given listint.
 * @current: pointer to the given listint.
 * @fast: pointer to the given listint.
 *
 * Return: The address of the node where
 * the loop starts, or NULL if there is no loop.
 */
int find(listint_t *head, listint_t *current, listint_t *fast)
{
	while (current && fast && fast->next)
	{
		current = current->next;
		fast = fast->next->next;
		if (current == fast)
		{
			if (current != head)
			{
				head = head->next;
				current = head;
				fast = head;
				find(head, current, fast);
			}
			else
			{
				return (1);
			}
		}
	}
	return (0);
}
