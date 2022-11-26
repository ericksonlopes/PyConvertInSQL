import csv


class ConverterCSVToSQL:
    def __init__(self, path_file: str, output_file: str):
        self.path_file = path_file

        # remove the extension and the path
        self.__file_name = self.path_file.split('/')[-1].replace(".csv", "")
        self.__output_file = output_file

    def get_head(self):
        with open(self.path_file, 'r', encoding='utf-8') as file_csv_read:
            return list(csv.reader(file_csv_read))[0]

    def __get_data(self):
        with open(self.path_file, 'r', encoding='utf-8') as file_csv_read:
            return list(csv.reader(file_csv_read))[1:]

    def __insert_data(self, line):
        with open(file=self.__output_file, mode='a', encoding='utf-8') as cs:
            cs.write(line)

    def generate_inserts(self):
        self.__insert_data(f"-- {self.__file_name} \n")
        # create the command to insert the data
        for line in self.__get_data():
            linha = tuple(map(lambda x: x.replace("'", "''"), line))
            self.__insert_data(f'INSERT INTO {self.__file_name} VALUES {linha} \n')


if __name__ == '__main__':
    # path of the file
    path_file = 'spotify_all_out_playlists_tracks.csv'

    # path of the output file
    output_file = 'querys.sql'

    # create the object
    converter = ConverterCSVToSQL(path_file, output_file)

    # show the data
    converter.generate_inserts()
    print(converter.get_head())
