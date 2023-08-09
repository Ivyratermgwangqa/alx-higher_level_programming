#include "lists.h"

/**
 * check_cycle - Checks if a linked list has a cycle.
 * @list: Pointer to the first node of the list.
 * Return: 1 if there is a cycle, 0 if not.
 */
int check_cycle(listint_t *list)
{
	if (list)
	{
		listint_t *e = list;
		listint_t *c = list;

		while (c && e->next)
		{
			e = e->next;
			c = c->next->next;

			if (e == c)
				return (1);
		}
	}
	return (0);
}
