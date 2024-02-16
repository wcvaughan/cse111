import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_squared_error, mean_absolute_error
import matplotlib.pyplot as plt
import joblib


def main(weather_data_path, alpha_value=0.1):

    # Define the variables we are predicting
    predictors = ["precip", "max_temp", "min_temp"]
    model_file = 'ridge_model.joblib'

    try:
        # Try loading the existing model
        reg = joblib.load(model_file)
    
    except FileNotFoundError:
        # If the model doesn't exist, train and save the model
        reg = Ridge(alpha=alpha_value)

        
        formatted_weather_data = clean_format_data_frame(weather_data_path)

        formatted_weather_data = create_target_predictor(formatted_weather_data)

        formatted_weather_data.dropna(inplace=True)

        training_data = create_train_set(formatted_weather_data)

        testing_data = create_test_set(formatted_weather_data)

        # Fit the model
        try:
            reg.fit(training_data[predictors], training_data[["target_max", "target_min"]])
            print("Model successfully fitted.")
            # Save the trained model to a file
            joblib.dump(reg, 'ridge_model.joblib')
        except Exception as e:
            print(f"Error occurred during model fitting: {e}")

    # Check if the model has the 'coef_' attribute (indicating it has been fitted)
    if hasattr(reg, 'coef_'):
        predictions = predict(reg, testing_data, predictors)
        mean_abs_err_max, mean_sqr_err_max, mean_abs_err_min, mean_sqr_err_min = test_prediction_accuracy(testing_data, predictions)
        print(f"Mean Absolute Error Max: {mean_abs_err_max}")
        print(f"Mean Squared Error Max: {mean_sqr_err_max}")
        print(f"Mean Absolute Error Min: {mean_abs_err_min}")
        print(f"Mean Squared Error Min: {mean_sqr_err_min}")
        compared_prediction = combine_prediction_actuals(testing_data, predictions)
        plot_comparison(compared_prediction) 
    else:
        print("Model not fitted successfully.")
    return

def clean_format_data_frame(weather_data):

    # Read the file provided and store as a dataframe using Pandas module
    weather_data = pd.read_csv(weather_data)

    # Assuming the file was a csv file downloaded from NOAA it came with standard columns and labels.
    # Delete columns irrelevant to the machine learning model
    relevant_columns = ["DATE", "PRCP", "TMAX", "TMIN"]
    columns_to_delete = [col for col in weather_data.columns if col not in relevant_columns]
    weather_data.drop(columns=columns_to_delete, inplace=True)


    # Convert string formatted dates to datetime objects
    weather_data['DATE'] = pd.to_datetime(weather_data["DATE"])
    

    # Where null values exist, forward fill with previous value.
    try:
        weather_data.fillna(method='ffill', inplace=True)
    except Exception as e:
        print(f"Error occurred during data processing: {e}")

    # Relabel default column labels
    new_column_labels = {'PRCP': 'precip', 'TMAX': 'max_temp', 'TMIN': 'min_temp'}
    weather_data.rename(columns=new_column_labels, inplace=True)

    # Save formatted and cleaned dataframe to a new csv file with added description as "modified"
    try:
        weather_data.to_csv('modified_weatherpalmerairport.csv', index=False)
    except Exception as e:
        print(f"Error occurred while saving the file: {e}")

    return weather_data

def create_target_predictor(weather_data):
    try:
        # Removes the most recent data entry
        weather_data["target_max"] = weather_data.shift(-1)["max_temp"]
        weather_data["target_min"] = weather_data.shift(-1)["min_temp"]
        # Formats data to everything up to the new last data point
        weather_data = weather_data.iloc[:-1,:]
    except Exception as e:
        print(f"Error occurred during data manipulation: {e}")

    return weather_data

def create_train_set(weather_data):

    most_recent_date = weather_data["DATE"].max()

    two_years_ago = most_recent_date - pd.DateOffset(years=2)

    # Limits set on training data to all data up to 2 years behind most recent data entry
    training_data = weather_data.loc[weather_data["DATE"] <= two_years_ago]

    return training_data.dropna(subset=["target_max", "target_min"])

def create_test_set(weather_data):

    most_recent_date = weather_data["DATE"].max()

    one_year_ago = most_recent_date - pd.DateOffset(years=1)

    # Limits set on testing data to all data from 1 year behind most recent data entry to present
    test_data = weather_data.loc[one_year_ago <= weather_data["DATE"]]

    return test_data

def predict(reg, test_data, predictors):

    # Using the test_data and the predictors defined, predict future values
    predictions = reg.predict(test_data[predictors])

    return predictions

def test_prediction_accuracy(test_data, predictions):

    # Test prediction accuracy by comparing with test data
    mean_abs_err_max = mean_absolute_error(test_data["target_max"], predictions[:,0])
    mean_sqr_err_max = mean_squared_error(test_data["target_max"], predictions[:,0])
    mean_abs_err_min = mean_absolute_error(test_data["target_min"], predictions[:,1])
    mean_sqr_err_min = mean_squared_error(test_data["target_min"], predictions[:,1])
    return mean_abs_err_max, mean_sqr_err_max, mean_abs_err_min, mean_sqr_err_min

def combine_prediction_actuals(test_data, predictions):

    # Organize results of predictions and actual values in test data for easier comparison
    combined_results = pd.concat([test_data["DATE"] ,test_data[["target_max", "target_min"]], pd.DataFrame(predictions, columns=["Predicted_Max", "Predicted_Min"])], axis=1)

    return combined_results

def plot_comparison(results):
    try:
        plt.figure(figsize=(10, 6))  # Adjust figure size
        plt.plot(results["DATE"], results["Actual"], label="Actual", linestyle='-', color='blue')  # Use "DATE" column as x-axis values
        plt.plot(results["DATE"], results["Predicted_Max"], label="Predicted Max", linestyle='--', color='green')
        plt.plot(results["DATE"], results["Predicted_Min"], label="Predicted Min", linestyle='--', color='orange')
        plt.xlabel("Date") # Label x-axis
        plt.ylabel("Temperature (°F)")  # Label y-axis
        plt.title("Actual vs. Predicted Temperatures")  # Add title
        plt.legend()  # Show legend
        plt.grid(True)  # Show gridlines
        plt.show()
    except Exception as e:
        print(f"Error occurred during plotting: {e}")
    return


if __name__ == "__main__":
    # Entry point of the program
    palmer_weather_data = "week06\weatherpalmerairport9724.csv"
    main(palmer_weather_data)