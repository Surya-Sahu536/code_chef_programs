#include <stdio.h>

int main(void) {
	// your code goes here
	int t,i,g,c;
	int h;
	scanf("%d",&t);
	for(i=0;i<t;i++)
	{
	    scanf("%d %d",&g,&c);
	    h=(c*c)/(2*g);
	    printf("%d\n",h);
	}
	return 0;
}

