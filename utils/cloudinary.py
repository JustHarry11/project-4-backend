from cloudinary.uploader import upload

def handle_file_upload(request, pathname = 'image_url'):
    data = request.data.dict()
    if isinstance(data.get(pathname), str):
        return request.data
    elif request.FILES.get(pathname, None):
        res = upload(request.FILES[pathname])
        return { **data, pathname: res['secure_url'] }
    else:
        return request.data