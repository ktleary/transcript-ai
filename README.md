# Readable YouTube Transcript Formatter

This project utilizes Python's YouTubeTranscriptApi to fetch transcripts for YouTube videos and then processes them with a Local Language Model (LLM) to format the text into well-structured and readable sentences.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.x installed on your system.
- Access to a Local Language Model executable and model binary file.
- The `YouTubeTranscriptApi` Python package installed.

## Installation

Clone the repository to your local machine:

```bash
git clone https://your-repository-url.git
cd your-repository-directory


```

## Installation

Clone the repository to your local machine:

```bash
git clone https://your-repository-url.git
cd your-repository-directory
```

Install the required Python packages:

```bash
pip install -r requirements.txt
```

## Usage

The script can be run with the following command:

```bash
python3 transcript_formatter.py
```

Make sure to update the paths in the invoke_llama function to point to your Local Language Model executable and model binary file.

## Configuration

The invoke_llama function takes two arguments:

input_file: The path to the file containing the raw transcript text.
output_file: The path where the formatted transcript text will be saved.
These files are currently set to 'raw_transcript.txt' and 'clean_transcript.txt', respectively, and can be changed as per your requirements.

## Contributing

Contributions to this project are welcome. To contribute:

- Fork the project.
- Create a new branch (git checkout -b feature/YourFeature).
- Make your changes.
- Commit your changes (git commit -am 'Add some feature').
- Push to the branch (git push origin feature/YourFeature).
- Open a pull request.

## License

GPL-3.0

## Contact

If you want to contact me you can reach me at ktleary@gmail.com.

## Acknowledgements

Thank you to the authors of the YouTubeTranscriptApi and the Local Language Model for making their tools available for public use.
