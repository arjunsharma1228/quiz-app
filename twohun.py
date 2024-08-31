from PyPDF2 import PdfReader
import re
import json

# Path to the PDF file
pdf_path = r"E:\linkedin post\two\full.pdf"

# Open and read the PDF file
reader = PdfReader(pdf_path)
questions_list = []

# Regular expression to match questions, options, and answers
question_pattern = re.compile(r'(\d+)\.\s+(.*?)\n\s*\(a\)(.*?)\(b\)(.*?)\(c\)(.*?)\(d\)(.*?)\(e\)(.*?)\n\s*Ans\s*:\s*\((.)\)', re.DOTALL)

# Iterate through all pages
for page in reader.pages:
    text = page.extract_text()
    if text:
        matches = question_pattern.findall(text)
        
        # Process each matched question
        for match in matches:
            question = {
                "question_number": match[0].strip(),
                "question": match[1].strip(),
                "options": {
                    "a": match[2].strip(),
                    "b": match[3].strip(),
                    "c": match[4].strip(),
                    "d": match[5].strip(),
                    "e": match[6].strip()
                },
                "answer": match[7].strip()
            }
            questions_list.append(question)

# Save the list of questions to a JSON file
output_path = r"E:\linkedin post\two\full.json"
with open(output_path, 'w') as json_file:
    json.dump(questions_list, json_file, indent=4)

print(f"Extraction complete. JSON data saved to {output_path}")
