#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np
import pickle

sizes = (2, 3)                             # Cube sizes.
weights = tuple(n / 10 for n in range(7))  # BWAS weights.

# Solution attributes and their graph properties.
attrs = {
    'len': {'title': 'Length', 'color': 'blue', 'scale': 'linear'},
    'time': {'title': 'Time (s)', 'color': 'green', 'scale': 'log'},
    'nodes': {'title': 'Nodes generated', 'color': 'purple', 'scale': 'log'}
}


def load_stats(size):
    """Return solution statistics for Rubik's cube of given size."""
    stats = {attr: {'means': [], 'stds': []} for attr in attrs}
    for weight in weights:
        picklename = f'results/cube{size}weight{weight}/results.pkl'
        with open(picklename, 'rb') as picklefile:
            pickledata = pickle.load(picklefile)
        lens = tuple(map(len, pickledata['solutions']))
        times = pickledata['times']
        nodes = pickledata['num_nodes_generated']
        for attr, vals in zip(attrs, (lens, times, nodes)):
            stats[attr]['means'].append(np.mean(vals))
            stats[attr]['stds'].append(np.std(vals))
    return stats


def main():
    """Plot graphs."""
    # Set up matplotlib.
    plt.rcParams.update({'figure.constrained_layout.use': True,
                         'font.size': 18,
                         'text.usetex': True})

    fig, axs = plt.subplots(len(sizes), len(attrs), sharex=True)
    for row, size in zip(axs, sizes):
        stats = load_stats(size)
        for ax, (attr, val) in zip(row, attrs.items()):
            spec = ax.get_subplotspec()
            if spec.is_first_row():
                ax.set_title(val['title'])
            if spec.is_first_col():
                ax.set(ylabel=f'Size {size}')
            color = val['color']
            means = stats[attr]['means']
            stds = stats[attr]['stds']
            ax.plot(weights, means, c=color)
            ax.fill_between(weights, np.subtract(means, stds),
                            np.add(means, stds), alpha=0.1, color=color)
            ax.set_yscale(val['scale'])
            if attr == 'time':
                ax.set_ylim(bottom=1)
    fig.supxlabel('Weight')
    plt.show()
    plt.close()


if __name__ == '__main__':
    main()
