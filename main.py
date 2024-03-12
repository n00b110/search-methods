import time
from collections import deque
import math
import heapq
import csv

# City information and adjacencies
cities_info = {}  # Key: city name, Value: (latitude, longitude)
city_adjacencies = {}  # Key: city name, Value: list of adjacent cities

def load_data():
    global cities_info, city_adjacencies

    # Load cities information
    with open('coordinates.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            city, lat, lon = row[0], float(row[1]), float(row[2])
            cities_info[city] = (lat, lon)

    # Load city adjacencies ensuring bidirectionality
    with open('Adjacencies.txt', 'r') as file:
        for line in file:
            cities = line.strip().split()
            for i in range(len(cities) - 1):
                city1 = cities[i]
                city2 = cities[i + 1]
                if city1 not in city_adjacencies:
                    city_adjacencies[city1] = []
                if city2 not in city_adjacencies:
                    city_adjacencies[city2] = []
                city_adjacencies[city1].append(city2)
                city_adjacencies[city2].append(city1)

def haversine(lat1, lon1, lat2, lon2):
    # Calculate the great circle distance between two points
    # on the earth (specified in decimal degrees)
    # Returns distance in kilometers
    R = 6371  # Radius of the Earth in kilometers
    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)
    delta_phi = math.radians(lat2 - lat1)
    delta_lambda = math.radians(lon2 - lon1)

    a = math.sin(delta_phi / 2) ** 2 + math.cos(phi1) * math.cos(phi2) * math.sin(delta_lambda / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return R * c

def user_input():
    # Collect user input for start and end cities and validate against the cities_info
    cities = list(cities_info.keys())
    print(cities)
    while True:
        start_city = input("Enter the start city: ").strip()
        if start_city in cities:
            break
        else:
            print("Invalid city name. Please try again.")

    while True:
        end_city = input("Enter the end city: ").strip()
        if end_city in cities:
            break
        else:
            print("Invalid city name. Please try again.")

    # Ask for the search method
    search_method = input("Enter the search method (BFS, DFS, ID-DFS, Best-First, A*): ").strip().upper()

    # Returns start_city, end_city, search_method
    return start_city, end_city, search_method

def bfs(start, goal):
    # Implement Breadth-First Search
    start_time = time.time()
    queue = deque([(start, [start])])
    visited = set()

    while queue:
        node, path = queue.popleft()
        if node == goal:
            return path, time.time() - start_time, calculate_route_distance(path)

        if node not in visited:
            visited.add(node)
            for neighbor in city_adjacencies[node]:
                new_path = path + [neighbor]
                queue.append((neighbor, new_path))

    return None, time.time() - start_time, 0

def dfs(start, goal):
    # Implement Depth-First Search
    start_time = time.time()
    stack = [(start, [start])]
    visited = set()

    while stack:
        node, path = stack.pop()
        if node == goal:
            return path, time.time() - start_time, calculate_route_distance(path)

        if node not in visited:
            visited.add(node)
            for neighbor in city_adjacencies[node]:
                new_path = path + [neighbor]
                stack.append((neighbor, new_path))

    return None, time.time() - start_time, 0

def id_dfs(start, goal):
    # Implement Iterative Deepening Depth-First Search
    start_time = time.time()
    for depth in range(len(city_adjacencies)):
        result, time_taken, distance = id_dfs_limited(start, goal, depth)
        if result is not None:
            return result, time_taken, distance

    return None, time.time() - start_time, 0

def id_dfs_limited(start, goal, depth):
    if depth == 0:
        if start == goal:
            return [start], 0, 0
        return None, 0, 0

    visited = set()
    stack = [(start, [start])]

    while stack:
        node, path = stack.pop()
        if node == goal:
            return path, 0, calculate_route_distance(path)

        if node not in visited:
            visited.add(node)
            for neighbor in city_adjacencies[node]:
                new_path = path + [neighbor]
                if len(new_path) <= depth + 1:
                    stack.append((neighbor, new_path))

    return None, 0, 0

def best_first_search(start, goal):
    # Implement Best-First Search using a heuristic
    start_time = time.time()
    queue = [(haversine(cities_info[start][0], cities_info[start][1],
                        cities_info[goal][0], cities_info[goal][1]),
              start, [start])]
    visited = set()

    while queue:
        _, node, path = heapq.heappop(queue)
        if node == goal:
            return path, time.time() - start_time, calculate_route_distance(path)

        if node not in visited:
            visited.add(node)
            for neighbor in city_adjacencies[node]:
                new_path = path + [neighbor]
                heuristic = haversine(cities_info[neighbor][0], cities_info[neighbor][1],
                                      cities_info[goal][0], cities_info[goal][1])
                heapq.heappush(queue, (heuristic, neighbor, new_path))

    return None, time.time() - start_time, 0

def a_star_search(start, goal):
    # Implement A* Search
    start_time = time.time()
    queue = [(0, start, [start])]
    visited = set()

    while queue:
        cost, node, path = heapq.heappop(queue)
        if node == goal:
            return path, time.time() - start_time, calculate_route_distance(path)

        if node not in visited:
            visited.add(node)
            for neighbor in city_adjacencies[node]:
                new_path = path + [neighbor]
                new_cost = cost + haversine(cities_info[node][0], cities_info[node][1],
                                            cities_info[neighbor][0], cities_info[neighbor][1])
                heuristic = haversine(cities_info[neighbor][0], cities_info[neighbor][1],
                                      cities_info[goal][0], cities_info[goal][1])
                heapq.heappush(queue, (new_cost + heuristic, neighbor, new_path))

    return None, time.time() - start_time, 0

def calculate_route_distance(route):
    # Calculate the total distance of the route
    # Use haversine function for distance calculation between cities
    total_distance = 0
    for i in range(len(route) - 1):
        start_city = route[i]
        end_city = route[i + 1]
        start_lat, start_lon = cities_info[start_city]
        end_lat, end_lon = cities_info[end_city]
        total_distance += haversine(start_lat, start_lon, end_lat, end_lon)

    return total_distance

def main():
    load_data()

    while True:
        start_city, end_city, method = user_input()

        if method == 'BFS':
            route, time_taken, total_distance = bfs(start_city, end_city)
        elif method == 'DFS':
            route, time_taken, total_distance = dfs(start_city, end_city)
        elif method == 'ID-DFS':
            route, time_taken, total_distance = id_dfs(start_city, end_city)
        elif method == 'BEST-FIRST':
            route, time_taken, total_distance = best_first_search(start_city, end_city)
        elif method == 'A*':
            route, time_taken, total_distance = a_star_search(start_city, end_city)
        else:
            print("Invalid search method. Please try again.")
            continue

        if route:
            print(f"Route: {' -> '.join(route)}")
            print(f"Time Taken: {time_taken:.6f} seconds")
            print(f"Total Distance: {total_distance:.2f} km")
        else:
            print("No route found.")

        # Ask if user wants to try another search method
        another_search = input("Do you want to try another search? (y/n) ").strip().lower()
        if another_search != 'y':
            break

if __name__ == "__main__":
    main()
