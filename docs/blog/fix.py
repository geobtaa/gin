import os

folder_path = 'posts'  # Change this to your folder's path

for filename in os.listdir(folder_path):
    if filename.endswith('.md'):
        filepath = os.path.join(folder_path, filename)
        
        with open(filepath, 'r') as file:
            lines = file.readlines()

        with open(filepath, 'w') as file:
            for line in lines:
                if "date:" in line and "'" in line:
                    line = line.replace("'", "")
                file.write(line)

print("All done! The dates have been updated! 🎉")