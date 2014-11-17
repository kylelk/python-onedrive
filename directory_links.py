from onedrive import api_v5, conf
api = api_v5.PersistentOneDriveAPI.from_conf()
res = list(api.listdir(resolve_path(optz.folder), offset=offset, limit=limit))