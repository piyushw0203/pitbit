import json

resume_text = """
John Doe
Email: john.doe@example.com
Phone: 123-456-7890

Education:
- B.Sc. in Computer Science, XYZ University, 2020

Experience:
- Software Engineer at ABC Corp, 2021-Present
  - Developed web applications using Flask and React.
  - Implemented AWS solutions for file storage.

Skills:
- Python, JavaScript, AWS, Flask, React
"""

# Define the JSON structure
resume_data = {
    "name": "John Doe",
    "contact": {
        "email": "john.doe@example.com",
        "phone": "123-456-7890"
    },
    "education": [
        {
            "degree": "B.Sc. in Computer Science",
            "institution": "XYZ University",
            "year": 2020
        }
    ],
    "experience": [
        {
            "position": "Software Engineer",
            "company": "ABC Corp",
            "duration": "2021-Present",
            "responsibilities": [
                "Developed web applications using Flask and React.",
                "Implemented AWS solutions for file storage."
            ]
        }
    ],
    "skills": ["Python", "JavaScript", "AWS", "Flask", "React"]
}

# Convert to JSON
resume_json = json.dumps(resume_data, indent=4)

# Write JSON to file
with open('resume.json', 'w') as json_file:
    json_file.write(resume_json)

print("JSON file created successfully.")
