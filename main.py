import csv
import os


class ConverterCSVToSQL:
    def __init__(self, path_file: str, output_file: str, delimiter: str = ','):
        self.path_file = path_file
        self.delimiter = delimiter

        # remove the extension and the path
        self.__file_name = self.path_file.split('/')[-1].replace(".csv", "")
        self.__output_file = output_file

    def show(self):
        try:
            if not os.path.exists(self.path_file):
                raise FileNotFoundError(f"File not found: {self.path_file}")

            # open the file to read
            with open(self.path_file, 'r', encoding='utf-8') as file_csv_read:
                # open the file to write
                self.__insert_data_in_file(file_csv_read)
        except Exception as error:
            raise error

    def __insert_data_in_file(self, file_csv_read):
        try:
            with open(self.__output_file, 'a') as cs:
                # write the name of the file
                cs.write('-- ' + self.path_file + '--' * 54 + '\n')

                # write the command to insert the data
                for line in list(csv.reader(file_csv_read, delimiter=self.delimiter))[1:]:
                    linha = self.__clear_line(line)
                    cs.write(f'INSERT INTO {self.__file_name} VALUES {linha} \n')
        except Exception as error:
            raise error

    @staticmethod
    def __clear_line(line):
        try:
            line = tuple(map(lambda x: x.replace("'", "''"), line))
            line = str(line).replace("'NULL'", 'NULL')
        except Exception as error:
            raise error

        return line


if __name__ == '__main__':
    ConverterCSVToSQL(path_file='test.csv', output_file='result.sql').show()
