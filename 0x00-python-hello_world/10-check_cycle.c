#include "lists.h"

/**
  * check_cycle - checks whether a linked list is cyclic
  * @list: head of a linked list
  *
  * Return: 0 if there is no cycle, 1 if there is
  */

int check_cycle(listint_t *list)
{
	listint_t *current = list;

	if (!list || !(list->next))
		return (0);

	current = current->next;

	while (current)
	{
		if (current == list)
		{
			return (1);
		}

		current = current->next;
	}

	return (0);
}

