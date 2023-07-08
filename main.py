from src.file_handler import FileHandler
from src.config_handler import ConfigHandler
from src.proxy_handler import handle_proxies
from src.argparser import parse_args


def main(input_file_path, output_file_path, json_file_path):
    (
        default_input_directory,
        default_output_directory,
        proxies,
    ) = ConfigHandler.handle_config(json_file_path)
    full_input_path, full_output_path = FileHandler.handle_file_paths(
        input_file_path,
        output_file_path,
        default_input_directory,
        default_output_directory,
    )
    good_proxies = handle_proxies(full_input_path, proxies)

    if output_file_path:
        FileHandler.write_to_file(full_output_path, good_proxies)
    else:
        FileHandler.write_to_file(full_input_path, good_proxies)


if __name__ == "__main__":
    args = parse_args()
    main(args.input_file_path, args.output_file_path, args.json_file_path)
