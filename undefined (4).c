#include <stdio.h>

int main(void) {
	// your code goes here
	int t,i,d,x,y,z,a,b;
	scanf("%d",&t);
	for(i=0;i<t;i++)
	{
	    scanf("%d %d %d %d",&d,&x,&y,&z);
	    a=7*x;
	    b=d*y+(7-d)*z;
	    if(a>b)
	     printf("%d\n",a);
	    else
	     printf("%d\n",b);
	}
	return 0;
}

