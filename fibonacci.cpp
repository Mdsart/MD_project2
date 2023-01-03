/**
auteur: Maduka David <mdsartb@gmail.com>
version: fibonacci c++

 **/



#include <iostream>

using namespace std;

/**programme qui affiche une suite fibonacci
le resultat apres execution donnera une suite de:
1, 2, 3, 5, 8, 13, 21, 34,  55
**/

int main()
{
    int i= 1, a=1, b=1, c=1;
    while (i<10)
    {
         cout <<b<<endl;
         b= a+c;
         c=a;
         a=b;
         i= i+1;
     }	
}
