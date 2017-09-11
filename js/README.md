# Parse JSON
* https://www.w3schools.com/js/js_json_parse.asp
  * simple, and list
* https://www.w3schools.com/js/js_json.asp
  * Example for json list, e.g. employees
```
{
    "name":"John",
    "age":31,
    "pets":[
        { "animal":"dog", "name":"Fido" },
        { "animal":"cat", "name":"Felix" },
        { "animal":"hamster", "name":"Lightning" }
    ]
}
```

```
<!DOCTYPE html>
<html>
<body>

<h2>Use the XMLHttpRequest to get the content of a file.</h2>
<p>The content is written in JSON format, and can easily be converted into a JavaScript object.</p>

<p id="demo"></p>

<script>

var xmlhttp = new XMLHttpRequest();
xmlhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
        var myObj = JSON.parse(this.responseText);
        document.getElementById("demo").innerHTML = myObj.name + "<br>";
        document.getElementById("demo").innerHTML += myObj.pets[0].animal + "," + myObj.pets[0].name + "<br>";
        document.getElementById("demo").innerHTML += myObj.pets[1].animal + "," + myObj.pets[1].name + "<br>";
        document.getElementById("demo").innerHTML += myObj.pets[2].animal + "," + myObj.pets[2].name + "<br>";
    }
};
xmlhttp.open("GET", "json_demo.txt", true);
xmlhttp.send();

</script>

<p>Take a look at <a href="json_demo.txt" target="_blank">json_demo.txt</a></p>

</body>
</html>
```

# Command Line Processor jq
## Install
```
sudo apt install jq
```
## Get a value of a key
```
cat <json file> | jq .key, where .key is called a filter
e.g. Get the value of "tag_name" from the release file.
curl -s https://api.github.com/repos/go-swagger/go-swagger/releases/latest | jq -r .tag_name
```
