from pytube import YouTube
import requests

url = "https://ytstream-download-youtube-videos.p.rapidapi.com/dl"

querystring = {"id":"JFm7YDVlqnI","geo":"DE"}

headers = {
    'x-rapidapi-key': "00e1aed8bfmshb9459b236153b8ep13e2f2jsn79fc58ff8d5a",
    'x-rapidapi-host': "ytstream-download-youtube-videos.p.rapidapi.com"
    }

response = requests.get(url, headers=headers)

print(response.text)
print(f'Status code: {response.status_code}')
#ask for the link from user
link = input("Enter the link of YouTube video you want to download:  ")
yt = YouTube(link)

#Showing details
print("Title: ",yt.title)
print("Number of views: ",yt.views)
print("Length of video: ",yt.length)
print("Rating of video: ",yt.rating)
#Getting the highest resolution possible
ys = yt.streams.get_highest_resolution()

#Starting download
print("Downloading...")
ys.download()