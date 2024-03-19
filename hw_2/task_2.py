from latex_generator_2 import LatexGenerator
import subprocess
pdflatex_path = 'C:/texlive/2024/bin/windows/pdflatex.exe'

example = [['Machine ID', 'Type', 'Manufacturer', 'Production Year'],
            ['M001', 'CNC Milling Machine', 'Haas Automation', 2020],
            ['M002', 'Injection Molding Machine', 'Arburg GmbH + Co KG', 2018],
            ['M003', 'Laser Cutting Machine', 'Trumpf GmbH', 2021]]

latex = '''
\\documentclass{article}
\\usepackage{graphicx}
\\begin{document}
'''
latex += LatexGenerator.generate_table(example)
latex += LatexGenerator.generate_image(image_path='img.png')
latex += '\n\\end{document}'

with open('task_2.tex', 'w') as file:
    file.write(latex)

process = subprocess.Popen([pdflatex_path, '-interaction=nonstopmode', '-output-directory=.', '-jobname=task_2', 'task_2.tex'],
                           stdout=subprocess.PIPE, stderr=subprocess.PIPE)

output, error = process.communicate()
