#include <stdio.h>

static int global_target = 1337;

void functiontarget(int parameter_target) {
    printf("Using pwn.college is : %d\n", parameter_target);
}

int main() {
    int value = global_target;
    functiontarget(value);
    return 0;
}
