import pandas as pd
from tabulate import tabulate

def printTables(myTable, myTable2, myTable3):
  myTable_formatted = tabulate(myTable, headers='keys', tablefmt='psql', numalign='center')
  myTable2_formatted = tabulate(myTable2, headers='keys', tablefmt='psql', numalign='center')
  myTable3_formatted = tabulate(myTable3, headers='keys', tablefmt='psql', numalign='center')
  
  print(myTable_formatted)
  print()
  print(myTable2_formatted)
  print()
  print(myTable3_formatted)
  
def read_file_to_vector(file_path):
    lines = []
    with open(file_path, 'r') as file:
        for i, line in enumerate(file):
            line = line.strip()
            if not line or i >= 7:
                break
            lines.append(line)
    return lines

def despacho_instruction(instruction, instruction_index, controle):
    tokens = instruction.split()
    operation = tokens[0]
    
    if operation == "add":
        instruction_tokens = instruction.split(" ")
        instruction_tokens = [s.replace(",", "") for s in instruction_tokens]
        if controle == False: myTable.loc[len(myTable)] = [instruction_index + 1, " ", instruction_tokens, " ", instruction_tokens[1], f"Regs[{instruction_tokens[2]}] + Regs[{instruction_tokens[3]}]"]
      
        verificaatt = 0
        names = ['add1', 'add2', 'add3']  
        
        for name in names:
            add_rows = myTable2[myTable2['Name'].isin([name])]
            for _, row in add_rows.iterrows():
                busy_column = row['Busy']
                if busy_column.strip() == "":
                  
                    dependencies = find_true_dependencies(instruction_tokens[2], instruction_tokens[3])
                    
                    if dependencies == " " or instruction_index == 0:
                      #atualiza tabela1
                      for _, row in myTable.iterrows():
                        if row['Instruction'] == instruction_tokens:
                            myTable.at[_, 'Busy'] = "Yes"
                            myTable.at[_, 'State'] = "Despacho"
                    
                      #atualiza tabela3
                      for column in myTable3.columns[1:]:
                        if column == instruction_tokens[1]:
                            myTable3.at[0, column] = instruction_index + 1
                            myTable3.at[1, column] = "Yes"
                          
                      myTable2.loc[add_rows.index, 'Busy'] = "Yes"
                      myTable2.loc[add_rows.index, 'Vj'] = instruction_tokens[2]
                      myTable2.loc[add_rows.index, 'Vk'] = instruction_tokens[3]
                      myTable2.loc[add_rows.index, 'Dest'] = instruction_index+1
                      myTable2.loc[add_rows.index, 'Op'] = operation

                      if controle == True: 
                          for index, row in myTable.iterrows():
                            if row['Instruction'] == instruction_tokens:
                                  print(instruction)
                                  myTable2.loc[add_rows.index, 'Dest'] = index+1
                                  for column in myTable3.columns[1:]:
                                    if column == instruction_tokens[1]:
                                        myTable3.at[0, column] = index + 1


                      verificaatt = 1
                      execution_instructions.append(instruction_tokens)
                      
                    else:
                      #atualiza tabela1
                      for _, row in myTable.iterrows():
                        if row['Instruction'] == instruction_tokens:
                            myTable.at[_, 'Busy'] = "Yes"
                            myTable.at[_, 'State'] = "Despacho"
                    
                      #atualiza tabela3
                      for column in myTable3.columns[1:]:
                        if column == instruction_tokens[1]:
                            myTable3.at[0, column] = instruction_index + 1
                            myTable3.at[1, column] = "Yes"
                          
                      myTable2.loc[add_rows.index, 'Busy'] = "Yes"
                      
                      if instruction_tokens[2] == dependencies:
                        myTable2.loc[add_rows.index, 'Qj'] = instruction_tokens[2]
                        myTable2.loc[add_rows.index, 'Vk'] = instruction_tokens[3]
                      else:
                        myTable2.loc[add_rows.index, 'Vk'] = instruction_tokens[2]
                        myTable2.loc[add_rows.index, 'Qk'] = instruction_tokens[3]
                        
                      myTable2.loc[add_rows.index, 'Dest'] = instruction_index+1
                      myTable2.loc[add_rows.index, 'Op'] = operation
                      if controle == True: 
                          for index, row in myTable.iterrows():
                            if row['Instruction'] == instruction_tokens:
                                  print(instruction)
                                  myTable2.loc[add_rows.index, 'Dest'] = index+1
                                  for column in myTable3.columns[1:]:
                                    if column == instruction_tokens[1]:
                                        myTable3.at[0, column] = index + 1 
                      verificaatt = 1
                      execution_instructionsTD.append(instruction_tokens)
                  
                else:
                  verificaatt = 0
                  
            if verificaatt == 1:
                break
        if verificaatt == 0 and controle == False:
          execution_instructionsRFD.append(instruction)
          execution_instructionsRF.append(instruction_tokens)
        

    elif operation == "sub":
        instruction_tokens = instruction.split(" ")
        instruction_tokens = [s.replace(",", "") for s in instruction_tokens]
        if controle == False:myTable.loc[len(myTable)] = [instruction_index + 1, " ", instruction_tokens, " ", instruction_tokens[1], f"Regs[{instruction_tokens[2]}] - Regs[{instruction_tokens[3]}]"]
      
        verificaatt = 0
        names = ['add1', 'add2', 'add3']  
        
        for name in names:
            add_rows = myTable2[myTable2['Name'].isin([name])]
            for _, row in add_rows.iterrows():
                busy_column = row['Busy']
                if busy_column.strip() == "":
                  
                    dependencies = find_true_dependencies(instruction_tokens[2], instruction_tokens[3])
                    
                    if dependencies == " " or instruction_index == 0:
                      #atualiza tabela1
                      for _, row in myTable.iterrows():
                        if row['Instruction'] == instruction_tokens:
                            myTable.at[_, 'Busy'] = "Yes"
                            myTable.at[_, 'State'] = "Despacho"
                    
                      #atualiza tabela3
                      for column in myTable3.columns[1:]:
                        if column == instruction_tokens[1]:
                            myTable3.at[0, column] = instruction_index + 1
                            myTable3.at[1, column] = "Yes"
                          
                      myTable2.loc[add_rows.index, 'Busy'] = "Yes"
                      myTable2.loc[add_rows.index, 'Vj'] = instruction_tokens[2]
                      myTable2.loc[add_rows.index, 'Vk'] = instruction_tokens[3]
                      myTable2.loc[add_rows.index, 'Dest'] = instruction_index+1
                      myTable2.loc[add_rows.index, 'Op'] = operation
                      if controle == True: 
                          for index, row in myTable.iterrows():
                            if row['Instruction'] == instruction_tokens:
                                  print(instruction)
                                  myTable2.loc[add_rows.index, 'Dest'] = index+1
                                  for column in myTable3.columns[1:]:
                                    if column == instruction_tokens[1]:
                                        myTable3.at[0, column] = index + 1  
                      verificaatt = 1
                      execution_instructions.append(instruction_tokens)
                      
                    else:
                      #atualiza tabela1
                      for _, row in myTable.iterrows():
                        if row['Instruction'] == instruction_tokens:
                            myTable.at[_, 'Busy'] = "Yes"
                            myTable.at[_, 'State'] = "Despacho"
                    
                      #atualiza tabela3
                      for column in myTable3.columns[1:]:
                        if column == instruction_tokens[1]:
                            myTable3.at[0, column] = instruction_index + 1
                            myTable3.at[1, column] = "Yes"
                          
                      myTable2.loc[add_rows.index, 'Busy'] = "Yes"
                      
                      if instruction_tokens[2] == dependencies:
                        myTable2.loc[add_rows.index, 'Qj'] = instruction_tokens[2]
                        myTable2.loc[add_rows.index, 'Vk'] = instruction_tokens[3]
                      else:
                        myTable2.loc[add_rows.index, 'Vk'] = instruction_tokens[2]
                        myTable2.loc[add_rows.index, 'Qk'] = instruction_tokens[3]
                        
                      myTable2.loc[add_rows.index, 'Dest'] = instruction_index+1
                      myTable2.loc[add_rows.index, 'Op'] = operation
                      if controle == True: 
                          for index, row in myTable.iterrows():
                            if row['Instruction'] == instruction_tokens:
                                  print(instruction)
                                  myTable2.loc[add_rows.index, 'Dest'] = index+1
                                  for column in myTable3.columns[1:]:
                                    if column == instruction_tokens[1]:
                                        myTable3.at[0, column] = index + 1                      
  
                      verificaatt = 1
                      execution_instructionsTD.append(instruction_tokens)
                  
                else:
                    verificaatt = 0
            if verificaatt == 1:
                break
        if verificaatt == 0 and controle == False:
          execution_instructionsRFD.append(instruction)
          execution_instructionsRF.append(instruction_tokens)

    elif operation == "mul":
        instruction_tokens = instruction.split(" ")
        instruction_tokens = [s.replace(",", "") for s in instruction_tokens]
        if controle == False:myTable.loc[len(myTable)] = [instruction_index + 1, " ", instruction_tokens, " ", instruction_tokens[1], f"Regs[{instruction_tokens[2]}] * Regs[{instruction_tokens[3]}]"]
      
        verificaatt = 0
        names = ['mult1', 'mult2']  
        
        for name in names:
            add_rows = myTable2[myTable2['Name'].isin([name])]
            for _, row in add_rows.iterrows():
                busy_column = row['Busy']
                if busy_column.strip() == "":
                  
                    dependencies = find_true_dependencies(instruction_tokens[2], instruction_tokens[3])
                    
                    if dependencies == " " or instruction_index == 0:
                      #atualiza tabela1
                      for _, row in myTable.iterrows():
                        if row['Instruction'] == instruction_tokens:
                            myTable.at[_, 'Busy'] = "Yes"
                            myTable.at[_, 'State'] = "Despacho"
                    
                      #atualiza tabela3
                      for column in myTable3.columns[1:]:
                        if column == instruction_tokens[1]:
                            myTable3.at[0, column] = instruction_index + 1
                            myTable3.at[1, column] = "Yes"
                          
                      myTable2.loc[add_rows.index, 'Busy'] = "Yes"
                      myTable2.loc[add_rows.index, 'Vj'] = instruction_tokens[2]
                      myTable2.loc[add_rows.index, 'Vk'] = instruction_tokens[3]
                      myTable2.loc[add_rows.index, 'Dest'] = instruction_index+1
                      myTable2.loc[add_rows.index, 'Op'] = operation
                      if controle == True: 
                          for index, row in myTable.iterrows():
                            if row['Instruction'] == instruction_tokens:
                                  print(instruction)
                                  myTable2.loc[add_rows.index, 'Dest'] = index+1
                                  for column in myTable3.columns[1:]:
                                    if column == instruction_tokens[1]:
                                        myTable3.at[0, column] = index + 1  
                      verificaatt = 1
                      execution_instructions.append(instruction_tokens)
                      
                    else:
                      #atualiza tabela1
                      for _, row in myTable.iterrows():
                        if row['Instruction'] == instruction_tokens:
                            myTable.at[_, 'Busy'] = "Yes"
                            myTable.at[_, 'State'] = "Despacho"
                    
                      #atualiza tabela3
                      for column in myTable3.columns[1:]:
                        if column == instruction_tokens[1]:
                            myTable3.at[0, column] = instruction_index + 1
                            myTable3.at[1, column] = "Yes"
                          
                      myTable2.loc[add_rows.index, 'Busy'] = "Yes"
                      
                      if instruction_tokens[2] == dependencies:
                        myTable2.loc[add_rows.index, 'Qj'] = instruction_tokens[2]
                        myTable2.loc[add_rows.index, 'Vk'] = instruction_tokens[3]
                      else:
                        myTable2.loc[add_rows.index, 'Vk'] = instruction_tokens[2]
                        myTable2.loc[add_rows.index, 'Qk'] = instruction_tokens[3]
                        
                      myTable2.loc[add_rows.index, 'Dest'] = instruction_index+1
                      myTable2.loc[add_rows.index, 'Op'] = operation
                      if controle == True: 
                          for index, row in myTable.iterrows():
                            if row['Instruction'] == instruction_tokens:
                                  print(instruction)
                                  myTable2.loc[add_rows.index, 'Dest'] = index+1
                                  for column in myTable3.columns[1:]:
                                    if column == instruction_tokens[1]:
                                        myTable3.at[0, column] = index + 1  
                      verificaatt = 1
                      execution_instructionsTD.append(instruction_tokens)
                  
                else:
                    verificaatt = 0
            if verificaatt == 1:
                break
        if verificaatt == 0 and controle == False:
          execution_instructionsRFD.append(instruction)
          execution_instructionsRF.append(instruction_tokens)

    elif operation == "str":
        instruction_tokens = instruction.split(" ")
        instruction_tokens[1] = instruction_tokens[1].replace(",", "")
        offset = instruction_tokens[2].split("(")[0]
        register = instruction_tokens[2].split("(")[1].replace(")", "")
        if controle == False: myTable.loc[len(myTable)] = [instruction_index + 1, " ", instruction_tokens, " ", f"Mem[{offset} + Regs[{register}]", f"Mem[{offset} + Regs[{register}]"]
      
        verificaatt = 0
        names = ['load1', 'load2']  
        
        for name in names:
            add_rows = myTable2[myTable2['Name'].isin([name])]
            for _, row in add_rows.iterrows():
                busy_column = row['Busy']
                if busy_column.strip() == "":
                  
                    dependencies = find_true_dependencies(offset, register)
                    
                    if dependencies == " " or instruction_index == 0:
                      #atualiza tabela1
                      for _, row in myTable.iterrows():
                        if row['Instruction'] == instruction_tokens:
                            myTable.at[_, 'Busy'] = "Yes"
                            myTable.at[_, 'State'] = "Despacho"
    
                      myTable2.loc[add_rows.index, 'Busy'] = "Yes"
                      myTable2.loc[add_rows.index, 'Dest'] = instruction_index+1
                      myTable2.loc[add_rows.index, 'Op'] = operation
                      myTable2.loc[add_rows.index, 'A'] = f"Mem[{offset} + Regs[{register}]"
                      if controle == True: 
                          for index, row in myTable.iterrows():
                            if row['Instruction'] == instruction_tokens:
                                  print(instruction)
                                  myTable2.loc[add_rows.index, 'Dest'] = index+1
                                  for column in myTable3.columns[1:]:
                                    if column == instruction_tokens[1]:
                                        myTable3.at[0, column] = index + 1                    
                      verificaatt = 1
                      execution_instructions.append(instruction_tokens)
                      
                    else:
                      #atualiza tabela1
                      for _, row in myTable.iterrows():
                        if row['Instruction'] == instruction_tokens:
                            myTable.at[_, 'Busy'] = "Yes"
                            myTable.at[_, 'State'] = "Despacho"
                    
                      myTable2.loc[add_rows.index, 'Busy'] = "Yes"
                      myTable2.loc[add_rows.index, 'Qj'] = register
                      myTable2.loc[add_rows.index, 'Dest'] = instruction_index+1
                      myTable2.loc[add_rows.index, 'Op'] = operation
                      myTable2.loc[add_rows.index, 'A'] = f"Mem[{offset} + Regs[{register}]"
                      if controle == True: 
                          for index, row in myTable.iterrows():
                            if row['Instruction'] == instruction_tokens:
                                  print(instruction)
                                  myTable2.loc[add_rows.index, 'Dest'] = index+1
                                  for column in myTable3.columns[1:]:
                                    if column == instruction_tokens[1]:
                                        myTable3.at[0, column] = index + 1  
                      verificaatt = 1
                      execution_instructionsTD.append(instruction_tokens)
                else:
                    verificaatt = 0
                  
            if verificaatt == 1:
                break
        if verificaatt == 0 and controle == False:
          execution_instructionsRFD.append(instruction)
          execution_instructionsRF.append(instruction_tokens)

    elif operation == "ld":
        instruction_tokens = instruction.split(" ")
        instruction_tokens[1] = instruction_tokens[1].replace(",", "")
        offset = instruction_tokens[2].split("(")[0]
        register = instruction_tokens[2].split("(")[1].replace(")", "")
        if controle == False:myTable.loc[len(myTable)] = [instruction_index + 1, " ", instruction_tokens, " ", instruction_tokens[1], f"Mem[{offset} + Regs[{register}]"]
      
        verificaatt = 0
        names = ['load1', 'load2']  
        
        for name in names:
            add_rows = myTable2[myTable2['Name'].isin([name])]
            for _, row in add_rows.iterrows():
                busy_column = row['Busy']
                if busy_column.strip() == "":
                  
                    dependencies = find_true_dependencies(offset, register)
                    
                    if dependencies == " " or instruction_index == 0:
                      #atualiza tabela1
                      for _, row in myTable.iterrows():
                        if row['Instruction'] == instruction_tokens:
                            myTable.at[_, 'Busy'] = "Yes"
                            myTable.at[_, 'State'] = "Despacho"
                    
                      #atualiza tabela3
                      for column in myTable3.columns[1:]:
                        if column == instruction_tokens[1]:
                            myTable3.at[0, column] = instruction_index + 1
                            myTable3.at[1, column] = "Yes"
                          
                      myTable2.loc[add_rows.index, 'Busy'] = "Yes"
                      myTable2.loc[add_rows.index, 'Dest'] = instruction_index+1
                      myTable2.loc[add_rows.index, 'Op'] = operation
                      myTable2.loc[add_rows.index, 'A'] = f"Mem[{offset} + Regs[{register}]"
                      if controle == True: 
                          for index, row in myTable.iterrows():
                            if row['Instruction'] == instruction_tokens:
                                  print(instruction)
                                  myTable2.loc[add_rows.index, 'Dest'] = index+1
                  
                      verificaatt = 1
                      execution_instructions.append(instruction_tokens)
                      
                    else:
                      #atualiza tabela1
                      for _, row in myTable.iterrows():
                        if row['Instruction'] == instruction_tokens:
                            myTable.at[_, 'Busy'] = "Yes"
                            myTable.at[_, 'State'] = "Despacho"
                    
                      #atualiza tabela3
                      for column in myTable3.columns[1:]:
                        if column == instruction_tokens[1]:
                            myTable3.at[0, column] = instruction_index + 1
                            myTable3.at[1, column] = "Yes"
                          
                      myTable2.loc[add_rows.index, 'Busy'] = "Yes"
                      myTable2.loc[add_rows.index, 'Qj'] = register
                      myTable2.loc[add_rows.index, 'Dest'] = instruction_index+1
                      myTable2.loc[add_rows.index, 'Op'] = operation
                      myTable2.loc[add_rows.index, 'A'] = f"Mem[{offset} + Regs[{register}]"
                      if controle == True: 
                          for index, row in myTable.iterrows():
                            if row['Instruction'] == instruction_tokens:
                                  print(instruction)
                                  myTable2.loc[add_rows.index, 'Dest'] = index+1

                      verificaatt = 1
                      execution_instructionsTD.append(instruction_tokens)
                else:
                    verificaatt = 0
        
            if verificaatt == 1:
                break
        if verificaatt == 0 and controle == False:
          execution_instructionsRFD.append(instruction)
          execution_instructionsRF.append(instruction_tokens)

    elif operation == "beq" or operation == "bne":
        instruction_tokens = instruction.split(" ")
        instruction_tokens = [s.replace(",", "") for s in instruction_tokens]
        if controle == False:myTable.loc[len(myTable)] = [instruction_index + 1, " ", instruction_tokens, " ", " ", f"{instruction_tokens[3]} + Regs[PC]"]
      
        verificaatt = 0
        names = ['add1', 'add2', 'add3']  
        
        for name in names:
            add_rows = myTable2[myTable2['Name'].isin([name])]
            for _, row in add_rows.iterrows():
                busy_column = row['Busy']
                if busy_column.strip() == "":
                  
                    dependencies = find_true_dependencies(instruction_tokens[1], instruction_tokens[2])
                    print(dependencies)
                    print(instruction_tokens[1])
                    print(instruction_tokens[2])
                    if dependencies == " " or instruction_index == 0:
                      #atualiza tabela1
                      for _, row in myTable.iterrows():
                        if row['Instruction'] == instruction_tokens:
                            myTable.at[_, 'Busy'] = "Yes"
                            myTable.at[_, 'State'] = "Despacho"
                          
                      myTable2.loc[add_rows.index, 'Busy'] = "Yes"
                      myTable2.loc[add_rows.index, 'A'] = f"{instruction_tokens[3]} + Regs[PC]"
                      myTable2.loc[add_rows.index, 'Dest'] = instruction_index+1
                      myTable2.loc[add_rows.index, 'Op'] = operation
                      if controle == True: 
                          for index, row in myTable.iterrows():
                            if row['Instruction'] == instruction_tokens:
                                  print(instruction)
                                  myTable2.loc[add_rows.index, 'Dest'] = index+1

                      verificaatt = 1
                      execution_instructions.append(instruction_tokens)

                    else:
                      #atualiza tabela1
                      for _, row in myTable.iterrows():
                        if row['Instruction'] == instruction_tokens:
                            myTable.at[_, 'Busy'] = "Yes"
                            myTable.at[_, 'State'] = "Despacho"
    
                      myTable2.loc[add_rows.index, 'Busy'] = "Yes"
                      myTable2.loc[add_rows.index, 'Dest'] = instruction_index+1
                      myTable2.loc[add_rows.index, 'Op'] = operation
                      myTable2.loc[add_rows.index, 'A'] = f"{instruction_tokens[3]} + Regs[PC]"
                      
                      if instruction_tokens[1] == dependencies:
                        myTable2.loc[add_rows.index, 'Qj'] = instruction_tokens[1]
                      else:
                        myTable2.loc[add_rows.index, 'Qk'] = instruction_tokens[2]
                      if controle == True: 
                          for index, row in myTable.iterrows():
                            if row['Instruction'] == instruction_tokens:
                                  print(instruction)
                                  myTable2.loc[add_rows.index, 'Dest'] = index+1
                                  for column in myTable3.columns[1:]:
                                    if column == instruction_tokens[1]:
                                        myTable3.at[0, column] = index + 1     
                      verificaatt = 1
                      execution_instructionsTD.append(instruction_tokens)
                  
                else:
                    verificaatt = 0
            if verificaatt == 1:
                break
        if verificaatt == 0 and controle == False:
          execution_instructionsRFD.append(instruction)
          execution_instructionsRF.append(instruction_tokens)
            
def find_true_dependencies(reg1, reg2):
  for _, row in myTable.iterrows():
    if row['Destination'] == reg1:
      return reg1
      
    elif row['Destination'] == reg2:
      return reg2
      
  return " "      

def instruction_execution(instructions):
  instruction_index = 0
  while instruction_index < len(instructions):
        if instruction_index < len(instructions):
            print("Press 's' to skip to the next step or any other key to exit: ")
            user_input = input()

            if user_input != 's':
                break
        instruction = instructions[instruction_index]
        for _, row in myTable.iterrows():
          if row['Instruction'] == instruction:
            myTable.at[_, 'State'] = "Execução"  
        instruction_index += 1
        printTables(myTable, myTable2, myTable3)
               
def instruction_writeResult(instructions):
  instruction_index = 0
  while instruction_index < len(instructions):
        if instruction_index < len(instructions):
            print("Press 's' to skip to the next step or any other key to exit: ")
            user_input = input()
            if user_input != 's':
                break  
        instruction = instructions[instruction_index]
        
        for _, row in myTable.iterrows():
          if row['Instruction'] == instruction:
            myTable.at[_, 'State'] = "Escrita de resultado"   
            
        beq_instruction(instruction)
        instruction_index += 1
        printTables(myTable, myTable2, myTable3)
    
def beq_instruction(instruction):
  x = 0
  if  instruction[0] == 'beq' or instruction[0] == 'bne':
    num = int(instruction[3])
    
    for index, row in myTable.iterrows():
        if row['Instruction'] == instruction:
            while(x <= num):
              linha = index + x
              myTable.loc[linha, myTable.columns[1:]] = ''
              myTable2.loc[myTable2['Dest'] == linha+1, myTable2.columns[1:]] = ''
              for column, value2 in myTable3.iloc[0].items():
                if linha+1 == value2: 
                  myTable3.at[0, column] = ''
                  myTable3.at[1, column] = ''
              x += 1
            break

def instruction_commit(instructions):
  instruction_index = 0
  while instruction_index < len(instructions):
        if instruction_index < len(instructions):
            print("Press 's' to skip to the next step or any other key to exit: ")
            user_input = input()

            if user_input != 's':
                break        
        instruction = instructions[instruction_index]
        for _, row in myTable.iterrows():
          if row['Instruction'] == instruction:
            myTable.at[_, 'State'] = "Commit"  
        instruction_index += 1
        printTables(myTable, myTable2, myTable3)

def delete_instructions():
    entry = []

    for _, row in myTable.iterrows():
        if row['State'] == "Commit":
            entry.append(row['Entry'])

    for value in entry:
        if value < len(entry):
            print("Press 's' to skip to the next step or any other key to exit: ")
            user_input = input()

            if user_input != 's':
                break          
        myTable.loc[myTable['Entry'] == value, myTable.columns[1:]] = ''
        myTable2.loc[myTable2['Dest'] == value, myTable2.columns[1:]] = ''
      
        for column, value2 in myTable3.iloc[0].items():
          if value == value2: 
            myTable3.at[0, column] = ''
            myTable3.at[1, column] = ''
        
    printTables(myTable, myTable2, myTable3)

def execute_tomasulo():
    instructions = read_file_to_vector('instrucoes.txt')
    instruction_index = 0
    global execution_instructions
    global execution_instructionsTD
    global execution_instructionsRFD
    global execution_instructionsRF
    execution_instructions = []  
    execution_instructionsTD = []  
    execution_instructionsRFD = []  
    execution_instructionsRF = []  

    while instruction_index < len(instructions):
        instruction = instructions[instruction_index]
        despacho_instruction(instruction, instruction_index, False)
        instruction_index += 1
        printTables(myTable, myTable2, myTable3)
        if instruction_index < len(instructions):
            print("Press 's' to skip to the next step or any other key to exit: ")
            user_input = input()

            if user_input != 's':
                break
            
    instruction_execution(execution_instructions)           
    instruction_writeResult(execution_instructions)     
    instruction_commit(execution_instructions) 
    delete_instructions()

    instruction_index = 0
    while instruction_index < len(execution_instructionsRFD):
        instruction = execution_instructionsRFD[instruction_index]
        despacho_instruction(instruction, instruction_index, True)
        instruction_index += 1
        printTables(myTable, myTable2, myTable3)

        if instruction_index < len(execution_instructionsRFD):
            print("Press 's' to skip to the next step or any other key to exit: ")
            user_input = input()

            if user_input != 's':
                break
            
    instruction_execution(execution_instructionsTD)           
    instruction_writeResult(execution_instructionsTD)     
    instruction_commit(execution_instructionsTD) 
    delete_instructions()

    instruction_execution(execution_instructionsRF)           
    instruction_writeResult(execution_instructionsRF)     
    instruction_commit(execution_instructionsRF) 
    delete_instructions()
    
myTable = pd.DataFrame([], columns=["Entry", "Busy", "Instruction", "State", "Destination", "Value"])

myTable2 = pd.DataFrame([
    ["load1", " ", " ", " ", " ", " ", " ", " ", " "],
    ["load2", " ", " ", " ", " ", " ", " ", " ", " "],
    ["add1", " ", " ", " ", " ", " ", " ", " ", " "],
    ["add2", " ", " ", " ", " ", " ", " ", " ", " "],
    ["add3", " ", " ", " ", " ", " ", " ", " ", " "],
    ["mult1", " ", " ", " ", " ", " ", " ", " ", " "],
    ["mult2", " ", " ", " ", " ", " ", " ", " ", " "]
], columns=["Name", "Busy", "Op", "Vj", "Vk", "Qj", "Qk", "Dest", "A"])

myTable3 = pd.DataFrame([
    ["Reorder", "", "", "", "", "", "", "", ""],
    ["Busy", "", "", "", "", "", "", "", ""]
], columns=["Field", "r1", "r2", "r3", "r4", "r5", "r6", "r7", "r8"])

execute_tomasulo()
