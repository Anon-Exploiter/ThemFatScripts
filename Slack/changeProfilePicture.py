import requests
import os
import json

SLACK_TOKEN = "xoxc-"
HEADERS = {
    "accept": "*/*",
    "accept-language": "en-US,en;q=0.9",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Linux"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "cookie": "d=;",
}


def listDirectory(path):
    images = os.listdir(path)
    _images = []

    for imageNames in images:
        extension = imageNames.split(".")[::-1][0]

        if (
            extension == "png"
            or extension == "jpg"
            or extension == "gif"
            or extension == "svg"
            or extension == "jpeg"
        ):
            _images.append(path + imageNames)

    return _images


def changeProfilePicture(pictures):
    for picture in pictures:
        request = requests.post(
            f"https://slack.com/api/users.preparePhoto",
            headers=HEADERS,
            files={"image": open(picture, "rb")},
            data={"token": SLACK_TOKEN},
        )

        response = json.loads(request.text)
        print(response)

        if response["ok"] == True:
            image_id = response["id"]

            set_pfp = requests.post(
                f"https://slack.com/api/users.setPhoto",
                headers=HEADERS,
                data={"id": image_id, "token": SLACK_TOKEN},
            )

            print(set_pfp.text)


def main():
    currentDirectory = "/home/user/scripts/pepe-images/"
    filesInDirectory = listDirectory(currentDirectory)

    while True:
        changeProfilePicture(filesInDirectory)


if __name__ == "__main__":
    main()
