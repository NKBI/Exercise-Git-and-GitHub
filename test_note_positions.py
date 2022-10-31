import note_positions as note_position

"""test whether passing in the same value for target and string gives a return value of 0"""
if note_position.get_fret("B", "B") == 0:
    print("Correct  #1")
else:
    print("Error")

"""test at least one case where target corresponds to a larger number in your dictionary than string (for example, if target is "A" and string is "C")"""
if note_position.get_fret("C", "A") == 3:
    print("Correct #2")
else:
    print("Error")

"""test at least one case where target corresponds to a smaller number in your dictionary than string (for example, if target is "C" and string is "A")"""
if note_position.get_fret("A", "C") == 9:
        print("Correct #3")
else:
    print("Error")

"""for a note that has two names, test whether the function returns the same value when target is the sharp as when target is the flat 
(for example, does "A#" give the same fret as "Gb"?)"""
if note_position.get_fret("G#", "B") == note_position.get_fret("Ab", "B"):
        print("Correct #4")
else:
    print("Error")

"""test the function with a list consisting of a single string (e.g., ["G"]); check whether the function returns a dictionary with one key, 
and check whether the corresponding value is correct"""
dictionary = note_position.get_frets("A", ["G"])
if dictionary["G"] == 2:
        print("Correct #5")
else:
    print("Error")

"""test the function with a list consisting of multiple strings of different values[2] (e.g., ["G", "D", "A"]); 
check whether the function returns a dictionary with the same number of keys as the number of strings you passed in 
(assuming the strings are unique), and check whether the corresponding values are correct"""
dictionary = note_position.get_frets("B", ["G", "D", "A"])
if (dictionary["G"] == 4) and (dictionary["D"] == 9) and (dictionary["A"] == 2):
        print("Correct #6")
else:
    print("Error")