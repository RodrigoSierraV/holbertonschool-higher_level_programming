#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

/**
 * insert_node - adds a new node at the end of a listint_t list.
 * @head: pointer to the given listint.
 * @number: number to add in the new node.
 * Return: the address of the new element, or NULL if it failed.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *current = *head, *before = *head;
	int i = 0, b = 0;

	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);
	new->n = number;
	new->next = NULL;
	if (*head == NULL)
	{	*head = new;
		return (new);
	}
	else
	{
		while (current)
		{
			if (number > current->n)
			{	current = current->next;
				i++;
			}
			else
				break;
		}
	}
	current = *head;
	while (b < i)
	{	current = current->next;
		if (b > 0)
			before = before->next;
		b++;
	}
	if (i == 0)
	{	*head = new;
		new->next = current;
		return (new);
	}
	new->next = current;
	before->next = new;
	return (new);
}
