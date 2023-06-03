import dropbox 
# this code uploads a file to drop box with given acces key
class TransferData:
    def __init__(self,access_token):
        self.access_token = access_token
    
    def UploadFile(self,File_From,File_To):
        dbx = dropbox.Dropbox(self.access_token)
        with open(File_From, 'rb') as f:
            dbx.files_upload(f.read(),File_To)

def main():
    access_token = 'sl.BfrbUZnu9jbTKM9KzGK9wF5ZM70xgclLwh6P_CJEM2B-T39G7aFSfOyLVDg0Z0-vHkXph7PUzRGFkIFak7W5Hhti_lOjqDtoEf7yammwia2ZSOwG5bfefAbVHTwMxaLMBoJNH9yzSa4'
    transferData = TransferData(access_token)
    # File_From = input("Enter the file path to transfer-")
    # File_To = input("Enter the full path to upload to DropBox")
    transferData.UploadFile('./newFile2.txt', '/Apps/ne')
    print("File has been moved")

main()