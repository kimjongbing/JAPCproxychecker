from tqdm import tqdm


class ProgressBar:
    def __init__(self, total):
        self.pbar = tqdm(total=total, bar_format="{l_bar}{bar}| {postfix}")

    def update(self, counter):
        self.pbar.set_postfix(counter.values(), refresh=True)
        self.pbar.update(1)

    def close(self):
        self.pbar.close()
