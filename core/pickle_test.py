import pickle
import unittest


class Model:
    def __init__(self):
        self.artifacts = {'key1': 'value1'}

    def predict(self):
        print('predict: ', self.artifacts)


class MyTestCase(unittest.TestCase):
    def test_save_and_load(self):
        model = Model()
        print('before save')
        model.predict()

        model_filename = '../temp/test-model.pkl'
        with open(model_filename, 'wb') as model_file:
            pickle.dump(model, model_file)
        print('saved')

        with open(model_filename, 'rb') as model_file:
            model_loaded = pickle.load(model_file)

        print('loaded')
        model_loaded.predict()
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
