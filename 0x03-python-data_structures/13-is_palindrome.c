#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - checks whether a linked list is a palindrome
 * @head: the head of the linked list
 *
 * Return: 0 if it's not a palindrome, 1 if it is
*/


int is_palindrome(listint_t **head)
{
	listint_t *current;
	size_t length, counter, length_for_loop;
	int *integer_array;

	if (!(*head) || !(*head)->next)
		return (1);

	current = *head;
	length = counter = 0;
	integer_array = malloc(1 * sizeof(int));

	if (!integer_array)
		return (0);

	while (current)
	{
		length++;
		integer_array = realloc(integer_array, length * sizeof(int));

		if (!integer_array)
			return (0);

		integer_array[length - 1] = current->n;
		current = current->next;
	}

	length_for_loop = length - 1;
	while (length > counter && counter != length_for_loop)
	{
		if (integer_array[counter] != integer_array[length_for_loop])
		{
			free(integer_array);
			return (0);
		}

		counter++;
		length_for_loop--;
	}
	free(integer_array);
	return (1);
}
