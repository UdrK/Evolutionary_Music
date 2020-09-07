# Genetic_Music
This project's aim is to produce a genetic algorithm capable of composing short melodic lines.

Genetic algorithms work as follows:
1. Randomly generate an initial population of individuals

2. 1. Evaluate fitness of each individual
   2. Select the fittest individuals for reproduction
   3. Breed new individuals through __crossover__ and __mutation__
   4. Replace least fit individuals with the new individuals
   5. repeat

In order to use this approach to produce melodic lines i have to:
1. Understand how to randomly generate melodies
2. Find a way to evaluate and select the "fittest" melodies
3. Define what it means to have 2 melodies reproduce

For problem number one i'm going to read the book "Making Music with Computers" by Bill Manaris and Andrew R. Brown.

For problem number two i'm going to have the user (me) evaluate and select the fittest melodies. Later on i may train a neural network or other machine learning algorithm based on my scores to select melodies for me. 

For problem number three i don't have a solution at the moment, but i'm confident i'll find one as i develop the random
generator.
