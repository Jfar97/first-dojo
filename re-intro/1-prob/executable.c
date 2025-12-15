#include <stdio.h>
#include <string.h>
#include <stdlib.h>

// All strings are injected by .init
#ifndef S1
#define S1 "missing"
#endif
#ifndef S2
#define S2 "missing"
#endif
#ifndef S3
#define S3 "missing"
#endif
#ifndef S4
#define S4 "missing"
#endif
#ifndef S5
#define S5 "missing"
#endif
#ifndef S6
#define S6 "missing"
#endif
#ifndef S7
#define S7 "missing"
#endif
#ifndef S8
#define S8 "missing"
#endif
#ifndef S9
#define S9 "missing"
#endif
#ifndef S10
#define S10 "missing"
#endif
#ifndef S11
#define S11 "missing"
#endif
#ifndef S12
#define S12 "missing"
#endif
#ifndef S13
#define S13 "missing"
#endif
#ifndef S14
#define S14 "missing"
#endif
#ifndef S15
#define S15 "missing"
#endif

// Used vars for key - .data
char var1[]  = S1;
char var2[]  = S2;
char var3[]  = S3;
char var4[]  = S4;
char var5[]  = S5;
char var6[]  = S6;
char var7[]  = S7;
char var8[]  = S8;
char var9[]  = S9;

// Decoys - .data
char var10[] = S10;
char var11[] = S11;
char var12[] = S12;
char var13[] = S13;

// Misleading function that uses decoys
static void fake_path(char *out) {
    // Need to make volatile for higher optimization levels
    size_t x = 0;
    x += strlen(var10);
    x += strlen(var11);
    x += strlen(var12);
    x += strlen(var13);
}

// Final key format
//   var1 + var2 + var3 + var4 + var5 + var6 + var7 + var8 + var9
static void step_a(char *out) {
    strcpy(out, var1);
    strcat(out, var2);
}

static void step_b(char *out) {
    strcat(out, var3);
    fake_path(out);
    strcat(out, var4);
}

static void step_c(char *out) {
    strcat(out, var5);
    fake_path(out);
}

static void step_d(char *out) {
    strcat(out, var6);
    strcat(out, var7);
}

static void step_e(char *out) {
    strcat(out, var8);
    strcat(out, var9);
}


// Build expected key via nested calls
static void build_expected(char *out) {
    step_a(out);
    fake_path(out);
    step_b(out);
    step_c(out);
    fake_path(out);
    step_d(out);
    step_e(out);
}

int main(void) {
    char input[512];
    char expected[512];

    build_expected(expected);

    if (!fgets(input, sizeof(input), stdin)) {
        return 1;
    }

    input[strcspn(input, "\n")] = '\0';

    if (strcmp(input, expected) == 0) {
        puts("Correct key.");
    } else {
        puts("Wrong key.");
    }
    return 0;
}
