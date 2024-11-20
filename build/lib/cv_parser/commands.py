import argparse
from cv_parser.cvparser import CVParser

def main():
    cvParser = CVParser()
    parser = argparse.ArgumentParser(description="Replace fields on your CV template to match the job position and company")
    subparser = parser.add_subparsers(dest='cmd')

    templateParser = subparser.add_parser('add-template')
    templateParser.add_argument("-n", "--template-name", help="(Optional) Set template name (necessary if you want to use CVs)", default="template")
    templateParser.add_argument("template_path", help="Path to template")

    createCVParser = subparser.add_parser('create-cv')
    createCVParser.add_argument("-c", "--company", required=True, help="Replace the field ${Company} with the appropriate company name")
    createCVParser.add_argument("-p", "--position", required=True, help="Replace the field ${Position} with the appropriate position title")
    createCVParser.add_argument("-n", "--template-name", help="(Optional) Template name if previously set", default="template")
    createCVParser.add_argument("-o", "--output-path", help="(Optional) Specify where to save the updated CV. By default, file will be saved in the same path as the template")
    createCVParser.add_argument("-m", "--merge-resume", help="(Optional) Provide a path to your resume to merge your CV and resume to one file")
    args = parser.parse_args()

    if args.cmd == 'add-template':
        try:
            cvParser.addTemplate(args.template_path, args.template_name)
            print("\nTemplate Successfully Saved!\n")
        except Exception as e:
            print(f'\n{e}\n')
            print("For further help, please try: \n parsecv add-template --help\n")
    elif args.cmd == 'create-cv':
        try:
            location = cvParser.createCV(args.company, args.position, args.template_name, args.output_path)
            print(f'\nCover Letter successfully saved to: {location}\n')
        except Exception as e:
            print(f'\n{e}\n')
            print("For further help, please try: \n parsecv create-cv --help\n")
    else:
        parser.print_help()

'''
    doc = Document(template_path)
    x = "Test Company"
    y = "Test Position"
    keys = docx_replace(doc, Company=x, Position=y)
    print(args)
    doc.save(f'{template_path[:-5]}')
    print('File has been successfully saved!')
'''