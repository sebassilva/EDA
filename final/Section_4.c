#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <omp.h>
#include <time.h>



int main()
{
    FILE * file;
    clock_t tf,ti;
    char * line = NULL;
    char list[1000][80];
    int line_num=0,i,total,aux;
    int promedio,tid;

    size_t len = 0;
    ssize_t read;

    file = fopen("list.txt", "r");
    if (file == NULL){
        printf("Archivo Vacio\n");
        return -1;
    }

    while ((read = getline(&line, &len, file)) != -1) {
        
        strcpy(list[line_num],line);
        line_num=line_num+1;
    }

    ti=clock();

    #pragma omp parallel for num_threads(4) private(tid)
    
    for(i=0;i<line_num;i++){
    	aux=strlen(list[i]);
    	tid=omp_get_thread_num();
    	#pragma omp critical
    	{
    	printf("Thread:%d Word:%s\n",tid,list[i]);
    	total=total+aux;
    	}
    }



    promedio=total/line_num;
    printf("Promedio:%d \n",promedio);

    fclose(file);
    if (line)
        free(line);

    printf("Time:%f ms\n", ((double)clock()-ti));
}