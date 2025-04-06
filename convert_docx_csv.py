import csv
from docx import Document

def convert_docx_to_csv(docx_file, csv_file):
    # Load the DOCX file
    doc = Document(docx_file)
    
    # Prepare a list to hold the character data
    characters = []

    # Iterate through paragraphs in the document
    count = 0
    for paragraph in doc.paragraphs:
        
        if len(paragraph.text.strip())>0:  # Check if the paragraph is not empty
            count += 1
            if count== 1:
                # Extract character name and age from the first line
                first_line =  paragraph.text.strip().split("(")
                
                name = first_line[0].strip()  # Join all but the last word as name
                name = name[1:].replace('司鐸／',"")  # Remove any trailing parenthesis
                print("Name:",name)
                age = first_line[1].split('[')[0].strip().replace(')',"")  # Last word as age
                print("Time Range:",age)
            if count == 2:
                # Extract story from the second line
                id = len(characters) + 1
                story = paragraph.text.strip().replace('司鐸／',"")
                print("Story:",story)

                text_image = f"{id:03}.jpg"
                # Append the character data as a tuple
                characters.append((id, name, age, story,text_image))
                count = 0
    # Write to CSV file
    with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['ID', 'Name', 'Time_rage', 'Story', 'Image'])  # Write header
        writer.writerows(characters)  # Write character data

# Example usage
convert_docx_to_csv('data.docx', 'data.csv')