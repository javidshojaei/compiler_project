def calculate_first_sets():
    first_sets = {
        'S': set(),
        'A': {'a'},
        'B': {'c', 'ε', 'd'},
        'D': {'d'}
    }
    first_sets['S'] = first_sets['A']  # Since S -> AB and A -> a
    return first_sets

def calculate_follow_sets(first_sets):
    follow_sets = {
        'S': {'$'},
        'A': set(),
        'B': set(),
        'D': set()
    }
    
    follow_sets['A'].update(first_sets['B'] - {'ε'})  # From S -> AB
    if 'ε' in first_sets['B']:
        follow_sets['A'].update(follow_sets['S'])  # If B can be ε, add Follow(S) to Follow(A)
    
    return follow_sets

first_sets = calculate_first_sets()
follow_sets = calculate_follow_sets(first_sets)

print("Follow(A) =", follow_sets['A'])
