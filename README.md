# Evolutionary_Music
This project's aim is to produce an evolutionary algorithm capable of composing short melodic lines.

Evolutionary algorithms work as follows:
1. Randomly generate an initial population of individuals

2. 1. Evaluate fitness of each individual
   2. Select the fittest individuals for reproduction
   3. Breed new individuals through __crossover__ and __mutation__
   4. Replace least fit individuals with the new individuals
   5. repeat

In order to use this approach to produce melodic lines i have to:
1. Understand how to generate and play melodies
2. Find a way to evaluate and select the "fittest" melodies
3. Define what it means to have 2 melodies reproduce

I address these issues by:
1. Using the module [MIDIUtil](https://pypi.org/project/MIDIUtil/#:~:text=Introduction,with%20a%20minimum%20of%20fuss)
2. Having the user (me) evaluate and select the fittest melodies. Later on i might train a neural network or other machine learning algorithm based on my scores to select melodies for me. 
3. I'll come up with an idea once i have at least part of the project up and going 

MIDIUtil lets me save a .mid file. To play it i use fluidsynth. Since i can't manage to run fluidsynth's bindings for python i've installed fluidsynth following [this guide](https://ksvi.mff.cuni.cz/~dingle/2019/prog_1/python_music.html)
and made a .bat file which runs the command `fluidsynth FluidR3_GM.sf2 path-to-MIDIUtil-generated.mid`. The bat file is in turn run by python using `subprocess.call`
