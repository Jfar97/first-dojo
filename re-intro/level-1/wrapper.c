#include <unistd.h>
#include <stdio.h>

int main(int argc, char *argv[]) {
  execl("/usr/bin/env", "python3", "/challenge/.hidden_runtest.py", argv[1], NULL);
  return 0;
}
