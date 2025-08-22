#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int global_initialized = 42;              
int global_UNinitialized;    

int main(int argc, char* argv[]) {
    int local = 16;
    const char* message = "Hello World";
    
    char* allocated = (char*)malloc(6);
    strcpy(allocated, "Hello");

    printf("Hello, ELF! argc=%d\n", argc);  
    printf("%s\n", message);
    printf("%s\n", allocated);


    free(allocated);

    return argc + global_initialized + global_UNinitialized + local;
}
