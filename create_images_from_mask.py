from PIL import Image

def mask_to_img(input_img_path, ingredient_mask_path):
    '''Function that can be used to convert two images, given their path, to a single full-black image with the ingredient only, pasted following the mask (found using segmentation) '''
    input_img = Image.open(input_img_path).convert("RGB")
    ingredient_mask = Image.open(ingredient_mask_path).convert("L")
    new_black = Image.new("RGB",input_img.size,(0,0,0))
    new_black.paste(input_img,(0,0),ingredient_mask)
    return new_black


