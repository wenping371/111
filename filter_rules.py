# filter_rules.py

def filter_projects(projects, equipment_types, exclusion_rules):
    """
    Filters the given projects based on equipment types and exclusion rules.

    :param projects: List of projects to filter
    :param equipment_types: List of equipment types to include
    :param exclusion_rules: List of rules to exclude certain projects
    :return: Filtered list of projects
    """
    filtered_projects = []

    for project in projects:
        if project['equipment_type'] in equipment_types:
            exclude = False
            for rule in exclusion_rules:
                if rule in project['name']:
                    exclude = True
                    break
            if not exclude:
                filtered_projects.append(project)

    return filtered_projects

# Example usage:
projects = [
    {'name': 'Concrete Project A', 'equipment_type': 'Excavator'},
    {'name': 'Concrete Project B', 'equipment_type': 'Bulldozer'},
    {'name': 'Other Project', 'equipment_type': 'Crane'},
]

equipment_types = ['Excavator', 'Bulldozer']
exclusion_rules = ['Other']

filtered = filter_projects(projects, equipment_types, exclusion_rules)
print(filtered)