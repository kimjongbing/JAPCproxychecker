from src import (
    parse_args,
    handle_config,
    handle_file_paths,
    write_proxies_to_file,
    handle_proxies,
)


def main(input_file_path, output_file_path, json_file_path):
    default_input_directory, default_output_directory, proxies = handle_config(
        json_file_path
    )
    full_input_path, full_output_path = handle_file_paths(
        input_file_path,
        output_file_path,
        default_input_directory,
        default_output_directory,
    )
    good_proxies = handle_proxies(full_input_path, proxies)

    if output_file_path:
        write_proxies_to_file(full_output_path, good_proxies)
    else:
        write_proxies_to_file(full_input_path, good_proxies)


if __name__ == "__main__":
    args = parse_args()
    main(args.input_file_path, args.output_file_path, args.json_file_path)
