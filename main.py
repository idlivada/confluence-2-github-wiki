import os
import subprocess


input_root_path = "/home/pawan/wiki_conversion/wiki-exports/"
output_root_path = "/tmp/output/" 
wiki_space_prefixes = ["CS", "EN", "PROD"]

def main():
    for space in wiki_space_prefixes:
        convert_space(space)

def convert_space(wiki_space_prefix):
    wiki_space_prefix += "/"
    assert(wiki_space_prefix.endswith("/"))
    input_path = os.path.join(input_root_path, wiki_space_prefix)

    output_path = os.path.join(output_root_path, wiki_space_prefix)        
    if not os.path.isdir(output_path):
        os.mkdir(output_path)

    for filename in os.listdir(input_path):
        filepath = os.path.join(input_path, filename)

        if filepath.endswith('.html'):
            convert_file(filepath, wiki_space_prefix)
        continue

    
def convert_file(input_filepath, wiki_space_prefix):
    filename = os.path.split(input_filepath)[-1]
    output_path = os.path.join(output_root_path, wiki_space_prefix)        
    output_filepath = os.path.join(output_path, filename)
    
    command = '/usr/bin/pandoc -f html -t markdown_github -o %s %s' % (output_filepath, input_filepath)
    print command
    subprocess.call(command.split())

    f = open(output_filepath, 'r')
    contents = f.read()
    f.close()

    f = open(output_filepath, 'w')
    contents = contents.replace("attachments/", "http://www.curata.com/wiki/%sattachments/" % wiki_space_prefix)
    contents = contents.replace("images/", "http://www.curata.com/wiki/%simages/" % wiki_space_prefix)    
    f.write(contents)
    f.close()

if __name__ == "__main__":
    main()
