# encoding: utf-8

from xhtml2pdf import pisa             # import python module
from bs4 import BeautifulSoup
import pdfkit

# Define your data
path = 'test.html'
htmlfile = open(path, 'r', encoding='utf-8')
htmlhandle = htmlfile.read()

source_html = ""
output_filename = "test.pdf"

# Utility function
def convert_html_to_pdf(source_html, output_filename):
    # open output file for writing (truncated binary)
    result_file = open(output_filename, "w+b")

    # convert HTML to PDF
    pisa_status = pisa.CreatePDF(
            source_html,                # the HTML to convert
            dest=result_file)           # file handle to recieve result

    # close output file
    result_file.close()                 # close output file

    # return False on success and True on errors
    return pisa_status.err

# Main program
if __name__ == "__main__":
    pisa.showLogging()
    #print(htmlhandle)
    convert_html_to_pdf(htmlhandle , output_filename)



    pdfkit.from_file('test.html', 'test.pdf')
