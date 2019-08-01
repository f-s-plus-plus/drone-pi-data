Save your login credentials for drone pi to credentials json

Here is an example `credentials.json`
```json
{
  "email": "jones@gmail.com",
  "password": "password"
}
```

`Record.py` is responsible for recording gps coordinates and uploading flights to the drone pi application

`Video.py` checks for a valid internet connection and records video. As soon as the internet connection cuts out, it stops recording  