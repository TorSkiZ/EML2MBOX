# Overview
This repository contains a Python script that converts EML and JSON files into a single MBOX file. The script reads EML files and their corresponding metadata from JSON files, combines the data, and saves it into an MBOX file.

## Table of Contents
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Script Details](#script-details)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Requirements
- Python 3.x
- `mail-parser` library

## Installation
1. Clone the Repository
```
git clone https://github.com/TorSkiZ/EML2MBOX.git
cd EML2MBOX
```

2. Install Dependence
```
pip install mail-parser
```

## Usage
1. Directory Structure
   Place your EML files and corresponding JSON metadata files in a directory. The JSON files should have the same name as the EML files, with an additional `.metadata.json` extension.
   Example:
   ```
   input/
   ├── email1.eml
   ├── email1.metadata.json
   ├── email2.eml
   └── email2.metadata.json
   ```

2. Run the Script
   ```
   python main.py
   ```

## Script Details
The script performs the following steps:
1. Load JSON Metadata
   The `load_json_metadata` function reads the JSON metadata file and returns the content as a dictionary.

2. Add EML to MBOX
   The `add_eml_to_mbox` function reads an EML file, parses it using `mail-parser`, and creates a `mailbox.mboxMessage` object. It then adds the metadata to the message headers and appends the message to the MBOX file.

3. Convert EML and JSON to MBOX
   The `convert_eml_json_to_mbox` function iterates over the files in the specified directory, matches each EML file with its corresponding JSON metadata file, and processes them using the above functions. If no metadata file is found for an EML file, a message is printed.

## Contributing
Contributions are welcome! If you have any suggestions or find any issues, please open an issue or submit a pull request. Please ensure your contributions align with the project's goals and coding standards.

## License
This project is licensed under the MIT License. See the LICENSE file for more information.

## Contact
If you have any feedback, please reach out to me at wiktor.wasinski@wiciu.pl