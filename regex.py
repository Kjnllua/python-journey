# %%
import re

text = "The quick brown fox jumps over 12 lazy dogs"

print(re.findall(r"\b\w{4, }\b", text))
