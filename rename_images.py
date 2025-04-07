import os

# Specify the folder containing the images
folder_path = 'web'

# Loop through the range of slides
for i in range(1, 121):
    old_name = f'Slide{i}.PNG'
    new_name = f'{i:03}.png'  # Format the new name with leading zeros
    old_path = os.path.join(folder_path, old_name)
    new_path = os.path.join(folder_path, new_name)
    
    # Rename the file
    if os.path.isfile(old_path):
        os.rename(old_path, new_path)
        print(f'Renamed: {old_name} to {new_name}')
    else:
        print(f'File not found: {old_name}')