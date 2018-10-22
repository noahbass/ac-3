from ac3 import CSPSolver

# Adds a interactive layer above csp_ac3.py to visually show the ac-3 algorithm
# Go to next step in the ac-3 algorithm by hitting the enter key


# Show the heading row
def show_head_row():
    print("Edge    | New Domain     | Edges to Reconsider")
    print("--------|----------------|--------------------")


# Display a single row of ac-3
def show_row(edge: tuple, xi: str, new_domain: list, edges_to_reconsider: list):
    print(str(edge) + "  |  " + str(xi) + "=" + str(new_domain) + "  |  " + str(edges_to_reconsider))


# solve the given CSP and print the results from the generated solve funcion
def show_solver(arcs: list, domains: dict, constraints: dict):
    solver = CSPSolver(arcs, domains, constraints)
    result = solver.solve(True)  # True indicates that we are using the method as a generator

    for step in result:
        continue_input = input()  # continue with the function generator only on user input (ex: enter key)

        if step == None:
            # found an inconsistency
            print("Inconsistent!. No solution possible.")
        else:
            edge = step[0]

            if edge == None:
                # reached the final result
                final_domain = step[1]
                print("Result:", final_domain)
            else:
                xi = edge[0]
                new_domain = step[1][xi]
                edges_to_reconsider = step[2]
                show_row(edge, xi, new_domain, edges_to_reconsider)


if __name__ == "__main__":
    show_head_row()

    # arcs, domains, and constraints
    arcs = [('a', 'b'), ('b', 'a'), ('b', 'c'), ('c', 'b'), ('c', 'a'), ('a', 'c')]

    domains = {
        'a': [2, 3, 4, 5, 6, 7],
        'b': [4, 5, 6, 7, 8, 9],
        'c': [1, 2, 3, 4, 5]
    }

    # constraints:
    # b = 2*a
    # a = c
    # b >= c - 2
    # b <= c + 2
    constraints = {
        ('a', 'b'): lambda a, b: a * 2 == b,
        ('b', 'a'): lambda b, a: b == 2 * a,
        ('a', 'c'): lambda a, c: a == c,
        ('c', 'a'): lambda c, a: c == a,
        ('b', 'c'): lambda b, c: b >= c - 2,
        ('b', 'c'): lambda b, c: b <= c + 2,
        ('c', 'b'): lambda c, b: b >= c - 2,
        ('c', 'b'): lambda c, b: b <= c + 2
    }

    show_solver(arcs, domains, constraints)
