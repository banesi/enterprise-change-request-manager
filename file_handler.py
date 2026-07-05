import json

class FileHandler:
    def __init__(self,input_file,output_file=None):
        self.input_file = input_file
        self.output_file = output_file
    def load_from_json(self):
        try:
            with open (self.input_file, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            print ("The File was not found")
            return []
        except json.JSONDecodeError:
            print (f" The {self.input_file} formatting is wrong")
            return []
        except Exception as error:
            print(f"Error: {error} was found")
            return []
        
    def dump_to_json(self,data_file):
        with open (self.output_file,'w') as f:
            return json.dump(data_file,f,indent=4)
        