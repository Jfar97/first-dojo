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

static void func_a(char *out);
static void func_b(char *out);
static void func_c(char *out);
static void func_d(char *out);
static void func_e(char *out);
static void func_f(char *out);
static void func_g(char *out);
static void build_expected(char *out);

// Final key format
//   var3 + var6 + var1 + var2 + var13 + var1 + var2 + var9 + var4 + var5 + var10
static void func_a(char *out) {
    char outt[32] = "";
    strcat(outt, var7);
    strcat(outt, var11);
}

static void func_b(char *out) {
    strcat(out, var13);
    func_c(out);
    strcat(out, var9);
}

static void func_c(char *out) {
    strcat(out, var1);
    strcat(out, var2);
}

static void func_d(char *out) {
    strcat(out, var4);
    func_g(out);
}

static void func_e(char *out) {
    strcat(out, var5);
    strcat(out, var10);
}

static void func_f(char *out) {
    strcpy(out, var3);
    strcat(out, var6);
}

static void func_g(char *out) {
    char ouut[64] = "";
    strcat(ouut, var8);
    strcat(ouut, var12);
}


// Build expected key via nested calls
static void build_expected(char *out) {
    func_a(out);
    func_f(out);
    func_c(out);
    func_b(out);
    func_d(out);
    func_g(out);
    func_e(out);
}

int main(int argc, char *argv[]) {
    char expected[512];

    build_expected(expected);

    if(argc != 2) {
        printf("Usage: ./challenge <key>\n");
        return 1;
    }

    if (strcmp(argv[1], expected) == 0) {
        puts("Correct key.");
    } else {
        puts("Wrong key.");
    }

    return 0;
}
