def read_proxies_from_file(file_path):
    with open(file_path, "r") as f:
        return [line.strip() for line in f.readlines()]


def write_proxies_to_file(file_path, proxies):
    with open(file_path, "w") as f:
        for proxy in proxies:
            f.write(f"{proxy}\n")
