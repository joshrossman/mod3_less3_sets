#1. Python Sets Adventure
# Objective: The aim of this assignment is to deepen 
# your understanding and application of Python sets.
# Task 1: Flight Route Comparison Imagine you work for an airline and need to compare 
# the flight routes of your airline with a competitor. 
# You have two sets of flight destinations, one for each airline. Write a Python program to find out:
# 1. Destinations that both airlines fly to.
# 2. Destinations unique to your airline.
# 3. Whether there are any destinations that neither airline shares.
# Example Code:
#our_routes = {"LAX", "JFK", "CDG", "DXB"}
#competitor_routes = {"JFK", "CDG", "LHR", "BKK"}

our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}
joint_destination = our_routes.intersection(competitor_routes)
unique_routes = our_routes.difference(competitor_routes)
unique_to_both= our_routes.symmetric_difference(competitor_routes)

print(f"Shared routes include: {joint_destination}\nOur unique routes are: {unique_routes}\nDestinations which are not shared: {unique_to_both}")