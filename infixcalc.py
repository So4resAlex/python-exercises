# Código desenvolvido durante treinamento de Python base da Linux Tips
import sys
from unittest import result

from pydantic import validate_email

arguments = sys.argv[1:]

if not arguments:
    operation = input("operação:")
    n1 = input("n1:")
    n2 = input("n2:")
    arguments = [operation, n1, n2]
elif len(arguments) != 3:
    print("Número de argmentos invalidos")
    print("ex: `sum 5 5`")
    sys.exit(1)

operation, *nums = arguments

valid_operations = ("sum", "sub", "mul", "div")
if operation not in valid_operations:
    print("Operação invalida")
    print(valid_operations)
    sys.exit(1)

validated_nums = []
for num in nums:
    if not num.replace(".", "").isdigit():
        print(f"Numero inválido {num}")
        sys.exit(1)
    if "." in num:
        num = float(num)
    else:
        num = int(num)
    validated_nums.append(num)

n1 , n2 = validated_nums

if operation == "sum":
    result = n1 + n2
elif operation == "sub":
    result = n1 - n2 
elif operation == "sub":
    result = n1 * n2 
elif operation == "sub":
    result = n1 / n2 

print(f"O resultado é {result}")


