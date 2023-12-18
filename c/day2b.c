#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main(void)
{
    int sum = 0;
    char line[900];
    while (fgets(line, sizeof(line), stdin))
    {
        int game, min[3] = {0};
        sscanf(line, "Game %d:", &game);
        char delim[] = " ,;:\n";
        char *token = strtok(line, delim);
        strtok(NULL, delim);
        token = strtok(NULL, delim);
        while (token != NULL)
        {
            int val = atoi(token);
            token = strtok(NULL, delim);
            if (strcmp(token, "red") == 0 && val > min[0])
                min[0] = val;
            else if (strcmp(token, "green") == 0 && val > min[1])
                min[1] = val;
            else if (strcmp(token, "blue") == 0 && val > min[2])
                min[2] = val;
            token = strtok(NULL, delim);
        }
        sum += min[0] * min[1] * min[2];
    }
    printf("%d\n", sum);
}