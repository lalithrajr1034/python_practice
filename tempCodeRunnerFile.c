#include<stdio.h>
void main(){
int arr[] = {6, 3, 9, 5, 2, 8};
int size = sizeof(arr) / sizeof(arr[0]);//length
printf("Before sorting: ");
printArray(arr, size);
}