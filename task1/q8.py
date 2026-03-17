def embed_bit(pixel_value,secret_bit):
    if secret_bit==1:
        pixel_value=(pixel_value|1)
    else:
        pixel_value=(pixel_value&~1)
    return pixel_value
    
pixel_value=int(input("enter pixel value:"))
secret_bit=int(input("enter secret bit:"))
result=embed_bit(pixel_value,secret_bit)

print(result)
