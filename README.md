# Video2Text

Video2Text (https://video2text.de) allows you to easily convert a youtube video to text. This process is also called transcription.
It is completely free to use and runs locally on your pc.

## Table of Contents

- [Overview](#overview)
- [Getting Started](#getting-started)
- [Installation](#installation)
- [Help](#help)
- [Credits](#credits)
- [Acknowledgments](#acknowledgments)
- [License](#license)

# Getting Started
--------------------------------------

```$ apt-get install ffmpeg```
or
```$ brew install ffmpeg```

## Installation

1. Clone the repo with
  ```bash
  git clone https://github.com/XamHans/video-2-text.git`
  ```
2. Run
  ```bash
  cd into webserver
  ```
3. Run
  ```bash
  pip3 install -r requirements.txt
  ```
4. To run app
  ```bash
  streamlit run app.py
  ```
## Help

If you should have any troubles try to re-install pytube.
```
pip uninstall pytube
pip uninstall pytube3
pip install pytube
```
if you should run into an error where streamlit is not recognized by your terminal, try this command in your terminal: export PATH="$HOME/.local/bin:$PATH"

If you still have problems, create a new issue.

## Credits

Johannes Hayer
https://jhayer.tech

## License

This project is licensed under the MIT license

## Acknowledgments

OpenAI Whisper\* [here](https://github.com/openai/whisper)
