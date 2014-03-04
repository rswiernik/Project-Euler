#include <stdio.h>
#include <time.h>

int main(){
	int x = 1, y = 2, z = 0;
	int sum = 0, limit = 4000000;
	
	clock_t time = clock();

	do{
		z = x + y;
		if( y % 2 == 0)
			sum += y;
		x = y; y = z;
	} while(y<4000000);
	
	time = clock()-time;

	printf("<C> Sum of Fibonacci sequence less than %d: %d  (found in %f seconds)\n", limit, sum, ((double)time/CLOCKS_PER_SEC));

	return 0;
}
