from EmotionDetection.emotion_detection import emotion_detector
import unittest # Library for unit testing

"""
This file contains unit tests for the emotion detection functionality.
"""
# Create class for unit testing
class TestEmotionDetector(unittest.TestCase):

    # Define unit test method 
    def test_emotion_detector(self):

        # Test case for dominated emotion 'joy'
        result_1 = emotion_detector('i am glad this happned')
        # Equal verify
        self.assertEqual(result_1['emotions'], 'joy')

        # Test case for dominated emotion 'anger'
        result_2 = emotion_detector('i am really mad about this')
        # Equal verify
        self.assertEqual(result_1['emotions'], 'anger')

        # Test case for dominated emotion 'disgust'
        result_3 = emotion_detector('i feel disgusted just hearing about this')
        # Equal verify
        self.assertEqual(result_1['emotions'], 'disgust')

        # Test case for dominated emotion 'sadness'
        result_4 = emotion_detector('i am so sad about this')
        # Equal verify
        self.assertEqual(result_1['emotions'], 'sadness')

        # Test case for dominated emotion 'fear'
        result_5 = emotion_detector('i am really afraid that this will happen')
        # Equal verify
        self.assertEqual(result_1['emotions'], 'fear')

unittest.main()