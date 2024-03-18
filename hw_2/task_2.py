from latex_generator_2 import LatexGenerator
import subprocess
pdflatex_path = 'C:/texlive/2024/bin/windows/pdflatex.exe'

latex = '''
\\documentclass{article}
\\begin{document}
'''
latex += LatexGenerator.generate_table([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
latex += LatexGenerator.generate_image(image_path='/img.png')
latex += '\n\\end{document}'

with open('file.tex', 'w') as file:
    file.write(latex)

process = subprocess.Popen([pdflatex_path, '-interaction=nonstopmode', '-output-directory=.', '-jobname=task_2', 'file.tex'],
                           stdout=subprocess.PIPE, stderr=subprocess.PIPE)


output = process.communicate()
output, error = process.communicate()

if process.returncode == 0:
    print('PDF generated')
else:
    print('Error occurred:', error.decode('utf-8'))
