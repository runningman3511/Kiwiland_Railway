from neograph import Neograph


def main():

    input_graph = ['AB5', 'BC4', 'CD8', 'DC8', 'DE6', 'AD5', 'CE2', 'EB3', 'AE7']
    neograph=Neograph()
    try:
        for input_data in input_graph:
            neograph.add_edge(input_data[0],input_data[1], input_data[2])
    except:
        print(f'Please check your input graph since it caused an error')

    print(f'Output #1: {neograph.solve_distance("A-B-C")}')
    print(f'Output #2: {neograph.solve_distance("A-D")}')
    print(f'Output #3: {neograph.solve_distance("A-D-C")}')
    print(f'Output #4: {neograph.solve_distance("A-E-B-C-D")}')
    print(f'Output #5: {neograph.solve_distance("A-E-D")}')

    print(f'Output #6: {neograph.solve_same_start_stop_maximum("C","C",3)}')
    print(f'Output #7: {neograph.solve_start_stop_exact("A","C",4)}')
 
    print(f'Output #8: {neograph.solve_shortest_routev2("A","C")}')
    print(f'Output #9: {neograph.solve_shortest_routev2("B","B")}')

    print(f'Output #10: {neograph.solve_number_of_different_routes("C","C",30)}')
if __name__ == "__main__":
    main()