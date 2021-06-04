void QuickSort(int R[], int lo, int hi){
    int i = lo, j = hi;
    int temp;
    if(i < j){
        temp = R[i];
        while (i != j)
        {
            while(j > i && R[j] >= temp)-- j;
            R[i] = R[j];
            while(i < j && R[i] =< temp)++ i;
            R[j] = R[i];
        }
        R[i] = temp;
        QuickSort(R, lo, i - 1);
        QuickSort(R, i + 1, hi);
    }
}

for (i=0; i<len-1; i++){ /* 外循环为排序趟数，len个数进行len-1趟 */
    for (j=0; j<len-1-i; j++) { /* 内循环为每趟比较的次数，第i趟比较len-i次 */
        if (arr[j] > arr[j+1]) { /* 相邻元素比较，若逆序则交换（升序为左大于右，降序反之） */
            temp = arr[j];
            arr[j] = arr[j+1];
            arr[j+1] = temp;
        }
    }
}