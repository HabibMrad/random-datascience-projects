# Imports
import numpy as np
import pandas as pd


def plot_pca_importances(pca):
    '''
    Compute and plot the ratio of explained variance per component of a PCA decomposition.

    Args:


    '''

    # Get the explained by each principal component
    var_explained = pca.explained_variance_ratio_
    var_explained_cum = np.cumsum(var_explained)

    # Plot the importances
    sns.barplot(x = np.arange(var_explained.shape[0]), y = var_explained, color = 'deepskyblue')

    # Plot the cummulative variance explained
    sns.lineplot(x = np.arange(var_explained.shape[0]), y = var_explained_cum, color = 'black')

    # Add a line for comparison
    plt.axhline(y = 1.0, linestyle = '--',color = 'black')
    
    # Formatting
    plt.title('Ratio of explained variance per principal component', fontsize = 16, fontweight = 'bold')
    plt.xlabel('Number of component', fontsize = 12)
    plt.ylabel('Ratio of explained variance', fontsize = 12)