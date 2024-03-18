from latex_gen_12 import LatexGenerator

example = [['Machine ID', 'Type', 'Manufacturer', 'Production Year'],
            ['M001', 'CNC Milling Machine', 'Haas Automation', 2020],
            ['M002', 'Injection Molding Machine', 'Arburg GmbH + Co KG', 2018],
            ['M003', 'Laser Cutting Machine', 'Trumpf GmbH', 2021]]

latex_code = LatexGenerator.generate_table(example)

with open('task_1.tex', 'w') as file:
    file.write(latex_code)
