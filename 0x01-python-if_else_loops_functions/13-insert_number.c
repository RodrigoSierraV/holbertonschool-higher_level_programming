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
	listint_t *new;
	listint_t *current = *head;

	new = malloc(sizeof(listint_t));
	if (!new)
	{
		free(new);
		return (NULL);
	}
	new->n = number;
	new->next = NULL;
	if (*head == NULL)
		*head = new;
	else
	{
		while (current->next)
			current = current->next;
		current->next = new;
	}
	return (new);
}
