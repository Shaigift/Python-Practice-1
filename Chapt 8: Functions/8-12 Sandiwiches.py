def sandwiches(*ordered_sandwiches):
    """Printing ordered sandwiches"""
    print("\nMaking a sandwich with the following ingredients")
    for ordered_sandwiche in ordered_sandwiches:
        print(f"- {ordered_sandwiche}")
sandwiches('Salami')
sandwiches('chicken mushroom', 'bacon sandwich' , 'egg sandwich')
sandwiches('tomatoe' , 'avacado')


