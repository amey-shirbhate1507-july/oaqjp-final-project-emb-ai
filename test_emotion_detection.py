import unittest
from emotion_detection import emotion_detector

class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detector(self):
        result_1 = emotion_detector('I am really mad about this')
        self.assertIn('anger', str(result_1).lower())

if __name__ == '__main__':
    unittest.main()
