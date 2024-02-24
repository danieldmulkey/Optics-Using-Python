#include <stdio.h>
int main(void)
{
    char list_of_surfaces[4][11] = {
        "lens",
        "free space",
        "lens",
        "detector"
    };
    int i;
    for (i = 0; i < 4 ; i++)
    {
        printf("Surface: %s\n", list_of_surfaces + i);
    }
    return 0;
}

