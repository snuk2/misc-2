#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include "ships.h"

using namespace std;

int main(){
    ifstream fin("Boats.txt");
    ofstream fout("referenceShips.txt");
    vector<Boat> boats;

    loadShips(boats, fin);
    selectShips(boats);
    printShips(boats, fout);
    fout.close();

    int numberShips = boats.size();
    cout << "We found " << numberShips
         << " ships that match your criteria" <<endl;
}
