#include<iostream>
using namespace std;

int main()
{
	int numero = 0;

	for (int numero = 0; numero < 101; numero++)
	{
        

		if (numero % 3 == 0)
		{
			cout << "fizz" << endl;
            
                if (numero % 5 == 0)
                {
                    cout << "buzz" << endl;
                   
                }
                    if (numero % 5 == 0 && numero % 3 == 0)
                    {
                        cout << "fizzbuzz" << endl;
                        
                    }
            continue;
		}
		else {cout << numero <<endl;}

	}
}