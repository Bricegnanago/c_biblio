#include <stdio.h>
#include <stdlib.h>


#define SHELLSCRIPT "\
#/bin/bash \n\
python python.py \n\
"
/*Also you can write using char array without using MACRO*/
/*You can do split it with many strings finally concatenate 
  and send to the system(concatenated_string); */

int main()
{    
    system(SHELLSCRIPT);    //it will run the script inside the c code. 
    return 0;
}