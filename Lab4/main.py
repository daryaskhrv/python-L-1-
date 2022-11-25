import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import cv2


def add_number_class (df: pd.DataFrame) -> None:
    """Adding a column with numeric labels"""
    i=0
    labels_number = []
    while i < len (df):
        labels_number.append(int(df['label'].iloc[i] == 'bay horse'))
        i+=1
    df["numerical_class"] = labels_number


def filter_labels(df: pd.DataFrame, label: str) -> pd.DataFrame:
    """Create a new indexed dataframe by label"""
    tmp = df[df.label == label]
    tmp.reset_index(drop=True, inplace=True)
    return tmp


def filter_options(df: pd.DataFrame, label: str, max_height: int, max_width: int) -> pd.DataFrame:
    """Create a new indexed dataframe by label and maximum sizes"""
    tmp = df[((df.label == label) & (df.width <= max_width) & (df.height <= max_height))]
    tmp.reset_index(drop=True, inplace=True)
    return tmp


def add_columns_size(df: pd.DataFrame)-> None:
    """Add image information to the DataFrame"""
    width=[]
    height=[]
    channels=[]
    for image_path in df['absolute_path']:
        image = cv2.imread(image_path)
        img_height, img_width, img_channels = image.shape
        width.append(img_width)
        height.append(img_height)
        channels.append(img_channels)
    df["width"] = width
    df["height"] = height
    df["channels"] = channels


def group_df(df: pd.DataFrame)-> tuple:
    """Calculating the number of pixels and grouping DataFrame"""
    df['pixels'] = df['width'] * df['height']
    return df.groupby('label').max(), df.groupby('label').min(), df.groupby('label').mean()


def histogram_build(df: pd.DataFrame, label: str) -> list:
    """Build a histogram from a random image"""
    tmp = filter_labels(df, label)
    image_path = np.random.choice(tmp.absolute_path.to_numpy())
    image = cv2.imread(image_path)
    hist = []
    for i in range(3):
        hist.append(cv2.calcHist([image],[i],None,[256],[0,256]))
    return hist


def draw_histogram(df: pd.DataFrame, label: str) -> None:
    """Histogram display"""
    hist = histogram_build(df, label)
    colors = ['b', 'g', 'r']
    for i in range(3):
        plt.plot(hist[i], color=colors[i])
    plt.title('Image Histogram')
    plt.xlabel('Intensity color')
    plt.ylabel('Density pixel')
    plt.xlim([0, 256])
    plt.show()


if __name__ == "__main__":
    df = pd.read_csv("Lab4/data.csv", usecols = ['Абсолютный путь','Метка'])
    df = df.rename(columns={'Абсолютный путь': 'absolute_path', 'Метка': 'label'}) 
    add_number_class(df)
    add_columns_size(df)
    df.to_csv('result.csv')
    filtered_df = filter_options(df, 'zebra', 350, 350)
    print(filtered_df)
    draw_histogram(df, "zebra")  