import numpy as np
import os
from typing import List
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from constants import *

def get_labels_paths(root_dir: str, sequence: str) -> List[str]:
    """
    Get the paths of label files in a list, given a root directory and a sequence.

    Args:
        root_dir (str): Root directory containing label files.
        sequence (str): Name of the sequence.

    Returns:
        List[str]: List of label file paths.
    """
    labels_paths = []
    for root, _, label_files in os.walk(os.path.join(root_dir, f"sequences/{sequence}/predictions")):
        for file in sorted(label_files):
            labels_paths.append(os.path.join(root, file))
    print(f"Total number of Predictions in given directory.: {len(labels_paths)}")
    return labels_paths

def load_label_file(labels_paths: List[str], limit_label_files: int) -> List[np.ndarray]:
    """
    Load label files from the given paths and limit the number of files to load.

    Args:
        labels_paths (List[str]): List of label file paths.
        limit_label_files (int): Number of label files to load.

    Returns:
        List[np.ndarray]: List of loaded label data arrays.
    """
    labels = []
    for label_path in labels_paths[:limit_label_files]:
        label = np.fromfile(label_path, dtype=np.int32)
        label = label.reshape((-1))
        labels.append(label)
    return labels

def create_df(labels: List[np.ndarray]) -> List[pd.DataFrame]:
    """
    Create DataFrames from the labels.

    Args:
        labels (List[np.ndarray]): List of label data arrays.

    Returns:
        List[pd.DataFrame]: List of DataFrames containing label data.
    """
    labels_df_list = []
    for label in labels:
        df = pd.DataFrame({'predictions': label})
        df['class'] = df['predictions'].map(labels_map)
        print(f"Total Unique Predictions: {sorted(df['predictions'].unique())}, and Length: {len(df['predictions'].unique())}")
        labels_df_list.append(df)
    return labels_df_list

def plot_df(df: pd.DataFrame, index:int, save_plot:bool=False):
    """
    Plot the DataFrame.

    Args:
        df (pd.DataFrame): DataFrame containing label data.
    """
    sns.set_theme(style="whitegrid")

    ax = sns.countplot(data=df, y='class')

    for patch, value in zip(ax.patches, df['predictions'].unique()):
        # color the bar, according to the given bgr value in the color map
        class_data = CLASS_INFO.get(value, {"label": str(value), "color": [0, 0, 0]})
        color_bgr = [c / 255 for c in class_data["color"]]  # normalize to [0, 1] range
        color_rgb = color_bgr[::-1]  # Convert BGR to RGB by reversing the order
        # put the total count on the top of the bar/patch
        ax.annotate(f'{patch.get_width()}', (patch.get_width(), patch.get_y() + patch.get_height() / 2.),
                    ha='left', va='center', xytext=(5, 0), fontsize=8, textcoords='offset points')
        patch.set_facecolor(color_rgb)
    ax.set_title(f"Predictions Distribution of Scan:{index}")
    ax.set_xlabel("Count")
    ax.set_ylabel("Classes")
    # bold the x, and y axis titles
    ax.xaxis.label.set_fontweight('bold')
    ax.yaxis.label.set_fontweight('bold')

    plt.tight_layout()
    if save_plot:
        plt.savefig(f"plot_{index}.png")
    plt.show()



def main():
    # Get lales paths as a list, from the given root directory, and sequence
    labels_paths = get_labels_paths(root_dir=ROOT_DIR, sequence=SEQUENCE)
    # load the lables
    labels = load_label_file(labels_paths, limit_label_files=LIMIT_LABEL_FILES)
    # create the dataframe from the loaded labels
    labels_df = create_df(labels=labels)
    # plot the df
    for idx, df in enumerate(labels_df):
        plot_df(df, index=idx, save_plot=SAVE_PLOT)

if __name__ == '__main__':
    main()
