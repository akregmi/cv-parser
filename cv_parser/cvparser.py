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
        if path.exists(f'{self.templateDir}/info.json'):
            self.templateInfo = json.load(open(f'{self.templateDir}/info.json'))
        else:
            if not path.exists(self.templateDir): os.makedirs(self.templateDir)
    
    def addTemplate(self, filepath, TemplateName):
        if path.exists(filepath) and path.splitext(filepath)[1] == '.docx':
            self.templateInfo[TemplateName] = path.dirname(path.abspath(filepath))
            shutil.copy2(filepath, f'{self.templateDir}/{TemplateName}.docx')
            json.dump(self.templateInfo, open(f'{self.templateDir}/info.json', 'w+'))
        else:
            raise Exception("Please ensure the path to your CV template is correct and is in .docx format.")
        
    def createCV(self, company: str, position: str, TemplateName: str, output: str):
        template_path = f'{self.templateDir}/{TemplateName}.docx'
        if not path.exists(template_path) or not self.templateInfo[TemplateName]:
            raise Exception("Template not found. Please ensure you have uploaded your template first using:\n"+
                            "parsecv add-template /path/to/CV-Template.docx")
        if not output:
            output = f'{self.templateInfo[TemplateName]}/{company.replace(" ", "-")}-CV.docx'
        
        doc = Document(template_path)
        docx_replace(doc, Company=company, Position=position)
        doc.save(output)
        return path.abspath(output)