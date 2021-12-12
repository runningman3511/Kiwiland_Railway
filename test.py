import unittest
from neograph import Neograph

class TestNeoGraphMethods(unittest.TestCase):

    neograph=None

    @classmethod
    def setUpClass(cls):
        cls.neograph=Neograph()
        input_graph = ['AB5', 'BC4', 'CD8', 'DC8', 'DE6', 'AD5', 'CE2', 'EB3', 'AE7']
        for input_data in input_graph:
            cls.neograph.add_edge(input_data[0],input_data[1], input_data[2])

    def test_task1(self):
        self.assertEqual(self.neograph.solve_distance("A-B-C"),9)

    def test_task2(self):
        self.assertEqual(self.neograph.solve_distance("A-D"),5)    

    def test_task3(self):
        self.assertEqual(self.neograph.solve_distance("A-D-C"),13)

    def test_task4(self):
        self.assertEqual(self.neograph.solve_distance("A-E-B-C-D"),22)

    def test_task5(self):
        self.assertEqual(self.neograph.solve_distance("A-E-D"),"NO SUCH ROUTE")

    def test_task6(self):
        self.assertEqual(self.neograph.solve_same_start_stop_maximum('C','C',3),2)

    def test_task7(self):
        self.assertEqual(self.neograph.solve_start_stop_exact('A','C',4),3)

    def test_task8(self):
        self.assertEqual(self.neograph.solve_shortest_routev2('A','C'),9)

    def test_task9(self):
        self.assertEqual(self.neograph.solve_shortest_routev2('B','B'),9)

    def test_task10(self):
        self.assertEqual(self.neograph.solve_number_of_different_routes('C','C',30),7)

if __name__ == '__main__':
    unittest.main()