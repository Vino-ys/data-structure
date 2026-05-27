#include <stdio.h>

// void swap(int a, int b) {
//     int temp = a;
//     a = b;
//     b = temp;
// }
// call by value 

// char 형 변수: 1byte
// int 형 변수: 4byte
// float 형 변수: 4byte

// int main(void){
//     int number = 10;
//     int *p;
//     p = &number;
//     printf("%d",*p); // 역참조~
// }
int main() {
    int a = 10;
    int *p;
    p = &a;

    *p = 36; //역참조해서 값 저장

    printf("%d %d", *p, a);

    return 0;
}