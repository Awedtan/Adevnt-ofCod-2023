#include <stdio.h>
#include <ctype.h>

int main(void)
{
    int sum = 0;
    char line[90];
    while (fgets(line, sizeof(line), stdin))
    {
        int vals[90], index = 0;
        for (int i = 0; line[i] != '\0'; i++)
            if (isdigit(line[i]))
                vals[index++] = line[i] - '0';
        sum += 10 * vals[0] + vals[index - 1];
    }
    printf("%d\n", sum);
}