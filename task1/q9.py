def extract_bit(pixel_value):
    return pixel_value&1

pixel_value=int(input("pixel value"))

print(extract_bit(pixel_value)) 