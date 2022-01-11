#include <stdio.h>

int handleComputation(int* a, int* b) {
    int res = 0;

    if (*a > *b) {
        res = 1;
    }
    *b = *a;

    return res;
}

int main() {
    FILE * fp = fopen("day1_input.txt", "r");
    
    int prev, curr = 0, ch, count = 0;

    while ((ch = fgetc(fp)) != EOF) {
        if (ch != 10) { // reading the number
            curr *= 10;
            curr += ch - 48;
        } else if (ch == 10) { // finished reading the number
            count += handleComputation(&curr, &prev);
            curr = 0;
        }
    }
    
    if (curr != 0) {
        count += handleComputation(&curr, &prev);
    }

    printf("%d", count);
}