#include <stdio.h>
#include <ctype.h>
#include <string.h>

int main(void)
{
    char words[] = "onetwothreefourfivesixseveneightnine";
    int indices[] = {0, 3, 6, 11, 15, 19, 22, 27, 32, 36};
    int sum = 0;
    char line[90];
    while (fgets(line, sizeof(line), stdin))
    {
        int vals[90], index = 0;
        for (int i = 0; line[i] != '\0'; i++)
            if (isdigit(line[i]))
                vals[index++] = line[i] - '0';
            else
                for (int k = 0; k < 9; k++)
                    if (strncmp(line + i, words + indices[k], indices[k + 1] - indices[k]) == 0)
                        vals[index++] = k + 1;
        sum += 10 * vals[0] + vals[index - 1];
    }
    printf("%d\n", sum);
}