#include <cassert>
#include <iostream>
#include <array>
#include "Pack.hpp"

using namespace std;

 // EFFECTS: Initializes the Pack to be in the following standard order:
  //          the cards of the lowest suit arranged from lowest rank to
  //          highest rank, followed by the cards of the next lowest suit
  //          in order from lowest to highest rank, and so on.
  // NOTE: The standard order is the same as that in pack.in.
  // NOTE: Do NOT use pack.in in your implementation of this function
  Pack::Pack(){
    //initialize a count variable to iterate through the 
    //cards array
    int count_cards = 0;
    //find integer values of the largest
    //and smallest suits and ranks
    int smallest_suit = SPADES;
    int largest_suit = DIAMONDS;
    int smallest_rank = NINE;
    int largest_rank = ACE;
    //iterate through the four suits with i 
    //corresponding to integer value of each suit
    for(int i = smallest_suit; i <= largest_suit; ++i){
      //iterate through each rank 
      for(int j = smallest_rank; j <= largest_rank; ++j){
        //initialize a new card with the current rank and suit
        Card current(static_cast<Rank>(j), static_cast<Suit>(i));
        //add the current card to the cards array 
        cards[count_cards] = current;
        //go onto the next element of the cards array
        count_cards++;
      }
    }
    //the next card to be dealt is the first card
    //in the cards array
    next = 0;
  }

  // REQUIRES: pack_input contains a representation of a Pack in the
  //           format required by the project specification
  // MODIFIES: pack_input
  // EFFECTS: Initializes Pack by reading from pack_input.
  Pack::Pack(std::istream& pack_input){
    //initialize a count variable to iterate through the 
    //cards array
    int count_cards = 0;
    //initialize two variables for the rank and suit
    //in each line of input (assume all lines of input have
    //a suit and a rank) and a variable for " of "
    Rank rank;
    string middle = " of ";
    Suit suit;
    //read in the cards from the pack (for any size of the pack)
    //for each line set the rank and suit and omit " of "
    while(pack_input >> rank >> middle >> suit){
      //initialize a card with the read-in rank and suit
      Card current(rank, suit);
      //add the current card to the cards array
      cards[count_cards] = current;
      //go onto the next element of the cards array
      count_cards++;
    }
    //the next card to be dealt is the first card
    //in the cards array
    next = 0;
  }

  // REQUIRES: cards remain in the Pack
  // EFFECTS: Returns the next card in the pack and increments the 
  //next index
  Card Pack::deal_one(){
    //increment next to the next card index
    //(always greater than 0 after increment)
    int index = next;
    next++;
    //return the Card at the next index in the cards array
    //go back one card as next has already been incremented 
    return cards[index];
  }

  // EFFECTS: Resets next index to first card in the Pack
  void Pack::reset(){
    //set next to 0 as the first card index
    next = 0; 
  }

  // EFFECTS: Shuffles the Pack and resets the next index. This
  //          performs an in shuffle seven times. See
  //          https://en.wikipedia.org/wiki/In_shuffle.
  void Pack::shuffle(){
    //initialize an array for the deck before shuffling
    array<Card, PACK_SIZE/2> cards_half_top;
    array<Card, PACK_SIZE/2> cards_half_bottom;
    //repeat the in-shuffle process 7 times
    for(int i = 0;  i < 7; ++i){
      //set cards_half_top to the first 12 cards
      for(int j = 0; j < 12; ++j){
        cards_half_top[j] = cards[j];
      }
      //set cards_half_bottom to the last 12 cards
      for(int j = 12; j < PACK_SIZE; ++j){
        cards_half_bottom[j - 12] = cards[j];
      }
      //iterate though cards and change values 
      //alernating bottom and top cards
      int index_top = 0;
      int index_bottom = 0;
      for(int j = 0; j < PACK_SIZE; ++j){
        if(j % 2 == 0){
          cards[j] = cards_half_bottom[index_bottom];
          index_bottom = index_bottom + 1;
        }
        if (j % 2 == 1){
          cards[j] = cards_half_top[index_top];
          index_top = index_top + 1;
        } 
      }
      
    }
  }

  // EFFECTS: returns true if there are no more cards left in the pack
  bool Pack::empty() const{
    //if the next index is to 24 (passed the last
    //card at 23) then we have used all the cards
    if(next == 24){
      return true;
    }
    //otherwise return false
    return false;
  }

