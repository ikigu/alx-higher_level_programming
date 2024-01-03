#include "lists.h"
#include <stdio.h>

/**
 * insert_node - inserts a node into a sorted linked list
 * @head: the head of the linked list
 * @number: the number to insert
 *
 * Return: the address of the new node
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *copy_of_current_previous, *previous, *current, *new_node;

	if (*head == NULL || (*head)->next == NULL)
	{
		new_node = add_nodeint_end(head, number);
		return (new_node);
	}

	new_node = malloc(sizeof(listint_t));
	previous = current = *head;

	if (!new_node)
		return (NULL);
	new_node->n = number;

	if (current->n >= number)
	{
		copy_of_current_previous = *head;
		*head = new_node;
		new_node->next = copy_of_current_previous;
		return (new_node);
	}

	while (current)
	{
		if (number <= current->n)
		{
			copy_of_current_previous = previous->next;
			previous->next = new_node;
			new_node->next = copy_of_current_previous;
			return (new_node);
		}
		previous = current;
		current = current->next;
	}

	free(new_node);
	new_node = add_nodeint_end(head, number);
	return (new_node);
}

