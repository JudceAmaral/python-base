#!/usr/bin/env python3

responses = {}

polling_active = True

while polling_active:
    name = input("\nWhat is your name?: ")
    response = input("\nWhich mountain would you like to climb someday?: ")
    
    responses[name] = response
    repeat = input("\nWould you like to let another person respond? (y/n): ")
    if repeat == 'n':
        polling_active = False
    

for name, response in responses.items():
    print("\n ---> " + name + " would like to climb " + response + ".")