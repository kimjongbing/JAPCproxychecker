import json, os


class FileHandler:
    @staticmethod
    def read_from_file(file_path):
        with open(file_path, "r") as f:
            return [line.strip() for line in f.readlines()]

    @staticmethod
    def write_to_file(file_path, content):
        with open(file_path, "w") as f:
            for item in content:
                f.write(f"{item}\n")

    @staticmethod
    def read_json_file(json_file_path):
        with open(json_file_path, "r") as json_file:
            return json.load(json_file)

    @staticmethod
    def get_proxy_sources_from_json(json_file_path):
        data = FileHandler.read_json_file(json_file_path)
        return data["sources"]

    @staticmethod
    def get_full_file_path(file_path, default_directory):
        return os.path.join(default_directory, file_path)

    @staticmethod
    def handle_file_paths(
        input_file_path,
        output_file_path,
        default_input_directory,
        default_output_directory,
    ):
        full_input_path = FileHandler.get_full_file_path(
            input_file_path, default_input_directory
        )
        full_output_path = FileHandler.get_full_file_path(
            output_file_path, default_output_directory
        )
        return full_input_path, full_output_path
