import os, os.path as path
import json
import shutil
from docx import Document
from python_docx_replace import docx_replace
import cv_parser

class CVParser:

    def __init__(self):
        self.templateInfo = {}
        self.templateDir = path.dirname(path.abspath(__file__))+'/CV-Templates'
        print('Initializing...\nReading template folder at: '+self.templateDir)
        if path.exists(f'{self.templateDir}/info.json'):
            self.templateInfo = json.load(open(f'{self.templateDir}/info.json'))
        else:
            if not path.exists(self.templateDir): os.makedirs(self.templateDir)
    
    def addTemplate(self, filepath, TemplateName):
        if path.exists(filepath) and path.splitext(filepath)[1] == '.docx':
            print(f'Saving template {path.abspath(filepath)}...')
            self.templateInfo[TemplateName] = path.dirname(path.abspath(filepath))
            shutil.copy2(filepath, f'{self.templateDir}/{TemplateName}.docx')
            json.dump(self.templateInfo, open(f'{self.templateDir}/info.json', 'w+'))
        else:
            raise Exception("Please ensure the path to your CV template is correct and is in .docx format.")
        
    def createCV(self, company: str, position: str, TemplateName: str, output: str):
        template_path = f'{self.templateDir}/{TemplateName}.docx'
        print(f'Creating CV using {TemplateName} template...')
        print(f'Retrieving CV template from {self.templateDir}...')
        if not path.exists(template_path) or not self.templateInfo[TemplateName]:
            print(path.exists(template_path), self.templateInfo)
            raise Exception("Template not found. Please ensure you have uploaded your template first using:\n"+
                            "parsecv add-template /path/to/CV-Template.docx")
        if not output:
            output = f'{self.templateInfo[TemplateName]}/{company.replace(" ", "-")}-CV.docx'
        
        doc = Document(template_path)
        docx_replace(doc, Company=company, Position=position)
        doc.save(output)
        return path.abspath(output)