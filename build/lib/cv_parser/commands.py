import argparse
from cv_parser.cvparser import CVParser
from pick import pick

def main():
    cvParser = CVParser()
    title = "Please select an option:"
    options = ["Add CV Template", "Generate CV From Template"]
    option, index = pick(title=title, options=options)
    try:
        addTemplate(cvParser) if index == 0 else generateCV(cvParser)
    except Exception as e:
        print(e)

def generateCV(cvParser: CVParser):
    templates = cvParser.getTemplateTitles()
    if templates == []:
        print("No CV templates found. Please add a template first.")
        return
    title = "Select a template to use:"
    option, _ = pick(title=title, options=templates)
    company = input("Enter company name: ").strip("\"\'").strip()
    position = input("Enter the position title: ").strip("\"\'").strip()
    output_path = input(f"(Optional) Enter the output path [default: {cvParser.templateInfo[option]}]").strip("\"\'").strip()
    location = cvParser.createCV(company, position, option, output_path)
    print(f'\nCover Letter successfully saved to: {location}\n')



def addTemplate(cvParser: CVParser):
    filepath = input("Please enter the file path location of your CV template: ").strip("\"\'").strip()
    name = input("(Optional) Please enter a name for your template (necessary if you want to save multiple templates): ").strip("\"\'").strip() or "default"
    cvParser.addTemplate(filepath, name)
    print("Template successfully added!")