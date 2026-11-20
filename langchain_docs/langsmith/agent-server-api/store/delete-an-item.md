---
title: "Delete an item. - Docs by LangChain"
url: https://docs.langchain.com/langsmith/agent-server-api/store/delete-an-item
scraped_at: 2026-11-15T03:38:13.195168
word_count: 555
---

Delete an item.

cURL

```
curl --request DELETE \
  --url https://api.example.com/store/items \
  --header 'Content-Type: application/json' \
  --data '
{
  "key": "<string>",
  "namespace": [
    "<string>"
  ]
}
'
```

```
import requests

url = "https://api.example.com/store/items"

payload = {
    "key": "<string>",
    "namespace": ["<string>"]
}
headers = {"Content-Type": "application/json"}

response = requests.delete(url, json=payload, headers=headers)

print(response.text)
```

```
const options = {
  method: 'DELETE',
  headers: {'Content-Type': 'application/json'},
  body: JSON.stringify({key: '<string>', namespace: ['<string>']})
};

fetch('https://api.example.com/store/items', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://api.example.com/store/items",
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => "",
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 30,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => "DELETE",
  CURLOPT_POSTFIELDS => json_encode([
    'key' => '<string>',
    'namespace' => [
        '<string>'
    ]
  ]),
  CURLOPT_HTTPHEADER => [
    "Content-Type: application/json"
  ],
]);

$response = curl_exec($curl);
$err = curl_error($curl);

curl_close($curl);

if ($err) {
  echo "cURL Error #:" . $err;
} else {
  echo $response;
}
```

```
package main

import (
	"fmt"
	"strings"
	"net/http"
	"io"
)

func main() {

	url := "https://api.example.com/store/items"

	payload := strings.NewReader("{\n  \"key\": \"<string>\",\n  \"namespace\": [\n    \"<string>\"\n  ]\n}")

	req, _ := http.NewRequest("DELETE", url, payload)

	req.Header.Add("Content-Type", "application/json")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(string(body))

}
```

```
HttpResponse<String> response = Unirest.delete("https://api.example.com/store/items")
  .header("Content-Type", "application/json")
  .body("{\n  \"key\": \"<string>\",\n  \"namespace\": [\n    \"<string>\"\n  ]\n}")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.example.com/store/items")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Delete.new(url)
request["Content-Type"] = 'application/json'
request.body = "{\n  \"key\": \"<string>\",\n  \"namespace\": [\n    \"<string>\"\n  ]\n}"

response = http.request(request)
puts response.read_body
```

422

```
{
  "detail": "<string>"
}
```

DELETE

/

store

/

items

Try it

Delete an item.

cURL

```
curl --request DELETE \
  --url https://api.example.com/store/items \
  --header 'Content-Type: application/json' \
  --data '
{
  "key": "<string>",
  "namespace": [
    "<string>"
  ]
}
'
```

```
import requests

url = "https://api.example.com/store/items"

payload = {
    "key": "<string>",
    "namespace": ["<string>"]
}
headers = {"Content-Type": "application/json"}

response = requests.delete(url, json=payload, headers=headers)

print(response.text)
```

```
const options = {
  method: 'DELETE',
  headers: {'Content-Type': 'application/json'},
  body: JSON.stringify({key: '<string>', namespace: ['<string>']})
};

fetch('https://api.example.com/store/items', options)
  .then(res => res.json())
  .then(res => console.log(res))
  .catch(err => console.error(err));
```

```
<?php

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_URL => "https://api.example.com/store/items",
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => "",
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 30,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => "DELETE",
  CURLOPT_POSTFIELDS => json_encode([
    'key' => '<string>',
    'namespace' => [
        '<string>'
    ]
  ]),
  CURLOPT_HTTPHEADER => [
    "Content-Type: application/json"
  ],
]);

$response = curl_exec($curl);
$err = curl_error($curl);

curl_close($curl);

if ($err) {
  echo "cURL Error #:" . $err;
} else {
  echo $response;
}
```

```
package main

import (
	"fmt"
	"strings"
	"net/http"
	"io"
)

func main() {

	url := "https://api.example.com/store/items"

	payload := strings.NewReader("{\n  \"key\": \"<string>\",\n  \"namespace\": [\n    \"<string>\"\n  ]\n}")

	req, _ := http.NewRequest("DELETE", url, payload)

	req.Header.Add("Content-Type", "application/json")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(string(body))

}
```

```
HttpResponse<String> response = Unirest.delete("https://api.example.com/store/items")
  .header("Content-Type", "application/json")
  .body("{\n  \"key\": \"<string>\",\n  \"namespace\": [\n    \"<string>\"\n  ]\n}")
  .asString();
```

```
require 'uri'
require 'net/http'

url = URI("https://api.example.com/store/items")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Delete.new(url)
request["Content-Type"] = 'application/json'
request.body = "{\n  \"key\": \"<string>\",\n  \"namespace\": [\n    \"<string>\"\n  ]\n}"

response = http.request(request)
puts response.read_body
```

422

```
{
  "detail": "<string>"
}
```

#### Body

application/json

Request to delete an item.

key

string

required

The unique identifier for the item.

namespace

string[]

A list of strings representing the namespace path.

#### Response

204

Success

Was this page helpful?

YesNo