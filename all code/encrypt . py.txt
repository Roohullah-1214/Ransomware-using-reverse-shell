import os
import shutil
import pyzipper

# Ask the user for the source directory to zip
source_directory = input("Please enter the directory path you want to zip: ")

# Validate if the source directory exists
if not os.path.isdir(source_directory):
    print(f"The directory '{source_directory}' does not exist. Please provide a valid path.")
else:
    # Ask the user what files or directories to encrypt with a password
    files_or_dirs_to_encrypt_input = input("Please enter the files or directories (separated by commas) you want to encrypt (or 'all' to zip everything): ").strip()

    # Initialize variables
    target_folder = os.path.join(source_directory, "temp_zip_folder")
    files_to_skip = ["encrypt upgrade.py"]  # Initialize as needed

    # If user entered 'all', zip everything in the directory
    if files_or_dirs_to_encrypt_input.lower() == "all":
        if not os.path.exists(target_folder):
            os.mkdir(target_folder)

        # Move files and directories (except skipped ones) to the target folder
        for file_name in os.listdir(source_directory):
            file_path = os.path.join(source_directory, file_name)

            # Skip directories and specified files
            if file_name not in files_to_skip:
                target_path = os.path.join(target_folder, file_name)

                # If it's a file, move it to the target folder
                if os.path.isfile(file_path):
                    shutil.move(file_path, target_path)
                # If it's a directory, move the entire directory to the target folder
                elif os.path.isdir(file_path):
                    shutil.move(file_path, target_folder)

        # Define the name of the ZIP file (to be created in the source directory)
        zip_filename = os.path.join(source_directory, "Protected_Folder.zip")

        # Ask the user for the password to apply to the ZIP file
        password = input("Please enter the password to encrypt the ZIP file: ").encode()

        # Create a password-protected ZIP file
        with pyzipper.AESZipFile(zip_filename, 'w', compression=pyzipper.ZIP_DEFLATED, encryption=pyzipper.WZ_AES) as zip_file:
            zip_file.setpassword(password)

            # Function to recursively add files and directories to the ZIP file
            def add_to_zip(path):
                # If it's a file, add it directly
                if os.path.isfile(path):
                    zip_file.write(path, arcname=os.path.relpath(path, start=target_folder))
                    os.remove(path)  # Delete the file after zipping
                # If it's a directory, recursively add its contents
                elif os.path.isdir(path):
                    for root, dirs, files in os.walk(path):
                        for file in files:
                            file_path = os.path.join(root, file)
                            zip_file.write(file_path, arcname=os.path.relpath(file_path, start=target_folder))
                            os.remove(file_path)  # Delete the file after zipping
                    # After all files in the directory are processed, remove the empty directory
                    shutil.rmtree(path)  # Delete the directory after zipping

            # Walk through the target folder and add files to the zip
            for item in os.listdir(target_folder):
                item_path = os.path.join(target_folder, item)
                add_to_zip(item_path)

        # Clean up by removing the temporary folder
        shutil.rmtree(target_folder)

        print(f"All files have been zipped into a password-protected ZIP file: {zip_filename}")

    else:
        # Split the input into individual file/folder names and strip extra spaces
        files_or_dirs_to_encrypt = [item.strip() for item in files_or_dirs_to_encrypt_input.split(',')]

        # Use the source directory as the destination folder for the ZIP file
        destination_folder = source_directory

        # Define the name of the ZIP file (to be created in the source directory)
        zip_filename = os.path.join(destination_folder, "Protected_Folder.zip")

        # Ask the user for the password to apply to the selected files
        password = input("Please enter the password to encrypt the ZIP file: ").encode()

        # Create a password-protected ZIP file
        with pyzipper.AESZipFile(zip_filename, 'w', compression=pyzipper.ZIP_DEFLATED, encryption=pyzipper.WZ_AES) as zip_file:
            zip_file.setpassword(password)

            # Function to recursively add files and directories to the ZIP file
            def add_to_zip(path):
                # If it's a file, add it directly
                if os.path.isfile(path):
                    zip_file.write(path, arcname=os.path.relpath(path, start=source_directory))
                    os.remove(path)  # Delete the file after zipping
                # If it's a directory, recursively add its contents
                elif os.path.isdir(path):
                    for root, dirs, files in os.walk(path):
                        for file in files:
                            file_path = os.path.join(root, file)
                            zip_file.write(file_path, arcname=os.path.relpath(file_path, start=source_directory))
                            os.remove(file_path)  # Delete the file after zipping
                    # After all files in the directory are processed, remove the empty directory
                    shutil.rmtree(path)  # Delete the directory after zipping

            # Walk through the source directory and process each file/folder
            for item in os.listdir(source_directory):
                item_path = os.path.join(source_directory, item)

                # Check if the item is in the list of files or directories to be encrypted
                if any(file_name in item_path for file_name in files_or_dirs_to_encrypt):
                    add_to_zip(item_path)

        print(f"Selected files and folders have been zipped into a password-protected ZIP file: {zip_filename}")