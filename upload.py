import dropbox

class TransferData:
    def __init__ (self,access_token):
        self.access_token=access_token

    def upload_file(self, file_from,file_to):
        dbx=dropbox.Dropbox(self.access_token)
        f = open(file_from,"rb")
        dbx.files_upload(f.read(),file_2)

def main ():
    access_token='qgDxVul_VAUAAAAAAAAAAUx6HL4Sr4T91ZiCU0EFlzOtqjBvm9WGxaFxbToVL1pF'
    transferdata=TransferData(access_token)
    file_from=input("enter the file path to be transferred")
    file_to=input("enter the full path to upload to dropbox")
    transferdata.upload_file(file_from,file_to)
    print("file has been moved")

main()