import subprocess

# Array of input strings
inputs = ['27.7\n', '31.0\n', '32.7\n', '34.7\n', '35.9\n', '37.4\n', '38.2\n', '39.5\n', '40.3\n', '42.2\n', '41.3\n', '40.4\n', '39.8\n', '38.7\n', '36.5\n', '35.7\n','33.4\n' , 'STOP\n']

# Run the program using subprocess and feed it the inputs
process = subprocess.Popen(['python3', 'groundhog.py', '7'], stdin=subprocess.PIPE)
for input_str in inputs:
    process.stdin.write(input_str.encode())  # Feed the input
    process.stdin.flush()  # Flush the input buffer
    # output_bytes = process.stdout.read(1024)  # Read up to 1024 bytes of output
    # output_str = output_bytes.decode()
    # print(output_str.strip())  # Print the output
process.stdin.close()
