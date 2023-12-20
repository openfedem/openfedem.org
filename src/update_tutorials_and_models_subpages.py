from pathlib import Path
import requests
import shutil


def download_file_from_github(url, local_filename=None):
    # Send a GET request to the URL
    r = requests.get(url)

    # Check if the request was successful
    if r.status_code == 200:
        # Write the content of the response to a local file
        if local_filename is None:
            return r.content.decode('utf-8')
        else:
            with open(local_filename, 'wb') as f:
                f.write(r.content.encode('utf-8'))
            print(f"File downloaded successfully: {local_filename}")
    else:
        print(f"Failed to download file: HTTP status code {r.status_code}")


def download_binary_file(url, local_filename):
    # Send a GET request to the URL
    r = requests.get(url, stream=True)
    print("øl")
    # Check if the request was successful
    if True:  #r.status_code == 200:
        # Open the local file in binary write mode
        with open(local_filename, 'wb') as f:
            # Write the content of the response to the local file
            for chunk in r.iter_content(chunk_size=8192):
                # If you have chunk encoded response uncomment if
                # and set chunk_size parameter to None.
                # if chunk:
                f.write(chunk)
        print(f"File downloaded successfully: {local_filename}")
    else:
        print(f"Failed to download file: HTTP status code {r.status_code}")

def temp():
    # URL of the raw file content on GitHub
    file_url = "https://raw.githubusercontent.com/openfedem/tutorials/main/floating_cylinder/test_file.txt?token=GHSAT0AAAAAACLVQM7C65JCB4SECSCFPDV6ZMAU7VA"

    # Local path where you want to save the file
    local_file_path = '../image.txt'

    # Download the file
    #download_file_from_github(file_url, local_file_path)

    #https://github.com/openfedem/tutorials/tree/c0fcb2683ced2d115d635b317e36383b99c68978/floating_cylinder
    #https://github.com/openfedem/tutorials/blob/main/floating_cylinder/model.zip

    print("klømsdf")
    # URL of the binary file content (e.g., raw GitHub URL)
    file_url = 'https://github.com/openfedem/tutorials/blob/main/floating_cylinder/picture1.png'
    file_url = "https://raw.githubusercontent.com/openfedem/tutorials/main/floating_cylinder/picture1.png"
    #https://github.com/[username]/[repository]/blob/[branch]/[path-to-file
    file_url = "https://github.com/openfedem//blob/main/tutorials/picture1.png"
    # Local path where you want to save the file
    local_file_path = '../image.png'

    # Download the file
    download_binary_file(file_url, local_file_path)

    #lag en markdown template fil med en linje som dekodes for en path til en markdown fil i tutorisal sitt repo, decode fiilreferansene der og last de ned


def find_links_in_files(markdown_text, links = []):
    for chunk in markdown_text.split("](")[1:]:
        links.append(chunk[:chunk.find(")")])
    return links


template = open("template.md").read()

inserts_files = Path("../../").rglob("openfedem.md")

inserts = {}
for f in inserts_files:
    key = f.parent.stem
    inserts[key] = insert = open(f).read()

    links = find_links_in_files(insert)
    for link in links:
        print(link)

        # Define the source and destination file paths
        source_file = 'path/to/source/file.txt'
        destination_file = 'path/to/destination/file.txt'

        # Copy the file
        shutil.copy(source_file, destination_file)



open("realization.md", "w").write(template.format(**inserts))






exit()
IDENTIFIER = "<!github.com/openfedem:"

def find_markdown_files(path, identifier="<!github.com/openfedem:"):
    markdown_text = open(path, 'r').read()
    return [chunk.split("\n")[0].strip()[:-1] for chunk in markdown_text.split(identifier)[1:]]






github_urls = find_markdown_files("template.md")

for github_url in github_urls:
    #username = "openfedem"
    #repository = "openfedem"
    #branch = "main"
    #path = "tutorials/README.md"
    #path = f"https://github.com/{username}/{repository}/blob/{branch}/{path}"

    content = download_file_from_github(github_url)
    print(content)

    links = find_links_in_files(content)
    for link in links:
        print(link)

