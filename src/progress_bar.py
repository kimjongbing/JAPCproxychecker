import colorama
from tqdm import tqdm

colorama.init()


class ProgressBar:
    def __init__(self, total):
        self.bars = {
            "Checked": tqdm(total=total, colour="cyan", position=0, desc="Checked"),
            "Succeeded": tqdm(total=total, colour="green", position=1, desc="Succeeded", bar_format="{desc}: {percentage:3.0f}%|{bar}| {n_fmt}/{total_fmt} [{rate_fmt}]"),
            "Failed": tqdm(total=total, colour="red", position=2, desc="Failed", bar_format="{desc}: {percentage:3.0f}%|{bar}| {n_fmt}/{total_fmt} [{rate_fmt}]"),
        }

    def update(self, key):
        self.bars[key].update()

    def close(self):
        for bar in self.bars.values():
            bar.close()
