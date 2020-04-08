from dropbox.exceptions import ApiError
from app import dropbox

def delete_photo(model):
    try:
        dropbox.files_delete(model.cloud_dir())
        model.photo_url = ''
    except ApiError:
        pass

def upload_photo(model, local_dir):
    delete_photo(model)
    with open(local_dir, 'rb') as local_file:
        dropbox.files_upload(local_file.read(), model.cloud_dir())
    model.photo_url = dropbox.sharing_create_shared_link(model.cloud_dir()).url.replace('dl=0','raw=1')
