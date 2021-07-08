#include <stdio.h>

int main(void) {
	// your code goes here
	int t,n,k,i,j,l,c;
	scanf("%d",&t);
	for(i=0;i<t;i++)
	{
	    scanf("%d %d",&n,&k);
	    int arr[n];
	    for(j=0;j<n;j++)
	    {
	        scanf("%d",&arr[j]);
	    }
	    int bt[33];
	    for(j=0;j<33;j++)
	      bt[j]=0;
	    for(j=0,l=33;j<n;j++)
	    {

	        while(arr[j]>0)
	        {
	            bt[l]=bt[l]+arr[j]%2;
	            arr[j]=arr[j]/2;
	            l--;
	        }
	    }
	    c=0;
	    for(j=0;j<33;j++)
	    {
	        if(bt[j]%k==0)
	         c=c+bt[j]/k;
	        else
	         c=c+1+bt[j]/k;
	    }
	    printf("%d\n",c);
	}
	return 0;
}

