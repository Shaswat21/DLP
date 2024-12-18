#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

bool is_valid(char *input)
{
    int i = strlen(input);
    if (input[0] == '\0')
    {
        return false;
    }
    if ((input[i - 1] != 'b') || (input[i - 2] != 'b'))
    {
        return false;
    }
    for (int j = i - 3; j >= 0; j--)
    {
        if (input[j] != 'a')
        {
            return false;
        }
    }
    return true;
}

int main()
{
    char *input = (char *)malloc(7 * sizeof(char));
    printf("Enter a string: ");
    scanf("%s", input);
    printf("You entered: %s\n", input);
    bool valid = is_valid(input);
    printf("The string is %s\n", valid ? "valid" : "invalid");
    return 0;
}