#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include "word_library.h"

using namespace std;

// TODO: Write the loadDictionary function


// TODO: Write the containsWord function

// This function has been implemented for you; it can be called from main() to test loadDictionary
void testLoadDictionary() {
  vector<string> fake_dictionary_words;
  ifstream fin("words.txt");
  loadDictionary(fake_dictionary_words, fin);

  if( fake_dictionary_words.size() == 58112 ) {
    cout << "loadDictionary function is working properly!" << endl;
  } else {
    cout << "loadDictionary function is NOT working properly, try debugging it further." << endl;
  }
}

// This function has been implemented for you; it can be called from main() to test containsWord
void testContainsWord() {
    vector<string> fake_dictionary_words;
    fake_dictionary_words.push_back("flimflam");
    fake_dictionary_words.push_back("humdrum");
    fake_dictionary_words.push_back("snickerdoodle");

    if( containsWord(fake_dictionary_words, "snickerdoodle") && !containsWord(fake_dictionary_words, "hullabaloo") ) {
        cout << "containsWord function is working properly!" << endl;
    } else {
        cout << "containsWord function is NOT working properly, try debugging it further." << endl;
    }
}