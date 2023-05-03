import pyshorteners

url = input("Enter URL: \n")

print("Short URL:- ", pyshorteners.Shortener().tinyurl.short(url))