from sys import argv
print(argv)
script, input_file, output_file = argv
lines = open(input_file).readlines()
print("num_lines pre", len(lines))
new_lines = list()
for line in lines:
    tokens = line.split()
    new_line = list()
    for token in tokens:
        factor = token.split("|")
        diff = int(factor[1]) - int(factor[0])
        if diff == 1:
            new_token = list()
            new_token.append(factor[2])
            new_token.append(factor[3])
            new_line.append("|".join(new_token))
        elif diff > 1:
            words = factor[2].split("_")
            new_tokens = list()
            for i in range(diff):
                new_token = list()
                new_token.append(words[i])
                new_token.append(factor[3])
                new_line.append("|".join(new_token))
    #        new_token = list()
     #   new_line.append(factor[2])
    new_line.append("\n")
    new_lines.append(" ".join(new_line))
print("num_lines post", len(new_lines))
open(output_file, 'w').writelines(new_lines)
