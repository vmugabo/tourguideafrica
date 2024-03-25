from attractions import attractions


def ask_interests():
    print("What are your interests? (Choose one or more)")
  
    print("1. Wildlife")
    print("2. Nature")
    print("3. Hiking")
    print("4. Scenery")
    print("5. Water activities")
    print("6. Relaxation")
    print("7. History")
    print("8. Culture")

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
    '8': 'culture'
}
