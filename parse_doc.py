import jsonlines
import re
from docutils.parsers import rst
from docutils.io import StringInput
from docutils.core import publish_doctree, publish_from_doctree
import subprocess
import fileinput
import json
import numpy as np
import openai
import uuid
import time

context = "Name_of_Your_Publications"

def openai_convert_table(table_set):
        openai.api_key="Your_Key"
        api_key=openai.api_key
        # Make an API call
        response = openai.Completion.create(
        #engine="text-davinci-003",
        model="gpt-3.5-turbo-instruct",
        prompt= f"Generate a descriptive paragraph providing a detailed overview of the content presented in the table {table_set}. The descriptive paragraphwill be append next to the table. This table pertains to {context}. The first row is the header and there's no need to describe it.",
        temperature = 1,
        max_tokens=2048,  # Adjust based on the requirements
        api_key=api_key,
        top_p=1
        )

        # Extract the generated description from the API response
        description = response.choices[0].text
        return(description)


def search_table(file_path):

    with open(file_path, 'r', encoding="utf-8") as file:
        document_content = file.read()

    table_pattern = r"^\s*\+[-+=]*\+.*\n((?:^[|+].*[|+].*\n)+)(?:^\s*\+[-+=]*\+[\t ]*$|\n)"

    tables = re.findall(table_pattern, document_content, re.MULTILINE)
    modified_content = document_content
    for i, table in enumerate(tables, start=1):
        table_set=table
        table_descript=openai_convert_table(table_set)
        table_update = table_descript + '\n'+'\n' +table
        modified_content = modified_content.replace(table, table_update)

        time.sleep(30) # sleep 30 s to be able to use the free version api

    with open(file_path, 'w', encoding="utf-8") as file:
        file.write(modified_content)


def rst_to_json(input_rst, output_json):
    with open(input_rst, 'r') as rst_file:
        rst_text = rst_file.read()

    document = publish_doctree(rst_text)

    with jsonlines.open(output_json, 'w') as writer:
        for node in document.traverse():
            if node.__class__.__name__ == 'document':
                writer.write({'node_type': node.__class__.__name__, 'text': node.astext()})


if __name__ == "__main__":
    input_rst_file = "./test.rst"
    search_table(input_rst_file)
    output_json_file = "output.jsonl"
    rst_to_json(input_rst_file, output_json_file)
                                                 


