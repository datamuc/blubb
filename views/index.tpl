<pre>
blubb(1)                          BLUBB                          blubb(1)

NAME
    blubb: command line pastebin.

SYNOPSIS
    &lt;command&gt; | curl -F 'blubb=<-' {{url}}

DESCRIPTION
    add <a href="http://pygments.org/docs/lexers/">?&lt;lang&gt;</a> to resulting url for line numbers and syntax highlighting
    use <a href='data:text/html,<form enctype="multipart/form-data" accept-charset="UTF-8" action="{{url}}" method="POST"><textarea name="blubb" cols="80" rows="24"></textarea><br><button type="submit">blubb</button></form>'>this form</a> to paste from a browser

EXAMPLES
    ~$ curl -F 'blubb=<-' {{url}} < /usr/bin/ack
    {{url}}VZiY
    ~$ firefox '{{url}}VZiY?perl#n-7'
</pre>
