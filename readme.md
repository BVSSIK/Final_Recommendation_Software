# Destiny Game Machine

The basis of the project was to create a recommendation system in the command line terminal. With how much I love games I decided to create a video game recommendation system. I wrote down all the data from Steam and other online video game stores and then created an html parser to organize my data in a list of lists for later use in the Tree/Linked-List data structure. The video games themselves are stored in their sub-genre linked lists which are then stored in a graph by their parent genres. (think RPG as a parent to ARPG)

**To run the program all you need to do is run the script.py file as it contains the main loop of the system.**

You will be prompted with 2 different types of searches genre search and tag search. Genre search moves down the tree from genre to sub-genre, from the user's input, then displaying all choices of that sub-genre. Tag search gives the user 3 possible tags to enter being the games flavor/genre, (includes things like sci-fi or singleplayer but also arpg or team sports) price, (from a given list) and review out of 5. 

[GitHub](https://github.com/BVSSIK/Final_Recommendation_Software "Github home")