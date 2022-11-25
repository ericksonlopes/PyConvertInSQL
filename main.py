import csv


class ConverterCSVToSQL:
    def __init__(self, path_file: str, output_file: str):
        self.path_file = path_file

        # remove the extension and the path
        self.__file_name = self.path_file.split('/')[-1].replace(".csv", "")
        self.__output_file = output_file

    def show(self):

        if os.path.exists(self.path_file):
            raise FileNotFoundError(f"File not found: {self.path_file}")

        # open the file to read
        with open(self.path_file, 'r', encoding='utf-8') as file_csv_read:
            # open the file to write
            with open(self.__output_file, 'a') as cs:
                # write the name of the file
                cs.write('--' + self.path_file + '--' * 75 + '\n')
                # write the command to disable the constraints
                cs.write(f"ALTER TABLE {self.__file_name} NOCHECK CONSTRAINT ALL \n"
                         f"SET IDENTITY_INSERT {self.__file_name} ON \n")

                # write the command to insert the data
                for line in list(csv.reader(file_csv_read))[1:]:
                    linha = tuple(map(lambda x: x.replace("'", "''"), line))

                    cs.write(f'INSERT INTO {self.__file_name} VALUES {linha} \n')

                # write the command to enable the constraints
                cs.write(f'SET IDENTITY_INSERT {self.__file_name} OFF \n'
                         f'ALTER TABLE {self.__file_name} CHECK CONSTRAINT ALL \n\n')
