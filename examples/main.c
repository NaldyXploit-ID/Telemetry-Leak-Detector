/* Simple C program: print a small demonstration */
#include <stdio.h>
#include <time.h>
int main(void){
  time_t t = time(NULL);
  char buf[64];
  struct tm *tm = gmtime(&t);
  strftime(buf, sizeof(buf), "%Y-%m-%dT%H:%M:%SZ", tm);
  printf("Project: %s\n", "Telemetry-Leak-Detector");
  printf("Time UTC: %s\n", buf);
  printf("Demo C program compiled simple output\n");
  return 0;
}
