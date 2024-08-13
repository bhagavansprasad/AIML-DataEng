def save_to_file(data, filename):
    """
    Saves a list of data to a text file, one item per line.
    """
    try:
        with open(filename, 'w') as file:
            for item in data:
                file.write(f"{item}\n")
        print(f"Data successfully saved to {filename}.")
    except IOError as e:
        print(f"An error occurred while saving to file: {e}")
