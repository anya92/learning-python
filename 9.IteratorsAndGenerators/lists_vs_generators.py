# The main advantage of generator over a list is that it take much less memory.
import sys

list_comp = sys.getsizeof([x for x in range(10000)])
gen_expe = sys.getsizeof(x for x in range(10000))

print(f"List Comprehension: {list_comp} bytes")
print(f"Generator Expression: {gen_expe} bytes")

# List Comprehension: 43816 bytes
# Generator Expression: 64 bytes
