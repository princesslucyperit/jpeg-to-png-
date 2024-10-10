import os
from PIL import Image

def convert_to_png(input_path):
    try:
        # Open the image
        with Image.open(input_path) as img:
            # Get the file name without extension
            file_name = os.path.splitext(os.path.basename(input_path))[0]
            
            # Create the output path
            output_path = f"{file_name}.png"
            
            # Convert and save as PNG
            img.save(output_path, "PNG")
            
            print(f"Converted {input_path} to {output_path}")
            return True
    except Exception as e:
        print(f"Error converting {input_path}: {str(e)}")
        return False

def main():
    while True:
        input_path = input("Enter the path to the JPEG image (or 'q' to quit): ")
        
        if input_path.lower() == 'q':
            print("Exiting the program.")
            break
        
        if not os.path.exists(input_path):
            print("File does not exist. Please try again.")
            continue
        
        if not input_path.lower().endswith(('.jpg', '.jpeg')):
            print("File is not a JPEG. Please provide a JPEG file.")
            continue
        
        success = convert_to_png(input_path)
        
        if success:
            print("Conversion completed successfully.")
        else:
            print("Conversion failed. Please try again.")

if __name__ == "__main__":
    main()
