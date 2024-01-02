from project import get_start_time
from project import get_end_time
from project import get_duration
from project import get_csv_data
from project import update_csv
import time
import sys
import pytest
import csv

def test_get_start_time_empty_input(monkeypatch):
    # Simulate an empty input using monkeypatch.setattr
    monkeypatch.setattr('builtins.input', lambda _: '')

    result = get_start_time("")

    assert isinstance(result, (int, float))

def test_get_start_time_retry_with_empty_input(monkeypatch):
    # Simulate an invalid input followed by an empty input
    inputs = iter(['invalid', ''])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    result = get_start_time("")

    assert isinstance(result, (int, float))

def test_get_start_time_exception_handling(monkeypatch):
    # Simulate an exception during user input
    monkeypatch.setattr('builtins.input', lambda _: KeyboardInterrupt)  # Raises an exception

    try:
        get_start_time("")
    except SystemExit:
        print("SystemExit was raised as expected.")
    else:
        print("SystemExit was not raised.")


#testing get_end_time()

def test_get_end_time_empty_input(monkeypatch):
    # Simulate an empty input using monkeypatch.setattr
    monkeypatch.setattr('builtins.input', lambda _: '')

    result = get_end_time("")

    assert isinstance(result, (int, float))

def test_get_end_time_retry_with_empty_input(monkeypatch):
    # Simulate an invalid input followed by an empty input
    inputs = iter(['invalid', ''])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    result = get_end_time("")

    assert isinstance(result, (int, float))

def test_get_end_time_exception_handling(monkeypatch):
    # Simulate an exception during user input
    monkeypatch.setattr('builtins.input', lambda _: KeyboardInterrupt)  # Raises an exception

    try:
        get_end_time("")
    except SystemExit:
        print("SystemExit was raised as expected.")
    else:
        print("SystemExit was not raised.")


def test_get_duration():
    # Example start_time and end_time values
    start_time = 10  # Replace with the actual start time
    end_time = 30    # Replace with the actual end time

    # Call the function with the provided values
    result = get_duration(start_time, end_time)

    # Assert that the result is as expected
    expected_duration = end_time - start_time
    assert result == expected_duration

# Replace 'your_module' with the actual module name

CSV_FILE_PATH = '/workspaces/87431606/project/project.csv'

@pytest.mark.parametrize("csv_data, expected_result", [
    # Define test cases with input CSV data and expected output
    ([{'field1': 'value1', 'field2': 'value2'}, {'field1': 'value3', 'field2': 'value4'}],
     [{'field1': 'value1', 'field2': 'value2'}, {'field1': 'value3', 'field2': 'value4'}]),
    # Add more test cases as needed
])

@pytest.fixture
def csv_file(tmp_path):
    # Create a temporary CSV file with some data
    csv_file_path = tmp_path / "test.csv"
    with open(csv_file_path, "w", newline='') as csvfile:
        fieldnames = ["task", "number_of_times_timed", "total_time", "average_time"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow({"task": "task1", "number_of_times_timed": 1, "total_time": 10, "average_time": 10.0})

    return csv_file_path



def test_get_csv_data(csv_file):
    # Use the temporary CSV file for testing
    data = get_csv_data(csv_file)


    assert len(data) == 1
    assert data[0]["task"] == "task1"


def test_update_csv_existing_task():
    # Mock data with an existing task
    data = [
        {'task': 'existing_task', 'number_of_times_timed': 1, 'total_time': 5, 'average_time': 5},

    ]

    pathway = '/workspaces/87431606/project/project.csv'
    task_input = 'existing_task'
    duration = 10

    # Call the function
    result = update_csv(task_input, duration, data, pathway)

    # Assert that the result is as expected
    assert result == 7.5



def test_update_csv_new_task():
    # Mock data without the task
    data = [
        {'task': 'other_task', 'number_of_times_timed': 2, 'total_time': 15, 'average_time': 7.5},
    ]

    pathway = '/workspaces/87431606/project/project.csv'
    task_input = 'new_task'
    duration = 5

    # Call the function
    result = update_csv(task_input, duration, data, pathway)

    # Assert that the result is as expected
    assert result == 5