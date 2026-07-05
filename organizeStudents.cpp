#include <iostream>
#include <fstream>
#include <string>
using namespace std;

string students_at_table(string filename, int tablenumber) {
    ifstream fin(filename);

    if (fin_is_open()){
        cout << "Can't open file!" << endl;
    }

    string studentName;
    int tableNum;
    String students;

    while (fin >> studentName >> tableNum){
        if (tableNum == tablenumber){
            students += studentName;
        }
return students;
}

int main(){
    string filename;
    string students;
    cout << "Enter your roster of students" << endl;
    cin >> filename;
    for(i = 1; i <5; i++){
        students = students_at_table(filename, i);
        cout << students;
    }
    
}
