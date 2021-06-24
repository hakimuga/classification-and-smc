#include"utilities.hpp"

/** here are the parameters of the system **/
/** notice that the period must be longer 
enough wrt the propagation delays. Otherwise, 
deadlocks will appear in the model **/

/** time unit = microseconds **/

/** ~ 10 minutes would be enough **/
int INFINIT()
{
	return 600 * 1000 *1000 ; 
}

/** synchronisation period, fixed to 1 min **/
int PERIOD()
{ 
	return 60 * 1000 * 1000; 
}

int MIN(int d1, int d2, int d3, int d4){ 
	int d12 = (d1 < d2) ? d1 : d2; 
	int d34 = (d3 < d4) ? d3 : d4;
	return (d12 < d34) ? d12 : d34; 
}

/** FollowUp delay is uniform(10,20) 
This choice enforces the reception and sending 
of the Synch msg before the reception of the 
FollowUp msg **/
int chooseFollowUpDelay()
{ 
	return  10 + (random() % 10); 
}


const char* getfield(char* line, int num)
{
    const char* tok;
    for (tok = strtok(line, ",");
            tok && *tok;
            tok = strtok(NULL, ",\n"))
    {
        if (!--num)
            return tok;
    }
    return NULL;
}

const float getfield1(char* filecsv, int ln, int cl)
{

   /* int x=1;
    int y=5;
    char* s="src1/test1.csv";*/

    FILE* stream = fopen(filecsv, "r");
     int i=0;
     char line[1000];
    while (fgets(line, 1000, stream) && i<366)
            {
       		char* tmp = strdup(line);
       		if (ln==i)
       		 return atof(getfield(tmp, cl));

       	    //printf("%s",line);
       	    free(tmp);
       		i++;}
}


float minDIST(float n1, float n2, float n3){
    if( n1<=n2 && n1<=n3 )
        {return  n1;}
    if( n2<=n1 && n2<=n3 )
        {return  n2;}
    if( n3<=n1 && n3<=n2 )
        {return  n3;}
    return 0;
}

float minDISTT(float n1, float n2){
    if( n1<=n2 )
        {return  n1;}
    if( n2<n1)
        {return  n2;}
    return 0;
}


float readWH(int item){

return getfield1("discritization_test.csv", item, 3);
}

float readWV(int item){

return getfield1("discritization_test.csv", item, 4);
}

float readWP(int item){

return getfield1("discritization_test.csv", item, 2);
}

float readDIST0(int item){

return getfield1("discritization_test.csv", item, 7);
}

float readDIST1(int item){

return getfield1("discritization_test.csv", item, 8);
}

float readDIST2(int item){

return getfield1("discritization_test.csv", item, 9);
}

float readDIST3(int item){

return getfield1("discritization_test.csv", item, 10);
}

float readDIST4(int item){

return getfield1("discritization_test.csv", item, 11);
}

float readDIST5(int item){

return getfield1("discritization_test.csv", item, 12);
}

