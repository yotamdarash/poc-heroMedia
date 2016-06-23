from instagram.client import InstagramAPI
api = InstagramAPI(client_id='YOUR_CLIENT_ID', client_secret='YOUR_CLIENT_SECRET')
popular_media = api.media_popular(count=5)
for media in popular_media:
    print media.images['standard_resolution'].url