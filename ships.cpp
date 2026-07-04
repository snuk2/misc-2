#include <iostream>
#include <fstream>
#include <vector>
#include <cmath>
#include "ships.h"

using namespace std;

// read through the Boats.txt file and store each boat in the boat struct
void loadShips(vector<Boat> &boats, ifstream& boat_data){
    // TODO: Write a function to read in the ship data into the boats vector
    // Data in order goes: name, flag, TEUs, speed
    // Hint: Make element and push it into the vector


}

bool checkOneShip(const Boat& boat){
    // TODO: Write a function to verify the criteria for one boat
    // Remember, for US flagged entries, the flag will be "USA"


}

void selectShips(vector<Boat> &boats){
    // TODO: Write a function that removes the entries that don't meet the
    // requirements


}

void printShips(vector<Boat> &boats, ofstream& os){
    // The printShips function is written for you, but look through it to see
    // how the information is printed
    for(int x = 0; x < boats.size(); ++x ){
        os << boats.at(x).name << "\t"
             << boats.at(x).flag << "\t"
             << boats.at(x).speed << "\t"
             << boats.at(x).TEU << endl;
    }
}