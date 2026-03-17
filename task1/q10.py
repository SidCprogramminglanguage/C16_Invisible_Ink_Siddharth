def embed_bit(pixel_value,secret_bit):
    if secret_bit==1:
        pixel_value=(pixel_value|1)
    else:
        pixel_value=(pixel_value&~1)
    return pixel_value

pixels = list(map(int, input("enter list of pixels: ").split()))
secret_bits = list(map(int, input("enter list of secret bits: ").split()))
modified_pixels=[]

for i,j in zip(pixels, secret_bits):
    modified_pixels.append(embed_bit(i,j))

print(modified_pixels)
