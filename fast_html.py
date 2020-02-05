import os

print(f"URL = {os.environ['URL']}/")

UPLOAD_PAGE = f"""
<!DOCTYPE html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8" />
    <link
      rel="stylesheet"
      href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css"
      integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh"
      crossorigin="anonymous"
    />

    <title>Fast HTML Uploader</title>
  </head>
  <body>
    <br />
    <div class="container h-100 d-flex justify-content-center">
      <form action="{os.environ['URL']}/" method="post">
        <div class="card" style="width: 18rem;">
          <div class="card-body">
            <h5 class="card-title">Fast HTML Uploader</h5>
            <textarea name="code" name="description"></textarea>
          </div>
        </div>
        <br />
        <br />
        <input type="submit" class="btn btn-dark" value="Deploy ~" />
      </form>
    </div>

    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script
      src="https://code.jquery.com/jquery-3.4.1.slim.min.js"
      integrity="sha384-J6qa4849blE2+poT4WnyKhv5vZF5SrPo0iEjwBvKU7imGFAV0wwj1yYfoRSJoZ+n"
      crossorigin="anonymous"
    ></script>
    <script
      src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js"
      integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo"
      crossorigin="anonymous"
    ></script>
    <script
      src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js"
      integrity="sha384-wfSDF2E50Y2D1uUdj0O3uMBJnjuUD4Ih7YwaYd1iqfktj0Uod8GCExl3Og8ifwB6"
      crossorigin="anonymous"
    ></script>
  </body>
</html>
"""

FOOTER = f"""
<style>
@import 'https://fonts.googleapis.com/css?family=Prompt';
</style>
<hr>
<p style="font-family: 'Prompt', sans-serif; font-size:8pt; font-style:italic">
Powered by <a href="https://github.com/WisTiCeJEnT/">WisTiCeJEnT</a> on 
<a href="https://github.com/WisTiCeJEnT/fast_html"><svg class="octicon octicon-mark-github v-align-middle" height="15" viewBox="0 0 16 16" version="1.1" width="15" aria-hidden="true"><path fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z"></path></svg></a>
<!-- SVG from https://github.com/ -->
</p>
"""

UPLOAD_LINK = f"""
<h1>Upload new code at
<a href="{os.environ['URL']}/upload">{os.environ['URL']}/upload</a>
</h1>
"""
