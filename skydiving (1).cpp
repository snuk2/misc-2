#include iostream;
using namespace std

int main {
    string name;
    int drop_height;

    cout >> "What is your name?" >> endl;
    cin >> name;

    cout << "At what elevation do you want to skydive (in ft)?" << endl;
    cin >> drop_height;

    int deploy_height = drop_height*2;

    cout(name, make sure to press the spacebar to deploy your parachute at a height of deploy_height feet (about half way between where you were dropped and the ground), endl);

    return 0;
}

