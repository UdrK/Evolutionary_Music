# Evolutionary_Music
This project's aim is to produce an evolutionary algorithm capable of composing simple short melodic lines.

Evolutionary algorithms work as follows:
1. Randomly generate an initial population of individuals

2. 1. Evaluate fitness of each individual
   2. Select the fittest individuals for reproduction
   3. Produce new individuals through __crossover__ and __mutation__
   4. Replace least fit individuals with the new individuals
   5. repeat

In order to use this approach to produce melodic lines i had to:
1. Understand how to generate and play melodies
2. Find a way to evaluate and select the "fittest" individuals
3. Define what it means to have 2 individuals reproduce

I addressed these issues by:
1. Using the module [MIDIUtil](https://pypi.org/project/MIDIUtil/#:~:text=Introduction,with%20a%20minimum%20of%20fuss)
2. Having the user (me) evaluate and select the fittest melodies. Later on i might train a neural network or other machine learning algorithm based on my scores to select melodies for me. 
3. Instead of using the usual crossover and mutation approach i modeled genes as probabilities, where probabilities are high for both parents, the child will have high probability. 

MIDIUtil lets me save a .mid file. To play it i use fluidsynth. Since i can't manage to run fluidsynth's bindings for python i've installed fluidsynth following [this guide](https://ksvi.mff.cuni.cz/~dingle/2019/prog_1/python_music.html)
and made a .bat file which runs the command `fluidsynth FluidR3_GM.sf2 path-to-MIDIUtil-generated.mid`. The bat file is in turn run by python using `subprocess.call`

## Project structure

### Individual
This class represents an Individual, a generator capable of producing sequences of notes. The most important attributes of an Individual are its genes:
Each individual has 3 matrices:
1. note_genes
2. duration_genes
3. dynamic_genes

Row i-th of each matrix represents the distribution of probability of each possible value (note, duration, dynamics) for the i-th note in the sequence.
For example, notes_genes[3][5] is the probability that the 4-th note of the sequence will be the 6-th note of the possible_notes list. This mechanisms
is the same for the other matrices, but the probability is referred to different aspects of the music: duration of the note, dynamics (volume) of the note.

### IndividualBuilder
IndividualBuilder has 2 methods that return a new fully functional Individual:
1. from_chance
2. from_individuals

The first method randomly generates an Individual. It takes a root note, a scale, and a phrase_length. The root note and scale are needed to determine
the pool of notes used by the individual to generate the music. The phrase_length simply says how many notes will be in the music generated. I might want
to add random generation using perlin noise.

The second method takes 2 individuals and mixes their genes to produce a third. This is done by: 
```
for each distribution from i1, i2 # that is, for each row of the individuals' matrices representing the genes
 for each probability of a single value from i1, i2
  if probability from i1 + probability from i2 > 3/2 * max(probability)
   then i3's probability = ( probability from i1 + probability from i2 )/sum(i3's probabilities)
  else
   i3's probability = min ( probability from i1 , probability from i2 )
```
This pseudo-code isn't accurate, it only needs to convey the idea. The division by the sum of i3's probabilities has to be done last
because you need the sum of i3's probabilities to do it. It is needed to keep the distributions as such (that is, such that the sum of probabilities = 1)

A graphical example:

![Figure_1](https://user-images.githubusercontent.com/26527575/93075252-d43be600-f685-11ea-9bd8-3ab403ae8de7.png)


The graph shows what probability has the first note of a generated piece to be a specific musical note.

The x axis shows possible notes in MIDI format (60 = C4)

The y axis represents probabilities.

So, from the graph we can tell that for i1 (individual1) the first note (because the graph shows the first row of the matrix) of the sequence has probability around 0.075 to be a 60 = C4.

The red line shows 3/2 * max(probability)

The purple line indicates the sum if i1's + i2's probabilities

The green line is the new probability as calculated by the pseudocode above.

### Environment
Environment is a sort of main. It will be executed to listen to a series of melodies generated by new individuals, and give a score
to each. The melodies will be saved as .mid files in a folder named `outputs`. With them will also be saved a .txt file that represents the melody (a list of: midi-note-representation_duration-in-beats) The environment will then:
1. Order individuals from best scoring to worst scoring
2. Keep the best half
3. On the other half:
    1. Replace half with individuals generated from the best scoring ones
    2. Replace the other half with individuals from chance

The environment will ask to continue, `y` will result in continuation, anything else will stop the execution. Before ending, the environment
will save the genes of every individual currently in the list of individuals in some .txt files. These can then be read by individuals using 
the `read_genes` method.

### visualize_genes
A simple file that uses matplotlib to produce a similar plot to the one shown above

### Music
A file that defines a series of constants regarding music. It defines:
1. Notes (integers)
2. Durations (float)
3. Dynamics (float)
4. Scales (represented as lists of integers representing absolute intervals from the root)