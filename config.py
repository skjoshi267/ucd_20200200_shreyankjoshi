class Configuration:
    DATABASE_PATH = "stock_database/jl_stock.csv"

    def set_file_path(self,file_path):
        Configuration.DATABASE_PATH = file_path