import unittest
import pandas as pd
from weather_prediction_lm import clean_format_data_frame, create_train_set, create_test_set

class TestCleanFormatDataFrame(unittest.TestCase):

    def setUp(self):
        # Create a sample weather data frame for testing
        self.weather_data = pd.DataFrame({
            'STATION': ['station1', 'station2', 'station3'],
            'NAME': ['name1', 'name2', 'name3'],
            'DATE': ['2024-01-01', '2024-01-02', '2024-01-03'],
            'PRCP': [0.5, None, 0.8],
            'PRCP_ATTRIBUTES': ['A', 'B', 'C'],
            'TMAX': [20, 25, None],
            'TMAX_ATTRIBUTES': ['D', 'E', 'F'],
            'TMIN': [10, None, 15],
            'TMIN_ATTRIBUTES': ['G', 'H', 'I'],
            'SNWD': [None, None, None],
            'SNWD_ATTRIBUTES': [None, None, None]
        })

    def test_clean_format_data_frame(self):
        # Call the function with sample weather data frame
        cleaned_data = clean_format_data_frame(self.weather_data)

        # Check if the columns irrelevant to the machine learning model are deleted
        self.assertNotIn('STATION', cleaned_data.columns)
        self.assertNotIn('NAME', cleaned_data.columns)
        self.assertNotIn('PRCP_ATTRIBUTES', cleaned_data.columns)
        self.assertNotIn('SNWD', cleaned_data.columns)
        self.assertNotIn('SNWD_ATTRIBUTES', cleaned_data.columns)
        self.assertNotIn('TMAX_ATTRIBUTES', cleaned_data.columns)
        self.assertNotIn('TMIN_ATTRIBUTES', cleaned_data.columns)

        # Check if the string formatted dates are converted to datetime objects
        self.assertIsInstance(cleaned_data['DATE'][0], pd.Timestamp)

        # Check if null values are filled with previous values
        self.assertEqual(cleaned_data['PRCP'][1], 0.5)
        self.assertEqual(cleaned_data['TMAX'][2], 25)
        self.assertEqual(cleaned_data['TMIN'][1], 10)

        # Check if the column labels are relabeled correctly
        self.assertEqual(cleaned_data.columns.tolist(), ['DATE', 'precip', 'max_temp', 'min_temp'])


class TestCreateTrainAndTestSets(unittest.TestCase):

    def setUp(self):
        # Create a sample weather data frame for testing
        self.weather_data = pd.DataFrame({
            'DATE': pd.date_range(start='2022-01-01', end='2024-01-01'),
            'precip': [0.5, 0.6, 0.7] + [None] * 731,
            'max_temp': [20, 25, 30] + [None] * 731,
            'min_temp': [10, 15, 20] + [None] * 731
        })

    def test_create_train_set(self):
        # Call the function with sample weather data frame
        training_data = create_train_set(self.weather_data)

        # Check if the training data contains only data up to 2 years behind the most recent date
        most_recent_date = self.weather_data['DATE'].max()
        two_years_ago = most_recent_date - pd.DateOffset(years=2)
        expected_training_data = self.weather_data.loc[self.weather_data['DATE'] <= two_years_ago]
        self.assertTrue(training_data.equals(expected_training_data))

    def test_create_test_set(self):
        # Call the function with sample weather data frame
        test_data = create_test_set(self.weather_data)

        # Check if the test data contains data from 1 year behind the most recent date to the present
        most_recent_date = self.weather_data['DATE'].max()
        one_year_ago = most_recent_date - pd.DateOffset(years=1)
        expected_test_data = self.weather_data.loc[one_year_ago <= self.weather_data['DATE']]
        self.assertTrue(test_data.equals(expected_test_data))

if __name__ == '__main__':
    unittest.main()