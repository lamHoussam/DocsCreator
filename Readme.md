# DocsCreator

This is a Python script that generates documentation for C# files. It uses the PLY library to tokenize C# files and extract relevant information such as class definitions, method signatures, and serialized member definitions. The script then generates Markdown files for each C# file in a specified folder.


## Usage
To use the script, clone the repository 
```
git clone https://github.com/lamHoussam/DocsCreator.git
``` 
then navigate to project folder and open a terminal and run 
```
pip install -r requirements.txt
```
then execute a simple 

```
python main.py [--option] <project_path>
```

The script is designed to generate documentation for C# files in your project folder (you can chose to make it recursive). You can change this folder name by modifying the folder_name variable in the csharp_doc_gen.py file.

When you run the script, it will generate Markdown files for each C# file in the specified folder. The Markdown files will be named after the C# files with a .md extension.


## Generated Markdown
Each Markdown file will have the following sections:

* Class definition
* Properties (serialized members)
* Methods

The class definition will include the class name, base class (if any), and description (if any).

The properties section will include a list of serialized members (i.e. private fields marked with the `[SerializeField]` attribute), along with their types and descriptions.

The methods section will include a list of public methods, along with their signatures and descriptions (if any).


## Contributing

If you find a bug or have a feature request, please open an issue on the GitHub repository. Contributions are also welcome – if you'd like to contribute to the project, please submit a pull request.

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).

## Credits

This project was created by [lamHoussam](https://github.com/lamHoussam). 
