#include<stdio.h>
    int main()
    {
        char str[100];
        int len, i;
        printf("Enter the word:"\n);
        scanf("%c",str);
        len = strlen(str);
        for(i = 0; i < len/2; i++)
        {
            if (str[i] != str[len - i -1])

            {
                flag = 1;
                break;
            }
        }
        if (flag)
        {
            printf("The given word is not a palindrome!");
        }
        else
        {
            printf("The given word is a palindrome!");
        }
        return 0;

    }