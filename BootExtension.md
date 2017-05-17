
<html>

<head>
<link rel=stylesheet href="style.css" type="text/css">
<title>How to compute the password to unlock the protected debug-mode
AT-commands of a Zyxel Prestige 941 Cable Modem/Router</title>
</head>

<body>

<p><b><font size="3">How to compute the password to unlock the protected debug-mode AT-commands of
a Zyxel Prestige 941 Cable Modem/Router</font></b></p>
<p><b>Symtom: </b>Some of the debug-mode commands (boot commands) of the Zyxel
P941 do not work.
The response is always &quot;ERROR&quot;.</p>
<p><b>Hardware:</b>  Zyxel Prestige 941 cable router.<br>
Note: Some other Zyxel Prestige modems/routers (e.g. 642 and 650) use the same password
algorithm.</p>
<p><b>Software:</b> Zyxel-Firmware: Bootbase version V1.6.</p>
<p><b>Cause:</b>  Some of the debug-mode AT-commands are protected and must be
enabled using a randomly generated password.</p>
<p><b>Solution:</b>  Use the &quot;ATSE&quot; command to display the seed of the password
generator. Compute the password and enter the password with the command &quot;ATEN
1,password&quot;. After that, &quot;ATHE&quot; (help) will include the protected
commands in the list.</p>
<p>The following formula can be used to compute the password:</p>
<blockquote>
  <p>a = first 3 bytes of seed value<br>
  b = a + 0x10F0A563<br>
  c = (last byte of seed value) AND 7<br>
  password = (b ROR c)&nbsp; XOR a<br>
  <br>
  Note: ROR is a 32-bit rotate-right operation.</p>
</blockquote>
<p>I don't publish the source code or a program to compute the password, because the
protected debug-mode AT commands of the Router should be used by experts only.</p>

<p>Author: <a href="http://www.inventec.ch/chdh" target="_top">Christian d'Heureuse</a> (<a href="mailto:chdh@inventec.ch">chdh@inventec.ch</a>, <a href="http://www.source-code.biz" target="_top">www.source-code.biz</a>)<br>
<a href="swhw_notes.htm">Index</a></p>

<p>From <a href="http://www.inventec.ch/chdh/notes/5.htm">http://www.inventec.ch/chdh/notes/5.htm</a></p>


</body>

</html>
