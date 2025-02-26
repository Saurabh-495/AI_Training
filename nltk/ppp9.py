from bs4 import BeautifulSoup

# Example HTML string
html_doc = """
<html>
  <head>
    <title>Example Page</title>
    <style>
      body {font-family: Arial;}
    </style>
    <script>
      console.log("Hello, world!");
    </script>
  </head>
  <body>
    <h1>Welcome to the Example Page</h1>
    <p>This is a <strong>sample</strong> paragraph with <a href="http://example.com">a link</a>.</p>
  </body>
</html>
"""

# Create a BeautifulSoup object
soup = BeautifulSoup(html_doc, 'html.parser')

print(soup)