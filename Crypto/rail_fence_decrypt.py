def rail_fence_decrypt(ciphertext, rails):
    # Create a list to hold the positions of the rails
    rail = [['\n' for _ in range(len(ciphertext))] for _ in range(rails)]
    
    # Determine the direction of the rail fence (down and up)
    dir_down = None
    row, col = 0, 0

    # Place the characters in the rail
    for i in range(len(ciphertext)):
        if row == 0:
            dir_down = True
        if row == rails - 1:
            dir_down = False
        
        rail[row][col] = '*'
        col += 1

        if dir_down:
            row += 1
        else:
            row -= 1

    index = 0
    for i in range(rails):
        for j in range(len(ciphertext)):
            if (rail[i][j] == '*' and index < len(ciphertext)):
                rail[i][j] = ciphertext[index]
                index += 1

    # Read the characters in the zigzag pattern
    result = []
    row, col = 0, 0
    for i in range(len(ciphertext)):
        if row == 0:
            dir_down = True
        if row == rails - 1:
            dir_down = False
        
        if rail[row][col] != '\n':
            result.append(rail[row][col])
            col += 1

        if dir_down:
            row += 1
        else:
            row -= 1

    return ''.join(result)

# Example usage
if __name__ == "__main__":
    encrypted_message = "Ta _7N6D49hlg:W3D_H3C31N__A97ef sHR053F38N43D7B i33___N6"
    rails = 4
    decrypted_message = rail_fence_decrypt(encrypted_message, rails)
    
    # Format the final flag
    flag = f'picoCTF{{{decrypted_message}}}'
    print(flag)
