# log_parser.py

import re
from datetime import datetime

class LogParser:
    """
    A class used to parse log files.

    Attributes:
    ----------
    log_file : str
        The path to the log file.
    log_entries : list
        A list of parsed log entries.

    Methods:
    -------
    parse_log_file()
        Parses the log file and stores the entries in log_entries.
    get_log_entries()
        Returns the list of parsed log entries.
    """

    def __init__(self, log_file):
        """
        Initializes the LogParser object.

        Parameters:
        ----------
        log_file : str
            The path to the log file.
        """
        self.log_file = log_file
        self.log_entries = []

    def parse_log_file(self):
        """
        Parses the log file and stores the entries in log_entries.
        """
        try:
            with open(self.log_file, 'r') as file:
                for line in file:
                    # Regular expression to match log entries
                    match = re.match(r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (.*)', line)
                    if match:
                        # Extract timestamp and log message
                        timestamp = datetime.strptime(match.group(1), '%Y-%m-%d %H:%M:%S')
                        log_message = match.group(2)
                        # Store the log entry
                        self.log_entries.append({'timestamp': timestamp, 'message': log_message})
        except FileNotFoundError:
            print(f"Error: The log file '{self.log_file}' was not found.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def get_log_entries(self):
        """
        Returns the list of parsed log entries.

        Returns:
        -------
        list
            A list of dictionaries containing the timestamp and log message.
        """
        return self.log_entries


# main.py

import log_parser

def main():
    """
    The main function.
    """
    log_file = 'log.txt'
    parser = log_parser.LogParser(log_file)
    parser.parse_log_file()
    log_entries = parser.get_log_entries()
    for entry in log_entries:
        print(f"Timestamp: {entry['timestamp']}, Message: {entry['message']}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nExiting program.")
    except Exception as e:
        print(f"An error occurred: {e}")