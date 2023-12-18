#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main(void)
{
    int sum = 0;
    char line[900];
    while (fgets(line, sizeof(line), stdin))
    {
        int game, check = 1;
        sscanf(line, "Game %d:", &game);
        char delim[] = " ,;:\n";
        char *token = strtok(line, delim);
        strtok(NULL, delim);
        token = strtok(NULL, delim);
        while (token != NULL)
        {
            int val = atoi(token);
            token = strtok(NULL, delim);
            if (strcmp(token, "red") == 0 && val > 12)
                check = 0;
            else if (strcmp(token, "green") == 0 && val > 13)
                check = 0;
            else if (strcmp(token, "blue") == 0 && val > 14)
                check = 0;
            token = strtok(NULL, delim);
        }
        if (check)
            sum += game;
    }
    printf("%d\n", sum);
}