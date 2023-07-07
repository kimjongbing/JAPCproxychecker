from src import directory_handler

def read_proxies_from_file(file_path):
    with open(file_path, "r") as f:
        return [line.strip() for line in f.readlines()]


def write_proxies_to_file(file_path, proxies):
    with open(file_path, "w") as f:
        for proxy in proxies:
            f.write(f"{proxy}\n")


def handle_file_paths(input_file_path, output_file_path, default_input_directory, default_output_directory):
    full_input_path = directory_handler.get_full_file_path(input_file_path, default_input_directory)
    full_output_path = directory_handler.get_full_file_path(output_file_path, default_output_directory)

    return full_input_path, full_output_path
