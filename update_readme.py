import requests

# Define your statuses here
statuses = {
    "currently": "online",
    "playing": "nothing",
    "coding": "nothing",
    "listening": "nothing"
}

readme_path = "README.md"

def update_readme():
    with open(readme_path, "r") as file:
        readme_content = file.readlines()

    new_readme_content = []
    for line in readme_content:
        if line.strip().startswith("currently:"):
            new_readme_content.append(f"currently: {statuses['currently']}\n")
        elif line.strip().startswith("playing:"):
            new_readme_content.append(f"playing: {statuses['playing']}\n")
        elif line.strip().startswith("coding:"):
            new_readme_content.append(f"coding: {statuses['coding']}\n")
        elif line.strip().startswith("listening:"):
            new_readme_content.append(f"listening: {statuses['listening']}\n")
        else:
            new_readme_content.append(line)

    with open(readme_path, "w") as file:
        file.writelines(new_readme_content)

if __name__ == "__main__":
    update_readme()
