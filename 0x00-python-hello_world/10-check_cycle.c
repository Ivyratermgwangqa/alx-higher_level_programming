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
		listint_t *f_loop;
		listint_t *s_loop;

		if (list == NULL || list->next == NULL)
			return  (0);

		f_loop = list->next;
		s_loop = list->next->next;

		while (f_loop && s_loop && s_loop->next)
		{
			if (f_loop == s_loop->next)
			{
				return (1);
			}
			f_loop = f_loop->next;
			s_loop = s_loop->next->next;
		}
	}
	return (0);
}
