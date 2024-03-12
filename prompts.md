# Route-Finding Assignment

## Introduction

This assignment is a practical exploration into route-finding algorithms, focusing on a small set of cities and their connections. The objective is to find a path from a starting city (City A) to a destination city (City X) using various search strategies. This will involve implementing and comparing different search algorithms to understand their efficiencies and applicabilities in route-finding scenarios.

## Assignment Background

The context of this assignment involves utilizing resources such as generative models to rapidly implement versions of major route-finding methods discussed in Chapter 2 of our course material. This experimental report aims to detail the findings from comparing each method's effectiveness in route-finding. It emphasizes not only the technical implementation but also the use of generative models as a tool in the development process, showcasing the integration of modern AI tools in solving classic computer science problems.


### Everything Below this Line is a Prompt ###
-------------------------------------------
## Programming Details

- **Languages Supported:** C, C++, Python, C#, Java. (Other languages may be considered upon prior discussion.)
- **Data Files Provided:**
  - A list of cities, mostly small towns in southern Kansas, along with their latitude and longitude. City names are formatted with underscores for spaces (e.g., South_Haven).
  - A CSV file listing pairs of adjacent towns. Adjacency is symmetric; if A is adjacent to B, then B is adjacent to A. It's crucial to ensure this symmetry is reflected in your program's data structures.

## Program Requirements

1. **User Input:**
   - The program should prompt the user for the starting and ending towns, ensuring both are in the database.
   - The user is then asked to select a search method to find a route to the destination.

2. **Search Methods to Implement:**
   - **Undirected (Blind) Brute-Force Approaches:**
     - Breadth-First Search
     - Depth-First Search
     - ID-DFS Search
   - **Heuristic Approaches:**
     - Best-First Search
     - A* Search

3. **Program Output:**
   - If a route exists, the program should print the route found, from origin to destination.
   - Optionally, it can display the route as a map or as a projection in 2D space based on location and connectivity.

4. **Performance Measurement:**
   - The program should measure and print the total time needed to find the route, including a time-out feature.
   - Calculate and display the total distance (node to node) for the cities visited on the selected route.
   - Optionally, determine the total memory used to find the solution.

5. **Search Method Selection:**
   - The program should allow for the re-selection of the search method for comparative analysis without restarting.

## Additional Notes

- Utilize existing implementations where possible, but ensure to follow the pseudocode and function descriptions from the textbook as a guideline.
- Include the prompts used for any generative model assistance as part of your source documentation, emphasizing good practice in prompt-centric engineering. This inclusion highlights the novel approach of integrating generative AI into the software development process for this assignment.
- The database is intentionally limited, and many real-world roads are omitted for simplicity.

## Submission

Your submission should include the source code, a detailed experimental report comparing the different search methods, and any additional notes on your implementation choices or challenges faced. The use of generative models in aiding the code generation should be clearly documented, including the specific prompts used, to provide insight into the role of AI in modern software development practices.

