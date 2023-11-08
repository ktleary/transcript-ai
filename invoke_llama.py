import subprocess

def invoke_llama(input_file, output_file):
    command = '/Users/kleary/dev/explore/llama.cpp/main -t 4 -m /Users/kleary/models/Wizard-Vicuna-7B-Uncensored.ggmlv3.q4_1.bin --temp 0.3 -p'

    with open(input_file, 'r') as file:
        input_data = file.read().strip()  # Remove trailing newlines

    prompt = f'"### Instruction: Convert the following unformatted text into well-structured sentences. \\n Unformatted Text: {input_data}"'

    command = f"{command} {prompt}"

    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()

    with open(output_file, 'w') as file:
        file.write(output.decode())

def main():
    input_file = 'raw_transcript.txt'
    output_file = 'clean_transcript.txt'
    invoke_llama(input_file, output_file)

if __name__ == "__main__":
    main()

