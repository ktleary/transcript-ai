import subprocess
import textwrap

def invoke_llama(input_file, output_file):
    command = '/Users/kleary/dev/explore/llama.cpp/main'
    arguments = [
        '-t', '4',
        '-m', '/Users/kleary/models/Wizard-Vicuna-7B-Uncensored.ggmlv3.q4_1.bin',
        '--temp', '0.3',
        '--ctx-size', '2048',  # Set context window size back to 2048
        '-p'
    ]

    with open(input_file, 'r') as file:
        input_data = file.read().strip()  # Remove trailing newlines

    chunks = textwrap.wrap(input_data, 2048)  # Break into chunks of up to 2048 tokens

    with open(output_file, 'w') as output_file:
        for chunk in chunks:
            prompt = f"### Instruction: Convert the following unformatted text into well-structured sentences. \n### Unformatted Text: {chunk}"
            process = subprocess.Popen([command] + arguments + [prompt], stdout=subprocess.PIPE)
            output, error = process.communicate()

            output_file.write(output.decode())

def main():
    input_file = 'raw_transcript.txt'
    output_file = 'clean_transcript.txt'
    invoke_llama(input_file, output_file)

if __name__ == "__main__":
    main()

