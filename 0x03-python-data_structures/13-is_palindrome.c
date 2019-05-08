#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * print_listint - prints all elements of a listint_t list
 * @h: pointer to head of list
 * Return: number of nodes
 */
int is_palindrome(listint_t **head)
{
	listint_t *aux = *head;
	int i = 0, len = 0, step = 0, beg = 0, comp = 0;

	if (!*head)
		return(1);
	while (aux)
	{
		len++;
		aux = aux->next;
	}
	aux = *head;
	beg = len - 1;
	while (step < len / 2)
	{
		i = 0;
		while (i < beg)
		{
			aux = aux->next;
			i++;
		}
		if ((*head)->n == aux->n)
			comp++;
		beg -= 2;
		step++;
		*head = (*head)->next;
		aux = *head;
	}
	if (comp == len / 2)
		return (1);
	return (0);
}
