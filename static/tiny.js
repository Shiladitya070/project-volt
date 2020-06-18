let script = document.createElement("script");
script.type = "text/javascript";
script.src = "https://cdn.tiny.cloud/1/no-api-key/tinymce/5/tinymce.min.js";
document.head.append(script);
console.log("im am in");
tinymce.init({
  selector: "#id_content",
});
