import unittest
import calc


class TestAddNum(unittest.TestCase):
  
  def test_add(self):
    self.assertEqual(calc.add(10,5),15)
    
    
    
if _name_ == '_main_':
  unittest.main()
