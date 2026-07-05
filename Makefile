CXX ?= g++
CXXFLAGS ?= -Wall -Werror -pedantic -g --std=c++11

# Compile the tests you wrote for buggy_flip
delivery.exe: delivery.cpp
	$(CXX) $(CXXFLAGS) delivery.cpp -o delivery.exe

# Remove automatically generated files
clean :
	rm -rvf *.exe *~ *.out *.dSYM *.stackdump
