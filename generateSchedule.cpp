#include <iostream>
#include <fstream>
#include <vector>
#include <cmath>
#include <string>

using namespace std;

// Create a struct, Course, with information from Atlas scheduling tool
struct Course{
    string id; // The course code, with department and course number
    int credits; // The number of credits the course is worth
    string median_grade; // The median letter grade received in the course
    double workload; // The percentage of students (in decimal form) rating the course as more workload than typical
    double understanding; // The percentage of students (in decimal form) rating the course as increasing their understanding
    bool selected; // A boolean representing whether the course has been selected already
}

// Load the courses from the course catalog file into a vector of possible courses we could add to the schedule
void loadCourses(vector<Course> &catalog, ifstream &is){
    // Create a new course variable
    Course course;
    // Fill the course variable with information from the istream
    while(is >> course.id >> course.credits >> course.median_grade >> course.workload >> course.understanding){
        // Add the course to the catalog vector
        catalog.pop_back(Course);
    }
}

int main(){
    // set seed
    srand(1);

    // Establish an ifstream
    ifstream courseData("courseCatalog.txt");
    vector<Course> catalog;

    // Load the courses into a vector
    loadCourses(&catalog, &courseData);
    
    // Create another vector to hold the courses in the generated schedule
    vector<Course> schedule;

    // Initialize variables
    int total_credits = 0;
    double total_workload = 0;
    double average_workload;

    // Continue to add classes while the generated schedule meets the criteria
    while(total_credits <= 15 && average_workload <= 0.4){
        // Generate a random index to select from the course catalog
        int rand_index = rand() % catalog.size();

        // if the course has not been selected, then add it to the schedule
        // and update running totals and average workload
        if (!catalog.at(rand_index).selected) {
            catalog.at(rand_index).selected = true;
            schedule.push_back(catalog.at(rand_index));
            total_credits += catalog.at(rand_index).credits;
            total_workload += catalog.at(rand_index).workload;
            average_workload = total_workload / schedule.size();
        }

    // Once the schedule is complete, output the courses and their credits
    for(size_t i = 0; i < schedule.size(); ++i){
        cout << schedule.at(i).id << " ";
        cout << schedule.at(i).credits << endl;
    }

}