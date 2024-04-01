from attractions import attractions

# Constants
APP_NAME = "Tourist Attractions Recommendation System"

interest_mapping = {
    '1': 'wildlife',
    '2': 'nature',
    '3': 'hiking',
    '4': 'scenery',
    '5': 'water activities',
    '6': 'relaxation',
    '7': 'history',
    '8': 'culture',
    '9': 'art',
    '10': 'night life',
    '11': 'urbanization',
}


def recommend_attractions(interests):
    recommended_attractions = []
    for key, attraction in attractions.items():
        if any(interest.lower() in attraction['interests'] for interest in interests):
            recommended_attractions.append(attraction)

    # If no recommendation is found, recommend the first attraction that matches any interest
    if not recommended_attractions:
        for key, attraction in attractions.items():
            if any(interest.lower() in attraction['interests'] for interest in interests):
                recommended_attractions.append(attraction)
                break

    return recommended_attractions


def exitTheApplication():
    print(f'Thanks for using the ${APP_NAME} app!')
    return exit(1)


def ask_interests():
    print("What are your interests? (Choose one or more)")
    print()
    print("1. Wildlife")
    print("2. Nature")
    print("3. Hiking")
    print("4. Scenery")
    print("5. Water activities")
    print("6. Relaxation")
    print("7. History")
    print("8. Culture")
    print("9. Art")
    print("10. Night Life")
    print("11. Urbanization")

    print("To exit the application press -1")
    print()
    interests_input = input(
        "Enter the numbers corresponding to your interests, separated by commas: ")

    if interests_input == "-1":
        exitTheApplication()
    interests = [interest_mapping.get(interest.strip())
                 for interest in interests_input.split(',')]
    return [interest for interest in interests if interest]


print("=========== Welcome to the Rwanda " + APP_NAME + "! ===========")
print()
print("================ Here are some popular tourist attractions in Rwanda: ==================")
print()

while True:
    selected_interests = ask_interests()

    # Creating a new dictionary that contains any of the selected interests variable

    filtered_data = {key: value for key, value in attractions.items() if
                     any(interest in value.get('interests', []) for interest in selected_interests)}

    if filtered_data:
        print("\nHere are the attractions matching your interests:")
        recommended_attractions = recommend_attractions(selected_interests)
        for key, value in filtered_data.items():
            print('Name: {},'.format(value['name']))
            print('Description: {},'.format(value['description']))
            print('Location: {}, {},'.format(value['district'], value['province']))
            print('Interests: {},'.format(', '.join(value['interests'])))
            print('-' * 80)

    else:
        print("Sorry, there are no attractions matching your interests.")

    next_action = input("Press any key to continue and -1 to exit")
    if next_action == "-1":
        exitTheApplication()
