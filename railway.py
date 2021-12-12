from neograph import Neograph


def main():

    input_graph = ['AB5', 'BC4', 'CD8', 'DC8', 'DE6', 'AD5', 'CE2', 'EB3', 'AE7']
    neograph=Neograph()
    try:
        for input_data in input_graph:
            neograph.add_edge(input_data[0],input_data[1], input_data[2])
    except:
        print(f'Please check your input graph since it caused an error')

    print(neograph.solve_distance("A-B-C",'Output #1:'))
    print(neograph.solve_distance("A-D",'Output #2:'))
    print(neograph.solve_distance("A-D-C",'Output #3:'))
    print(neograph.solve_distance("A-E-B-C-D",'Output #4:'))
    print(neograph.solve_distance("A-E-D",'Output #5:'))

    print(neograph.solve_same_start_stop_maximum('C','C',3,'Output #6:'))
    print(neograph.solve_start_stop_exact('A','C',4,'Output #7:'))
 
    print(neograph.solve_shortest_routev2('A','C','Output #8:'))
    print(neograph.solve_shortest_routev2('B','B','Output #9:'))

    print(neograph.solve_number_of_different_routes('C','C',30,'Output #10:'))
if __name__ == "__main__":
    main()