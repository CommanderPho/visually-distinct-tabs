from xml.etree.ElementTree import Element, SubElement, tostring, parse
from enum import Enum
from pathlib import Path
import json


class Shape(Enum):
    CIRCLE = "circle"
    TRIANGLE = "triangle"
    SQUARE = "square"

def add_shape_to_svg(svg_file_path, shape, color="red"):
    # Parse the SVG file and get the root element
    svg_tree = parse(svg_file_path)
    svg_file_path = Path(svg_file_path)
    
    svg_root = svg_tree.getroot()

    # Get the width and height of the SVG element
    width = int(svg_root.attrib["width"])
    height = int(svg_root.attrib["height"])

    # Create a new element for the specified shape and add it to the SVG root
    if shape == Shape.CIRCLE:
        shape_element = Element("circle")
        shape_element.attrib["cx"] = str(width // 2)
        shape_element.attrib["cy"] = str(height // 2)
        shape_element.attrib["r"] = str(min(width, height) // 2 * 0.8)  # Set the radius to 80% of the smaller dimension
    elif shape == Shape.TRIANGLE:
        shape_element = Element("polygon")
        shape_element.attrib["points"] = f"{width//2},{height//4} {width//4*3},{height//4*3} {width//4},{height//4*3}"
    elif shape == Shape.SQUARE:
        shape_element = Element("rect")
        shape_element.attrib["x"] = str(width // 4)
        shape_element.attrib["y"] = str(height // 4)
        shape_element.attrib["width"] = str(width // 2)
        shape_element.attrib["height"] = str(height // 2)
    else:
        raise ValueError(f"Invalid shape: {shape}")

    shape_element.attrib["fill"] = color
    svg_root.insert(0, shape_element)

    # Save the modified SVG file
    file_parent_path = svg_file_path.parent
    file_basename = svg_file_path.stem
    destination_parent_path = Path('fileicons\images\generated')
    modified_basename = f"{file_basename}-{shape.value}-{color}"
    modified_filename = f"{modified_basename}.svg"
    modified_svg_file_path = destination_parent_path.joinpath(modified_filename)
    with open(modified_svg_file_path, "w") as f:
        f.write(tostring(svg_root).decode())
    return modified_basename, modified_svg_file_path


# def add_red_circle_to_svg(svg_file_path):
#     # Parse the SVG file and get the root element
#     svg_tree = parse(svg_file_path)
#     svg_root = svg_tree.getroot()

#     # Get the width and height of the SVG element
#     width = int(svg_root.attrib["width"])
#     height = int(svg_root.attrib["height"])

#     # Create a new circle element and add it to the SVG root
#     circle = Element("circle")
#     circle.attrib["cx"] = str(width // 2)
#     circle.attrib["cy"] = str(height // 2)
#     circle.attrib["r"] = str(min(width, height) // 2 * 0.8)  # Set the radius to 80% of the smaller dimension
#     circle.attrib["fill"] = "red"
#     svg_root.insert(0, circle)


# 	# Create a new polygon element for the triangle and add it to the SVG root
#     triangle = Element("polygon")
#     triangle.attrib["points"] = f"{width//2},{height//4} {width//4*3},{height//4*3} {width//4},{height//4*3}"
#     triangle.attrib["fill"] = "red"
#     svg_root.insert(0, triangle)
    

#     # Save the modified SVG file
#     file_basename = svg_file_path.split(".")[0]
#     modified_svg_file_path = f"{file_basename}_circle_red.svg"
#     with open(modified_svg_file_path, "w") as f:
#         f.write(tostring(svg_root).decode())

#     return modified_svg_file_path


if __name__ == "__main__":
    original_svg_paths = ['fileicons\images\document-dark.svg']
    shape_variants = (Shape.CIRCLE, Shape.TRIANGLE, Shape.SQUARE)
    color_variants = ('red', 'green')
    modified_svg_paths = {}
    icon_definitions_entries = {}
        
    for original_svg_path in original_svg_paths:
        modified_svg_paths[original_svg_path] = []
        for a_shape_variant in shape_variants:
            for a_color_variant in color_variants:
                modified_basename, _out_path = add_shape_to_svg(original_svg_path, a_shape_variant, color=a_color_variant)
                ## Generate json entry
                modified_variable_name = f"_{modified_basename.replace('-','_')}" # build variable name
                # icon_definitions_entry 
                icon_definitions_entries[modified_variable_name] = {"iconPath": f"./images/generated/{modified_basename}.svg"}
                modified_svg_paths[original_svg_path].append(_out_path)
        
    # modified_svg_paths.append(add_red_circle_to_svg(original_svg_paths[0]))
    print(f'modified_svg_paths: {modified_svg_paths}\n')
    # print(f'icon_definitions_entries: {icon_definitions_entries}')
    
    final_json_dict = {'iconDefinitions': icon_definitions_entries}

    # Convert the dictionary to JSON
    json_str = json.dumps(final_json_dict)
    # Print the JSON string
    print(json_str)







