import subprocess

def run_padel(input_file, output_file, padel_jar_path):
    command = [
        'java', '-jar', padel_jar_path,
        '-dir', input_file,  # Directory of input SMILES file
        '-file', output_file,  # Output CSV file
        '-2d'  # 2D descriptors
    ]

    try:
        subprocess.run(command, check=True)
        print("PaDEL-Descriptor calculation completed successfully.")
    except subprocess.CalledProcessError as e:
        print("Error during PaDEL-Descriptor calculation:", e)
