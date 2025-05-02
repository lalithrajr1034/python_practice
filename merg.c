#include <stdio.h>

void merge(int arr[], int left, int mid, int right) {
    int i, j, k;
    int n1 = mid - left + 1;//first
    int n2 = right - mid;   //second
 
    int L[n1], R[n2];       // Create temporary arrays

    // Copy data to temp arrays L[] and R[]
    for (i = 0; i < n1; i++)
        L[i] = arr[left + i];
    for (j = 0; j < n2; j++)
        R[j] = arr[mid + 1 + j];

    // Merge the temp arrays back into arr[]
    i = 0; j = 0; k = left;
    while (i < n1 && j < n2) {
        if (L[i] <= R[j]) {
            arr[k++] = L[i++];
        } else {
            arr[k++] = R[j++];
        }
    }

    // Copy remaining elements of L[]
    while (i < n1) {
        arr[k++] = L[i++];
    }

    // Copy remaining elements of R[]
    while (j < n2) {
        arr[k++] = R[j++];
    }
}

void mergeSort(int arr[], int left, int right) {
    if (left < right) {
        int mid = left + (right - left) / 2;

        // Sort first and second halves
        mergeSort(arr, left, mid);
        mergeSort(arr, mid + 1, right);

        merge(arr, left, mid, right);
    }
}

// Utility function to print an array
void printArray(int arr[], int size) {
    for (int i = 0; i < size; i++)
        printf("%d ", arr[i]);
    printf("\n");
}

// Main function to run the code
int main() {
    int arr[] = {6, 3, 9, 5, 2, 8};
    int size = sizeof(arr) / sizeof(arr[0]);

    printf("Before sorting: ");
    printArray(arr, size);

    mergeSort(arr, 0, size - 1);

    printf("After sorting: ");
    printArray(arr, size);

    return 0;
}
