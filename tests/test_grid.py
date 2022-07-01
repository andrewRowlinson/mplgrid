""" Tests for mplgrid."""

from mplgrid import grid, grid_dimensions
import numpy as np
import matplotlib.pyplot as plt


def test_figsize():
    """ Test that the right figure size is created."""
    for i in range(100):
        ax_aspect = np.random.uniform(0.3, 2)
        nrows = np.random.randint(1, 6)
        ncols = np.random.randint(1, 6)
        figwidth = np.random.uniform(0.5, 10)
        figheight = np.random.uniform(0.5, 10)
        max_grid = np.random.uniform(0.5, 1)
        space = np.random.uniform(0, 0.2)

        grid_width, grid_height = grid_dimensions(ax_aspect=ax_aspect,
                                                  figwidth=figwidth,
                                                  figheight=figheight,
                                                  nrows=nrows,
                                                  ncols=ncols,
                                                  max_grid=max_grid,
                                                  space=space)
        assert np.isclose(grid_height - max_grid, 0) or np.isclose(grid_width - max_grid, 0)

        fig, ax = grid(ax_aspect=ax_aspect,
                       figheight=figheight,
                       nrows=nrows,
                       ncols=ncols,
                       grid_height=grid_height,
                       grid_width=grid_width,
                       space=space,
                       endnote_height=0,
                       title_height=0)
        check_figwidth, check_figheight = fig.get_size_inches()

        assert np.isclose(check_figwidth - figwidth, 0)
        assert np.isclose(check_figheight - figheight, 0)
        plt.close(fig)


def test_return_shape():
    """ Test that the return shape is the same as plt.subplots."""
    for nrows in range(1, 4):
        for ncols in range(1, 4):
            fig1, ax1 = plt.subplots(nrows=nrows, ncols=ncols)
            fig2, ax2 = grid(nrows=nrows, ncols=ncols)
            if nrows > 1 or ncols > 1:
                assert ax1.shape == ax2.shape
            plt.close(fig1)
            plt.close(fig2)
