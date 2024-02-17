import subprocess

# Define the path to your requirements file
requirements_file = 'requirements.txt'

# Function to install packages from the requirements file
def install_packages():
    with open(requirements_file) as f:
        packages = f.readlines()
        for package in packages:
            package = package.strip()
            try:
                subprocess.run(['pip', 'install', package], check=True)
            except subprocess.CalledProcessError as e:
                print(f"Error installing package: {package}. Error: {e}")

if __name__ == '__main__':
    install_packages()
