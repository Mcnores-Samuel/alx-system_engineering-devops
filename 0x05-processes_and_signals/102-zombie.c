#include <stdio.h>
#include <sys/types.h>
#include <unistd.h>
#include <stdlib.h>

/**
 * zombie - create 5 zombie processes and display their PIDs
 * Return: nothing
 */
void zombie(void)
{
	pid_t child;
	int n;

	for (n = 5; n > 0; n--)
	{
		child = fork();

		if (child > 0)
		{
			printf("Zombie process created, PID: %d\n", child);
			sleep(1);
		}
		else
			exit(0);
	}
}

/**
 * infinite_while - keeps the zombie processes in their zombie state.
 * Return: 0 on exit.
 */
int infinite_while(void)
{
    while (1)
    {
        sleep(1);
    }
    return (0);
}

/**
 * main - calls zombie and infinite_while processes.
 * Return: 0 on success.
 */
int main(void)
{
	zombie();
	infinite_while();
	return (0);
}
