import csv
import time
from queue import Queue

# Read the coordinates from the CSV file
def read_coordinates(file_path):
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        coordinates = {rows[0]: (float(rows[1]), float(rows[2])) for rows in reader}
    return coordinates

# Read the adjacencies from the TXT file
def read_adjacencies(file_path):
    with open(file_path, 'r') as file:
        adjacencies = {}
        for line in file:
            cities = line.strip().split(' ')
            if cities[0] not in adjacencies:
                adjacencies[cities[0]] = []
            adjacencies[cities[0]].append(cities[1])
            # Since adjacency is symmetric, add the reverse as well
            if cities[1] not in adjacencies:
                adjacencies[cities[1]] = []
            adjacencies[cities[1]].append(cities[0])
    return adjacencies

# Calculate the distance between two coordinates (simplified, not accounting for earth's curvature)
def calculate_distance(coord1, coord2):
    return ((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)**0.5

# Perform BFS to find the shortest path from start to end
def bfs(adjacencies, start, end):
    visited = {city: False for city in adjacencies}
    previous = {city: None for city in adjacencies}
    queue = Queue()
    queue.put(start)
    visited[start] = True
    while not queue.empty():
        current_city = queue.get()
        if current_city == end:
            break
        for neighbor in adjacencies[current_city]:
            if not visited[neighbor]:
                queue.put(neighbor)
                visited[neighbor] = True
                previous[neighbor] = current_city
    # Reconstruct the path from end to start
    path = []
    while end is not None:
        path.insert(0, end)
        end = previous[end]
    return path

# Given a path of cities, calculate the total distance
def path_distance(path, coordinates):
    total_distance = 0
    for i in range(len(path) - 1):
        total_distance += calculate_distance(coordinates[path[i]], coordinates[path[i + 1]])
    return total_distance

# Main program function
def find_route(start_city, end_city, coordinates_file, adjacencies_file):
    coordinates = read_coordinates(coordinates_file)
    adjacencies = read_adjacencies(adjacencies_file)
    if start_city not in coordinates or end_city not in coordinates:
        return "Start or end city not in database."
    
    start_time = time.time()
    path = bfs(adjacencies, start_city, end_city)
    end_time = time.time()
    
    if len(path) <= 1:  # If the path contains only the start city or is empty, no route was found
        return "No route found."
    
    total_distance = path_distance(path, coordinates)
    elapsed_time = end_time - start_time
    
    return {
        "route": path,
        "total_distance": total_distance,
        "time_taken": elapsed_time
    }

# Replace 'coordinates.csv' and 'Adjacencies.txt' with the actual file paths
coordinates_file_path = 'coordinates.csv'
adjacencies_file_path = 'Adjacencies.txt'

# Example use-case (replace 'Anthony' and 'Wichita' with user inputs)
result = find_route('Anthony', 'Wichita', coordinates_file_path, adjacencies_file_path)
print(result)
