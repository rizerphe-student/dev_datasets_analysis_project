"""Download the results of the stackoverflow developer survey."""
import zipfile

import requests


def download_file(url, filename):
    """Download a file from a url."""
    response = requests.get(url, stream=True)
    total_size_in_bytes = int(response.headers.get("content-length", 0))
    total_downloaded = 0
    with open(filename, "wb") as handle:
        for data in response.iter_content(chunk_size=4096):
            handle.write(data)
            total_downloaded += len(data)
            print(
                f"Downloaded {total_downloaded} of {total_size_in_bytes} bytes ({total_downloaded / total_size_in_bytes * 100}%)",
                end="\r",
            )


def unzip_file(filename, directory):
    """Unzip a file."""
    with zipfile.ZipFile(filename, "r") as zip_ref:
        zip_ref.extractall(directory)


def main():
    datasets = [
        {
            "url": "https://info.stackoverflowsolutions.com/rs/719-EMH-566/images/stack-overflow-developer-survey-2022.zip",
            "filename": "stack-overflow-developer-survey-2022.zip",
            "directory": "stack-overflow-developer-survey-2022",
        },
        {
            "url": "https://info.stackoverflowsolutions.com/rs/719-EMH-566/images/stack-overflow-developer-survey-2021.zip",
            "filename": "stack-overflow-developer-survey-2021.zip",
            "directory": "stack-overflow-developer-survey-2021",
        },
    ]
    for dataset in datasets:
        print(f"Downloading {dataset['url']}")
        download_file(dataset["url"], dataset["filename"])
        print(f"Unzipping {dataset['filename']}")
        unzip_file(dataset["filename"], dataset["directory"])


if __name__ == "__main__":
    main()
