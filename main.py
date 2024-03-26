from attractions import attractions


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
    print()
    interests_input = input(
        "Enter the numbers corresponding to your interests, separated by commas: ")
    interests = [interest_mapping.get(interest.strip())
                 for interest in interests_input.split(',')]
    return [interest for interest in interests if interest]


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


print("=========== Welcome to the Rwanda Tourist Attractions Recommendation System! ===========")
print()
print("================ Here are some popular tourist attractions in Rwanda: ==================")
print()
selected_interests = ask_interests()
# Creating a new dictionary that contains any of the selected interests variable
filtered_data = {key: value for key, value in attractions.items() if any(interest in value.get('interests', []) for interest in selected_interests)}
for key, value in filtered_data.items():
    print('Name: {},'.format(value['name']))
    print('Description: {},'.format(value['description']))
    print('Location: {}, {},'.format(value['district'], value['province']))
    print('Interests: {},'.format(', '.join(value['interests'])))
    print('-' * 80)