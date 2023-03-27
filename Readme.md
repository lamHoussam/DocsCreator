# DocsCreator

This is a Python script that generates documentation for C# files. It uses the PLY library to tokenize C# files and extract relevant information such as class definitions, public method signatures, serialized and public member definitions, and public properties. The script then generates Markdown files for each C# file in a specified folder.


## Usage
To use the script, clone the repository 
```
git clone https://github.com/lamHoussam/DocsCreator.git
``` 
then navigate to it and open a terminal and run 
```
pip install -r requirements.txt
```
then execute a simple 

```
usage: main.py [-h] [--recursive] project_path

Create markdown documentation for C# project

positional arguments:
  project_path

optional arguments:
  -h, --help    show this help message and exit
  --recursive
```

The script is designed to generate documentation for C# files in your project folder (you can chose to make it recursive). You can change the output folder name by modifying the folder_name variable in the main.py file.

When you run the script, it will generate Markdown files for each C# file in the specified folder. The Markdown files will be named after the C# files with a .md extension.


## Generated Markdown
Each Markdown file will has the following sections:

* Class definition
* Serialized Members
* Public Members
* Public Properties 
* Public Methods

The class definition will include the class name, base class (if any), implemented interfaces (if any) and description (if any).

The serialized members section will include a list of serialized members (i.e. private fields marked with the `[SerializeField]` attribute), along with their types and descriptions.

The public members section will include a list of public members, along with their types and descriptions.

The properties section will include a list of public properties 
(i.e. ```public float Value => value``` or `public int Test { get; set; }`)
, along with their types and descriptions.

The methods section will include a list of public methods, along with their signatures and descriptions.

## Contributing

If you find a bug or have a feature request, please open an issue on the GitHub repository. Contributions are also welcome – if you'd like to contribute to the project, please submit a pull request.

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).

## Credits

This project was created by [lamHoussam](https://github.com/lamHoussam). 
