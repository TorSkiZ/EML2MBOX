import json
import os
import mailbox
import mailparser

def load_json_metadata(json_file):
    with open(json_file, 'r', encoding='utf-8') as f:
        return json.load(f)

def add_eml_to_mbox(mbox, eml_file, metadata):
    with open(eml_file, 'r', encoding='utf-8', errors='ignore') as f:
        eml_data = f.read()
    
    mail = mailparser.parse_from_string(eml_data)
    msg = mailbox.mboxMessage(eml_data)
    
    for key, value in metadata.items():
        msg[key] = str(value)
    
    mbox.add(msg)

def convert_eml_json_to_mbox(eml_dir, mbox_file):
    mbox = mailbox.mbox(mbox_file)
    mbox.lock()
    
    try:
        for filename in os.listdir(eml_dir):
            if filename.endswith('.eml'):
                eml_file = os.path.join(eml_dir, filename)
                json_file = os.path.join(eml_dir, filename.replace('.eml', '.metadata.json'))
                
                if os.path.exists(json_file):
                    metadata = load_json_metadata(json_file)
                    add_eml_to_mbox(mbox, eml_file, metadata)
                else:
                    print(f"No metadata file found for {eml_file}")
    finally:
        mbox.flush()
        mbox.unlock()

input = 'input'
output = 'output.mbox'
convert_eml_json_to_mbox(input, output)