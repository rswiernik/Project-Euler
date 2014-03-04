#include <stdio.h>
#include <time.h>

int main() {
	
	int limit = 1000;
	int sum = 0;

	clock_t time = clock();
	
	for(int i=0;i<limit;i++){
		if(i%3==0 || i%5==0){
			sum += i;
		}
	}
	
	time = clock()-time;

	printf("<C> Sum of digits less than %d: %d  (found in %f seconds)\n", limit, sum, ((double)time/CLOCKS_PER_SEC));

	return 0;
}
