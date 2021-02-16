import unittest
from Triangle import classifyTriangle
class test_list_copy(unittest.TestCase):
    def test_Equilateral_Triangle(self):
        self.assertEqual(classifyTriangle(1,1,1), 'Equilateral','1,1,1 should be equilateral')

    def test_Isoceles_TriangleA(self):
        self.assertEqual(classifyTriangle(1,2,2), 'Isoceles','1,2,2 is a Isoceles triangle')

    def test_Isoceles_TriangleB(self):    
        self.assertEqual(classifyTriangle(2,1,2), 'Isoceles','2,1,2 is a Isoceles triangle')

    def test_Isoceles_TriangleC(self):
        self.assertEqual(classifyTriangle(2,2,1), 'Isoceles','2,2,1 is a Isoceles triangle')
        
    def test_Right_TriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5), 'Right','3,4,5 is a Right triangle')
    
    def test_Right_TriangleB(self): 
        self.assertEqual(classifyTriangle(4,3,5), 'Right','4,3,5 is a Right triangle')
    
    def test_Right_TriangleC(self):
        self.assertEqual(classifyTriangle(13,5,12), 'Right','13,5,12 is a Right triangle')

    def test_Scalene_Triangle(self):
        self.assertEqual(classifyTriangle(4,2,3), 'Scalene','4,2,3 is a Scalene triangle')
    
    def test_Not_Triangle(self):
        self.assertEqual(classifyTriangle(1,1,2), 'NotATriangle','1,1,2 is not a Scalene triangle')
        
    def test_Invalid_InputA(self):
        self.assertEqual(classifyTriangle(100,210,150), 'InvalidInput')

    def test_Invalid_InputB(self):
        self.assertEqual(classifyTriangle(2.2,2.1,3), 'InvalidInput')

    def test_Invalid_InputC(self):
        self.assertEqual(classifyTriangle(-1,1,0), 'InvalidInput')

if __name__ =='__main__':
    print('Running unit tests')
    unittest.main(exit=False, verbosity=2)